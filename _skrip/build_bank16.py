# -*- coding: utf-8 -*-
"""
Bank 16 — TOEFL ITP Level 1, Practice Test A & B (ETS, Volume 3).
Tiga bagian: Structure (15), Written Expression (25), Reading (50) tiap test,
ditambah Listening (50) yang memakai naskah audio resmi dari bukunya.

Kunci jawaban dibaca dari halaman "Answer Key" (tiga kolom Section 1/2/3),
dipetakan lewat posisi kolomnya supaya tidak tertukar antarbagian.
Jalankan: python3 _skrip/build_bank16.py
"""
import re, io, os, json, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itp_extract as EX

FLAT = "/tmp/itp_flat.txt"          # pdftotext -layout (untuk answer key)
PAGES = "/tmp/itp_pages.txt"        # pdfplumber sadar kolom

# batas halaman PDF (1-based)
LAYOUT = {
    "A": {"struct": (34, 35), "we": (37, 39), "read": (44, 62), "listen": (21, 32), "script": (110, 125)},
    "B": {"struct": (78, 80), "we": (82, 85), "read": (88, 106), "listen": (67, 76), "script": (126, 141)},
}

def pages():
    if not os.path.exists(PAGES):
        subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "itp_extract.py")], check=True)
    T = io.open(PAGES, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"<<<PAGE (\d+)( 2KOL)?>>>\n(.*?)(?=<<<PAGE |\Z)", T, re.S):
        out[int(m.group(1))] = m.group(3)
    return out

def flat():
    if not os.path.exists(FLAT):
        subprocess.run(["pdftotext", "-layout", EX.PDF, FLAT], check=False)
    return io.open(FLAT, encoding="utf-8", errors="replace").read()

# ---------------- answer key ----------------
PAIR = re.compile(r"(\d{1,2})\s+([A-D])(?![A-Za-z])")

def answer_keys():
    """-> {'A': {1:{no:huruf}, 2:{...}, 3:{...}}, 'B': ...}

    Tiap baris kunci memuat 6 pasangan (nomor, huruf) berurutan:
    S1 1-25, S1 26-50, S2 1-20, S2 21-40, S3 1-25, S3 26-50.
    Pada baris 21-25 Section 2 sudah habis sehingga hanya ada 4 pasangan,
    yang berarti kolom 0,1,4,5. Pemetaan memakai urutan pasangan, bukan
    posisi karakter, supaya tidak terpengaruh perataan angka.
    """
    txt = flat().split("\n")
    COLS = {6: [0, 1, 2, 3, 4, 5], 4: [0, 1, 4, 5], 2: [0, 1]}
    SEC = {0: 1, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}
    res = {}
    for tag in ("A", "B"):
        rows = None
        for k, l in enumerate(txt):
            if ("Practice Test %s - Answer Key" % tag) not in l:
                continue
            cand = []
            for r in txt[k + 1: k + 60]:
                if "Answer Key" in r or "Answer Keys" in r:
                    break
                cand.append(r)
            if any(len(PAIR.findall(r)) == 6 for r in cand):
                rows = cand; break
        if not rows:
            continue
        sec = {1: {}, 2: {}, 3: {}}
        for r in rows:
            pr = PAIR.findall(r)
            if len(pr) not in COLS:
                continue
            for i, (num, ltr) in enumerate(pr):
                sec[SEC[COLS[len(pr)][i]]][int(num)] = ltr
        res[tag] = sec
    return res

# ---------------- pemenggal soal pilihan ganda ----------------
BOILER = re.compile(
    r"^\s*(This is the end of .*|Stop work on .*|Read the directions .*|"
    r"Go on to the next page\.?|Turn the page.*|Section \d continues\.?|"
    r"The questions for this passage.*|next page\.|Comprehension\.|"
    r"and begin work\.|section of the test for|Do not read or work on any other|"
    r"on Section \d only\.|At the end of \d+ minutes.*|Use exactly \d+ minutes.*|"
    r"When you finish .*|You may go back .*)\s*$", re.I)

