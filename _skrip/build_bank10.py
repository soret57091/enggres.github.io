# -*- coding: utf-8 -*-
"""Bank 10 — Barron's IELTS: soal isian/pencocokan huruf diubah jadi pilihan ganda.
Pengecoh diambil dari daftar pilihan yang memang disediakan buku, dipilih yang
panjangnya paling mirip dengan kunci supaya set opsi berimbang."""
import sys, re, json, io
sys.path.insert(0,'/home/claude')
import barron_parse as B
from blist import optlist, LETT, ROM

def keyclean(k):
    m=re.match(r'^([A-L])\b',k or '')
    return m.group(1) if m else None

def romnorm(tok):
    t=tok.lower().replace('l','i').replace('1','i').replace('|','i').replace('!','i')
    t=t.replace('¡','i').replace('í','i')
    return t if re.fullmatch(r'(i|ii|iii|iv|v|vi|vii|viii|ix|x|xi|xii)',t) else None

def romlist(txt):
    """daftar heading i..xii, toleran OCR"""
    found=[]
    for l in txt.split('\n'):
        m=re.search(r'(?:^|\s{2,})([ivxIVX1l|!]{1,5})[.)]?\s{1,}([A-Z][^\n]*?)\s*$', l.rstrip())
        if not m: continue
        r=romnorm(m.group(1)); t=B.clean(m.group(2))
        if not r or len(t)<4 or len(t)>70: continue
        if re.search(r'answer sheet|on lines|correct (letter|number)|LIST OF',t,re.I): continue
        found.append((r,t))
    best=[];cur=[]
    for r,t in found:
        if not cur:
            if r=='i': cur=[(r,t)]
        elif ROM.index(r)==ROM.index(cur[-1][0])+1: cur.append((r,t))
        elif r=='i':
            if len(cur)>len(best): best=cur
            cur=[(r,t)]
    if len(cur)>len(best): best=cur
    return best if len(best)>=4 else None

def blanks_text(txt, lo, hi, drop):
    body=[]
    for l in txt.split('\n'):
        s=B.clean(l)
        if not s: continue
        if s in drop: continue
        if re.match(r'^Questions?\s*[\d \-‐-―−]+$',s): continue
        if re.match(r'^(Complete|Choose|Write|Read the text|Answer the questions|Use NO MORE|List of|On lines|You may use|There are more|The following|Look at|Match each|Which paragraph)',s,re.I): continue
        if re.match(r'^(the box below|the passage|below\b|from the)',s,re.I): continue
        if len(s)<3: continue
        body.append(s)
    t=re.sub(r'\s+',' '," ".join(body))
    def rep(m):
        n=int(re.sub(r'\D','',m.group(1)))
        return ' __(%d)__ '%n if lo<=n<=hi else m.group(0)
    t=re.sub(r'(\d[\d ]{0,3}?)\s*_{3,}\.?', rep, t)
    t=re.sub(r'_{3,}','______',t)
    t=re.sub(r'\s+([,.;:])',r'\1',t)
    return B.clean(re.sub(r'\s{2,}',' ',t))

qs=[]; passages={}; rot=0; STRIP={}
def emit(qid, sub, ref, stem, correct, dis, ex, pid=None, instr=None, theme='reading', fixed=None):
    global rot
    dis=[d for d in dis if d!=correct]
    if len(dis)<2: return False
    if fixed:
        o=list(fixed); 
        if correct not in o: return False
        pos=o.index(correct)
    else:
        o=list(dis); pos=rot%(len(o)+1); rot+=1
        o.insert(pos,correct)
    o=[tidy(x) for x in o]; correct=tidy(correct)
    if len(set(o))!=len(o) or len(stem)<10: return False
    if not all(ok_opt(x) for x in o): return False
    pos=o.index(correct) if correct in o else -1
    if pos<0: return False
    q={"id":qid,"theme":theme,"subtheme":sub,"ref":ref,
       "instruction":instr or "Pilih jawaban yang paling tepat berdasarkan bacaan.",
       "question":stem,"options":o,"answer":pos,"explain":ex}
    if pid: q["passageId"]=pid
    qs.append(q); return True

