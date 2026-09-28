import re, json
T=open('/home/claude/txt/barron.txt').read()
PAGES=T.split('\f')

def clean(s):
    s=s.replace('—','-').replace('–','-').replace('’',"'").replace('“','"').replace('”','"')
    s=re.sub(r'[ \t]+',' ',s)
    return s.strip()

def norm_page(p):
    p=re.sub(r'^\s*\d{1,3}\s+A ?c ?a ?d ?e ?m ?i ?c.*$','',p,flags=re.M|re.I)
    p=re.sub(r'^.*A ?c ?a ?d ?e ?m ?i ?c\s*M ?o ?d ?u ?l ?e.*$','',p,flags=re.M|re.I)
    p=re.sub(r'^.*G ?e ?n ?e ?r ?a ?l\s*T ?r ?a ?i ?n ?i ?n ?g.*$','',p,flags=re.M|re.I)
    p=re.sub(r'^\s*\d{1,3}\s*$','',p,flags=re.M)
    return p

def qnum_fix(s):   # "Questions 2 1 -2 3" -> (21,23)
    s=re.sub(r'[\u2010-\u2015\u2212]','-',s)
    d=re.sub(r'[^\d\-]','',s.replace(' ',''))
    m=re.match(r'(\d+)-?(\d+)?',d)
    return (int(m.group(1)), int(m.group(2)) if m.group(2) else int(m.group(1))) if m else None

def sections(kind='ACADEMIC'):
    """kembalikan daftar (label, halaman_awal, halaman_akhir) tiap tes"""
    marks=[]
    for i,p in enumerate(PAGES,1):
        if re.search(r'^\s*(ACADEMIC MODULE|GENERAL TRAINING MODULE)\s*$',p,re.M) and \
           re.search(r'^\s*PRACTICE TEST\s*(\d)',p,re.M):
            n=re.search(r'^\s*PRACTICE TEST\s*(\d)',p,re.M).group(1)
            mod='AC' if 'ACADEMIC' in p else 'GT'
            marks.append((f"{mod}{n}",i))
    out=[]
    for j,(lab,st) in enumerate(marks):
        en=marks[j+1][1]-1 if j+1<len(marks) else len(PAGES)
        out.append((lab,st,en))
    return out

RANGES={'AC1':(11,42),'AC2':(43,73),'AC3':(74,104),'AC4':(105,135),'AC5':(136,165),
        'AC6':(166,197),'GT1':(198,217),'GT2':(218,236),'GT3':(237,257),
        'GT4':(258,276),'GT5':(277,297),'GT6':(298,318)}

def key_pages(lab):
    a,b=RANGES[lab]; out=[]
    for pg in range(a,b+1):
        p=PAGES[pg-1]
        n=len(re.findall(r'(?<![\d.])\d{1,2}\.\s+\S',p))
        heads=len(re.findall(r'^\s*(Listening|Reading|Writing|Speaking)\s*$',p,re.M))
        expl=len(re.findall(r'\d{1,2}\.\s+\S[^\n]{40,}',p))
        heads2=len(re.findall(r'^\s*(Listening|Reading|Heading|Beading|Writing|Speaking)\s*$',p,re.M))
        if n>=14 and expl<n*0.5 and (heads2>=1 or re.search(r'A ?n ?s ?i?w ?e ?r\s*[HK]ey',p,re.I)):
            out.append(pg)
    return out

def parse_key(lab):
    out={}; sect=None
    kps=key_pages(lab)
    if kps: kps=sorted(set(kps+[kps[-1]+1]))
    for pg in kps:
        sect='Reading' if lab.startswith('GT') else None
        for line in PAGES[pg-1].split('\n'):
            s=line.strip()
            m=re.match(r'^(Listening|Reading|Heading|Beading|Writing|Speaking)\b[\s\d|Il.]*$',s)
            if m:
                sect=m.group(1)
                if sect in ('Heading','Beading'): sect='Reading'
                continue
            for mm in re.finditer(r'(?<![\d.])(\d{1,2})\s*\.\s*(\S[^\n]*?)(?=\s{2,}(?<![\d.])\d{1,2}\s*\.\s|\s*$)',line):
                n=int(mm.group(1)); v=clean(mm.group(2))
                if sect and 1<=n<=42: out.setdefault(sect,{}).setdefault(n,v)
    return out

