import re, glob, os, html, json, sys
ROOT = '/sessions/elegant-adoring-allen/mnt/goldstone-book-main'
OUT = '/sessions/elegant-adoring-allen/mnt/outputs/work/ind'

def norm(s):
    s = html.unescape(s)
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', ' ').replace('–', ' ').replace('-', ' ').replace('­', '')
    s = s.lower()
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r"[^a-z0-9' ]+", ' ', s)
    s = re.sub(r"'", '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

files = glob.glob(ROOT + '/transcribed/*') + glob.glob(ROOT + '/sources/trial-docs/**/*.txt', recursive=True) \
    + glob.glob(ROOT + '/sources/books/*.html') + glob.glob(ROOT + '/sources/genealogy/*.csv')
corpus = {}
for f in files:
    try:
        t = open(f, encoding='utf-8', errors='ignore').read()
    except Exception:
        continue
    corpus[os.path.relpath(f, ROOT)] = norm(t)
print('corpus docs', len(corpus), file=sys.stderr)

def chapters():
    out = []
    for f in sorted(glob.glob(ROOT + '/chapters/*.md')):
        out.append((os.path.basename(f), open(f, encoding='utf-8').read()))
    return out

qre = re.compile(r'[“"]([^“”"]{12,}?)[”"]')
def ngrams(toks, n=3):
    return set(tuple(toks[i:i+n]) for i in range(len(toks)-n+1))

doc_ngrams = {k: ngrams(v.split()) for k, v in corpus.items()}

res = []
for name, text in chapters():
    for m in qre.finditer(text):
        q = m.group(1).strip()
        nq = norm(q)
        if len(nq.split()) < 4:
            continue
        hit = [k for k, v in corpus.items() if nq in v]
        rec = {'chapter': name, 'quote': q, 'matched': bool(hit), 'docs': hit[:3]}
        if not hit:
            g = ngrams(nq.split())
            best = None; bs = 0
            for k, dg in doc_ngrams.items():
                if not g: break
                s = len(g & dg) / len(g)
                if s > bs:
                    bs = s; best = k
            rec['best_doc'] = best; rec['best_overlap'] = round(bs, 2)
        res.append(rec)
json.dump(res, open(OUT + '/quotes.json', 'w'), indent=1)
tot = len(res); mt = sum(1 for r in res if r['matched'])
print('quotes', tot, 'matched', mt, 'unmatched', tot - mt)
