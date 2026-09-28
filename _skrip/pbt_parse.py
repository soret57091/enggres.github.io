# -*- coding: utf-8 -*-
"""Pembaca TOEFL-PBT-Practice-test.pdf (17 practice test reading).
Dipakai oleh build_bank14.py. Jalankan sendiri untuk melihat statistiknya."""
import re, os, subprocess, io

PDF = os.path.expanduser("~/mnt/TOEFL IELTS/referensi 2/TOEFL-PBT-Practice-test.pdf")
TXT = "/tmp/pbt.txt"

def raw():
    if not os.path.exists(TXT):
        subprocess.run(["pdftotext", "-layout", PDF, TXT], check=False)
    return io.open(TXT, encoding="utf-8", errors="replace").read()

ARAB = re.compile("[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF\u200B-\u200F\u202A-\u202E\u2066-\u2069]")
NOISE = re.compile(r"^\s*(\d{1,3}|http\S*|Content|ANSWER KEY\s+TOEFL.*)\s*$", re.I)

def clean_lines(t):
    out = []
    for ln in t.split("\n"):
        ln = ln.replace("\f", "")
        if ARAB.search(ln):
            ln = ARAB.sub("", ln)
            ln = re.sub(r"\s+\d{1,3}\s*$", "", ln)
        ln = re.sub(r"\s*TOEFL Reading Comprehension\s*$", "", ln)
        if "zabanphd" in ln.lower():
            continue
        if NOISE.match(ln.strip()):
            continue
        out.append(ln.rstrip())
    return out

TEST_RE = re.compile(r"^\s*PRACTICE TEST (\d+)\s*$")
TESTHEAD_RE = re.compile(r"^\s*PRACTICE TEST (\d+)\s*[-–—]")
QBLOCK_RE = re.compile(r"^\s*Questions?\s*(\d+)\s*[-–—]\s*(\d+)\s*$", re.I)
PASSAGE_RE = re.compile(r"^\s*Passage\s+(\d+)\s*$", re.I)
QNUM_RE = re.compile(r"^\s{0,8}(\d{1,2})\.\s+(\S.*)$")
OPT_RE = re.compile(r"\(([A-D])\)\s*")

def split_tests(lines):
    """-> [(nomor_test, [baris...])] ; buang daftar isi & answer key."""
    marks = [i for i, l in enumerate(lines) if TEST_RE.match(l) or TESTHEAD_RE.match(l)]
    ak = next((i for i, l in enumerate(lines) if l.strip() == "ANSWER KEY"), len(lines))
    tests, cur, curn = [], None, None
    for i, l in enumerate(lines):
        if i >= ak:
            break
        m = TEST_RE.match(l) or TESTHEAD_RE.match(l)
        if m:
            n = int(m.group(1))
            if n != curn:
                if cur is not None and len(cur) > 20:
                    tests.append((curn, cur))
                cur, curn = [], n
            continue
        if cur is not None:
            cur.append(l)
    if cur is not None and len(cur) > 20:
        tests.append((curn, cur))
    # gabungkan potongan test bernomor sama
    merged, seen = [], {}
    for n, body in tests:
        if n in seen:
            merged[seen[n]][1].extend(body)
        else:
            seen[n] = len(merged); merged.append((n, body))
    return merged

MARK_RE = re.compile(r"^\s*(Line|\(\d+\))\s+")

def parse_test(num, lines):
    """-> (passages, questions) untuk satu practice test."""
    blocks, cur = [], None
    for l in lines:
        m = QBLOCK_RE.match(l)
        if m:
            if cur: blocks.append(cur)
            cur = {"lo": int(m.group(1)), "hi": int(m.group(2)), "lines": []}
            continue
        if cur is not None:
            cur["lines"].append(l)
    if cur: blocks.append(cur)

    # format kedua: "Passage N" dan penomoran soal mulai dari 1 tiap bacaan
    if not blocks:
        for l in lines:
            m = PASSAGE_RE.match(l)
            if m:
                if cur: blocks.append(cur)
                cur = {"lo": 1, "hi": 99, "lines": []}
                continue
            if cur is not None:
                cur["lines"].append(l)
        if cur: blocks.append(cur)

    passages, questions = {}, []
    for bi, b in enumerate(blocks):
        pid = "PBT%d-B%d" % (num, bi + 1)
        # pisahkan bacaan dari soal: soal pertama = "<lo>."
        first = None
        for i, l in enumerate(b["lines"]):
            m = QNUM_RE.match(l)
            if m and int(m.group(1)) == b["lo"]:
                first = i; break
        if first is None:
            continue
        ptxt = [MARK_RE.sub("", x).strip() for x in b["lines"][:first]]
        ptxt = [x for x in ptxt if x]
        if len(ptxt) < 4:
            continue
        passages[pid] = ptxt

        # ---- soal ----
        qs, cq = [], None
        expect = b["lo"]
        for l in b["lines"][first:]:
            m = QNUM_RE.match(l)
            if m and int(m.group(1)) == expect and "(" not in l[:m.end(1)]:
                if cq: qs.append(cq)
                cq = {"n": expect, "stem": [m.group(2)], "opt": []}
                expect += 1
                l = ""
            if cq is None:
                continue
            if OPT_RE.search(l) or cq["opt"]:
                if l.strip(): cq["opt"].append(l)
            elif l.strip():
                cq["stem"].append(l.strip())
        if cq: qs.append(cq)
        for q in qs:
            if q["n"] > b["hi"]:
                continue
            q["pid"] = pid; q["blk"] = bi
            questions.append(q)
    return passages, questions

def split_options(optlines):
    txt = " ".join(x.strip() for x in optlines)
    txt = re.sub(r"\s+", " ", txt)
    parts = list(OPT_RE.finditer(txt))
    if len(parts) < 2:
        return None
    out, letters = [], []
    for i, m in enumerate(parts):
        end = parts[i + 1].start() if i + 1 < len(parts) else len(txt)
        out.append(txt[m.end():end].strip().rstrip(".").strip())
        letters.append(m.group(1))
    if letters != ["A", "B", "C", "D"][:len(letters)]:
        return None
    return out

# ---------- answer key ----------
def answer_key(lines):
    """-> {nomor_test: (rangkaian_kunci, [kelompok,...])}"""
    ak = next((i for i, l in enumerate(lines) if l.strip() == "ANSWER KEY"), None)
    keys, cur = {}, None
    for l in lines[ak:]:
        m = re.match(r"^\s*PRACTICE TEST (\d+)\s*$", l)
        if m:
            cur = int(m.group(1)); keys.setdefault(cur, ["", []])
            continue
        if cur and re.match(r"^\s*[A-D][A-D\s]+$", l) and len(l.strip()) > 3:
            keys[cur][0] += re.sub(r"\s+", "", l.strip())
            keys[cur][1].extend(l.split())
    return dict((k, (v[0], v[1])) for k, v in keys.items())

if __name__ == "__main__":
    L = clean_lines(raw())
    T = split_tests(L)
    K = answer_key(L)
    tot = 0
    for n, body in T:
        p, q = parse_test(n, body)
        ok = sum(1 for x in q if split_options(x["opt"]))
        tot += ok
        key, grp = K.get(n, ("", []))
        blks = sorted(set(x["blk"] for x in q))
        per = [sum(1 for x in q if x["blk"] == b) for b in blks]
        print("Test %-3d bacaan %-3d soal %-3d (opsi ok %-3d) kunci %-3d | soal/blok %s | kunci/kel %s"
              % (n, len(p), len(q), ok, len(key), per, [len(g) for g in grp]))
    print("TOTAL soal", tot, "| test", len(T))
