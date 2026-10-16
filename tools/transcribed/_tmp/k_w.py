import json,sys,importlib
mod,out,sid=sys.argv[1:4]
m=importlib.import_module(mod)
idx=json.load(open('../../ict-lessons-images.json',encoding='utf8'))
s=[x for x in idx['sets'] if x['id']==sid][0]
ds=[q['d'] for q in s['qs']]
got=[q[0] for q in m.Q]
assert ds==got,(ds,got)
arr=[]
for d,q,qs in m.Q:
    o={"d":d,"q":q.strip()}
    if qs: o["qs"]=qs.strip()
    arr.append(o)
json.dump(arr,open(out,'w',encoding='utf8'),ensure_ascii=False,indent=1)
print(sid,len(arr))
