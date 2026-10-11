// Pulls question banks from github.com/nastaso/cloudcertprep (MIT, (c) 2026 Alex Santonastaso)
// and writes app/content/<file>.json in the shape app/build.js expects.
// Usage: node tools/sync-cloudcertprep.js [clf|saa|all]   (default: all; then `make content`)
const fs = require('fs');
const path = require('path');

const RAW = 'https://raw.githubusercontent.com/nastaso/cloudcertprep/main/src/data/';
const CHUNK = 50;

const EXAMS = {
  clf: {
    dir: 'clf-c02', out: 'cloudcertprep.json', idPrefix: 'ccp', chunk: true,
    domains: [
      { file: 'domain1.json', d: 'Cloud Concepts', short: 'Concepts' },
      { file: 'domain2.json', d: 'Security', short: 'Security' },
      { file: 'domain3.json', d: 'Technology', short: 'Technology' },
      { file: 'domain4.json', d: 'Billing', short: 'Billing' },
    ],
  },
  saa: {
    dir: 'saa-c03', out: 'saa-c03.json', idPrefix: 'saa', exam: 'saa', chunk: false,
    domains: [
      { file: 'domain1.json', d: 'Secure Architectures', short: 'Secure architectures' },
      { file: 'domain2.json', d: 'Resilient Architectures', short: 'Resilient architectures' },
      { file: 'domain3.json', d: 'High-Performing', short: 'High-performing' },
      { file: 'domain4.json', d: 'Cost-Optimized', short: 'Cost-optimized' },
    ],
  },
};

async function sync(key) {
  const cfg = EXAMS[key];
  const sets = [];
  for (const [di, dom] of cfg.domains.entries()) {
    const res = await fetch(`${RAW}${cfg.dir}/${dom.file}`);
    if (!res.ok) throw new Error(`${cfg.dir}/${dom.file}: HTTP ${res.status}`);
    const items = await res.json();
    const qs = items.map(it => {
      const keys = Object.keys(it.options).sort();
      const a = [].concat(it.answer).map(l => keys.indexOf(l));
      if (a.some(i => i < 0)) throw new Error(`${it.id}: answer not in options`);
      return { d: dom.d, q: it.question, o: keys.map(k => it.options[k]), a, e: (it.explanation || '').trim() };
    });
    const parts = cfg.chunk ? Array.from({ length: Math.ceil(qs.length / CHUNK) }, (_, i) => qs.slice(i * CHUNK, (i + 1) * CHUNK)) : [qs];
    parts.forEach((part, i) => {
      const set = {
        id: cfg.chunk ? `${cfg.idPrefix}${di + 1}_${i + 1}` : `${cfg.idPrefix}${di + 1}`,
        title: cfg.chunk ? `${dom.short} drill ${i + 1} (${part.length})` : `${dom.short} (${part.length})`,
        sub: 'cloudcertprep.io',
        qs: part,
      };
      if (cfg.exam) set.exam = cfg.exam;
      sets.push(set);
    });
    console.log(`${cfg.dir}/${dom.file}: ${qs.length} questions`);
  }
  const out = path.join(__dirname, '..', 'app', 'content', cfg.out);
  fs.writeFileSync(out, JSON.stringify({
    source: 'https://github.com/nastaso/cloudcertprep',
    license: 'MIT, Copyright (c) 2026 Alex Santonastaso',
    sets,
  }));
  console.log(`wrote ${sets.length} sets -> ${out}`);
}

const arg = process.argv[2] || 'all';
const keys = arg === 'all' ? Object.keys(EXAMS) : [arg];
if (keys.some(k => !EXAMS[k])) { console.error('Usage: node tools/sync-cloudcertprep.js [clf|saa|all]'); process.exit(1); }
(async () => { for (const k of keys) await sync(k); })().catch(e => { console.error(e); process.exit(1); });
