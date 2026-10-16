#!/usr/bin/env python3
"""Imports AL ICT past-paper MCQ explanation PDFs (app/content/ict-pdfs/*.pdf) into app/content/ict-al.json.

English text is read as-is. Sinhala in these PDFs uses legacy fonts (4u-Chami / FMMalithi), so it is
separated by font name and converted to Unicode with tools/fm2uni.py.

Usage: python tools/import-ict-pdfs.py [--report]
"""
import json, re, sys, glob, os
import pymupdf

sys.path.insert(0, os.path.dirname(__file__))
from fm2uni import fm_to_unicode

ROOT = os.path.join(os.path.dirname(__file__), '..')
PDF_DIR = os.path.join(ROOT, 'app', 'content', 'ict-pdfs')
OUT = os.path.join(ROOT, 'app', 'content', 'ict-al.json')
LEGACY = re.compile(r'Chami|Malithi|Abhaya|Kaputa', re.I)
WATERMARK = re.compile(r'Bandaranayake|ictfromabc|RAVINDU|All Rights Reserved|Information and Communication Technology\s*$|^\s*\d{4} AL ', re.I)


def lines_of(doc):
    """Yield (page, x, y, english, sinhala_raw) for every text line, in reading order."""
    for pn, page in enumerate(doc):
        for b in page.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                spans = l['spans']
                eng = ''.join(s['text'] for s in spans if not LEGACY.search(s['font']))
                sin = ''.join(s['text'] for s in spans if LEGACY.search(s['font']))
                x = round(min((s['bbox'][0] for s in spans), default=l['bbox'][0]))
                if eng.strip() or sin.strip():
                    yield pn, x, round(l['bbox'][1]), eng.rstrip(), sin.strip(), spans


def clean(t):
    return re.sub(r'[ \t]+', ' ', t).strip()


