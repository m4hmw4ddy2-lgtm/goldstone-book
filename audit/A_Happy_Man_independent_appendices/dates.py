import re,glob,os,datetime
ROOT='/sessions/elegant-adoring-allen/mnt/goldstone-book-main/chapters'
ords={w:i+1 for i,w in enumerate("first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth thirteenth fourteenth fifteenth sixteenth seventeenth eighteenth nineteenth twentieth".split())}
ords.update({'twenty-first':21,'twenty-second':22,'twenty-third':23,'twenty-fourth':24,'twenty-fifth':25,'twenty-sixth':26,'twenty-seventh':27,'twenty-eighth':28,'twenty-ninth':29,'thirtieth':30,'thirty-first':31})
months="January February March April May June July August September October November December".split()
wd="Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
W='|'.join(wd); M='|'.join(months); O='|'.join(sorted(ords,key=len,reverse=True))
pats=[
 re.compile(rf'\b({W})(?:,)? (?:the )?({O}|\d{{1,2}}) (?:of )?({M})(?:,? (\d{{4}}))?'),
 re.compile(rf'\b({W})(?:,)? ({M}) (\d{{1,2}})(?:,? (\d{{4}}))?'),
]
out=[]
for f in sorted(glob.glob(ROOT+'/*.md')):
    t=open(f,encoding='utf-8').read().replace('\n',' ')
    for p in pats:
        for m in p.finditer(t):
            g=m.groups()
            if p is pats[0]:
                w,d,mo,y=g; d=ords.get(d) or int(d)
            else:
                w,mo,d,y=g; d=int(d)
            ctx=t[max(0,m.start()-250):m.start()]
            yrs=re.findall(r'\b(1[89]\d\d)\b',ctx)
            yy=int(y) if y else (int(yrs[-1]) if yrs else None)
            if yy is None: out.append((os.path.basename(f),m.group(0),'no-year','?')); continue
            for cand in ([yy] if y else sorted({yy,yy-1,yy+1})):
                try:
                    dt=datetime.date(cand,months.index(mo)+1,d)
                except ValueError: continue
                ok=wd[dt.weekday()]==w
                if ok or cand==yy: out.append((os.path.basename(f),m.group(0),cand,'OK' if ok else f'MISMATCH actual {wd[dt.weekday()]}'))
                if ok: break
bad=[o for o in out if 'MISMATCH' in o[3] or o[2]=='no-year']
print(len(out),'dates',len(bad),'to review')
for b in bad: print(b)