GARBAGE=re.compile(r'[^\w\s,.\'\u2019()\-/&%:;$\u2014\u2013?!\"]')
def ok_opt(o):
    if not o or len(o)<2 or len(o)>90: return False
    if GARBAGE.search(o): return False
    if re.search(r'\s[A-N]\s',o): return False          # dua kolom kotak yang menyatu
    letters=sum(c.isalpha() or c.isspace() for c in o)
    return letters/len(o)>0.82

def tidy(s):
    s=re.sub(r'(?<=[a-z\u2019])\d+$','',s.strip())
    return re.sub(r'\s+',' ',s).strip()

def near(correct, pool, k=3):
    p=[t for t in pool if t!=correct]
    p.sort(key=lambda t: abs(len(t)-len(correct)))
    return p[:k]

TESTNAME={'AC':'Academic','GT':'General Training'}
stat={}
def bump(k): stat[k]=stat.get(k,0)+1

for lab in B.RANGES:
    key=B.parse_key(lab).get('Reading',{})
    P,blocks,spans=B.reading_blocks(lab)
    for pid,txt in P.items():
        passages.setdefault(pid,{"title":"Barron's %s PT%s — bacaan"%(TESTNAME[lab[:2]],lab[2]),"text":txt})
    if lab.startswith('GT'):
        for a,b,pid,prose in B.gt_sections(lab):
            if len(prose)>600:
                passages[pid]={"title":"Barron's General Training PT%s — bacaan"%lab[2],"text":prose}
                spans=[s for s in spans if s[2]!=pid]+[(a,b,pid)]
    # --- pulihkan bacaan yang hilang karena diawali blok soal ---
    st_,en_=B.reading_pages(lab)
    full="\n".join(B.norm_page(B.PAGES[pp-1]) for pp in range(st_,en_+1))
    mks=[(m.start(),m.group(2)) for m in re.finditer(r'^\s*(READING PASSAGE\s*(\d))\s*$',full,re.M)]
    for j,(pos,num) in enumerate(mks):
        pid="%s-P%s"%(lab,num)
        if pid in passages: continue
        end=mks[j+1][0] if j+1<len(mks) else len(full)
        reg=full[pos:end]
        cuts=[m.end() for m in re.finditer(r'^\s*\d{1,2}\s+(Section|Paragraph)\s+[A-Z]\s*$',reg,re.M)]
        if not cuts:
            cuts=[m.end() for m in re.finditer(r'^\s*(x|ix|viii|vii|vi|v|iv|iii|ii|i|X)\s{2,}[A-Z][^\n]{5,}$',reg,re.M)]
        if not cuts: continue
        body=B.clean(re.sub(r'\s{2,}',' ',reg[cuts[-1]:]))
        body=re.sub(r'^\s*[\d\W]{0,20}','',body)
        if len(body)>800:
            passages[pid]={"title":"Barron's %s PT%s — bacaan"%(TESTNAME[lab[:2]],lab[2]),"text":body}
            spans.append((1,13,pid) if num=='1' else (14,27,pid) if num=='2' else (28,40,pid))
    tname="Barron's IELTS — %s Practice Test %s, Reading"%(TESTNAME[lab[:2]],lab[2])
    merged={}
    for blk in blocks:
        if B.parse_block(blk): continue
        k=blk['rng']
        if k in merged: merged[k]['text']+="\n"+blk['text']
        else: merged[k]=dict(blk)
    for blk in merged.values():
        lo,hi=blk['rng']
        txt=blk['text']
        raw=[(key.get(n) or '').strip() for n in range(lo,hi+1)]
        rom=[romnorm(k) for k in raw]
        let=[keyclean(k) for k in raw]
        tf =[re.match(r'^(True|False|Not Given|Yes|No)\b',k,re.I) for k in raw]
        rpass=None
        for a,b,pid_ in spans:
            if a<=lo and hi<=b and pid_ in passages: rpass=pid_; break
        if not rpass and blk['passage'] in passages:
            sp=[(a,b) for a,b,pid_ in spans if pid_==blk['passage']]
            if sp and sp[0][0]<=lo and hi<=sp[0][1]: rpass=blk['passage']
        # ---------- TRUE / FALSE / NOT GIVEN ----------
        if sum(1 for x in tf if x)>len(raw)*0.8:
            vals=[x.group(1).title() for x in tf]
            yn = 'Yes' in vals or 'No' in vals
            opts=['Yes','No','Not Given'] if yn else ['True','False','Not Given']
            items=[]
            for l in txt.split('\n'):
                m=re.match(r'^\s*(\d{1,2})\s+(\S.*)$',l)
                if m and lo<=int(m.group(1))<=hi: items.append((int(m.group(1)),B.clean(m.group(2))))
            for n,st in items:
                v=vals[n-lo]
                if len(st)<15: continue
                if emit("brx-%s-%d"%(lab.lower(),n),"Benar/Salah/Tidak Disebut",tname,st,v,
                        [o for o in opts if o!=v],
                        "Kunci buku: <b>%s</b>. <i>%s</i> berarti keterangan itu tidak dapat ditemukan sama sekali di dalam bacaan."%(v,opts[2]),
                        rpass,"Apakah pernyataan berikut sesuai dengan bacaan?",fixed=opts):
                    bump('TFNG')
            continue
        # ---------- pencocokan paragraf / bagian berlabel huruf ----------
        mpar=re.search(r'(Which paragraph|Match each description|has s?.{0,3}ix paragraphs|paragraphs?,?\s*A\s*[-‐-―−]\s*([A-L]))',txt,re.I)
        box=optlist(txt,'letter')
        if mpar and not box and sum(1 for x in let if x)>len(raw)*0.8:
            mx=max(let, key=lambda c:ord(c) if c else 0)
            m2=re.search(r'A\s*[,-‐-―−]\s*(?:B,?\s*(?:or\s*)?)?([A-L])\b',txt)
            top=m2.group(1) if m2 and ord(m2.group(1))>=ord(mx) else mx
            unit='Bagian' if re.search(r'section',txt,re.I) else 'Paragraf'
            if re.search(r'canoe',txt,re.I): unit='Kano'
            opts=[f"{unit} {chr(c)}" for c in range(65,ord(top)+1)]
            if 3<=len(opts)<=8:
                items=[]
                for l in txt.split('\n'):
                    m=re.match(r'^\s*(\d{1,2})\s+(\S.*)$',l)
                    if m and lo<=int(m.group(1))<=hi: items.append((int(m.group(1)),B.clean(m.group(2))))
                for n,st in items:
                    L=let[n-lo]
                    if not L or len(st)<12: continue
                    cor=f"{unit} {L}"
                    if cor not in opts: continue
                    if emit("brx-%s-%d"%(lab.lower(),n),"Mencocokkan Informasi",tname,
                            "Di bagian mana keterangan berikut disebutkan? <i>%s</i>"%st, cor,
                            [o for o in opts if o!=cor],
                            "Kunci buku: <b>%s</b>."%cor, rpass,
                            "Tentukan bagian bacaan yang memuat keterangan tersebut.",fixed=opts):
                        bump('PARA')
                continue
        # ---------- daftar heading angka romawi ----------
        rl=romlist(txt)
        if rl and sum(1 for x in rom if x)>len(raw)*0.6:
            rd=dict(rl); pool=[t for _,t in rl]
            if rpass: STRIP.setdefault(rpass,[]).extend([r+' '+x for r,x in rl]+[x for _,x in rl])
            items=[]
            for l in txt.split('\n'):
                m=re.match(r'^\s*(\d{1,2})\s+(\S.*)$',l)
                if m and lo<=int(m.group(1))<=hi: items.append((int(m.group(1)),B.clean(m.group(2))))
            for n,st in items:
                r=rom[n-lo]
                if not r or r not in rd: continue
                cor=rd[r]
                if emit("brx-%s-%d"%(lab.lower(),n),"Memilih Judul Bagian",tname,
                        "Judul yang paling tepat untuk <b>%s</b> adalah …"%st, cor, near(cor,pool,3),
                        "Kunci buku: <b>%s — %s</b>."%(r,cor), rpass,
                        "Pilih judul yang paling sesuai dengan isi bagian tersebut."):
                    bump('HEAD')
            continue
        # ---------- ada kotak pilihan huruf ----------
        if box and len(box)>=4 and sum(1 for x in let if x)>len(raw)*0.8:
            boxd=dict(box); pool=[t for _,t in box]
            drop={t for _,t in box}
            rest_blanks=len(re.findall(r'\d[\d ]{0,3}\s*_{3,}',txt))
            if rest_blanks>=max(2,(hi-lo)):
                body=blanks_text(txt,lo,hi,drop)
                pid="%s-BOX%d"%(lab,lo)
                base=P.get(blk['passage'],'')
                for L,ot in box: body=body.replace(" %s %s"%(L,ot),"")
                body=re.sub(r'\s{2,}',' ',body).strip()
                passages[pid]={"title":"Bacaan + catatan (soal %d–%d)"%(lo,hi),
                               "text":(base+"\n\n— — —\nCATATAN / RINGKASAN:\n"+body) if base else body}
                for n in range(lo,hi+1):
                    L=let[n-lo]
                    if not L or L not in boxd: continue
                    cor=boxd[L]
                    if emit("brx-%s-%d"%(lab.lower(),n),"Melengkapi Catatan/Ringkasan",tname,
                            "Bagian <b>(%d)</b> pada catatan di samping paling tepat diisi dengan …"%n,
                            cor, near(cor,pool,3),
                            "Kunci buku: <b>%s — %s</b>."%(L,cor), pid,
                            "Lengkapi catatan/ringkasan di samping berdasarkan bacaan."):
                        bump('BOX')
            else:
                flat=txt.replace('\u00ad','').replace('\n',' ')
                flat=re.sub(r'\s+',' ',flat)
                flat=re.sub(r'\bfalets\b','facts',flat); flat=re.sub(r'\bans\\?wers\b','answers',flat)
                flat=re.sub(r'\bo ?f\b','of',flat); flat=re.sub(r'\busedfor\b','used for',flat)
                flat=re.sub(r'\bC T\b','CT',flat); flat=re.sub(r'\bamswer\b','answer',flat)
                flat=re.sub(r'\bmen ?-? ?tioned\b','mentioned',flat)
                flat=re.sub(r'\binthepassage\b','in the passage',flat)
                flat=re.sub(r'\bin ?the ?passage\b','in the passage',flat)
                flat=re.sub(r'\b(TWO|THREE|FOUR|FIVE|SIX)\s+of\b','of',flat)
                m=re.search(r'((?:Which|What)\b[^?.]{15,200}?)\s*(?:Choose|Write|On lines|on lines)',flat)
                lead=m.group(1) if m else None
                if not lead:
                    m=re.search(r'((?:Which|What)\b[^?]{15,200}\?)',flat); lead=m.group(1) if m else None
                items=[]
                for l in txt.split('\n'):
                    m=re.match(r'^\s*(\d{1,2})\s+(\S.*)$',l)
                    if m and lo<=int(m.group(1))<=hi: items.append((int(m.group(1)),B.clean(m.group(2))))
                if lead and not items:
                    lead=re.sub(r'\s+',' ',B.clean(lead)).rstrip(' .,;:')
                    if not lead.endswith('?'): lead+='?'
                    if len(lead)<25: lead=None
                    wrong=[t for L,t in box if L not in set(x for x in let if x)]
                    if lead and len(wrong)>=3:
                        for n in range(lo,hi+1):
                            L=let[n-lo]
                            if not L or L not in boxd: continue
                            cor=boxd[L]
                            if emit("brx-%s-%d"%(lab.lower(),n),"Informasi Rinci (pilih satu)",tname,
                                    lead, cor, near(cor,wrong,3),
                                    "Buku mencantumkan <b>%s — %s</b> sebagai salah satu jawaban benar; tiga pilihan lain tidak disebutkan dalam bacaan."%(L,cor),
                                    rpass,"Pilih SATU pernyataan yang memang disebutkan dalam bacaan."):
                                bump('CHOOSE')
                elif items:
                    for n,st in items:
                        L=let[n-lo]
                        if not L or L not in boxd or len(st)<12: continue
                        cor=boxd[L]
                        if emit("brx-%s-%d"%(lab.lower(),n),"Mencocokkan Informasi",tname,
                                st, cor, near(cor,pool,3),
                                "Kunci buku: <b>%s — %s</b>."%(L,cor), rpass,
                                "Cocokkan pernyataan berikut dengan pilihan yang tepat."):
                            bump('MATCH')