def reading_pages(lab):
    a,b=RANGES[lab]
    kp=key_pages(lab)
    end=(min(kp)-1) if kp else b
    start=None
    for pg in range(a,end+1):
        if re.search(r'READING PASSAGE\s*1\b',PAGES[pg-1]): start=pg; break
    if start is None:
        for pg in range(a,end+1):
            if re.search(r'READING|SECTION\s*1\b',PAGES[pg-1]): start=pg; break
    if start is None: start=a
    return start,end

def reading_blocks(lab):
    st,en=reading_pages(lab)
    txt="\n".join(norm_page(PAGES[p-1]) for p in range(st,en+1))
    txt=re.sub(r'\n{3,}','\n\n',txt)
    # tandai batas
    marks=[]
    for m in re.finditer(r'^\s*(READING PASSAGE\s*(\d)|SECTION\s*(\d))\s*$',txt,re.M):
        marks.append(('P',m.start(),m.group(2) or m.group(3)))
    for m in re.finditer(r'Read the (?:text|passage)s?[^\n]{0,40}below and answer Questions?\s*([\d ]+)\s*[-\u2010-\u2015\u2212]\s*([\d ]+)',txt):
        a=int(re.sub(r'\D','',m.group(1))); b=int(re.sub(r'\D','',m.group(2)))
        marks.append(('P',m.end(),f"{a}_{b}"))
    for m in re.finditer(r'^\s*Questions?\s*([\d ]+\s*[-\u2010-\u2015\u2212]\s*[\d ]+|\d[\d ]*)\s*$',txt,re.M):
        rng=qnum_fix(m.group(1))
        if rng: marks.append(('Q',m.start(),rng))
    marks.sort(key=lambda x:x[1])
    # buang penanda bacaan yang muncul persis setelah judul blok soal
    m2=[]
    for i,mk in enumerate(marks):
        if mk[0]=='P' and m2 and m2[-1][0]=='Q' and mk[1]-m2[-1][1]<320: continue
        m2.append(mk)
    marks=m2
    passages={}; blocks=[]; cur=None; prev_cur=None
    for i,(kind,pos,val) in enumerate(marks):
        prev_cur=cur
        nxt=marks[i+1][1] if i+1<len(marks) else len(txt)
        body=txt[pos:nxt]
        if kind=='P':
            cur=f"{lab}-P{val}"
            body2=clean(re.sub(r'^\s*(READING PASSAGE\s*\d|SECTION\s*\d)\s*','',body))
            if len(body2)>250: passages[cur]=body2
            else: cur=prev_cur
        else:
            blocks.append({'rng':val,'passage':cur,'text':body})
    # peta nomor soal -> bacaan
    spans=[]
    for i,(kind,pos,val) in enumerate(marks):
        if kind!='P': continue
        pid=f"{lab}-P{val}"
        if pid not in passages: continue
        if '_' in str(val):
            a,b=str(val).split('_'); spans.append((int(a),int(b),pid))
        else:
            nxt=[m for m in marks[i+1:] if m[0]=='P']
            endpos=nxt[0][1] if nxt else 10**9
            rs=[m[2] for m in marks[i+1:] if m[0]=='Q' and m[1]<endpos]
            if rs: spans.append((min(r[0] for r in rs),max(r[1] for r in rs),pid))
    return passages,blocks,spans

