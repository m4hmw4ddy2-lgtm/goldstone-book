import re,json,glob,os,sys,collections
exec(open('quotecheck.py').read().split("def chapters")[0])
def ngrams(toks, n=3):
    return set(tuple(toks[i:i+n]) for i in range(len(toks)-n+1))
doc_ng={k:ngrams(v.split()) for k,v in corpus.items()}
res=[]
for f in sorted(glob.glob(ROOT+'/chapters/*.md')):
    name=os.path.basename(f)
    for pi,para in enumerate(open(f,encoding='utf-8').read().split('\n\n')):
        parts=para.split('"')
        if len(parts)%2==0: parts=parts[:-1]
        for i in range(1,len(parts),2):
            q=parts[i].strip(); nq=norm(q)
            if len(nq.split())<3: continue
            hit=[k for k,v in corpus.items() if nq in v]
            rec={'chapter':name,'para':pi,'quote':q,'matched':bool(hit),'docs':[h.split('/')[-1] for h in hit[:2]]}
            if not hit:
                g=ngrams(nq.split()); best=None; bs=0
                for k,dg in doc_ng.items():
                    if not g: break
                    s=len(g&dg)/len(g)
                    if s>bs: bs=s;best=k
                rec['best_doc']=(best or '').split('/')[-1]; rec['best_overlap']=round(bs,2)
            res.append(rec)
json.dump(res,open('quotes2.json','w'),indent=1)
u=[x for x in res if not x['matched']]
print(len(res),len(res)-len(u),len(u))
cc=collections.Counter(x['chapter'] for x in u)
print(sorted(cc.items(), key=lambda t:(t[0]!='PROLOGUE.md', int(''.join(d for d in t[0] if d.isdigit()) or 0))))
os.makedirs('unmatched',exist_ok=True)
for ch in cc:
    with open(f'unmatched/{ch}.txt','w') as fo:
        for x in u:
            if x['chapter']==ch:
                fo.write(f"({x['best_overlap']}; {x['best_doc']}) {x['quote']}\n\n")
