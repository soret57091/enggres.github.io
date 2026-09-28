# -*- coding: utf-8 -*-
"""Ekstraksi TOEFL ITP Practice Tests Level 1 Vol.3 (ETS) — sadar dua kolom.
Menulis /tmp/itp_pages.txt dengan penanda <<<PAGE n>>>.
Jalankan: python3 _skrip/itp_extract.py"""
import os, io, sys
import pdfplumber

PDF = os.path.expanduser("~/mnt/TOEFL IELTS/referensi 2/itp-practice-test-level-1-volume-3-ebook.pdf")
OUT = "/tmp/itp_pages.txt"

def page_text(page, split_x=None):
    ws = page.extract_words(x_tolerance=1.6, y_tolerance=2.5, keep_blank_chars=False)
    if not ws:
        return ""
    if split_x is None:
        return lines_of(ws)
    left = [w for w in ws if w["x0"] < split_x]
    right = [w for w in ws if w["x0"] >= split_x]
    return lines_of(left) + "\n" + lines_of(right)

def lines_of(ws):
    rows = {}
    for w in ws:
        k = round(w["top"] / 4.0)
        rows.setdefault(k, []).append(w)
    out = []
    for k in sorted(rows):
        row = sorted(rows[k], key=lambda w: w["x0"])
        s, prev = "", None
        for w in row:
            if prev is not None and w["x0"] - prev > 12:
                s += "   "
            elif prev is not None:
                s += " "
            s += w["text"]; prev = w["x1"]
        out.append(s)
    return "\n".join(out)

def two_col(page):
    """Deteksi dua kolom lewat pita kosong vertikal di tengah.
    Baris selebar halaman (header/footer/keterangan) diabaikan lebih dulu."""
    h, w = page.height, page.width
    ws = [x for x in page.extract_words(x_tolerance=1.6, y_tolerance=2.5)
          if 0.06 * h < x["top"] < 0.94 * h]
    if len(ws) < 40:
        return None
    lo, hi = w * 0.34, w * 0.66
    rows = {}
    for x in ws:
        rows.setdefault(round(x["top"] / 4.0), []).append(x)
    keep = []
    for k, row in rows.items():
        row = sorted(row, key=lambda z: z["x0"])
        # apakah baris ini menembus pita tengah tanpa celah?
        gap, prev, solid = 0, None, False
        for z in row:
            if prev is not None and z["x0"] - prev > 12 and prev < hi and z["x0"] > lo:
                gap = max(gap, z["x0"] - prev)
            prev = z["x1"]
        spans = row[0]["x0"] < lo and row[-1]["x1"] > hi
        if spans and gap < 14:
            continue          # baris selebar halaman -> abaikan
        width = row[-1]["x1"] - row[0]["x0"]
        center = (row[-1]["x1"] + row[0]["x0"]) / 2.0
        if width < 0.55 * w and lo < center < hi and len(row) <= 8:
            continue          # baris pendek di tengah (footer/keterangan) -> abaikan
        keep.extend(row)
    if len(keep) < 30:
        return None
    occ = [False] * (int(hi - lo) + 2)
    for x in keep:
        a, b = max(lo, x["x0"]), min(hi, x["x1"])
        if b <= a:
            continue
        for k in range(int(a - lo), int(b - lo) + 1):
            if 0 <= k < len(occ):
                occ[k] = True
    best, run, start = (0, None), 0, 0
    for k, o in enumerate(occ + [True]):
        if not o:
            if run == 0: start = k
            run += 1
        else:
            if run > best[0]:
                best = (run, lo + start + run / 2.0)
            run = 0
    if best[0] < 14:
        return None
    right = [x for x in ws if x["x0"] >= best[1]]
    left = [x for x in ws if x["x0"] < best[1]]
    if len(right) < 15 or len(left) < 15:
        return None
    return best[1]

if __name__ == "__main__":
    buf = []
    with pdfplumber.open(PDF) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            sx = two_col(page)
            buf.append("<<<PAGE %d%s>>>" % (i, " 2KOL" if sx else ""))
            buf.append(page_text(page, sx))
    io.open(OUT, "w", encoding="utf-8").write("\n".join(buf))
    print("ditulis", OUT, os.path.getsize(OUT), "byte")