TF3=[('TRUE','FALSE','NOT GIVEN'),('YES','NO','NOT GIVEN')]
def parse_block(blk):
    lo,hi=blk['rng']; txt=blk['text']
    lines=[l.rstrip() for l in txt.split('\n')]
    # posisi item
    idx=[]
    for i,l in enumerate(lines):
        m=re.match(r'^\s*(\d{1,2})\s+(\S.*)$',l)
        if m and lo<=int(m.group(1))<=hi:
            if not idx or int(m.group(1))>idx[-1][1]: idx.append((i,int(m.group(1))))
    if not idx: return []
    head="\n".join(lines[:idx[0][0]])
    up=head.upper()
    kind=None; shared=None
    if 'NOT GIVEN' in up and ('TRUE' in up or 'FALSE' in up): kind='TFNG'; shared=['TRUE','FALSE','NOT GIVEN']
    elif 'NOT GIVEN' in up and ('YES' in up or re.search(r'\bNO\b',up)): kind='YNNG'; shared=['YES','NO','NOT GIVEN']
    else:
        mp=re.search(r'paragraphs?,?\s*([A-J])\s*[-\u2010-\u2015\u2212]\s*([A-J])',head)
        mq=re.search(r'(Which paragraph|In which paragraph|The passage has)',head,re.I)
        if mp and mq:
            a,b=mp.group(1),mp.group(2)
            if ord(b)>ord(a):
                kind='PARA'; shared=[f"Paragraf {chr(c)}" for c in range(ord(a),ord(b)+1)]
        lst=[]
        for l in lines[:idx[0][0]]:
            m=re.match(r'^\s*([A-J])\s+(\S.*)$',l)
            if m and len(m.group(2))<3: m=None
            if m: lst.append((m.group(1),clean(m.group(2))))
        seqok = len(lst)>=3 and [x[0] for x in lst]==[chr(65+k) for k in range(len(lst))]
        if shared is None and seqok:
            kind='MATCH'; shared=[f"{a} — {b}" for a,b in lst]
    out=[]
    for j,(i,num) in enumerate(idx):
        end=idx[j+1][0] if j+1<len(idx) else len(lines)
        body=lines[i:end]
        stem=re.sub(r'^\s*\d{1,2}\s+','',body[0])
        opts=[];rest=[]
        for l in body[1:]:
            m=re.match(r'^\s*([A-J])\s+(\S.*)$',l)
            if m: opts.append((m.group(1),clean(m.group(2))))
            elif l.strip(): rest.append(l.strip())
        if opts and not shared:
            stem=clean(stem+" "+" ".join(rest[:0]))
            letters=[o[0] for o in opts]
            if letters==sorted(letters) and len(set(letters))==len(letters) and len(opts)>=3:
                out.append({'n':num,'kind':'MC','stem':stem,'opts':[o[1] for o in opts],
                            'letters':letters,'passage':blk['passage']}); continue
        if shared:
            stem=clean(stem+(" "+" ".join(rest) if rest else ""))
            out.append({'n':num,'kind':kind,'stem':stem,'opts':shared,
                        'letters':[chr(65+k) for k in range(len(shared))],'passage':blk['passage']})
        elif opts:
            out.append({'n':num,'kind':'MC','stem':clean(stem),'opts':[o[1] for o in opts],
                        'letters':[o[0] for o in opts],'passage':blk['passage']})
    return out

def gt_sections(lab):
    st,en=reading_pages(lab)
    txt="\n".join(norm_page(PAGES[p-1]) for p in range(st,en+1))
    txt=re.sub(r'\n{3,}','\n\n',txt)
    ms=[m for m in re.finditer(r'^\s*SECTION\s*(\d)\s+QUESTIONS?\s*([\d ]+)\s*[-\u2010-\u2015\u2212]\s*([\d ]+)\s*$',txt,re.M|re.I)]
    best={}
    for i,m in enumerate(ms):
        a=int(re.sub(r'\D','',m.group(2))); b=int(re.sub(r'\D','',m.group(3)))
        end=ms[i+1].start() if i+1<len(ms) else len(txt)
        body=txt[m.end():end]
        keep=[]
        for l in body.split('\n'):
            t=l.strip()
            if not t: continue
            if re.match(r'^Questions?\s*[\d ]+\s*[-\u2010-\u2015\u2212]\s*[\d ]+\s*$',t): continue
            if re.match(r'^\d{1,2}\s+\S',t): continue
            if re.match(r'^[A-J]\s+\S',t) and len(t)<110: continue
            if re.match(r'^(Read the text|Write your answers|Choose|Complete|Do the following|You are advised|Look at|Use NO MORE|On lines|List of)',t,re.I): continue
            keep.append(t)
        prose=clean(" ".join(keep))
        pid=f"{lab}-S{m.group(1)}"
        if pid not in best or len(prose)>len(best[pid][3]):
            best[pid]=(a,b,pid,prose)
    return list(best.values())

def expl_pages(lab):
    a,b=RANGES[lab]; out=[]
    for pg in range(a,b+1):
        p=PAGES[pg-1]
        if re.search(r'A ?n ?s ?w ?e ?r\s*E ?x ?p ?l ?a ?n ?a ?t ?i ?o ?n ?s',p,re.I): out.append(pg)
    if out:
        last=out[-1]
        for pg in range(last+1,b+1):
            if len(re.findall(r'^\s*\d{1,2}\.\s+\S',PAGES[pg-1],re.M))>=4: out.append(pg)
            else: break
    return out

