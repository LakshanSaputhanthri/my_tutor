// Builds the app from the episode markdown files: node build.js
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const EPISODES = [
  { file: 'ep01_intro_cloud_concepts.md', id: 'ep1', short: 'Cloud Concepts', domain: 'Cloud Concepts' },
  { file: 'ep02_security_compliance.md', id: 'ep2', short: 'Security', domain: 'Security' },
  { file: 'ep03_compute_storage_databases.md', id: 'ep3', short: 'Compute, Storage, Databases', domain: 'Technology' },
  { file: 'ep04_networking_analytics_ai_more.md', id: 'ep4', short: 'Networking, AI, More', domain: 'Technology' },
  { file: 'ep05_billing_pricing_support.md', id: 'ep5', short: 'Billing and Support', domain: 'Billing' },
  { file: 'ep06_exam_strategy_final_revision.md', id: 'ep6', short: 'Strategy + Mock Exam', domain: 'Mock exam' },
];

const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
function inline(s) {
  return esc(s)
    .replace(/\*\*(.+?)\*\*/g, '<b>$1</b>')
    .replace(/(^|[^*\w])\*([^*\s][^*]*?)\*(?![*\w])/g, '$1<i>$2</i>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
}

function md(src) {
  const lines = src.replace(/\r/g, '').split('\n');
  const out = [];
  let para = [];
  const flush = () => { if (para.length) { out.push(`<p>${inline(para.join(' '))}</p>`); para = []; } };
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (!line.trim()) { flush(); continue; }
    let m;
    if ((m = line.match(/^(#{1,4})\s+(.*)$/))) {
      flush(); const lv = Math.min(m[1].length + 1, 5);
      out.push(`<h${lv}>${inline(m[2])}</h${lv}>`); continue;
    }
    if (/^---+\s*$/.test(line)) { flush(); out.push('<hr>'); continue; }
    if (/^>/.test(line)) {
      flush(); const buf = [];
      while (i < lines.length && /^>/.test(lines[i])) { buf.push(lines[i].replace(/^>\s?/, '')); i++; }
      i--; out.push(`<blockquote>${md(buf.join('\n'))}</blockquote>`); continue;
    }
    if (/^\|/.test(line)) {
      flush(); const rows = [];
      while (i < lines.length && /^\|/.test(lines[i])) { rows.push(lines[i]); i++; }
      i--;
      const cells = r => r.trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim());
      const head = cells(rows[0]);
      const body = rows.slice(2).map(cells);
      out.push(`<div class="tablewrap"><table><thead><tr>${head.map(c => `<th>${inline(c)}</th>`).join('')}</tr></thead><tbody>${body.map(r => `<tr>${r.map(c => `<td>${inline(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`);
      continue;
    }
    if (/^\s*[-*]\s+/.test(line)) {
      flush(); const items = [];
      while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) { items.push(lines[i].replace(/^\s*[-*]\s+/, '')); i++; }
      i--;
      out.push(`<ul>${items.map(t => t.startsWith('[ ] ') ? `<li class="task">${inline(t.slice(4))}</li>` : `<li>${inline(t)}</li>`).join('')}</ul>`);
      continue;
    }
    if (/^\s*\d+\.\s+/.test(line)) {
      flush(); const items = [];
      while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) { items.push(lines[i].replace(/^\s*\d+\.\s+/, '')); i++; }
      i--; out.push(`<ol>${items.map(t => `<li>${inline(t)}</li>`).join('')}</ol>`); continue;
    }
    para.push(line.trim());
  }
  flush();
  return out.join('\n');
}

function parseQuestions(qText) {
  const qs = {};
  const chunks = qText.split(/\n(?=\*\*Q\d+\.\*\*)/).filter(c => /^\*\*Q\d+\.\*\*/.test(c));
  for (const chunk of chunks) {
    const n = +chunk.match(/^\*\*Q(\d+)\.\*\*/)[1];
    let body = chunk.replace(/^\*\*Q\d+\.\*\*\s*/, '');
    body = body.split('\n').filter(l => l.trim() && !/^#/.test(l) && !/^---/.test(l)).join('\n');
    let stem, opts = [];
    if (body.includes('→ A.')) {
      const [s, o] = body.split('→');
      stem = s.trim();
      opts = [...o.matchAll(/([A-E])\.\s(.*?)(?=\s[A-E]\.\s|$)/g)].map(m => m[2].trim());
    } else {
      const sl = [];
      for (const l of body.split('\n')) {
        const m = l.match(/^([A-E])\.\s+(.*)$/);
        if (m) opts.push(m[2].trim()); else sl.push(l.trim());
      }
      stem = sl.join(' ');
    }
    qs[n] = { q: stem, o: opts };
  }
  return qs;
}

function parseAnswers(aText) {
  const ans = {};
  for (const m of aText.matchAll(/\*\*Q(\d+) — ([A-E](?:,\s*[A-E])*)\.?\*\*\.?\s*([^·\n]*)/g)) {
    ans[+m[1]] = { a: m[2].split(/,\s*/).map(x => 'ABCDE'.indexOf(x)), e: m[3].trim() };
  }
  for (const m of aText.matchAll(/^\|\s*(\d+)\s*\|\s*\*\*([A-E](?:,\s*[A-E])*)\*\*\s*\|\s*(.*?)\s*\|\s*$/gm)) {
    ans[+m[1]] = { a: m[2].split(/,\s*/).map(x => 'ABCDE'.indexOf(x)), e: m[3].trim() };
  }
  return ans;
}

const lessons = [];
const lessonSrc = {};
const sets = [];
const problems = [];

// Markdown → simple blocks for the Flutter app (inline text keeps **bold**).
function mdBlocks(src) {
  const lines = src.replace(/\r/g, '').split('\n');
  const out = [];
  let para = [];
  const flush = () => { if (para.length) { out.push({ t: 'p', x: para.join(' ') }); para = []; } };
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (!line.trim()) { flush(); continue; }
    let m;
    if ((m = line.match(/^(#{1,4})\s+(.*)$/))) { flush(); out.push({ t: 'h', l: m[1].length, x: m[2] }); continue; }
    if (/^---+\s*$/.test(line)) { flush(); out.push({ t: 'hr' }); continue; }
    if (/^>/.test(line)) {
      flush(); const buf = [];
      while (i < lines.length && /^>/.test(lines[i])) { buf.push(lines[i].replace(/^>\s?/, '')); i++; }
      i--; out.push({ t: 'q', b: mdBlocks(buf.join('\n')) }); continue;
    }
    if (/^\|/.test(line)) {
      flush(); const rows = [];
      while (i < lines.length && /^\|/.test(lines[i])) { rows.push(lines[i]); i++; }
      i--;
      const cells = r => r.trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim());
      out.push({ t: 'table', rows: [cells(rows[0])].concat(rows.slice(2).map(cells)) }); continue;
    }
    if (/^\s*[-*]\s+/.test(line) || /^\s*\d+\.\s+/.test(line)) {
      flush(); const ordered = /^\s*\d+\./.test(line); const items = [];
      const re = ordered ? /^\s*\d+\.\s+/ : /^\s*[-*]\s+/;
      while (i < lines.length && re.test(lines[i])) { items.push(lines[i].replace(re, '').replace(/^\[ \] /, '☐ ')); i++; }
      i--; out.push({ t: ordered ? 'ol' : 'ul', items }); continue;
    }
    para.push(line.trim());
  }
  flush();
  return out;
}
const htmlToMarks = s => s.replace(/<b>(.*?)<\/b>/g, '**$1**').replace(/<mark>(.*?)<\/mark>/g, '[[$1]]').replace(/<[^>]+>/g, '');

for (const ep of EPISODES) {
  const src = fs.readFileSync(path.join(ROOT, 'episodes', ep.file), 'utf8').replace(/\r/g, '');
  const title = src.match(/^#\s+(.*)$/m)[1];
  const start = src.search(/^## (Practice Questions|4\. Mock Exam)/m);
  const end = src.search(/^## Closing/m);
  const practice = src.slice(start, end);
  const lessonMd = (src.slice(0, start) + src.slice(end)).replace(/^#\s+.*\n/, '');
  lessons.push({ id: ep.id, title, short: ep.short, html: md(lessonMd) });
  lessonSrc[ep.id] = lessonMd;

  const ansStart = practice.search(/^#{2,3} (Answers|Mock Exam Answers)/m);
  const qs = parseQuestions(practice.slice(0, ansStart));
  const ans = parseAnswers(practice.slice(ansStart));
  const list = Object.keys(qs).map(Number).sort((a, b) => a - b).map(n => {
    const x = ans[n];
    if (!x) problems.push(`${ep.id} Q${n}: no answer`);
    if (qs[n].o.length < 2) problems.push(`${ep.id} Q${n}: options not parsed`);
    let d = ep.domain;
    if (ep.id === 'ep6') d = n <= 7 ? 'Cloud Concepts' : n <= 16 ? 'Security' : n <= 26 ? 'Technology' : 'Billing';
    return { d, q: qs[n].q, o: qs[n].o, a: x ? x.a : [0], e: x ? x.e : '' };
  });
  sets.push({ id: ep.id, title: ep.id === 'ep6' ? 'Mock exam (30)' : `Episode ${ep.id.slice(2)} · ${ep.short}`, qs: list });
}

const MOCKS = [
  { id: 'mock2', file: 'mock2.md', title: 'Mock exam 2 (65)' },
  { id: 'mock3', file: 'mock3.md', title: 'Mock exam 3 · What is it? (65)' },
];
for (const mk of MOCKS) {
  const src = fs.readFileSync(path.join(__dirname, 'content', mk.file), 'utf8').replace(/\r/g, '');
  const cut = src.search(/^### Answers/m);
  const qs = parseQuestions(src.slice(0, cut));
  const ans = parseAnswers(src.slice(cut));
  const list = Object.keys(qs).map(Number).sort((a, b) => a - b).map(n => {
    if (!ans[n]) problems.push(`${mk.id} Q${n}: no answer`);
    if (qs[n].o.length < 2) problems.push(`${mk.id} Q${n}: options not parsed`);
    if (ans[n] && ans[n].a.some(i => i >= qs[n].o.length)) problems.push(`${mk.id} Q${n}: answer letter has no option`);
    const d = n <= 16 ? 'Cloud Concepts' : n <= 36 ? 'Security' : n <= 58 ? 'Technology' : 'Billing';
    return { d, q: qs[n].q, o: qs[n].o, a: ans[n] ? ans[n].a : [0], e: ans[n] ? ans[n].e : '' };
  });
  if (list.length !== 65) problems.push(`${mk.id} has ${list.length} questions, expected 65`);
  sets.push({ id: mk.id, title: mk.title, qs: list });
}

// Extra practice per episode: content/extra_epN.md (same format as the mocks)
for (const ep of EPISODES) {
  const file = path.join(__dirname, 'content', `extra_${ep.id}.md`);
  if (!fs.existsSync(file)) continue;
  const src = fs.readFileSync(file, 'utf8').replace(/\r/g, '');
  const cut = src.search(/^### Answers/m);
  const qs = parseQuestions(src.slice(0, cut));
  const ans = parseAnswers(src.slice(cut));
  const list = Object.keys(qs).map(Number).sort((a, b) => a - b).map(n => {
    const id = `x${ep.id.slice(2)} Q${n}`;
    if (!ans[n]) problems.push(`${id}: no answer`);
    if (qs[n].o.length < 2) problems.push(`${id}: options not parsed`);
    if (ans[n] && ans[n].a.some(i => i >= qs[n].o.length)) problems.push(`${id}: answer letter has no option`);
    return { d: ep.domain, q: qs[n].q, o: qs[n].o, a: ans[n] ? ans[n].a : [0], e: ans[n] ? ans[n].e : '' };
  });
  sets.push({ id: `x${ep.id.slice(2)}`, title: `Episode ${ep.id.slice(2)} · More practice (${list.length})`, sub: ep.short, qs: list });
}

// Imported bank (tools/sync-cloudcertprep.js): content/cloudcertprep.json
const ccpFile = path.join(__dirname, 'content', 'cloudcertprep.json');
if (fs.existsSync(ccpFile)) {
  for (const s of JSON.parse(fs.readFileSync(ccpFile, 'utf8')).sets) {
    s.qs.forEach((x, i) => {
      if (x.a.some(k => k >= x.o.length)) problems.push(`${s.id} Q${i + 1}: answer index has no option`);
    });
    sets.push(s);
  }
}

// SAA-C03 bank (tools/sync-cloudcertprep.js saa): content/saa-c03.json. Sets carry exam:'saa'; sets without `exam` belong to CLF-C02.
const saaFile = path.join(__dirname, 'content', 'saa-c03.json');
if (fs.existsSync(saaFile)) {
  for (const s of JSON.parse(fs.readFileSync(saaFile, 'utf8')).sets) {
    s.exam = 'saa';
    s.qs.forEach((x, i) => {
      if (x.a.some(k => k >= x.o.length)) problems.push(`${s.id} Q${i + 1}: answer index has no option`);
    });
    sets.push(s);
  }
}

// AL ICT bank (bilingual): content/ict-al.json. Sets carry exam:'ict'; a question may add qs/os/es (Sinhala question, options, explanation).
// Lesson-wise bank (content/ict-lessons.json): MCQs with pending answers (a:[]) shown as page images (im:[...] under static/ictq),
// plus essay/structured sets (kind:'essay') that are read-only images.
for (const file of ['ict-lessons.json', 'ict-al.json']) {
  const ictFile = path.join(__dirname, 'content', file);
  if (!fs.existsSync(ictFile)) continue;
  for (const s of JSON.parse(fs.readFileSync(ictFile, 'utf8')).sets) {
    s.exam = 'ict';
    s.qs.forEach((x, i) => {
      if (x.a.some(k => k >= x.o.length)) problems.push(`${s.id} Q${i + 1}: answer index has no option`);
      if (x.os && x.os.length !== x.o.length) problems.push(`${s.id} Q${i + 1}: Sinhala options count differs`);
      for (const im of x.im || []) if (!fs.existsSync(path.join(__dirname, 'static', im))) problems.push(`${s.id} Q${i + 1}: missing image ${im}`);
    });
    sets.push(s);
  }
}

const cheat = fs.readFileSync(path.join(__dirname, 'content', 'cheatsheet.md'), 'utf8').replace(/\r/g, '');
lessons.push({ id: 'cheat', title: cheat.match(/^#\s+(.*)$/m)[1], short: 'Exam night', html: md(cheat.replace(/^#\s+.*\n/, '')) });
lessonSrc.cheat = cheat.replace(/^#\s+.*\n/, '');

if (problems.length) { console.error('PARSE PROBLEMS:\n' + problems.join('\n')); process.exit(1); }

const bridge = JSON.parse(fs.readFileSync(path.join(__dirname, 'content', 'bridge.json'), 'utf8'));
const data = JSON.stringify({ lessons, sets, ...bridge }).replace(/<\//g, '<\\/');
const template = fs.readFileSync(path.join(__dirname, 'template.html'), 'utf8');
const page = template.replace('/*__DATA__*/', `window.DATA=${data};`);

const appHead = '<!doctype html>\n<html lang="si">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="theme-color" content="#0D676B">\n<link rel="manifest" href="manifest.webmanifest">\n<link rel="icon" href="icon-192.png">\n</head>\n<body>\n';
fs.mkdirSync(path.join(__dirname, 'dist'), { recursive: true });
fs.writeFileSync(path.join(__dirname, 'dist', 'index.html'), appHead + page + '\n</body>\n</html>\n');
fs.writeFileSync(path.join(__dirname, 'artifact.html'), page);
const copyDir = (from, to) => {
  fs.mkdirSync(to, { recursive: true });
  for (const f of fs.readdirSync(from, { withFileTypes: true })) {
    f.isDirectory() ? copyDir(path.join(from, f.name), path.join(to, f.name)) : fs.copyFileSync(path.join(from, f.name), path.join(to, f.name));
  }
};
copyDir(path.join(__dirname, 'static'), path.join(__dirname, 'dist'));

const flutterAssets = path.join(ROOT, 'flutter_app', 'assets');
if (fs.existsSync(path.dirname(flutterAssets))) {
  fs.mkdirSync(flutterAssets, { recursive: true });
  const flutterData = {
    lessons: lessons.map(l => ({ id: l.id, title: l.title, short: l.short, blocks: mdBlocks(lessonSrc[l.id]) })),
    sets,
    words: bridge.words,
    patterns: bridge.patterns.map(p => p.map(htmlToMarks)),
    bridge: bridge.bridge,
    pairs: bridge.pairs,
  };
  fs.writeFileSync(path.join(flutterAssets, 'content.json'), JSON.stringify(flutterData));
  console.log('Flutter content.json written');
}

const total = sets.reduce((s, x) => s + x.qs.length, 0);
console.log(`OK: ${lessons.length} lessons, ${sets.length} sets, ${total} questions`);
sets.forEach(s => console.log(`  ${s.id}: ${s.qs.length} questions`));