DIRSTART = re.compile(r"^\s*(Part [ABC]|Directions:|In this part of the test|"
                      r"Now begin work|Example [IV]+|Sample Answer|This is the end|"
                      r"Stop work|Read the directions|Go on to|If you finish in less than)", re.I)
DIRSTOP = re.compile(r"^\s*(\d{1,2}\.|\([A-D]\)|Questions?\s+\d+)")
FRAG = re.compile(r"(begin work|Use exactly|check your work|end of Section|"
                  r"Comprehension\.|Directions:|Sample Answer|Do not read or work|"
                  r"work on any other|section of the test for|Section \d\b)", re.I)

def strip_boiler(lines):
    out, skip = [], False
    for l in lines:
        s = l.strip()
        if not s:
            out.append(l); continue
        if skip:
            if DIRSTOP.match(s):
                skip = False
            else:
                continue
        if BOILER.match(s) or FRAG.search(s):
            if not DIRSTOP.match(s):
                skip = True
                continue
            # baris soal/opsi yang tercemar penggalan petunjuk: potong bagian itu
            s = FRAG.split(s)[0].rstrip()
            if len(s) < 3:
                skip = True; continue
            out.append(s); continue
        if DIRSTART.match(s):
            skip = True; continue
        out.append(l)
    return out

QN = re.compile(r"^\s*(\d{1,2})\.\s*(.*)$")
OP = re.compile(r"^\s*\(([A-D])\)\s*(.*)$")

