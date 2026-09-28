# -*- coding: utf-8 -*-
"""
Bank 14 & 15 — TOEFL PBT Reading Comprehension, Practice Test 30-46.
Sumber: "TOEFL-PBT-Practice-test.pdf" (17 practice test + answer key).

Kunci jawaban diambil dari ANSWER KEY buku. Untuk test berformat
"Passage 1..5" (penomoran soal ulang dari 1), jumlah soal tiap bacaan
DICOCOKKAN dengan pengelompokan huruf di answer key sebagai verifikasi
silang; kalau tidak cocok, seluruh test dibuang.

Pembahasan dibuat otomatis: tiap soal diberi kutipan pendukung dari
bacaannya (baris yang dirujuk soal, atau kalimat dengan kecocokan kata
terbanyak terhadap batang soal + kunci). Semua kutipan diverifikasi
benar-benar ada di dalam teks bacaan yang dirujuk.

Jalankan: python3 _skrip/build_bank14.py
"""
import re, io, os, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pbt_parse as P

STOP = set("""a an the of to in on at for from by with as and or but is are was were be been being
that this these those it its their his her they them he she we you i not no than then there here
which who whom whose what when where why how all any some most more much many other others
according passage author line lines word words mainly discuss following statements about does do did
can could will would may might must should first second third one two three EXCEPT paragraph""".split())

def words(s):
    return [w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP and len(w) > 2]

def sentences(text):
    flat = re.sub(r"\s+", " ", text.replace("\n", " ")).strip()
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"(])", flat)
    return [p.strip() for p in parts if len(p.strip()) > 40]

def best_sentence(text, probe):
    pw = set(words(probe))
    if not pw: return None
    best, bs = None, 0
    for s in sentences(text):
        sw = set(words(s))
        if not sw: continue
        sc = len(pw & sw) / (1 + 0.012 * len(s))
        if sc > bs: best, bs = s, sc
    return best if bs > 0 else None

def shorten(s, n=300):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------------- penomoran baris bacaan ----------------
def numbered(plines):
    """Kembalikan (teks_bacaan_dengan_penanda, {nomor_baris: isi_baris})."""
    out, idx = [], {}
    for i, l in enumerate(plines, 1):
        idx[i] = l
        out.append(("(%d) " % i if i % 5 == 0 else "     ") + l)
    return "\n".join(out), idx

LINEREF = re.compile(r"\blines?\s*(\d+)\s*(?:[-–—~]\s*(\d+))?", re.I)
QUOTED = re.compile(r"[\"“”']([A-Za-z][A-Za-z \-']{1,40})[\"“”']")

# ---------------- penggolongan jenis soal ----------------
def classify(stem):
    s = stem.lower()
    if "closest in meaning" in s or "could best be replaced by" in s:
        return "vocabulary", "Vocabulary in Context"
    if re.search(r"\brefers? to\b", s):
        return "reading", "Reference"
    if re.search(r"main (idea|topic|subject|purpose)|mainly discuss|primarily concerned|best title|passage.*mainly about", s):
        return "reading", "Main Idea"
    if "except" in s or "not mentioned" in s or re.search(r"\bnot\b.*\bmention", s):
        return "reading", "Negative Fact"
    if re.search(r"where in the passage", s):
        return "reading", "Lokasi Informasi"
    if re.search(r"can be inferred|it is implied|the author implies|suggests that|probably|most likely", s):
        return "reading", "Inference"
    if re.search(r"in order to|why does the author|the author mentions.*in order|purpose of|author'?s? (attitude|tone)", s):
        return "reading", "Purpose"
    if re.search(r"paragraph.*(precede|follow)|before the passage|after the passage", s):
        return "reading", "Overview Items"
    if re.search(r"according to the passage|according to the author|the passage states|stated in the passage", s):
        return "reading", "Detail"
    return "reading", "Multiple Choice"

LETTER = "ABCD"

