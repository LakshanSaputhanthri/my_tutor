#!/usr/bin/env python3
"""Builds app/content/ict-lessons.json (text only) from tools/transcribed/*.json (agent transcriptions of the PDF page images,
listed in tools/ict-lessons-images.json). Answers stay pending (a: [])."""
import json, os, glob
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
T = os.path.join(ROOT, 'tools', 'transcribed')
src = json.load(open(os.path.join(ROOT, 'tools', 'ict-lessons-images.json'), encoding='utf8'))
out, problems = [], []
for s in src['sets']:
    f = os.path.join(T, s['id'] + '.json')
    if os.path.exists(f):
        rows = json.load(open(f, encoding='utf8'))
    else:
        rows = []
        for p in sorted(glob.glob(os.path.join(T, s['id'] + '.part*.json'))):
            rows += json.load(open(p, encoding='utf8'))
    if len(rows) != len(s['qs']):
        problems.append(f"{s['id']}: {len(rows)} transcribed vs {len(s['qs'])} expected")
        continue
    essay = s.get('kind') == 'essay'
    qs = []
    for i, (r, o) in enumerate(zip(rows, s['qs'])):
        q = {'q': (r.get('q') or '').strip(), 'o': [] if essay else [str(x).strip() for x in r.get('o', [])], 'a': [], 'd': o['d']}
        if not essay:
            q['n'] = r.get('n') or o.get('n')
            if not 4 <= len(q['o']) <= 5 or not all(q['o']):
                problems.append(f"{s['id']} #{i + 1}: options {len(q['o'])}")
        if r.get('qs'):
            q['qs'] = r['qs'].strip()
        if not essay and r.get('os'):
            if len(r['os']) == len(q['o']):
                q['os'] = [str(x).strip() for x in r['os']]
            else:
                problems.append(f"{s['id']} #{i + 1}: Sinhala options {len(r['os'])} vs {len(q['o'])}, dropped")
        if not q['q']:
            problems.append(f"{s['id']} #{i + 1}: empty question")
        qs.append(q)
    t = {k: v for k, v in s.items() if k != 'qs'}
    t['qs'] = qs
    out.append(t)
json.dump({'source': src['source'], 'sets': out}, open(os.path.join(ROOT, 'app', 'content', 'ict-lessons.json'), 'w', encoding='utf8'), ensure_ascii=False)
print('\n'.join(problems) or 'no problems')
print(sum(len(s['qs']) for s in out), 'questions in', len(out), 'sets')
