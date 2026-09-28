# -*- coding: utf-8 -*-
"""Deteksi daftar pilihan bersama (A-L atau i-xii) di dalam blok soal Barron's."""
import re, sys
sys.path.insert(0,'/home/claude')
import barron_parse as B

ROM=['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii']
LETT=[chr(65+i) for i in range(12)]

def _scan(lines, labels):
    """kembalikan daftar (label, teks) berurutan sesuai labels"""
    pat=re.compile(r'(?:^|\s{2,})('+'|'.join(re.escape(x) for x in labels)+r')[.)]?\s{1,}(\S.*?)\s*$')
    found=[]
    for l in lines:
        s=l.rstrip()
        if not s.strip(): continue
        m=pat.search(s)
        if not m: continue
        lab, txt = m.group(1), B.clean(m.group(2))
        if len(txt)<3 or re.match(r'^\d',txt): continue
        if re.search(r'answer sheet|on lines|write the correct|choose ',txt,re.I): continue
        found.append((lab,txt))
    # ambil rantai terpanjang yang berurutan mulai dari labels[0]
    best=[]; cur=[]
    for lab,txt in found:
        if not cur:
            if lab==labels[0]: cur=[(lab,txt)]
        elif labels.index(lab)==labels.index(cur[-1][0])+1: cur.append((lab,txt))
        elif lab==labels[0]:
            if len(cur)>len(best): best=cur
            cur=[(lab,txt)]
    if len(cur)>len(best): best=cur
    return best

def optlist(txt, kind='letter'):
    labels = LETT if kind=='letter' else ROM
    r=_scan(txt.split('\n'), labels)
    return r if len(r)>=3 else None

def strip_list(txt, opts):
    keep=[]
    texts={t for _,t in opts}
    for l in txt.split('\n'):
        s=B.clean(l)
        if any(s.endswith(t) and len(s)-len(t)<8 for t in texts): continue
        keep.append(l)
    return "\n".join(keep)