def parse_mc(lines, lo, hi):
    """Soal bernomor lo..hi dengan opsi (A)-(D) yang boleh melipat baris."""
    qs, cur, mode = [], None, None
    expect = lo
    for raw in lines:
        l = raw.rstrip()
        m = QN.match(l)
        if m and int(m.group(1)) == expect and not OP.match(l):
            if cur: qs.append(cur)
            cur = {"n": expect, "stem": [m.group(2).strip()], "opt": []}
            expect += 1; mode = "stem"
            if expect > hi + 1: break
            continue
        if cur is None:
            continue
        o = OP.match(l)
        if o:
            cur["opt"].append([o.group(1), o.group(2).strip()]); mode = "opt"; continue
        if not l.strip() or re.match(r"^\s*\d{1,3}\s*$", l):
            continue
        if mode == "opt" and cur["opt"]:
            cur["opt"][-1][1] += " " + l.strip()
        elif mode == "stem":
            cur["stem"].append(l.strip())
    if cur: qs.append(cur)
    out = []
    for q in qs:
        if len(q["opt"]) != 4:
            continue
        letters = [o[0] for o in q["opt"]]
        if letters != ["A", "B", "C", "D"]:
            # salah cetak huruf di buku: pakai urutan posisinya
            if len(set(letters)) < 4:
                pass
            else:
                continue
        opts = [re.sub(r"\s+", " ", o[1]).strip() for o in q["opt"]]
        if len(set(opts)) != 4 or min(len(o) for o in opts) < 1:
            continue
        if max(len(o) for o in opts) > 160:
            continue          # opsi kemasukan teks bacaan/petunjuk
        q["options"] = opts
        q["text"] = re.sub(r"\s+", " ", " ".join(q["stem"])).strip()
        if len(q["text"]) < 10:
            continue
        out.append(q)
    return out

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------------- bacaan Section 3 ----------------
def clean_passage(lines):
    """Buang penanda 'Line' dan angka baris di gutter, lalu beri nomor ulang."""
    out = []
    for l in lines:
        s = l.strip()
        if not s or s == "Line" or re.match(r"^\d{1,3}$", s):
            continue
        nxt = 5 * ((len(out) + 1) // 5 + 1) if (len(out) + 1) % 5 else (len(out) + 1)
        m = re.match(r"^(\d{1,2})\s+(\S.*)$", s)
        if m and int(m.group(1)) % 5 == 0 and abs(int(m.group(1)) - (len(out) + 1)) <= 2:
            s = m.group(2)
        out.append(s)
    txt, idx = [], {}
    for i, l in enumerate(out, 1):
        idx[i] = l
        txt.append(("(%d) " % i if i % 5 == 0 else "     ") + l)
    return "\n".join(txt), idx

def split_reading(pgs, lo, hi):
    """-> [(judul_blok, [baris_bacaan], [baris_soal])]"""
    body = []
    for n in range(lo, hi + 1):
        body.extend(pgs.get(n, "").split("\n"))
    blocks, cur = [], None
    for l in body:
        m = re.match(r"^\s*Questions?\s+(\d+)\s*[-–—]\s*(\d+)\s*$", l.strip())
        if m:
            if cur: blocks.append(cur)
            cur = {"lo": int(m.group(1)), "hi": int(m.group(2)), "lines": []}
            continue
        if cur is not None:
            if re.match(r"^\s*(Section 3 continues\.|Turn the page.*|The questions for this passage.*|next page\.|This is the end of Section 3\.)\s*$", l.strip()):
                continue
            cur["lines"].append(l)
    if cur: blocks.append(cur)
    out = []
    for b in blocks:
        first = None
        for i, l in enumerate(b["lines"]):
            m = QN.match(l)
            if m and int(m.group(1)) == b["lo"]:
                first = i; break
        if first is None or first < 4:
            continue
        out.append((b, b["lines"][:first], b["lines"][first:]))
    return out

# ---------------- Written Expression (deteksi garis bawah) ----------------
def extract_we(pdf, lo, hi):
    """-> [ {n, html, options[4]} ] dari halaman error-identification."""
    import pdfplumber  # noqa
    res = []
    for pno in range(lo, hi + 1):
        pg = pdf.pages[pno - 1]
        ws = pg.extract_words(x_tolerance=1.6, y_tolerance=2.5)
        uls = [l for l in pg.lines if abs(l.get("height", 0)) < 2 and (l["x1"] - l["x0"]) > 5]
        if not ws or not uls:
            continue
        rows = {}
        for w in ws:
            rows.setdefault(round(w["top"] / 4.0), []).append(w)
        rowk = sorted(rows)
        for k in rowk:
            rows[k].sort(key=lambda z: z["x0"])
        marker_rows = set(k for k in rowk
                          if rows[k] and all(re.fullmatch(r"[A-D]", z["text"]) for z in rows[k]))

        # peta kata -> (huruf penanda) lewat garis bawah
        tag = {}
        for u in uls:
            above = [w for w in ws if u["top"] - 15 < (w["top"] + w["bottom"]) / 2 < u["top"] - 0.5]
            hit = []
            for w in above:
                ov = min(w["x1"], u["x1"]) - max(w["x0"], u["x0"])
                if ov > 0 and ov / max(1.0, w["x1"] - w["x0"]) >= 0.55:
                    hit.append(w)
            below = [w for w in ws if u["top"] + 0.5 < w["top"] < u["top"] + 16
                     and re.fullmatch(r"[A-D]", w["text"])
                     and u["x0"] - 10 <= (w["x0"] + w["x1"]) / 2 <= u["x1"] + 10]
            if not hit or not below:
                continue
            uc = (u["x0"] + u["x1"]) / 2.0
            below.sort(key=lambda w: abs((w["x0"] + w["x1"]) / 2.0 - uc))
            L = below[0]["text"]
            for w in sorted(hit, key=lambda z: z["x0"]):
                tag[id(w)] = L

        # potong per soal
        starts = [(k, rows[k][0]) for k in rowk
                  if rows[k] and re.fullmatch(r"\d{1,2}\.", rows[k][0]["text"])]
        for si, (k0, w0) in enumerate(starts):
            k1 = starts[si + 1][0] if si + 1 < len(starts) else 10 ** 9
            parts, opts, curL, buf = [], {}, None, []
            for k in rowk:
                if k < k0 or k >= k1 or k in marker_rows:
                    continue
                for w in rows[k]:
                    if w is w0 or re.fullmatch(r"\d{1,3}", w["text"]):
                        continue
                    L = tag.get(id(w))
                    if L != curL:
                        if curL and buf:
                            parts.append("<u>%s</u><sup>%s</sup>" % (esc(" ".join(buf)), curL))
                            opts[curL] = " ".join(buf)
                        elif buf:
                            parts.append(esc(" ".join(buf)))
                        buf, curL = [], L
                    buf.append(w["text"])
            if curL and buf:
                parts.append("<u>%s</u><sup>%s</sup>" % (esc(" ".join(buf)), curL))
                opts[curL] = " ".join(buf)
            elif buf:
                parts.append(esc(" ".join(buf)))
            if sorted(opts) != ["A", "B", "C", "D"]:
                continue
            html = re.sub(r"\s+", " ", " ".join(parts)).strip()
            html = re.split(r"This is the end of|If you finish before|DO NOT read or work", html)[0].strip()
            html = re.sub(r"([.,;:!?]+)</u>", r"</u>\1", html)
            html = re.sub(r"</u>([.,;:!?]+)<sup>([A-D])</sup>", r"</u><sup>\2</sup>\1", html)
            html = html.replace(" ,", ",").replace(" .", ".").replace(" ;", ";")
            res.append({"n": int(w0["text"].rstrip(".")),
                        "html": html,
                        "options": [re.sub(r"[.,;:!?]+$", "", opts[c]).strip() for c in "ABCD"]})
    return res

# ---------------- Section 2 Structure: sisipkan tanda rumpang ----------------
def struct_lines(pdf, lo, hi):
    """Baris teks halaman Structure, dengan garis rumpang diganti '_____'.
    Di Practice Test B rumpangnya digambar sebagai garis, bukan karakter garis
    bawah, jadi harus dipulihkan dari koordinat garisnya."""
    out = []
    for pno in range(lo, hi + 1):
        pg = pdf.pages[pno - 1]
        sx = EX.two_col(pg)
        ws = pg.extract_words(x_tolerance=1.6, y_tolerance=2.5)
        blanks = [l for l in pg.lines if (l["x1"] - l["x0"]) > 5 and abs(l.get("height", 0)) < 2]
        cols = [[w for w in ws if sx is None or w["x0"] < sx]]
        if sx is not None:
            cols.append([w for w in ws if w["x0"] >= sx])
        for ci, col in enumerate(cols):
            rows = {}
            for w in col:
                rows.setdefault(round(w["top"] / 4.0), []).append(w)
            for k in sorted(rows):
                row = sorted(rows[k], key=lambda z: z["x0"])
                top = min(w["top"] for w in row); bot = max(w["bottom"] for w in row)
                items = [(w["x0"], w["text"]) for w in row]
                for b in blanks:
                    if not (top + 1 <= b["top"] <= bot + 4):
                        continue
                    if sx is not None and ((b["x1"] <= sx) != (ci == 0)):
                        continue
                    if any(min(w["x1"], b["x1"]) - max(w["x0"], b["x0"]) > 1 for w in row):
                        continue
                    items.append((b["x0"], "_____"))
                items.sort()
                out.append(" ".join(t for _, t in items))
    return out

# ---------------- Listening ----------------
def scripts(pgs, lo, hi):
    """-> ({nomor_soal: id_naskah}, {id_naskah: teks})"""
    body = []
    for n in range(lo, hi + 1):
        body.extend(pgs.get(n, "").split("\n"))
    body = [l for l in body
            if not re.match(r"^\s*(Listening Comprehension Script.*|Part [ABC]|\d{1,3}|"
                            r"This is the end of Section 1.*|Stop work on Section 1\.|"
                            r"Read the directions for Section 2 and begin work\.)\s*$", l.strip())]
    blocks, cur = [], None
    for l in body:
        s = l.strip()
        m = re.match(r"^Questions?\s+(\d+)\s+through\s+(\d+)\s*[:.]?\s*(.*)$", s, re.I)
        if m:
            if cur: blocks.append(cur)
            cur = {"lo": int(m.group(1)), "hi": int(m.group(2)),
                   "lines": ([m.group(3)] if m.group(3) else [])}
            continue
        m = re.match(r"^(\d{1,2})\.\s+(\(.*)$", s)
        if m and (cur is None or cur["hi"] < int(m.group(1))):
            if cur: blocks.append(cur)
            cur = {"lo": int(m.group(1)), "hi": int(m.group(1)), "lines": [m.group(2)]}
            continue
        if cur is not None and s:
            cur["lines"].append(s)
    if cur: blocks.append(cur)

    qmap, texts = {}, {}
    for b in blocks:
        if not b["lines"]:
            continue
        sid = "L%d" % b["lo"]
        texts[sid] = "\n".join(b["lines"])
        for n in range(b["lo"], b["hi"] + 1):
            qmap[n] = sid
    return qmap, texts

# ---------------- pembangunan ----------------
import build_bank14 as B14

HAND = {}
try:
    exec(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "itp_explain.py"),
                 encoding="utf-8").read())