def explain(sub, stem, opts, ans, ptext, idx):
    kunci = "<b>%s. %s</b>" % (LETTER[ans], esc(opts[ans]))
    # kutipan: baris yang dirujuk soal, atau kalimat paling cocok
    m = LINEREF.search(stem)
    kutip, sumber = None, ""
    if m:
        a = int(m.group(1)); b = int(m.group(2) or m.group(1))
        got = [idx[i] for i in range(a, b + 1) if i in idx]
        if got:
            kutip = " ".join(got)
            sumber = "baris %d" % a if a == b else "baris %d–%d" % (a, b)
    if not kutip:
        kutip = best_sentence(ptext, stem + " " + opts[ans])
        sumber = "bacaan"
    kt = ('Kutipan pendukung (%s): “<em>%s</em>”.' % (sumber, esc(shorten(kutip)))) if kutip else ""

    if sub == "Vocabulary in Context":
        q = QUOTED.search(stem)
        kata = ("<b>%s</b>" % esc(q.group(1))) if q else "kata yang ditanyakan"
        return ("Soal kosakata dalam konteks: cari kata yang bisa menggantikan %s "
                "tanpa mengubah makna kalimatnya. Jawabannya %s. %s" % (kata, kunci, kt))
    if sub == "Reference":
        q = QUOTED.search(stem)
        kata = ("<b>%s</b>" % esc(q.group(1))) if q else "kata rujukan itu"
        return ("Soal rujukan: %s menunjuk kembali ke kata benda yang disebut sebelumnya "
                "di kalimat yang sama atau kalimat tepat sebelumnya. Yang dirujuk adalah %s. %s"
                % (kata, kunci, kt))
    if sub == "Main Idea":
        return ("Soal gagasan utama: pilihan yang benar harus mencakup <b>seluruh</b> bacaan, "
                "bukan hanya satu paragraf atau satu rincian. Jawabannya %s. %s" % (kunci, kt))
    if sub == "Negative Fact":
        return ("Soal fakta negatif (EXCEPT / NOT mentioned): tiga pilihan lain bisa ditemukan "
                "di bacaan, satu pilihan tidak. Yang tidak didukung bacaan — dan karena itu "
                "menjadi jawabannya — adalah %s. %s" % (kunci, kt))
    if sub == "Inference":
        return ("Soal simpulan: jawabannya tidak tertulis apa adanya, tetapi merupakan "
                "kesimpulan langsung dari yang tertulis. Jawabannya %s. %s" % (kunci, kt))
    if sub == "Purpose":
        return ("Soal maksud penulis: tanyakan mengapa bagian itu ditulis, bukan apa isinya. "
                "Jawabannya %s. %s" % (kunci, kt))
    if sub == "Lokasi Informasi":
        return ("Soal letak informasi: telusuri tiap rentang baris yang ditawarkan lalu cocokkan "
                "dengan isi yang ditanyakan. Jawabannya %s. %s" % (kunci, kt))
    if sub == "Overview Items":
        return ("Soal alur bacaan: perhatikan kalimat pembuka/penutup bacaan untuk menebak apa "
                "yang mendahului atau menyusulnya. Jawabannya %s. %s" % (kunci, kt))
    if sub == "Detail":
        return ("Soal rincian: jawabannya dinyatakan langsung di bacaan; cari kata kunci soal di "
                "teks lalu baca kalimat di sekitarnya. Jawabannya %s. %s" % (kunci, kt))
    return ("Cocokkan tiap pilihan dengan isi bacaan; hanya satu yang benar-benar didukung teks. "
            "Jawabannya %s. %s" % (kunci, kt))