PH=[r'^\s*You should spend about \d+ (?:minutes|mimms) on Questions[^.]*\.\s*',
    r'^\s*\.?\s*reading passage below\.\s*', r'^\s*Questions?\s*[\d \-\u2010-\u2015\u2212]+\s*',
    r'^\s*The following (?:reading )?passage has [^.]*\.\s*',
    r'^\s*Choose the correct heading[^.]*\.\s*', r'^\s*Write the correct (?:number|letter)[^.]*\.\s*',
    r'^\s*There are more headings than [^.]*\.\s*', r'^\s*\.\s*',
    r'^\s*Choose the most suitable head-? ?ing f ?or each paragraph[^.]*\.\s*',
    r'^\s*(?:i|ii|iii|iv|v|vi|vii|viii|ix|x|V|X|I)\s+[A-Z][^\n]{3,45}?(?=\s+(?:i|ii|iii|iv|v|vi|vii|viii|ix|x|V|X|I)\s+[A-Z])',
    r'^\s*(?:i|ii|iii|iv|v|vi|vii|viii|ix|x|V|X|I)\s+[A-Z][a-z][^\n]{3,45}?\s+(?=[A-Z][a-z]+\s+[A-Z])']
def dehyph(s):
    s=s.replace('\u00ad','')
    s=re.sub(r'(\w)-\s*\n\s*(\w)',r'\1\2',s)
    s=re.sub(r'(\w)-\s{1,3}(?=[a-z])',r'\1',s)
    s=re.sub(r'\bLo cated\b','Located',s)
    return s