except IOError:
    pass

def blank_filled(stem, opt):
    if "_____" in stem:
        return re.sub(r"_+", "<b>" + esc(opt) + "</b>", stem, count=1)
    return None

def build():
    pgs = pages()
    keys = answer_keys()
    import pdfplumber
    questions, passages = [], {}
    stat = {}

    with pdfplumber.open(EX.PDF) as pdf:
        for t in ("A", "B"):
            K = keys[t]
            # ---- Section 2: Structure 1-15 ----
            for q in parse_mc(strip_boiler(struct_lines(pdf, *LAYOUT[t]["struct"])), 1, 15):
                a = "ABCD".find(K[2].get(q["n"], "?"))
                if a < 0: continue
                qid = "itp%s-st-%d" % (t.lower(), q["n"])
                filled = blank_filled(q["text"], q["options"][a])
                ex = HAND.get(qid) or (
                    "Jawabannya <b>%s. %s</b>.%s" % ("ABCD"[a], esc(q["options"][a]),
                    (" Kalimat utuhnya: “<em>%s</em>”." % filled) if filled else ""))
                questions.append({
                    "id": qid, "theme": "structure", "subtheme": "ITP Structure",
                    "ref": "Practice Test %s — Section 2 no.%d" % (t, q["n"]),
                    "instruction": "Pilih kata atau frasa yang paling tepat melengkapi kalimat.",
                    "question": esc(q["text"]).replace("_____", "______"),
                    "options": [esc(o) for o in q["options"]], "answer": a, "explain": ex})

            # ---- Section 2: Written Expression 16-40 ----
            for w in extract_we(pdf, *LAYOUT[t]["we"]):
                a = "ABCD".find(K[2].get(w["n"], "?"))
                if a < 0: continue
                qid = "itp%s-we-%d" % (t.lower(), w["n"])
                ex = HAND.get(qid) or (
                    "Bagian yang harus diperbaiki adalah <b>%s. %s</b>." % ("ABCD"[a], esc(w["options"][a])))
                questions.append({
                    "id": qid, "theme": "written", "subtheme": "ITP Written Expression",
                    "ref": "Practice Test %s — Section 2 no.%d" % (t, w["n"]),
                    "instruction": "Pilih bagian bergaris bawah yang harus diperbaiki.",
                    "question": w["html"],
                    "options": [esc(o) for o in w["options"]], "answer": a, "explain": ex})

            # ---- Section 3: Reading ----
            for b, plines, qlines in split_reading(pgs, *LAYOUT[t]["read"]):
                pid = "ITP%s-R%d" % (t, b["lo"])
                ptxt, idx = clean_passage(plines)
                got = parse_mc(strip_boiler(qlines), b["lo"], b["hi"])
                if not got: continue
                passages[pid] = {"title": "ITP Practice Test %s — Bacaan soal %d–%d" % (t, b["lo"], b["hi"]),
                                 "text": ptxt}
                for q in got:
                    a = "ABCD".find(K[3].get(q["n"], "?"))
                    if a < 0: continue
                    theme, sub = B14.classify(q["text"])
                    qid = "itp%s-rd-%d" % (t.lower(), q["n"])
                    questions.append({
                        "id": qid, "theme": theme, "subtheme": sub,
                        "ref": "Practice Test %s — Section 3 no.%d" % (t, q["n"]),
                        "passageId": pid, "question": esc(q["text"]),
                        "options": [esc(o) for o in q["options"]], "answer": a,
                        "explain": HAND.get(qid) or B14.explain(sub, q["text"], q["options"], a, ptxt, idx)})

            # ---- Section 1: Listening ----
            qmap, texts = scripts(pgs, *LAYOUT[t]["script"])
            lines = []
            for n in range(LAYOUT[t]["listen"][0], LAYOUT[t]["listen"][1] + 1):
                lines += pgs.get(n, "").split("\n")
            for q in parse_mc(strip_boiler(lines), 1, 50):
                a = "ABCD".find(K[1].get(q["n"], "?"))
                if a < 0: continue
                sid = qmap.get(q["n"])
                if not sid or sid not in texts: continue
                pid = "ITP%s-%s" % (t, sid)
                if pid not in passages:
                    passages[pid] = {"title": "Naskah audio — Practice Test %s, soal %s" % (t, sid[1:]),
                                     "text": texts[sid]}
                qid = "itp%s-ls-%d" % (t.lower(), q["n"])
                body, nar = [], False
                for x in texts[sid].split("\n"):
                    xs = x.strip()
                    if xs.startswith("(narrator)"):
                        nar = True; continue
                    if re.match(r"^\d{1,2}\.\s", xs):
                        continue
                    if nar:
                        if xs.startswith("(") or re.match(r"^\d{1,2}\.", xs):
                            nar = False
                        else:
                            continue
                    body.append(x)
                body = "\n".join(body)
                kut = B14.best_sentence(body, q["text"] + " " + q["options"][a])
                if kut and re.match(r"^(Listen to|Questions? \d)", kut.strip()):
                    kut = None
                ex = HAND.get(qid) or (
                    "Jawabannya <b>%s. %s</b>. %s" % ("ABCD"[a], esc(q["options"][a]),
                    ("Bagian naskah yang mendukung: “<em>%s</em>”." % esc(B14.shorten(kut))) if kut else
                    "Cocokkan tiap pilihan dengan isi naskahnya."))
                questions.append({
                    "id": qid, "theme": "listening", "subtheme": "ITP Listening (naskah)",
                    "ref": "Practice Test %s — Section 1 no.%d" % (t, q["n"]),
                    "passageId": pid,
                    "instruction": "Baca naskah audionya, lalu jawab. (Di ujian aslinya naskah ini tidak ditampilkan.)",
                    "question": esc(q["text"]),
                    "options": [esc(o) for o in q["options"]], "answer": a, "explain": ex})

    bank = {"source": {"id": "itp-vol3", "name": "TOEFL ITP Level 1 — Practice Tests Vol.3 (ETS)", "test": "TOEFL ITP"},
            "passages": passages, "questions": questions}
    out = "/* dibuat oleh _skrip/build_bank16.py — jangan diedit tangan */\nTOEFLDRILL.addBank(\n"
    out += json.dumps(bank, ensure_ascii=False, indent=1) + "\n);\n"
    io.open("data/bank-16-itp.js", "w", encoding="utf-8").write(out)
    for th in ("structure", "written", "reading", "vocabulary", "listening"):
        stat[th] = sum(1 for q in questions if q["theme"] == th)
    d = {}
    for q in questions:
        d["ABCD"[q["answer"]]] = d.get("ABCD"[q["answer"]], 0) + 1
    print("bank-16-itp.js:", len(questions), "soal,", len(passages), "bacaan")
    print("  tema:", stat, "| sebaran kunci:", d)
    print("  pembahasan tulis tangan:", sum(1 for q in questions if q["id"] in HAND))

if __name__ == "__main__":
    build()