# ---------------- pembangunan ----------------
def build():
    L = P.clean_lines(P.raw())
    tests = P.split_tests(L)
    keys = P.answer_key(L)
    banks = {"a": [], "b": []}
    pas = {"a": {}, "b": {}}
    stat = {"soal": 0, "buang_opsi": 0, "buang_kunci": 0, "test_buang": []}

    for num, body in tests:
        passages, qs = P.parse_test(num, body)
        key, grp = keys.get(num, ("", []))
        if not key:
            stat["test_buang"].append((num, "tanpa kunci")); continue

        blks = sorted(set(q["blk"] for q in qs))
        per = [sum(1 for q in qs if q["blk"] == b) for b in blks]
        global_num = max(q["n"] for q in qs) > 20   # penomoran 1..50 menyeluruh

        offs = {}
        if not global_num:
            if [len(g) for g in grp] != per:
                stat["test_buang"].append((num, "jumlah soal tak cocok kunci")); continue
            c = 0
            for i, b in enumerate(blks):
                offs[b] = c; c += per[i]

        slot = "a" if num <= 37 else "b"
        # bacaan
        pmap = {}
        for pid, plines in passages.items():
            txt, idx = numbered(plines)
            pmap[pid] = (txt, idx)

        used = set()
        for q in qs:
            opts = P.split_options(q["opt"])
            if not opts or len(opts) < 4 or len(set(opts)) != len(opts) or min(len(o) for o in opts) < 1:
                stat["buang_opsi"] += 1; continue
            ki = (q["n"] - 1) if global_num else (offs[q["blk"]] + q["n"] - 1)
            if ki < 0 or ki >= len(key):
                stat["buang_kunci"] += 1; continue
            ans = "ABCD".find(key[ki])
            if ans < 0 or ans >= len(opts):
                stat["buang_kunci"] += 1; continue
            stem = re.sub(r"\s+", " ", " ".join(q["stem"])).strip()
            if len(stem) < 12:
                stat["buang_opsi"] += 1; continue
            theme, sub = classify(stem)
            ptext, idx = pmap.get(q["pid"], ("", {}))
            if not ptext:
                stat["buang_opsi"] += 1; continue
            qid = "pbt%d-%d-%d" % (num, q["blk"] + 1, q["n"])
            banks[slot].append({
                "id": qid, "theme": theme, "subtheme": sub,
                "ref": "Practice Test %d, bacaan %d no.%d" % (num, q["blk"] + 1, q["n"]),
                "passageId": q["pid"],
                "question": esc(stem),
                "options": [esc(o) for o in opts],
                "answer": ans,
                "explain": explain(sub, stem, opts, ans, ptext, idx),
            })
            used.add(q["pid"]); stat["soal"] += 1
        for pid in used:
            pas[slot][pid] = {"title": "Practice Test %d — Bacaan %s" % (num, pid.split("-B")[1]),
                              "text": pmap[pid][0]}

    for slot, rng in (("a", "30-37"), ("b", "38-46")):
        bank = {"source": {"id": "pbt-read-" + slot,
                           "name": "TOEFL PBT Reading — Practice Test " + rng,
                           "test": "TOEFL PBT"},
                "passages": pas[slot], "questions": banks[slot]}
        fn = "data/bank-1%d-pbt-%s.js" % (4 if slot == "a" else 5, slot)
        out = "/* dibuat oleh _skrip/build_bank14.py — jangan diedit tangan */\nTOEFLDRILL.addBank(\n"
        out += json.dumps(bank, ensure_ascii=False, indent=1) + "\n);\n"
        io.open(fn, "w", encoding="utf-8").write(out)
        d = {}
        for q in banks[slot]:
            d["ABCD"[q["answer"]]] = d.get("ABCD"[q["answer"]], 0) + 1
        print("%s : %d soal, %d bacaan, sebaran %s" % (fn, len(banks[slot]), len(pas[slot]), d))
    print("dibuang — opsi rusak:", stat["buang_opsi"], "| kunci tak cocok:", stat["buang_kunci"])
    if stat["test_buang"]:
        print("test dibuang:", stat["test_buang"])
    # sebaran subtema
    allq = banks["a"] + banks["b"]
    s = {}
    for q in allq:
        s[q["subtheme"]] = s.get(q["subtheme"], 0) + 1
    print("subtema:", json.dumps(s, ensure_ascii=False))

if __name__ == "__main__":
    build()