for pid,pv in passages.items():
    s=dehyph(pv['text'])
    for frag in sorted(STRIP.get(pid,[]),key=len,reverse=True):
        if s.count(frag)>1 or len(s)-len(frag)>1500: s=s.replace(frag,' ',1)
    s=re.sub(r'\b(?:LIST OF HEADINGS|LIST OF Y?\[?EABINGS)\b','',s,flags=re.I)
    s=re.sub(r'^[^A-Za-z]{0,12}','',s)
    for _ in range(14):
        for re_ in PH: s=re.sub(re_,'',s,flags=re.I)
    s=re.sub(r'\s+([,.;:])',r'\1',re.sub(r'[ \t]{2,}',' ',s)).strip()
    flat=re.sub(r'\s+',' ',s)
    if re.search(r'[~]|\.{4,}|\bLIST OF\b', flat[:150]):
        m=re.search(r"([A-Z][A-Za-z'\- ]{10,60}?)\s+A\s+[A-Z]", flat[:900])
        if not m: m=re.search(r"[.,]\s+([A-Z][a-z]+(?:\s+\S+){5,})", flat[:400])
        if m: s=flat[m.start(1) if m.lastindex else m.start():]
    s=re.sub(r'\s+(?:[A-K]\s+[^A-K]{2,28}\s+){5,}[A-K]\s+\S+\s*$','',s)
    pv['text']=s.strip()
