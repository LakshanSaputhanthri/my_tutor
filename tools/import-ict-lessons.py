#!/usr/bin/env python3
"""Imports the lesson-wise AL ICT question PDFs (al-question-pdf/*.pdf) into app/content/ict-lessons.json.

* MCQs become text questions (English + Sinhala via fm2uni). Answers are NOT in these PDFs, so `a` is [] (pending);
  an answer key can be merged later with tools/apply-ict-answers.py.
* Essay / structured questions, and any MCQ that depends on a figure, table, subscript or maths, are also cropped from the
  PDF page into grayscale PNGs (app/static/ictq/) because plain text loses those.

Usage: python tools/import-ict-lessons.py
"""
import json, os, re, sys, glob, io
import pymupdf
from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
from fm2uni import fm_to_unicode
from lessonseg import segment, NUMLINE, LEGACY

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
PDF_DIR = os.path.join(ROOT, 'al-question-pdf')
OUT = os.path.join(ROOT, 'app', 'content', 'ict-lessons.json')
IMG_DIR = os.path.join(ROOT, 'app', 'static', 'ictq')
DPI = 100

# pdf timestamp -> list of (lesson slug, title) ; several entries = split by the "LESSON n PAST PAPERS" headings, in order
PDFS = {
    '2026-05-15_21-25-56': [('web', 'Web Design & Development')],
    '2026-05-15_21-26-35': [('fund', 'ICT Fundamentals & Computer Systems')],
    '2026-05-15_21-29-36': [('os', 'Operating Systems & Memory')],
    '2026-06-07_23-07-47': [('l11', 'Lesson 11 · Internet of Things'), ('l12', 'Lesson 12 · E-Commerce'), ('l13', 'Lesson 13 · Ubiquitous Computing & AI')],
    '2026-09-19_21-03-04': [('net', 'Data Communication & Networking')],
    '2026-09-19_21-11-56': [('num', 'Number Systems'), ('logic', 'Logic Gates & Boolean Algebra')],
    '2026-08-09_21-44-08': [('sad', 'System Analysis & Design')],
    '2025-12-10_20-37-23': [('db', 'Database Management')],
    '2026-04-08_22-41-36': [('prog', 'Programming (Python)')],
}
ALWAYS_IMAGE = {'num', 'logic'}          # subscripts / overbars do not survive text extraction
FIG_WORDS = re.compile(r'figure|diagram|following table|flow ?chart|circuit|graph|image|picture|shown (below|above)|screenshot|sketch|map\b', re.I)
MATH_CHARS = re.compile(r'[̀-ͯഀ-ൿ\U0001d400-\U0001d7ff∀-⋿]')
CONTENT_TOP, CONTENT_BOT_MARGIN = 40, 48


def clean(t):
    return re.sub(r'[ \t]+', ' ', t).strip()


def has_script(lines):
    """True when a line mixes normal and clearly smaller digits/letters (subscripts / superscripts)."""
    for _, ln in lines:
        sp = [s for s in ln['spans'] if s['text'].strip()]
        if len(sp) > 1:
            big = max(s['size'] for s in sp)
            if any(s['size'] < big * 0.8 and re.fullmatch(r'[0-9A-Za-z+\-]{1,3}', s['text'].strip()) and 'Chami' not in s['font'] and 'Malithi' not in s['font'] for s in sp):
                return True
    return False


def drawn_stuff(doc, pn, y0, y1):
    page = doc[pn]
    r = pymupdf.Rect(0, y0, page.rect.width, y1)
    for im in page.get_image_info():
        if pymupdf.Rect(im['bbox']).intersects(r) and im['width'] > 40 and im['height'] > 20:
            return True
    n = 0
    for d in page.get_drawings():
        rr = d['rect']
        if rr.intersects(r) and (rr.width > 20 or rr.height > 20):
            n += 1
    return n >= 3


