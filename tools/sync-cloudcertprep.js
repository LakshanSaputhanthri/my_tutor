// Pulls the CLF-C02 question bank from github.com/nastaso/cloudcertprep (MIT, (c) 2026 Alex Santonastaso)
// and writes app/content/cloudcertprep.json in the shape app/build.js expects.
// Usage: node tools/sync-cloudcertprep.js   (then `make content`)
const fs = require('fs');
const path = require('path');

const BASE = 'https://raw.githubusercontent.com/nastaso/cloudcertprep/main/src/data/clf-c02/';
const DOMAINS = [
  { file: 'domain1.json', d: 'Cloud Concepts', short: 'Concepts' },
  { file: 'domain2.json', d: 'Security', short: 'Security' },
  { file: 'domain3.json', d: 'Technology', short: 'Technology' },
  { file: 'domain4.json', d: 'Billing', short: 'Billing' },
];
const CHUNK = 50;
const LETTERS = 'ABCDEFGHIJ';

async function main() {
  const sets = [];
  for (const [di, dom] of DOMAINS.entries()) {
    const res = await fetch(BASE + dom.file);
    if (!res.ok) throw new Error(`${dom.file}: HTTP ${res.status}`);
    const items = await res.json();
    const qs = items.map(it => {
      const keys = Object.keys(it.options).sort();
      const a = [].concat(it.answer).map(l => keys.indexOf(l));
      if (a.some(i => i < 0)) throw new Error(`${it.id}: answer not in options`);
      return { d: dom.d, q: it.question, o: keys.map(k => it.options[k]), a, e: (it.explanation || '').trim() };
    });
    for (let i = 0; i < qs.length; i += CHUNK) {
      const part = qs.slice(i, i + CHUNK);
      const n = i / CHUNK + 1;
      sets.push({
        id: `ccp${di + 1}_${n}`,
        title: `${dom.short} drill ${n} (${part.length})`,
        sub: 'cloudcertprep.io',
        qs: part,
      });
    }
    console.log(`${dom.file}: ${qs.length} questions`);
  }
  const out = path.join(__dirname, '..', 'app', 'content', 'cloudcertprep.json');
  fs.writeFileSync(out, JSON.stringify({
    source: 'https://github.com/nastaso/cloudcertprep',
    license: 'MIT, Copyright (c) 2026 Alex Santonastaso',
    sets,
  }));
  console.log(`wrote ${sets.length} sets -> ${out}`);
}
main().catch(e => { console.error(e); process.exit(1); });
