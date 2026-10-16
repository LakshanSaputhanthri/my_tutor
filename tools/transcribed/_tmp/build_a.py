import json,sys
sys.path.insert(0,'.')
from a1 import B1
from a2 import B2
from a3 import B3
from a4 import B4
from a5 import B5
out=[]
for b in B1+B2+B3+B4+B5:
    o=dict(b)
    if 'os' in o and len(o['os'])!=len(o['o']): print('os mismatch',o['n'])
    assert 4<=len(o['o'])<=5 and all(o['o'])
    out.append(o)
assert [x['n'] for x in out]==list(range(1,37)),[x['n'] for x in out]
json.dump(out,open('../ictl-os-mcq.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out))
