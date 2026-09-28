import re,json
import pdfplumber
P="/mnt/user-data/uploads/TOEFL IELTS/soal-toefl-01.pdf"
_cache={}
def pagewords(pg):
    if pg not in _cache:
        with pdfplumber.open(P) as pdf:
            page=pdf.pages[pg-1]
            _cache[pg]=[w for w in page.extract_words(x_tolerance=1.5) if 40<w['top']<775]
    return _cache[pg]
def headings(pg):
    ws=pagewords(pg); rows={}
    for w in ws: rows.setdefault(round(w['top']/3.0),[]).append(w)
    out=[]
    for k in sorted(rows):
        line=" ".join(x['text'] for x in sorted(rows[k],key=lambda z:z['x0']))
        m=re.match(r'^\s*(EXERCISE [\d.]+|LESSON \d+|REVIEW TEST [A-Z])\b',line)
        if m: out.append((min(x['top'] for x in rows[k]), m.group(1)))
    return sorted(out)
def full_lines(pg,y0,y1):
    ws=[w for w in pagewords(pg) if y0<=w['top']<y1]
    rows={}
    for w in ws: rows.setdefault(round(w['top']/3.0),[]).append(w)
    return [" ".join(x['text'] for x in sorted(rows[k],key=lambda z:z['x0'])) for k in sorted(rows)]
def col_lines(pg, y0, y1, cut=300):
    ws=[w for w in pagewords(pg) if y0<=w['top']<y1]
    out=[]
    for lo,hi in ((0,cut),(cut,612)):
        rows={}
        for w in [x for x in ws if lo<=x['x0']<hi]: rows.setdefault(round(w['top']/3.0),[]).append(w)
        for k in sorted(rows):
            out.append(" ".join(x['text'] for x in sorted(rows[k],key=lambda z:z['x0'])))
    return out
def exercise_lines(name, pgs, mode='col'):
    lines=[]
    for pg in pgs:
        hs=headings(pg)
        y0,y1=None,10**6
        for i,(y,h) in enumerate(hs):
            if h=='EXERCISE '+name:
                y0=y+8; y1=hs[i+1][0]-4 if i+1<len(hs) else 10**6; break
        if y0 is None:
            # halaman lanjutan: berhenti di judul pertama
            y0=40; y1=hs[0][0]-4 if hs else 10**6
        if mode=='full': lines+=full_lines(pg,y0,y1)
        else: lines+=col_lines(pg,y0,y1,int(mode))
    return lines
def _parse(name,pgs,nmax,mode):
    lines=exercise_lines(name,pgs,mode)
    res={};cur=None;buf=[]
    for l in lines:
        m=re.match(r'^\s*(\d{1,2})\.\s+(\S.*)$',l)
        if m and 1<=int(m.group(1))<=nmax and (cur is None or int(m.group(1))!=cur):
            if cur is not None: res.setdefault(cur,[]).extend(buf)
            cur=int(m.group(1)); buf=[m.group(2)]
        elif cur is not None:
            if re.match(r'^\s*(Directions:|Focus:|www\.|SECTION|LESSON)',l) or re.match(r'^\s*\d{2,3}\s*$',l): continue
            buf.append(l)
    if cur is not None: res.setdefault(cur,[]).extend(buf)
    out={}
    for n,v in res.items():
        s=re.sub(r'\s+',' '," ".join(v)).strip()
        s=re.sub(r'(\w)- (\w)',r'\1\2',s)
        # potong di batas kalimat pertama yang sudah memuat pasangan (a/b)
        parts=re.split(r'(?<=[.?])\s+(?=[A-Z(])',s)
        acc=''
        for p in parts:
            acc=(acc+' '+p).strip()
            if re.search(r'\([^()]{1,40}?/[^()]{1,40}?\)',acc) and acc.rstrip().endswith(('.','?')): break
        out[n]=acc
        # butir lain yang menempel di ekor
        tail=s[len(acc):]
        for m in re.finditer(r'(?:^|\s)(\d{1,2})\.\s+([A-Z(][^\n]*?[.?])(?=\s+\d{1,2}\.|\s*$)',tail):
            k=int(m.group(1))
            if k not in out and k<=nmax: out[k]=re.sub(r'\s+',' ',m.group(2)).strip()
    return out

def parse_items(name,pgs,nmax=30):
    def score(d):
        ok=0
        for v in d.values():
            if len(re.findall(r'\(([^()]{1,40}?)/([^()]{1,40}?)\)',v))==1 and v.rstrip().endswith(('.','?')) and len(v)>35: ok+=1
        return ok
    best=None;bs=-1
    for mode in ('full','280','290','300','310','325'):
        try: d=_parse(name,pgs,nmax,mode)
        except Exception: continue
        s=score(d)
        if s>bs: bs=s; best=d
    return best or {}