def parse_mcq(doc):
    """Return list of dicts for the MCQ REVIEW section."""
    rows = sorted(lines_of(doc), key=lambda r: (r[0], r[2] // 3, r[1]))
    # MCQ section: from first "MCQ REVIEW" to "S.ESSAY"/"ESSAY REVIEW"
    start = next((i for i, r in enumerate(rows) if re.search(r'MCQ REVIEW', r[3])), None)
    if start is None:
        return []
    end = next((i for i, r in enumerate(rows) if i > start and re.search(r'ESSAY REVIEW', r[3])), len(rows))
    rows = [r for r in rows[start + 1:end] if not WATERMARK.search(r[3]) or re.match(r'\s*\d+\.', r[3])]

    qs, cur, want = [], None, 1
    for pn, x, y, eng, sin, spans in rows:
        m = re.match(r'\s*(\d+)\.\s+(\S.*)?$', eng)
        if m and int(m.group(1)) == want and cur is None or (m and int(m.group(1)) == want and cur and cur['state'] != 'stem'):
            if cur: qs.append(cur)
            cur = {'n': want, 'state': 'stem', 'stem': [m.group(2) or ''], 'stem_x': x, 'sin_stem': [sin] if sin else [],
                   'opts': {}, 'opt_sin': {}, 'opt_pos': {}, 'answer': None, 'exp': {}, 'exp_sin': {}, 'cur_exp': None, 'pages': {pn}}
            want += 1
            continue
        if not cur:
            continue
        cur['pages'].add(pn)
        a = re.match(r'\s*Answer\s*:\s*([\d,\s\)and]+)', eng)
        if a and cur['state'] in ('opts', 'stem'):
            cur['answer'] = [int(d) for d in re.findall(r'\d', a.group(1))]
            cur['state'] = 'exp'
            continue
        if cur['state'] == 'exp' or cur['answer'] is not None:
            om = re.match(r'\s*Option\s*/?\s*(\d)\)', eng)
            if om:
                cur['cur_exp'] = int(om.group(1))
                rest = eng[om.end():].strip()
                cur['exp'].setdefault(cur['cur_exp'], [])
                cur['exp_sin'].setdefault(cur['cur_exp'], [])
                if rest:
                    cur['exp'][cur['cur_exp']].append(rest)
                continue
            if cur['cur_exp'] and not re.match(r'\s*Explanation', eng):
                if eng.strip():
                    cur['exp'][cur['cur_exp']].append(eng.strip())
                if sin:
                    cur['exp_sin'][cur['cur_exp']].append(sin)
            continue
        # stem or options
        mk = [(int(mm.group(1)), mm.start()) for mm in re.finditer(r'(?:(?<=\s)|^)([1-5])\)\s', eng + ' ')]
        if mk or cur['state'] == 'opts':
            if mk:
                cur['state'] = 'opts'
                # split a line holding several option markers (multi-column layouts)
                for k, (num, pos) in enumerate(mk):
                    nxt = mk[k + 1][1] if k + 1 < len(mk) else len(eng)
                    body = eng[pos:nxt]
                    body = re.sub(r'^\s*[1-5]\)\s*', '', body)
                    cur['opts'][num] = [body.strip()] if body.strip() else []
                    cur['opt_sin'][num] = [sin] if (sin and len(mk) == 1) else []
                    cur['opt_pos'][num] = (x, y)
                    cur['last_opt'] = num
            else:
                # continuation line of an option (multi-line / code options)
                lo = cur.get('last_opt')
                best = None
                for num, (ox, oy) in cur['opt_pos'].items():
                    if x >= ox - 3 and y >= oy - 2 and (best is None or ox > cur['opt_pos'][best][0] or (ox == cur['opt_pos'][best][0] and oy > cur['opt_pos'][best][1])):
                        best = num
                best = best or lo
                if best:
                    if eng.strip(): cur['opts'][best].append(eng.strip())
                    if sin: cur['opt_sin'][best].append(sin)
            continue
        # still in the stem: keep indentation for code
        indent = ' ' * max(0, (x - cur['stem_x']) // 5)
        if eng.strip():
            cur['stem'].append(indent + eng.strip())
        if sin:
            cur['sin_stem'].append(sin)
    if cur:
        qs.append(cur)
    return qs


def build(year, raw):
    out, bad = [], []
    for r in raw:
        opts = [clean(' '.join(r['opts'].get(i, []))) if len(r['opts'].get(i, [])) < 2 or not any(re.search(r'[;{}()=]', t) for t in r['opts'][i]) else '\n'.join(r['opts'][i]) for i in range(1, 6)]
        opts = [o.rstrip('/ ').strip() for o in opts]
        if not r['answer'] or any(not o for o in opts):
            bad.append((r['n'], 'answer' if not r['answer'] else 'options'))
            continue
        stem = [ln for ln in r['stem']]
        # drop the trailing English-only repeat of the Sinhala question line artifacts
        q = '\n'.join(s for s in stem if s.strip()).strip()
        letters = 'ABCDE'
        exp_parts = [f"{letters[k - 1]}) " + clean(' '.join(v)) for k, v in sorted(r['exp'].items()) if 1 <= k <= 5 and v]
        item = {'d': f'{year} Paper', 'q': q, 'o': opts, 'a': [a - 1 for a in r['answer'] if 1 <= a <= 5], 'e': '\n'.join(exp_parts)}
        if item['a'] == []:
            bad.append((r['n'], 'answer'))
            continue
        qs_si = fm_to_unicode(' '.join(r['sin_stem']))
        if qs_si:
            item['qs'] = qs_si
        os_si = [fm_to_unicode(' '.join(r['opt_sin'].get(i, []))) for i in range(1, 6)]
        item['os'] = [o or opts[i] for i, o in enumerate(os_si)] if any(os_si) else None
        if item['os'] is None:
            del item['os']
        es_si = [f"{letters[k - 1]}) " + fm_to_unicode(' '.join(v)) for k, v in sorted(r['exp_sin'].items()) if 1 <= k <= 5 and v]
        if es_si:
            item['es'] = '\n'.join(es_si)
        item['n'] = r['n']
        out.append(item)
    return out, bad


def main():
    sets, report = [], []
    for path in sorted(glob.glob(os.path.join(PDF_DIR, '*.pdf'))):
        m = re.search(r'(\d{4})', os.path.basename(path))
        if not m:
            continue
        year = m.group(1)
        doc = pymupdf.open(path)
        raw = parse_mcq(doc)
        qs, bad = build(year, raw)
        report.append(f'{year}: {len(qs)} questions imported, {len(raw)} found, skipped {bad}')
        if qs:
            sets.append({'id': f'ict{year}', 'title': f'{year} A/L Paper · MCQ', 'sub': 'Past paper MCQs with explanations',
                         'exam': 'ict', 'qs': qs})
    sets.sort(key=lambda s: s['id'], reverse=True)
    with open(OUT, 'w', encoding='utf8') as f:
        json.dump({'source': 'ictfromabc.com free past-paper explanation PDFs (personal study use)', 'sets': sets}, f, ensure_ascii=False)
    print('\n'.join(report))
    print(f'wrote {OUT}: {sum(len(s["qs"]) for s in sets)} questions in {len(sets)} sets')


if __name__ == '__main__':
    main()