qs=[q for q in qs if q.get('passageId')]
used={q['passageId'] for q in qs}
passages={k:v for k,v in passages.items() if k in used}
print(stat,'| total dipakai',len(qs),'| bacaan',len(passages))
json.dump({'q':qs,'p':passages},open('/home/claude/bank10_draft.json','w'),ensure_ascii=False)
src={"id":"barron-completion","name":"Barron's IELTS Practice Exams (Isian & Pencocokan → Pilihan Ganda)","test":"IELTS"}
def jss(x): return json.dumps(x,ensure_ascii=False)
out=["/* Bank 10 — Barron's IELTS: soal isian, pencocokan huruf, pemilihan judul,",
     "   dan True/False/Not Given diubah menjadi pilihan ganda.",
     "   Pengecoh diambil dari daftar pilihan milik buku itu sendiri. */",
     "TOEFLDRILL.addBank({","source: "+jss(src)+",","passages: {"]
for k,v in passages.items():
    out.append(jss(k)+": { title:"+jss(v['title'])+", text:"+jss(v['text'])+" },")
out.append("},"); out.append("questions: [")
for q in qs:
    parts=["id:"+jss(q['id']),"theme:"+jss(q['theme']),"subtheme:"+jss(q['subtheme']),
           "ref:"+jss(q['ref']),"passageId:"+jss(q['passageId']),
           "\n instruction:"+jss(q['instruction']),"\n question:"+jss(q['question']),
           "\n options:"+jss(q['options'])+", answer:"+str(q['answer']),
           "\n explain:"+jss(q['explain'])]
    out.append("{"+", ".join(parts)+"},")
out.append("]\n});")
io.open('/mnt/user-data/outputs/TOEFL-Drill-Web/data/bank-10-barron-completion.js','w',encoding='utf-8').write("\n".join(out)+"\n")
print('bank-10 ditulis')
