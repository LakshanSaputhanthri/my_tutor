"""Segments the lesson-wise past-paper PDFs (al-question-pdf/*.pdf) into questions.

Every question in these PDFs ends with a bold tag line such as "( 2011 - 06 )" (MCQ) or "( 2013 S.ESSAY - 01 )"
(essay / structured). A segment is everything between the previous tag block and the next one.
"""
import re
import pymupdf

TAG = re.compile(r'^\(\s*(20\d\d)\s*[^\w\s]?\s*(?:(S\.?\s*ESSAY|ESSAY)\s*)?[^\w\s]?\s*(\d+)?\s*(\[[a-z]\])?\s*\)$', re.I)
LEGACY = re.compile(r'Chami|Malithi|Abhaya|Kaputa|Sawana', re.I)
LESSON = re.compile(r'^(?:LESSON\s+(\d+)|([A-Z][A-Z ]+?))\s+PAST PAPERS', re.I)
FOOTER = re.compile(r'^(ictfromabc\.com|\d{1,3})$')


def page_lines(page):
    """All text lines on a page, top to bottom, with their y-extent."""
    out = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            spans = l['spans']
            eng = ''.join(s['text'] for s in spans if not LEGACY.search(s['font'])).strip()
            sin = ''.join(s['text'] for s in spans if LEGACY.search(s['font'])).strip()
            if not (eng or sin):
                continue
            x = min(s['bbox'][0] for s in spans)
            out.append({'x': x, 'y0': l['bbox'][1], 'y1': l['bbox'][3], 'eng': eng, 'sin': sin,
                        'raw': ''.join(s['text'] for s in spans).strip(), 'spans': spans})
    out.sort(key=lambda r: (round(r['y0'] / 3), r['x']))
    return out


def segment(path):
    """Return (segments, headings). A segment: dict(kind, tags, pages:{pn:(y0,y1)}, lines:[(pn,line)])."""
    doc = pymupdf.open(path)
    segs, cur, headings = [], {'lines': [], 'pages': {}}, []
    pending_tags = []
    for pn, page in enumerate(doc):
        H = page.rect.height
        for ln in page_lines(page):
            t = ln['raw']
            if ln['y0'] > H - 60 and FOOTER.match(t):
                continue
            if t == 'ictfromabc.com' or (ln['y0'] < 45 and FOOTER.match(t)):
                continue
            m = LESSON.match(t)
            if m:
                headings.append((pn, ln['y0'], t.title() if not m.group(1) else f'Lesson {m.group(1)}'))
                continue
            tg = TAG.match(t)
            if tg and len(t) < 40:
                pending_tags.append((tg.group(1), 'E' if tg.group(2) else 'M', tg.group(3), tg.group(4), ln['y1'], pn))
                continue
            if pending_tags:       # first content line after a tag block closes the previous segment
                cur['tags'] = pending_tags
                segs.append(cur)
                cur, pending_tags = {'lines': [], 'pages': {}}, []
            cur['lines'].append((pn, ln))
    if pending_tags:
        cur['tags'] = pending_tags
        segs.append(cur)
    return doc, merge_orphans(segs), headings


NUMLINE = re.compile(r'^\s*(\d+)\s*\.\s*(\(|\S|$)')


def is_tail(ln):
    e = ln['eng']
    return (not e) or bool(re.match(r'^\(?[1-5]\)$', e)) or bool(re.match(r'^[1-5]\)\s', e)) or len(e) <= 3


def merge_orphans(segs):
    """A tag usually sits right after the English text, so the Sinhala line(s) / last option of a question can end up
    after it. Move such leading tail lines of a segment back to the previous segment; glue number-less segments."""
    out = []
    for s in segs:
        L = s['lines']
        has_num = any(NUMLINE.match(l['eng']) and l['x'] < 90 for _, l in L)
        if out and L and out[-1]['tags'][0][1] == s['tags'][0][1]:
            if not has_num:
                out[-1]['lines'] += L
                out[-1]['tags'] += s['tags']
                continue
            k = 0
            while k < len(L) and not (NUMLINE.match(L[k][1]['eng']) and L[k][1]['x'] < 90) and is_tail(L[k][1]):
                k += 1
            if k:
                out[-1]['lines'] += L[:k]
                s['lines'] = L[k:]
        out.append(s)
    return out
