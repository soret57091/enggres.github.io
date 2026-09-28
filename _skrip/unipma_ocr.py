# -*- coding: utf-8 -*-
"""OCR Section 2 (Structure & Written Expression) dari
"Soal Pelatihan TOEFL Mahasiswa" (UNIPMA) — PDF hasil pindaian.

Garis bawah pada soal Written Expression dideteksi dari piksel (deretan
piksel gelap mendatar), lalu tiap huruf penanda A-D dipasangkan dengan
garis tepat di atasnya. Cara ini sama dengan yang dipakai untuk
Best of The Best (lihat LANJUTAN.md bagian 5).

Jalankan: python3 _skrip/unipma_ocr.py   -> /tmp/unipma_sec2.json
"""
import os, io, re, json, subprocess, csv
import numpy as np
from PIL import Image

PDF = os.path.expanduser("~/mnt/TOEFL IELTS/referensi 2/"
                         "B006_15_08_2025_10_28_392025_Soal Pelatihan TOEFL Mahasiswa.pdf")
DIR = "/tmp/unipma"
STRUCT_PAGES = [12, 13]          # halaman PDF berisi soal 1-15
WE_PAGES = [15, 16, 17, 18, 19]  # halaman PDF berisi soal 16-40

def render():
    os.makedirs(DIR, exist_ok=True)
    for p in STRUCT_PAGES + WE_PAGES:
        f = os.path.join(DIR, "p-%02d.png" % p)
        if not os.path.exists(f):
            subprocess.run(["pdftoppm", "-r", "300", "-gray", "-png",
                            "-f", str(p), "-l", str(p), PDF, os.path.join(DIR, "p")], check=False)

def tsv(png):
    out = subprocess.run(["tesseract", png, "stdout", "--psm", "6", "tsv"],
                         capture_output=True, text=True).stdout
    rows = []
    for r in csv.DictReader(io.StringIO(out), delimiter="\t", quoting=csv.QUOTE_NONE):
        try:
            if r["text"] and r["text"].strip() and int(r["conf"]) > 20:
                rows.append({"t": r["text"].strip(), "x": int(r["left"]), "y": int(r["top"]),
                             "w": int(r["width"]), "h": int(r["height"])})
        except (ValueError, TypeError, KeyError):
            continue
    return rows

def underlines(png):
    """Deteksi garis bawah: deretan piksel gelap mendatar, lebar >=38px, tinggi <=6px."""
    a = np.array(Image.open(png).convert("L"))
    dark = a < 128
    H, W = dark.shape
    res = []
    y = 0
    while y < H:
        row = dark[y]
        if row.sum() < 30:
            y += 1; continue
        # cari deretan mendatar yang panjang
        idx = np.flatnonzero(row)
        start = None; prev = None
        for x in list(idx) + [None]:
            if x is not None and (prev is None or x - prev <= 2):
                if start is None: start = x
                prev = x; continue
            if start is not None and prev - start >= 38:
                thick = 0
                for dy in range(0, 8):
                    if y + dy < H and dark[y + dy, start:prev].mean() > 0.75:
                        thick += 1
                    else:
                        break
                if thick <= 6:
                    res.append((int(start), int(prev), int(y)))
            start = None if x is None else x
            prev = x
        y += 1
    # gabungkan garis yang bersebelahan (tebalnya lebih dari satu piksel)
    res.sort(key=lambda r: (r[2], r[0]))
    merged = []
    for x0, x1, y in res:
        hit = False
        for m in merged:
            if abs(m[2] - y) <= 6 and not (x1 < m[0] - 5 or x0 > m[1] + 5):
                m[0] = min(m[0], x0); m[1] = max(m[1], x1); hit = True; break
        if not hit:
            merged.append([x0, x1, y])
    return merged

def rows_of(words, tol=18):
    rows = {}
    for w in words:
        k = None
        for r in rows:
            if abs(r - (w["y"] + w["h"] / 2)) < tol:
                k = r; break
        if k is None:
            k = w["y"] + w["h"] / 2
            rows[k] = []
        rows[k].append(w)
    return [sorted(rows[k], key=lambda z: z["x"]) for k in sorted(rows)]

def parse_we(png):
    words = tsv(png)
    uls = underlines(png)
    rws = rows_of(words)
    marker_rows = [r for r in rws if r and all(re.fullmatch(r"[A-D]", w["t"]) for w in r) and len(r) <= 5]
    tagged = {}
    for x0, x1, y in uls:
        above = [w for w in words if y - 70 < w["y"] + w["h"] < y + 6 and w["y"] + w["h"] > y - 70]
        hit = [w for w in above
               if (min(w["x"] + w["w"], x1) - max(w["x"], x0)) / max(1.0, w["w"]) >= 0.55
               and 0 < y - (w["y"] + w["h"]) < 25]
        below = [w for w in words if 0 < w["y"] - y < 60 and re.fullmatch(r"[A-D]", w["t"])
                 and x0 - 25 <= w["x"] + w["w"] / 2 <= x1 + 25]
        if not hit or not below:
            continue
        uc = (x0 + x1) / 2.0
        below.sort(key=lambda w: abs(w["x"] + w["w"] / 2 - uc))
        for w in hit:
            tagged[(w["x"], w["y"], w["t"])] = below[0]["t"]
    return words, rws, marker_rows, tagged

if __name__ == "__main__":
    render()
    for p in WE_PAGES[:1]:
        png = os.path.join(DIR, "p-%02d.png" % p)
        words, rws, mrows, tagged = parse_we(png)
        print("halaman", p, "kata", len(words), "baris", len(rws), "baris penanda", len(mrows),
              "kata bergaris bawah", len(tagged))
        for r in rws[:14]:
            print("   ", " ".join((("[%s:%s]" % (w["t"], tagged[(w["x"], w["y"], w["t"])]))
                                   if (w["x"], w["y"], w["t"]) in tagged else w["t"]) for w in r))