def crop_region(doc, start, end, name):
    """Render the page area between start=(pn, y) and end=(pn, y) into PNG files; return their relative paths."""
    paths = []
    for pn in range(start[0], end[0] + 1):
        page = doc[pn]
        W, H = page.rect.width, page.rect.height
        y0 = start[1] if pn == start[0] else CONTENT_TOP
        y1 = end[1] if pn == end[0] else H - CONTENT_BOT_MARGIN
        if y1 - y0 < 6:
            continue
        clip = pymupdf.Rect(20, max(0, y0 - 0.5), W - 20, min(H, y1 + 0.5))
        pix = page.get_pixmap(dpi=DPI, clip=clip, colorspace=pymupdf.csGRAY)
        im = Image.frombytes('L', (pix.width, pix.height), pix.samples)
        bbox = Image.eval(im, lambda v: 255 - v).point(lambda v: 255 if v > 24 else 0).getbbox()
        if not bbox:
            continue
        pad = 6
        im = im.crop((max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(im.width, bbox[2] + pad), min(im.height, bbox[3] + pad)))
        if im.height < 12:
            continue
        im = im.quantize(16).convert('L') if False else im.point(lambda v: 255 if v > 235 else (v // 32) * 32)
        fn = f'{name}_{len(paths) + 1}.png'
        buf = io.BytesIO()
        im.convert('P', palette=Image.ADAPTIVE, colors=8).save(buf, 'PNG', optimize=True)
        with open(os.path.join(IMG_DIR, fn), 'wb') as f:
            f.write(buf.getvalue())
        paths.append('ictq/' + fn)
    return paths


def parse_mcq(lines):
    """lines: [(pn, line)] starting at the number line. Returns dict with stem/opts or None."""
    first = lines[0][1]
    m = NUMLINE.match(first['eng'])
    n = int(m.group(1))
    stem_x = first['x']
    stem, sin_stem, opts, opt_sin, opt_pos, state, last_opt = [], [], {}, {}, {}, 'stem', None
    for k, (pn, ln) in enumerate(lines):
        eng, sin, x, y = ln['eng'], ln['sin'], round(ln['x']), round(ln['y0'])
        if k == 0:
            eng = re.sub(r'^\s*\d+\s*\.\s*', '', eng)
        mk = [(int(mm.group(1)), mm.start()) for mm in re.finditer(r'(?:(?<=\s)|^)([1-5])\)\s*', eng + ' ')]
        if mk and (state == 'opts' or mk[0][0] == 1 or len(opts) == 0 and mk[0][0] <= 5):
            state = 'opts'
            for j, (num, pos) in enumerate(mk):
                nxt = mk[j + 1][1] if j + 1 < len(mk) else len(eng)
                body = re.sub(r'^\s*[1-5]\)\s*', '', eng[pos:nxt])
                opts[num] = [body.strip()] if body.strip() else []
                opt_sin[num] = [sin] if (sin and len(mk) == 1) else []
                opt_pos[num] = (x, y)
                last_opt = num
            continue
        if state == 'opts':
            best = None
            for num, (ox, oy) in opt_pos.items():
                if x >= ox - 3 and y >= oy - 2 and (best is None or ox > opt_pos[best][0] or (ox == opt_pos[best][0] and oy > opt_pos[best][1])):
                    best = num
            best = best or last_opt
            if best:
                if eng.strip():
                    opts[best].append(eng.strip())
                if sin:
                    opt_sin[best].append(sin)
            continue
        indent = ' ' * int(max(0, (x - stem_x - 18) // 5)) if x > stem_x + 25 else ''
        if eng.strip():
            stem.append(indent + eng.strip())
        if sin:
            sin_stem.append(sin)
    return n, stem, sin_stem, opts, opt_sin


def build_mcq(n, stem, sin_stem, opts, opt_sin):
    o = []
    for i in range(1, 6):
        parts = [p for p in opts.get(i, []) if p]
        code = len(parts) > 1 and any(re.search(r'[;{}()=:]', t) for t in parts)
        o.append(('\n'.join(parts) if code else clean(' '.join(parts))).rstrip('/ ').strip())
    item = {'q': '\n'.join(s for s in stem if s.strip()).strip(), 'o': o, 'a': []}
    qs = fm_to_unicode(' '.join(sin_stem))
    if qs:
        item['qs'] = qs
    os_ = [fm_to_unicode(' '.join(opt_sin.get(i, []))) for i in range(1, 6)]
    if any(os_):
        item['os'] = [x or o[i] for i, x in enumerate(os_)]
    item['n'] = n
    return item


def main():
    os.makedirs(IMG_DIR, exist_ok=True)
    for f in glob.glob(os.path.join(IMG_DIR, '*.png')):
        os.remove(f)
    sets, report = [], []
    for path in sorted(glob.glob(os.path.join(PDF_DIR, '*.pdf'))):
        key = re.search(r'\d+_(\d{4}-\d\d-\d\d_\d\d-\d\d-\d\d)', os.path.basename(path)).group(1)
        lessons = PDFS[key]
        doc, segs, heads = segment(path)
        by = {slug: {'M': [], 'E': []} for slug, _ in lessons}
        pre_shared = {}      # (slug, n) -> preface images for later questions covered by "questions N to M"
        for si, s in enumerate(segs):
            kind = s['tags'][0][1]
            L = s['lines']
            if not L:
                continue
            pn0 = L[0][0]
            slug = lessons[0][0]
            if len(lessons) > 1:
                hs = [h for h in heads if h[0] <= pn0]
                slug = lessons[len(hs) - 1][0] if hs else lessons[0][0]
            tag = s['tags'][-1]
            tag_end = (tag[5], tag[4])
            last = max(L, key=lambda r: (r[0], r[1]['y1']))
            end = max((last[0], last[1]['y1']), tag_end)
            tags = ', '.join(dict.fromkeys(f"{t[0]} {'ESSAY' if t[1] == 'E' else 'Q'}{t[2] or ''}{t[3] or ''}" for t in s['tags']))
            name = f'{slug}-{kind.lower()}{len(by[slug][kind]) + 1:03d}'
            k = next((i for i, (_, l) in enumerate(L) if NUMLINE.match(l['eng']) and l['x'] < 90), None)
            if kind == 'E':
                imgs = crop_region(doc, (L[0][0], L[0][1]['y0']), end, name)
                by[slug]['E'].append({'q': '', 'o': [], 'a': [], 'im': imgs, 'd': tags})
                continue
            if k is None:
                report.append(f'{key} seg{si}: no number line, skipped')
                continue
            pre, body = L[:k], L[k:]
            n, stem, sin_stem, opts, opt_sin = parse_mcq(body)
            item = build_mcq(n, stem, sin_stem, opts, opt_sin)
            item['d'] = tags
            bstart = (body[0][0], body[0][1]['y0'])
            ctx_imgs = []
            if pre:
                ctx_imgs = crop_region(doc, (pre[0][0], pre[0][1]['y0']), bstart, name + 'c')
                rng = re.findall(r'\d+', ' '.join(l['eng'] for _, l in pre if re.search(r'question', l['eng'], re.I) or re.search(r'\d+\s*(?:to|and|-|–)\s*\d+', l['eng'])))
                nums = sorted({int(x) for x in rng if 0 < int(x) < 200})
                if len(nums) >= 2 and nums[-1] - nums[0] < 8:
                    for q in range(nums[0], nums[-1] + 1):
                        pre_shared[(slug, q)] = ctx_imgs
            ctx_imgs = ctx_imgs or pre_shared.get((slug, n), [])
            bad_opts = sum(1 for o in item['o'] if not o)
            need_img = (slug in ALWAYS_IMAGE or bad_opts or ctx_imgs or has_script(body) or MATH_CHARS.search(item['q'] + ''.join(item['o']))
                        or FIG_WORDS.search(item['q']) or any(drawn_stuff(doc, pn, (bstart[1] if pn == bstart[0] else CONTENT_TOP), (end[1] if pn == end[0] else 9999)) for pn in range(bstart[0], end[0] + 1)))
            need_img = True      # Sinhala is stored in legacy fonts that cannot be converted reliably, so show the page itself
            if need_img:
                own = crop_region(doc, bstart, end, name)
                item['im'] = ([] if not pre else []) + ctx_imgs + own
                item['img'] = 1          # the picture is the source of truth; text is only a fallback
                if bad_opts or slug in ALWAYS_IMAGE:
                    item['o'] = [o or f'Option {i + 1}' for i, o in enumerate(item['o'])]
                    item.pop('os', None)
            by[slug]['M'].append(item)
        for slug, title in lessons:
            for kind, label in (('M', 'MCQ'), ('E', 'Essay & Structured')):
                qs = by[slug][kind]
                if not qs:
                    continue
                st = {'id': f'ictl-{slug}-{label.split()[0].lower()}', 'title': f'{title} · {label}', 'sub': 'Past paper questions by lesson' + (' · answers pending' if kind == 'M' else ' · written answers'),
                      'exam': 'ict', 'lesson': slug, 'qs': qs}
                if kind == 'E':
                    st['kind'] = 'essay'
                sets.append(st)
                report.append(f'{st["id"]}: {len(qs)} questions, {sum(1 for q in qs if q.get("im"))} with images')
    order = ['fund', 'os', 'num', 'logic', 'net', 'web', 'db', 'prog', 'sad', 'l11', 'l12', 'l13']
    sets.sort(key=lambda s: (order.index(s['lesson']), s.get('kind', '')))
    with open(OUT, 'w', encoding='utf8') as f:
        json.dump({'source': 'ictfromabc.com lesson-wise past-paper question PDFs (personal study use)', 'sets': sets}, f, ensure_ascii=False)
    print('\n'.join(report))
    print(f'wrote {OUT}: {sum(len(s["qs"]) for s in sets)} questions in {len(sets)} sets')


if __name__ == '__main__':
    main()