def parse_expl(lab):
    out={}
    sect='Reading' if lab.startswith('GT') else None
    for pg in expl_pages(lab):
        body=norm_page(PAGES[pg-1])
        body=re.sub(r'^.*Practice Test \d-Answer.*$','',body,flags=re.M)
        body=re.sub(r'^\s*(ACADEMIC|GENERAL TRAINING) MODULE.*$','',body,flags=re.M)
        cur=None
        for line in body.split('\n'):
            s=line.strip()
            m=re.match(r'^(Listening|Reading|Heading|Writing|Speaking)\b[\s\d|Il.]*$',s)
            if m:
                sect=m.group(1); sect='Reading' if sect in('Heading',) else sect; cur=None; continue
            mm=re.match(r'^(\d{1,2})\.\s+(\S.*)$',s)
            if mm and 1<=int(mm.group(1))<=42:
                if sect is None: cur=None; continue
                cur=int(mm.group(1))
                out.setdefault(sect,{}).setdefault(cur,[]).append(mm.group(2))
            elif cur is not None and s and sect:
                d=out.get(sect,{}).get(cur)
                if d is not None: d.append(s)
    return {sec:{n:clean(" ".join(v)) for n,v in items.items()} for sec,items in out.items()}

def parse_expl_all(lab):
    """kumpulkan semua penjelasan bernomor tanpa peduli bagian; bisa >1 kandidat per nomor"""
    out={}
    for pg in expl_pages(lab):
        body=norm_page(PAGES[pg-1])
        body=re.sub(r'^.*Practice Test \d-Answer.*$','',body,flags=re.M)
        body=re.sub(r'^\s*(ACADEMIC|GENERAL TRAINING) MODULE.*$','',body,flags=re.M)
        cur=None
        for line in body.split('\n'):
            s=line.strip()
            if re.match(r'^(Listening|Reading|Heading|Writing|Speaking)\b[\s\d|Il.]*$',s): cur=None; continue
            mm=re.match(r'^(\d{1,2})\.\s+(\S.*)$',s)
            if mm and 1<=int(mm.group(1))<=42:
                cur=int(mm.group(1)); out.setdefault(cur,[]).append([mm.group(2)])
            elif cur is not None and s and out.get(cur): out[cur][-1].append(s)
    return {n:[clean(" ".join(c)) for c in v] for n,v in out.items()}

def audio_scripts():
    """{nomor_tes: [(lo,hi,teks)]}"""
    out={}
    start=None
    for pg in range(300,len(PAGES)+1):
        if re.search(r'^\s*PRACTICE TEST 1\s*$',PAGES[pg-1],re.M) and pg>310: start=pg; break
    if not start: return out
    txt="\n".join(norm_page(PAGES[p-1]) for p in range(start,len(PAGES)+1))
    tests=[(m.start(),int(m.group(1))) for m in re.finditer(r'^\s*PRACTICE TEST (\d)\s*$',txt,re.M)]
    for i,(pos,num) in enumerate(tests):
        end=tests[i+1][0] if i+1<len(tests) else len(txt)
        blob=txt[pos:end]
        qs=[(m.start(),m.end(),int(m.group(1)),int(m.group(2))) for m in
            re.finditer(r'^\s*Questions?\s*(\d+)\s*(?:to|[-‐-―−])\s*(\d+)\s*$',blob,re.M)]
        segs=[]
        for j,(s,e,a,b) in enumerate(qs):
            en=qs[j+1][0] if j+1<len(qs) else len(blob)
            segs.append((a,b,clean(blob[e:en])))
        out[num]=segs
    return out

def listening_pages(lab):
    a,b=RANGES[lab]
    end=b
    for pg in range(a,b+1):
        if re.search(r'READING PASSAGE\s*1\b',PAGES[pg-1]): end=pg-1; break
    return a,end

def listening_blocks(lab):
    st,en=listening_pages(lab)
    txt="\n".join(norm_page(PAGES[p-1]) for p in range(st,en+1))
    txt=re.sub(r'\n{3,}','\n\n',txt)
    marks=[]
    for m in re.finditer(r'^\s*Questions?\s*([\d ]+\s*[-‐-―−]\s*[\d ]+)\s*$',txt,re.M):
        rng=qnum_fix(m.group(1))
        if rng: marks.append((m.start(),rng))
    blocks=[]
    for i,(pos,rng) in enumerate(marks):
        nxt=marks[i+1][0] if i+1<len(marks) else len(txt)
        blocks.append({'rng':rng,'passage':None,'text':txt[pos:nxt]})
    return blocks
