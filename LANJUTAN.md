# Catatan lanjutan — TOEFL/IELTS Drill Web

Dokumen ini untuk sesi berikutnya (atau siapa pun yang melanjutkan). Semua yang
dibutuhkan supaya bisa lanjut tanpa mengulang dari nol ada di sini.

---

## 1. Kondisi sekarang

**2.332 soal** dari **18 bank** dan **36 topik materi** dari 7 unit belajar.
Setiap topik materi punya **minimal 2 contoh soal berpembahasan** dan minimal
10 soal latihan yang cocok di bank.
Buka `index.html` (double-click, offline, tanpa internet).

| Tema | Soal |
|---|---|
| Reading | 1.158 |
| Written Expression | 402 |
| Structure | 333 |
| Vocabulary | 273 |
| Listening (pakai transkrip/naskah) | 147 |
| Writing | 13 |
| Speaking | 6 |

| Sumber | Soal | Isi |
|---|---|---|
| TOEFL PBT — Practice Test 30–37 | 396 | reading, 40 bacaan |
| TOEFL PBT — Practice Test 38–46 | 321 | reading, 45 bacaan |
| TOEFL ITP Level 1 Vol.3 (ETS) | 270 | 2 tes lengkap: listening bernaskah, structure, written expression, reading |
| Peterson's TOEFL Success — Structure | 223 | Lesson 13–22, Review Test D–G, Preview Test 2 |
| Structure & Written Expression — Sari Mubaroh (2021) | 180 | 18 latihan benar/salah, satu per sub-bab modulnya |
| Barron's IELTS Practice Exams | 163 | 6 Academic + 6 General Training, reading |
| Peterson's — latihan isian → pilihan ganda | 146 | Exercise 18.3–22.1 + 25.1 (preposisi) |
| Peterson's TOEFL Success — Reading | 139 | Preview Test 3, Lesson 33–37, Review Test H |
| ETS TOEFL iBT Practice Test 2 | 91 | resmi, format 2026, lengkap 4 skill |
| Practice Test TOEFL C-Media | 90 | Structure 40 + Reading 50 |
| Barron's IELTS — isian/pencocokan → pilihan ganda | 58 | kotak pilihan, pilih-satu, judul bagian, TFNG |
| 202 Useful Exercises for IELTS | 50 | True/False/Not Given |
| Barron's IELTS — blok pulihan → pilihan ganda | 49 | kotak pilihan yang rusak di OCR, dibaca ulang manual |
| Barron's IELTS — isian kata → pilihan ganda | 45 | ringkasan, melengkapi kalimat, jawaban singkat |
| Best of The Best TOEFL | 39 | pembahasan asli bahasa Indonesia |
| UNIPMA — Soal Pelatihan TOEFL (Diagnostic Pre-Test) | 39 | Section 2 saja; kunci ditetapkan ulang |
| Barron's IELTS — Listening | 18 | dengan naskah audio |
| Magoosh — Free TOEFL Practice Questions | 15 | 1 bacaan iBT + prompt speaking & writing |

Ditambah **264 bacaan, transkrip, dan naskah audio** lengkap.

### Materi belajar (tab "Belajar dulu yuk")

| Unit | Topik |
|---|---|
| Tata Bahasa Dasar | 18 |
| Fondasi Kalimat | 9 |
| Written Expression | 1 |
| Reading | 5 |
| Vocabulary | 1 |
| Listening | 1 |
| Writing & Speaking | 1 |

Urutan unit di halaman materi ditentukan oleh **urutan tag `<script>` di
`index.html`**, bukan oleh nama berkasnya. Sekarang urutannya sengaja
tata bahasa dasar → fondasi kalimat → written expression → reading → sisanya.

### Struktur folder

```
TOEFL-Drill-Web/
├── index.html                          ← aplikasinya (satu file, tanpa dependensi)
├── validate.js                         ← cek bank soal + materi + indeks: node validate.js
├── qcheck.js                           ← cek mutu pengecoh: node qcheck.js
├── qaudit.js                           ← cek kutipan pembahasan: node qaudit.js
├── LANJUTAN.md                         ← dokumen ini
├── _skrip/                             ← semua skrip pembuat bank
└── data/
    ├── bank-01-cmedia.js ... bank-18-unipma.js
    ├── lessons-01-structure.js ... lessons-03-tatabahasa.js
    └── topics.js                       ← indeks: soal setopik lintas bank
```

**Menambah bank baru:** buat `data/bank-19-xxx.js`, lalu tambahkan satu baris
`<script src>` di `index.html` (cari komentar `====== BANK SOAL ======`). Selesai.
**Menambah materi baru:** buat `data/lessons-05-xxx.js` dengan format yang sama
seperti berkas lessons lain, lalu daftarkan di bawah komentar `====== MATERI BELAJAR ======`
pada posisi yang kamu inginkan di urutan unit.

---

## 2. Format bank soal

```js
TOEFLDRILL.addBank({
  source: { id:'idunik', name:'Nama Buku', test:'TOEFL iBT' },

  passages: {                                  // opsional
    'id-bacaan': { title:'Judul', text:"baris 1\nbaris 2" }
  },

  questions: [
    { id:'unik-1',                             // wajib unik di seluruh bank
      theme:'reading',                         // structure|written|reading|vocabulary|
                                               // listening|writing|speaking
      subtheme:'Main Idea',                    // bebas, muncul sbg filter
      ref:'Practice Test 1 no.3',              // asal soal, tampil di pojok
      passageId:'id-bacaan',                   // opsional
      instruction:'Pilih ...',                 // opsional, tampil di atas soal
      question:"Teks soal. Boleh <b> <i> <u> <sup> <br>",
      options:["A","B","C"],                   // 2 opsi ke atas, tidak harus 4
      answer:2,                                // INDEKS (0=A, 1=B, 2=C, 3=D)
      explain:"Pembahasan bahasa Indonesia."
    },

    { id:'unik-2', theme:'writing', type:'open',   // soal terbuka (tanpa pilihan)
      question:"Prompt esai...",
      explain:"Panduan jawaban / rubrik."          // tidak ada options & answer
    }
  ]
});
```

Yang divalidasi: `id` unik, `answer` valid, opsi tidak ada yang kembar, `passageId`
harus ada di `passages`, `explain` tidak boleh kosong.

**Jalankan `node validate.js` setiap kali menambah bank.** Perhatikan sebaran kunci
A/B/C/D — kalau timpang berat, hampir pasti ada yang salah.

---

## 3. Yang masih tersisa

> **Catatan (9 Sep 2026):** bagian ini ditulis pada sesi ke-2 dan sebagian sudah
> dikerjakan. Daftar yang mutakhir ada di bagian **"Yang tersisa sesudah sesi ini"**
> di akhir dokumen.

Semua sumber di folder ini sudah digarap. Yang belum diambil beserta alasannya:

**a. Soal berformat isian / jawaban singkat.** Ini yang terbesar. IELTS punya banyak
sentence completion, summary completion, table/note completion, short answer, dan
labelling; Peterson's punya tabel word-form Lesson 18–19; C-Media punya 50 soal
listening. Semuanya tidak berbentuk pilihan ganda sedangkan webnya bertipe pilih-satu.
**Untuk menggarapnya, webnya perlu tipe soal baru** — misalnya isian teks dengan
pencocokan jawaban longgar (abaikan besar-kecil huruf, terima beberapa varian jawaban).
Itu perubahan di `index.html`, bukan sekadar tambah bank.

**b. Soal "pilih TIGA dari A–F"** di Barron's. Kuncinya satu huruf per nomor, tapi
ketiganya sama-sama benar untuk ketiga nomor itu — kalau dipaksakan jadi pilih-satu,
2 dari 3 jawaban benar akan dihitung salah. Sengaja dilewati.

**c. Sisa Best of The Best TOEFL** — 92 "Contoh Soal" dan 4 Practice Test. Alasannya
di bagian 5 di bawah.

**d. Soal yang dibuang karena teks rusak** — sekitar 90 soal dari berbagai sumber
(hasil ekstraksi PDF/OCR cacat). Prinsipnya: lebih baik hilang daripada salah.

---

## 4. Cara ekstraksi yang terbukti jalan — PDF berteks

Catatan teknis dari Peterson's dan Barron's, supaya tidak mengulang trial-and-error.

- **Layout dua kolom**: jangan pakai `pdftotext -layout` polos (kolom kiri-kanan
  tercampur dalam satu baris). Pakai `pdfplumber`, ambil kata beserta koordinatnya,
  pisahkan per kolom berdasarkan `x0` (batas ~300 pada halaman lebar 612), baru susun
  baris berdasarkan `top`.
- **Kata menempel** (`Thefirstrecorded...`): pakai `extract_words(x_tolerance=1.5)`.
  Default 3 terlalu longgar untuk sebagian font.
- **Soal error-identification** (bagian bergaris bawah bertanda A/B/C/D): garis
  bawahnya adalah **objek garis sungguhan** di PDF (`page.lines`). Cocokkan tiap huruf
  penanda dengan garis tepat di atasnya, lalu ambil kata yang rentang `x`-nya
  bertumpang tindih dengan garis itu.
- **Kotak "Directions"**: dibatasi dua garis horizontal selebar halaman. Buang kata
  yang jatuh di antaranya — tapi pastikan dulu kotaknya memang memuat kata
  "Directions", karena garis lebar juga dipakai untuk hal lain.
- **Kebocoran antar-halaman**: batasi rentang halaman tiap latihan secara ketat sampai
  halaman sebelum latihan berikutnya. Kalau tidak, soal dari latihan lain ikut terbaca
  dan **kuncinya bisa tertukar** — ini pernah terjadi dan baru ketahuan saat validasi.
- **Barron's IELTS**: strukturnya sangat rapi — blok `Questions X-Y`, lalu instruksi,
  lalu daftar berlabel (opsional), lalu butir bernomor `21 The first fire engines`
  (tanpa titik setelah angka) dengan opsi menjorok `A carried water...`. Tipe soal
  dikenali dari instruksinya: ada "TRUE/FALSE/NOT GIVEN" → 3 opsi tetap; ada
  "The passage has six paragraphs, A-F" → opsi Paragraf A–F; ada daftar berlabel
  sebelum butir pertama → matching.
- **Nomor soal OCR-an** seperti `Questions 2 1 -2 3`: normalkan dulu semua varian tanda
  hubung (– — ‒ −) jadi `-`, baru buang spasi. Kalau tidak, `11—15` terbaca `1115`.

---

## 5. Cara ekstraksi halaman pindaian (OCR)

- Render 300 DPI grayscale, lalu `tesseract ... tsv` untuk dapat **koordinat tiap kata**.
- **Garis bawah dideteksi dari piksel**: deretan piksel gelap horizontal selebar ≥38 px
  dan setinggi ≤6 px.
- Pasangkan tiap huruf penanda dengan garis bawah tepat di atasnya, lalu ambil kata
  yang **≥55% lebarnya** ada di dalam rentang garis. Kurang dari itu, opsinya
  tumpang-tindih dan salah.
- Garis bawah yang **tidak** punya huruf penanda di bawahnya = tanda rumpang; sisipkan
  `______` di posisi itu.
- **Selalu cari cara memverifikasi silang.** Yang dipakai di sini:
  - *Best of The Best*: kuncinya menuliskan teks opsi yang benar dalam kurung
    (`Jawaban: C (potential)`) — cocokkan dengan opsi hasil ekstraksi, buang yang beda.
  - *202 Exercises*: jumlah butir pernyataan (a–j) harus sama persis dengan jumlah
    jawaban di baris kunci Appendix 2. Enam latihan cocok sempurna, sisanya dibuang.

### Yang gagal di Best of The Best, jangan diulang

- **92 "Contoh Soal"**: huruf pilihan dicetak di kolom kiri terpisah dan hancur total
  di OCR (jadi `9 NF >`). Urutan bisa dipakai sebagai pengganti, tapi baris pertanyaan
  (`Narator : ...`) sering ikut terbaca sebagai opsi sehingga stem-nya rusak. Dari 92,
  hanya 5 lolos verifikasi dan 2 di antaranya cacat. **Tidak sepadan.**
- **16 dari 60 soal Latihan**: huruf penanda tidak terbaca, atau garis bawahnya menyatu
  dengan huruf (misal `to_use`).
- **4 Practice Test (hal. 334–362)**: kuncinya berbentuk grid, bukan per soal.
  Perlu pendekatan lain.

Hasil OCR mentahnya tersimpan di `_ocr-hasil/` (sejajar folder ini), format teks biasa
dengan penanda `<<<PAGE n>>>`.

---

## 6. Audit yang sudah dilakukan

Seluruh bank pernah diaudit menyeluruh (otomatis + pembacaan manual). Yang ditemukan
dan sudah diperbaiki:

- **4 kunci jawaban salah** — `pt-ex14-16`, `ptr-ex34_2-12`, `ptr-ex35_2-20`, `bb-l1-9`.
  Semuanya ketahuan karena pembahasannya bertentangan dengan kuncinya, lalu dicek ulang
  ke PDF aslinya. Dua di antaranya ternyata **salah cetak di bukunya** (Peterson's
  Exercise 34.2 no.12 dan 35.2 no.20 — bacaannya jelas mendukung jawaban lain);
  kuncinya diperbaiki dan diberi catatan di pembahasannya.
- **2 pembahasan tertukar/terbalik** — `ptr-ex37_2-6`, `bb-l4-1`.
- **1 pembahasan nyasar antar-bank** — `br-ac5-11` (pembahasan listening masuk ke soal
  reading); soalnya dibuang.
- **5 soal mustahil dijawab** — bacaan Anasazi (`EX34.2-P1`) terpotong sehingga soal
  no.4–8 tidak ada jawabannya di teks. Bacaannya diekstrak ulang jadi utuh (3.226 char).
- **8 soal lain dibuang** karena stem-nya terpotong di tengah atau isinya rusak.
- **25 stem** dibersihkan dari sisa instruksi ujian yang ikut terbaca (ada yang sampai
  menempelkan seluruh WRITING TASK).
- **35 pembahasan** dipangkas dari isi buku yang ikut tertempel (satu sampai 26 KB).
- **33 bacaan** dibersihkan dari instruksi, writing task, dan header/footer halaman.
- **Kata menempel tanpa spasi** (`ifyou`, `groundfloor`, `FredAllen`, dll.) diperbaiki.

Kalau menambah bank baru, ulangi audit serupa — terutama **poin 1: cocokkan kunci
dengan pembahasannya secara otomatis.** Itu yang paling banyak menangkap kesalahan.

---

## 7. Catatan pemakaian

Progres belajar disimpan di `localStorage` browser. Untuk file yang dibuka langsung
dari disk (`file://`), sebagian browser memblokirnya — makanya ada tombol
**Ekspor progres** di halaman Statistik. Pakai itu sebelum menutup tab kalau progresmu
mau disimpan, lalu **Impor progres** saat kembali.

---

## TAHAP TERAKHIR YANG DIKERJAKAN (8 Sep 2026) — TITIK LANJUT

### Sudah selesai ✅ — Tahap 9: Peterson's isian → pilihan ganda
`data/bank-09-petersons-inline.js` — **146 soal baru**, sudah masuk `index.html`,
`node validate.js` bersih (0 masalah), sebaran kunci A/B/C/D = 37/37/36/36.

Isinya (semuanya latihan isian yang diubah jadi 4 opsi):

| Latihan | Subtema | Soal |
|---|---|---|
| Exercise 25.1 | Preposisi | 48 |
| Exercise 18.3 | Bentuk Kata (Adjective/Adverb) | 20 |
| Exercise 19.5 | Kata Rancu Campuran | 16 |
| Exercise 22.1 | Infinitive / Gerund / Bentuk Dasar | 12 |
| Exercise 20.1 | Kesesuaian Subjek–Kata Kerja | 11 |
| Exercise 19.3 | another / other | 9 |
| Exercise 19.1 | do / make | 8 |
| Exercise 19.2 | so / such / too / as | 8 |
| Exercise 19.4 | many / much / few / little | 8 |
| Exercise 21.1 | Participle (-ing / -ed) | 6 |

**Aturan penyusunan opsi yang dipakai** (ikuti aturan yang sama untuk bank berikutnya):
1. Opsi = **bentuk kata nyata dari akar yang sama** (great/greatly/greater/greatest),
   jadi panjang dan jenis katanya otomatis setara — tidak ada opsi yang timpang.
2. Tidak pernah mengarang kata yang tidak ada.
3. Pengecoh yang secara tata bahasa **bisa ikut benar** dibuang dan diganti
   (mis. "almost all" untuk soal Most/Almost, "living" untuk soal live/alive).
4. Soal yang punya dua rumpang dipecah jadi dua soal; rumpang yang tidak ditanyakan
   diisi jawaban benarnya.
5. Posisi kunci dirotasi berurutan (A,B,C,D,A,…) supaya sebarannya rata.
6. Item yang kuncinya rusak di hasil OCR diperbaiki manual, bukan ditebak.

Skrip pembuatnya: `_skrip/build_bank9.py` (berisi seluruh naskah soal + pembahasan,
tinggal `python3 build_bank9.py`; sudah menulis langsung ke `data/`).

### Selesai ✅ — Tahap 10 & 11: Barron's IELTS isian → pilihan ganda

`data/bank-10-barron-completion.js` (**58 soal**) dan
`data/bank-11-barron-isian.js` (**45 soal**). Keduanya sudah masuk `index.html`.

**Bank 10 — dibuat otomatis** (`_skrip/build_bank10.py`, penunjang `_skrip/blist.py`).
Pengecohnya diambil dari daftar pilihan milik buku itu sendiri, dipilih tiga yang
panjangnya paling mirip kunci:

| Jenis | Soal |
|---|---|
| Mencocokkan informasi ke paragraf/bagian | 16 |
| Informasi rinci "pilih satu" (dari daftar A–F) | 16 |
| Memilih judul bagian (daftar heading) | 14 |
| Melengkapi catatan dari kotak pilihan A–K | 7 |
| True/False/Not Given yang sebelumnya lolos | 5 |

**Bank 11 — ditulis tangan** (`_skrip/build_bank11.py`), yaitu soal isian kata yang
tidak punya daftar pilihan sama sekali. Setiap set opsi disusun manual: empat pilihan
sejenis dan sepanjang, semuanya masuk akal secara tata bahasa, hanya satu yang
didukung bacaan. Pembahasannya mengutip kalimat aslinya.
Cakupan: AC2 1–5, AC5 28–36, AC6 22–27, GT1 21–27, GT1 35–40, GT2 5–7, GT2 15–20, GT6 28–30.

### Selesai ✅ — Tahap 12: verifikasi mutu

Tiga lapis pemeriksaan, semuanya sudah dijalankan:

1. `node validate.js` — 0 masalah (ID ganda, kunci di luar jangkauan, bacaan hilang, opsi kembar).
2. `node qcheck.js` — pemeriksa **mutu pengecoh**: mendeteksi set opsi timpang
   (terpanjang > 2,2× terpendek) dan kebocoran kunci lewat panjang opsi.
   Hasil: bank-09 dan bank-11 **0 set timpang, 0 kebocoran**. Bank lama tetap timpang
   di beberapa soal karena itu memang opsi asli dari bukunya — tidak diubah.
3. **Audit isi oleh subagent** atas ketiga bank baru. Temuan yang sudah diperbaiki
   lewat `node fixbanks2.js`:
   - 19 pengecoh yang ternyata ikut benar diganti (mis. `easier`, `much`, `lively`,
     `the other`, `simpler`, `closer`, dan `for` pada *open the door to*).
   - 7 soal kano Barron's yang tidak terjawab (opsinya cuma "Kano A/B/C" tanpa
     keterangan) diberi nama jenis kano yang jelas, dipastikan dari bacaan.
   - 2 soal Braille berkunci ganda: opsi "Paragraf D" yang juga benar dibuang.
   - 5 pembahasan True/False/Not Given ditulis ulang dengan kutipan bacaan.
   - 48 metadata `ref` ganda, 12 sisa angka catatan kaki OCR, 9 bacaan dipangkas
     dari halaman WRITING TASK dan potongan daftar soal.
   - 1 soal Barron's diperbaiki kalimatnya (`bri-gt1-36`).
4. `node fixsplit.js` — menyambung **83 kata yang terpecah OCR** di seluruh bacaan
   (`cam ouflage` → `camouflage`, `ani mals` → `animals`). Aman: hanya disambung bila
   bentuk gabungannya memang muncul utuh di tempat lain dan salah satu penggalannya
   bukan kata Inggris yang berdiri sendiri.
5. Uji jalan di browser (Playwright): 1.062 soal termuat, 101 bacaan, **0 error konsol**.

### Selesai ✅ — Tahap 13: memulihkan blok yang kotak pilihannya rusak di OCR

`data/bank-12-barron-pulih.js` — **49 soal**, dibuat dengan membaca ulang halaman
asli PDF satu per satu (`_skrip/build_bank12.py`). Setiap kunci dicocokkan kembali
dengan isi bacaan sebelum ditulis:

| Blok | Isi | Soal |
|---|---|---|
| GT4 1–7 | mencocokkan kesempatan jadi relawan (A–E) | 7 |
| GT6 1–7 | mencocokkan iklan penyewaan mobil (A–C) | 7 |
| AC2 27–32 | catatan Catastrophe vs Gradualist Theory (kotak A–K) | 6 |
| AC3 14–19 | mengelompokkan ciri penny bloods / dime novels / keduanya | 6 |
| AC4 28–33 | ringkasan kecerdasan burung gagak (kotak A–N) | 6 |
| GT5 21–27 | keuntungan & kerugian telecommuting (A–G, A–E) | 7 |
| GT6 31–36 | fakta energi panas bumi & surya (A–E) | 6 |
| AC3 2,3,5,6 | memilih judul bagian bacaan CT Scanner | 4 |

Contoh cara pemulihannya: kotak pilihan AC2 27–32 di hasil OCR berantakan —
huruf D, E, F terpisah dari katanya. Susunan yang benar (A short, B small,
C Charles Darwin, D long, E definite, F disasters, G James Hutton, H mysterious,
I Walter Alvarez, J evolution, K Georges Cuvier) dipastikan dengan mencocokkan
keenam kunci buku ke isi bacaan — semuanya cocok, jadi susunan itu benar.

**Yang tetap tidak bisa dipulihkan** (kotak pilihannya benar-benar hilang dari OCR,
bukan sekadar berantakan): AC3 20–23 (daftar peristiwa A–F) dan GT2 8–14
(daftar penutup kalimat A–M). Lebih baik hilang daripada ditebak.

### Belum dikerjakan
- C-Media Listening 50 soal — tidak ada audio/transkrip, tidak bisa dipakai.
- Best of The Best: 92 "Contoh Soal" + 4 Practice Test — hasil OCR terlalu rusak.
- Barron's AC3 20–23 dan GT2 8–14 (11 soal) — daftar pilihannya hilang dari OCR.
- Pembahasan bank-10 sebagian masih berbunyi "Kunci buku: X" tanpa kutipan
  pendukung. Kuncinya benar, tapi bisa diperkaya nanti.

### Berkas bantu di folder ini
`validate.js` (cek struktur) · `qcheck.js` (cek mutu pengecoh) ·
`fixbanks2.js` (perbaikan hasil audit) · `fixsplit.js` (penyambung kata OCR) ·
`_skrip/` (semua skrip pembuat bank).

---

## TITIK LANJUT (8 Sep 2026, sesi ke-3)

### Selesai ✅ — Tahap 14: memperkaya pembahasan bank-10 & bank-12

Skrip: `enrich10.js` lalu `patch_expl.js` (keduanya di folder ini, tinggal `node`).

**107 soal Barron's (bank-10 + bank-12) sekarang semuanya punya kutipan pendukung
dari bacaannya** — sebelumnya 58 di antaranya cuma berbunyi "Kunci buku: X".
Caranya: untuk soal paragraf/judul, paragraf sasaran dipotong dari bacaan; untuk
soal lain, kalimat dengan kecocokan kata terbanyak dicari otomatis; 10 sisanya
ditulis tangan. Stem "Judul yang paling tepat untuk Section A" juga sudah diberi
nama bacaannya supaya tidak kembar antar-tes.

`node validate.js` → 0 masalah.

### Selesai ✅ — Tahap 15: menindaklanjuti audit bank-12

Subagent sudah mengaudit ke-49 soal `bank-12` terhadap bacaannya.
**Semua 49 kunci BENAR** — tidak ada kunci salah, tidak ada soal tak terjawab.
Semua temuan lainnya sudah diperbaiki lewat `node fixbank12.js`:

- **1 pengecoh yang ikut benar** — `brz-ac4-32`: opsi "show her how to use" ternyata
  juga didukung kalimat yang sama dengan kuncinya. Diganti "take any interest in".
- **1 kunci bocor antarsoal** — batang `brz-ac2-31` memuat frasa "over a long period
  of time" yang persis jawaban `brz-ac2-32`. Batangnya diubah jadi "…happened gradually".
- **17 kutipan pembahasan salah ambil** diganti dengan kalimat yang benar
  (ac2-31, ac2-32, ac3-15, ac4-30, ac4-31, ac4-32, gt5-23, gt5-24, gt5-26, gt5-27,
  gt6-3, gt6-4, gt6-7, gt6-31, gt6-32, gt6-34, gt6-35). Penyebabnya: bacaan GT4-S1,
  GT5-S2, GT6-S1 dan GT6-S3 masing-masing memuat lebih dari satu teks, jadi pencarian
  kalimat otomatis kadang mengambil dari teks tetangga.
- **Alasan pengecoh** pada `brz-gt5-25/26/27` ditulis ulang satu per satu (sebelumnya
  memakai kalimat seragam yang cuma cocok untuk soal 25).
- **Bacaan GT6-S1 diperbaiki**: baris "10 percent off our usual low prices!" yang
  hilang di OCR dikembalikan, dan sisa penanda halaman "Practice Test B" dibuang.
- 11 sisa angka catatan kaki OCR dibersihkan (`fictionalized1`, `behavior1`,
  `paleontologists2`, `profes sionally`, dll.).

**Verifikasi menyeluruh:** semua **93 kutipan pendukung** di bank-10 dan bank-12
sekarang dicek otomatis — potongan kutipannya harus benar-benar ada di dalam teks
bacaan yang dirujuk. Hasilnya **0 tidak cocok**. Skrip pemeriksanya ada di dalam
`fixbank12.js` dan bisa dijalankan ulang kapan saja.

### Selesai ✅ — Tahap 16: dropdown setup diberi jumlah soal

Di halaman "Mulai drilling", dropdown **Sumber** dan **Sub-tema** sekarang
menampilkan jumlah soalnya dan diurutkan dari yang terbanyak, mis.
"Preposisi (48)", "Bentuk Kata (Adjective/Adverb) (20)".

### Ide berikutnya (opsional)
- Dropdown sub-tema di halaman setup bisa diberi jumlah soal, mis. "Preposisi (48)",
  dan diurutkan dari yang terbanyak — sekarang sudah ada filternya, tinggal dipercantik.

---

## TITIK LANJUT (9 Sep 2026, sesi ke-4) — sumber `referensi 2`

Seluruh isi folder `../referensi 2` digarap: **+1.221 soal** (1.111 → 2.332),
**+21 topik materi** (18 → 39), dan **+163 bacaan** (101 → 264).

### Selesai ✅ — Tahap 17: materi tata bahasa dasar

`data/lessons-03-tatabahasa.js` — unit baru **"Tata Bahasa Dasar"**
berisi **18 topik**, disarikan dari *Sari Mubaroh, "Structure & Written Expression
(Toefl Equivalent English)", 2021* (80 halaman, Chapter 1–4).

Semua tabel aslinya (Table 1–18: aturan jamak, countable/uncountable, possessive,
daftar connector, pola agreement, pola paralel, bentuk verb, modal) ikut dibawa.
Karena itu **`index.html` diberi CSS baru untuk `.lesson table` dan `.lesson .tw`**
(pembungkus yang bisa digeser mendatar) — cari blok tepat setelah `.lesson s{...}`.
Tanpa CSS itu tabel akan tampil polos tanpa garis.

Tiap topik: 2–4 bagian penjelasan + 2 contoh soal berpembahasan.

### Selesai ✅ — Tahap 18: soal latihan modul tata bahasa

`data/bank-13-swe-dasar.js` — **180 soal** (18 Exercise × 10 butir), dibuat oleh
`_skrip/build_bank13.py`.

Bentuknya bukan pilihan ganda empat opsi melainkan **dua opsi: "Benar (Correct)"
dan "Salah (Incorrect)"** — sesuai instruksi asli latihannya. Bank soal memang
mengizinkan 2 opsi ke atas, jadi tidak perlu mengubah apa pun di `index.html`.

Dua catatan penting kalau bank ini diaudit ulang:

1. **Kolom "Analysis" di buku sengaja dikosongkan** untuk diisi mahasiswa, jadi
   buku itu **tidak memuat kunci**. Semua kunci ditetapkan ulang dari kaidahnya,
   dan tiap pembahasan menyebutkan perbaikannya secara eksplisit sehingga kunci
   dan pembahasan saling memeriksa.
2. **Salah ketik yang jelas di naskah buku dinormalkan** supaya butirnya menguji
   yang seharusnya diuji, bukan salah ketiknya: `pollice`→`police`,
   `opporunites`→`opportunities`, `cacth`→`catch`, `proffessional`→`professional`,
   `asssigment`→`assignment`, `zoom`→`zoo`, `quests`→`guests`, `bought back`→
   `brought back`, `She spend`→`She spent`, `W offered`→`We offered`,
   `will took`→`will take`, `rode her house`→`ridden her horse`,
   `two year`→`two years`, `on two hours`→`for two hours`,
   `The tenants is in apartment`→`The tenants in the apartment`.
   Butir yang kesalahannya memang terletak pada tata bahasa **tidak** disentuh.

Sebaran kunci 78 "Benar" / 102 "Salah" — itu memang komposisi bukunya.

### Selesai ✅ — Tahap 19: TOEFL PBT 17 practice test

`data/bank-14-pbt-a.js` (**396 soal**, Practice Test 30–37) dan
`data/bank-15-pbt-b.js` (**321 soal**, Practice Test 38–46), total **717 soal
reading dengan 85 bacaan**. Pembacanya `_skrip/pbt_parse.py`, pembangunnya
`_skrip/build_bank14.py`.

**Dua format berbeda dalam satu PDF** — ini yang wajib diketahui sebelum
menyentuh berkas ini lagi:

* Test 30–37 dan 40–42 memakai penanda `Questions 1-10` dengan **penomoran soal
  menyeluruh 1–50**, dan kunci di answer key berupa satu deret 50 huruf.
  Pemetaan kuncinya sederhana: `kunci[nomor-1]`. Soal yang gagal terbaca tidak
  menggeser apa pun.
* Test 38, 39, 43–46 memakai penanda `Passage 1` … `Passage 5` dengan
  **penomoran soal ulang dari 1 di tiap bacaan**. Kuncinya dikelompokkan dengan
  spasi persis mengikuti jumlah soal tiap bacaan. Jadi pengelompokan itu dipakai
  sebagai **verifikasi silang**: kalau jumlah soal per blok tidak sama persis
  dengan panjang tiap kelompok huruf, seluruh test dibuang. Ketujuh belas test
  cocok sempurna.

Sebaran kunci hasilnya merata (A/B/C/D ≈ 178/190/176/173) — itu tanda pemetaan
kuncinya benar. Pemeriksaan manual dilakukan pada 7 soal berurutan Test 30 dan
6 soal berurutan Test 46 (dua format yang berbeda), semuanya cocok.

**Pembersihan yang harus diulang kalau PDF ini diproses lagi:** ada cap air
Persia (`آموزشگاه زبان ایران آکسفورد`) dan alamat `http://zabanphd.ir` di tiap
halaman. Rentang Unicode-nya **tidak cukup `U+0600–U+06FF`** — harus mencakup
Arabic Presentation Forms `U+FB50–U+FDFF` dan `U+FE70–U+FEFF`, plus tanda arah
`U+200B–U+200F`, `U+202A–U+202E`, `U+2066–U+2069`. Kalau tidak, sisa cap airnya
menempel di opsi terakhir tiap halaman. Nomor halaman yang menempel di ujung
baris juga harus dibuang setelah cap airnya dihapus.

12 soal dibuang karena opsinya kemasukan teks bacaan atau rusak.

### Selesai ✅ — Tahap 20: TOEFL ITP Level 1 Vol.3 (ETS)

`data/bank-16-itp.js` — **270 soal** dari 2 practice test lengkap:
95 listening (bernaskah), 46 written expression, 30 structure, 99 reading.
Ekstraksi: `_skrip/itp_extract.py`, pembangun: `_skrip/build_bank16.py`,
pembahasan tulis tangan: `_skrip/itp_explain.py`.

Empat masalah teknis dan cara mengatasinya:

1. **Halaman soal berbentuk dua kolom** dan `pdftotext -layout` mencampur
   kiri-kanan dalam satu baris. Dipakai `pdfplumber`, lalu kolom dipisah dengan
   mencari **pita kosong vertikal** di tengah halaman. Yang bikin deteksi gagal
   bukan header, melainkan **baris pendek yang terpusat** di bawah halaman
   ("The questions for this passage continue on the next page.") — baris seperti
   itu harus dibuang dulu dari perhitungan pita, begitu juga baris selebar
   halaman yang tidak punya celah di tengah.
2. **Rumpang di Practice Test B digambar sebagai garis, bukan karakter garis
   bawah.** Di Test A rumpangnya benar-benar `_____`, di Test B tidak ada
   karakternya sama sekali sehingga soalnya tampak tanpa rumpang. Dipulihkan
   lewat `struct_lines()`: garis yang letaknya di dalam rentang tinggi sebuah
   baris teks tetapi rentang `x`-nya tidak ditempati kata mana pun = rumpang.
3. **Soal Written Expression** memakai deteksi garis bawah `page.lines`, sama
   seperti Peterson's. Satu jebakan baru: kalau dua garis bawah berdekatan,
   huruf penanda yang pertama bisa masuk ke jangkauan garis kedua. Penanda
   harus dipilih berdasarkan **jarak titik tengah**, bukan yang pertama ditemui.
   46 dari 50 butir berhasil; 4 sisanya (A29, A39, A40, B18) dibuang.
4. **Answer key tiga kolom.** Tiap baris memuat 6 pasangan (nomor, huruf) urut:
   S1 1-25, S1 26-50, S2 1-20, S2 21-40, S3 1-25, S3 26-50. Pada baris 21–25
   Section 2 sudah habis sehingga hanya ada 4 pasangan, yang berarti kolom
   0,1,4,5. Pemetaan **memakai urutan pasangan, bukan posisi karakter** —
   memakai posisi karakter sempat membuat seluruh kunci Section 1 dan 2
   tertukar. Selain itu blok kunci Test A harus dipotong sebelum blok Test B,
   kalau tidak Test B menimpa Test A tanpa jejak.

**Ke-76 soal Section 2 (Structure + Written Expression) diberi pembahasan
tulis tangan** di `_skrip/itp_explain.py`; sisanya memakai pembahasan otomatis
berkutipan. Kalau ada soal yang pembahasannya perlu diperbaiki, cukup tambah
atau ubah entri di berkas itu lalu jalankan ulang `build_bank16.py` — kunci
dict-nya adalah `id` soal.

### Selesai ✅ — Tahap 21: Magoosh & UNIPMA

`data/bank-17-magoosh.js` — **15 soal**: 13 soal reading iBT berpembahasan
(disarikan ke bahasa Indonesia dari penjelasan resmi Magoosh) atas satu bacaan
"History of the Chickenpox Vaccine", plus 1 prompt speaking dan 1 prompt writing
bertipe `open`. Soal ke-14 bertipe tabel dua kelompok — dilewati. Bagian
listening-nya dilewati karena audionya berupa tautan luar dan naskahnya tidak
disertakan.

Catatan ekstraksi: PDF Magoosh memenggal baris di **setiap** kata bercetak tebal
atau miring, sehingga batas paragraf tidak bisa dikenali dari baris kosong.
Seluruh teks disambung jadi satu aliran lalu dipenggal di kalimat pembuka tiap
paragraf yang sudah diketahui (daftar `PARA` di `_skrip/build_bank17.py`).

`data/bank-18-unipma.js` — **39 soal** Section 2 dari "Soal Pelatihan TOEFL
Mahasiswa" (P2B UNIPMA), yang isinya Diagnostic Pre-Test (Paper) Longman.
PDF-nya pindaian, jadi dipakai OCR 300 dpi (`_skrip/unipma_ocr.py`) untuk
menemukan letak tiap huruf penanda A–D relatif terhadap kata di atasnya; naskah
soalnya lalu ditulis ulang tangan di `_skrip/build_bank18.py` beserta kunci dan
pembahasannya.

**PDF ini tidak punya lembar kunci sama sekali.** Karena itu:
* Section 1 (listening, 50 soal) dilewati — tanpa audio dan tanpa naskah.
* Section 3 (reading, 50 soal) **dilewati** — tanpa kunci, terlalu banyak untuk
  ditetapkan sendiri dengan aman. Bacaannya masih utuh di PDF kalau suatu saat
  kuncinya ditemukan; ini pekerjaan yang paling jelas tersisa.
* Soal 40 dibuang karena kalimatnya tidak memuat kesalahan yang bisa dipastikan.

### Selesai ✅ — Tahap 23: pemeriksaan mutu

1. `node validate.js` — **0 masalah**. Validator ini **diperluas**: sekarang ia
   juga memuat berkas `lessons-*.js` (butuh `global.window={}` di barisan awal —
   sebelumnya validator langsung mati begitu ada berkas materi) dan memeriksa
   materi: id pelajaran ganda, metadata kurang, bagian tanpa isi/judul, dan
   contoh soal yang kunci atau opsinya cacat.
2. `node qcheck.js` — juga diberi `global.window={}` supaya tidak mati.
   Bank tata bahasa dasar 0 set timpang. Bank PBT dan ITP punya beberapa set timpang,
   tetapi itu opsi asli bukunya — tidak diubah, sama seperti kebijakan bank lama.
3. **`node qaudit.js` (baru)** — memeriksa dua hal sekaligus di seluruh bank:
   * setiap kutipan pendukung di pembahasan harus benar-benar ada di dalam
     bacaan/naskah yang dirujuk soal → **893 kutipan diperiksa, 0 tidak cocok**;
   * huruf yang disebut di pembahasan harus sama dengan kunci soal → menangkap
     1 kesalahan (`itpa-we-33`, pembahasan menulis C padahal kuncinya B), sudah
     diperbaiki. **Jalankan pemeriksa ini setiap kali menambah bank.**
4. Uji jalan di browser (Playwright): 2.332 soal termuat, 264 bacaan, 39 materi,
   urutan unit benar, tabel materi tampil bergaris dan bisa digeser mendatar,
   halaman tidak meluber ke samping, **0 error konsol**.

### Yang tersisa sesudah sesi ini

* **UNIPMA Section 3 (50 soal reading)** — naskah dan bacaannya sudah ada di PDF,
  yang tidak ada hanya kuncinya.
* **Magoosh listening** (11 soal) dan **speaking task terpadu** — audionya berupa
  tautan luar.
* **C-Media Listening 50 soal** — tidak ada audio/transkrip (dari sesi lama).
* **Best of The Best: 92 "Contoh Soal" + 4 Practice Test** — OCR terlalu rusak.
* **Barron's AC3 20–23 dan GT2 8–14** (11 soal) — daftar pilihannya hilang di OCR.
* **ITP Written Expression A29, A39, A40, B18** — garis bawah/penanda tidak
  terbaca.
* Pembahasan otomatis pada bank PBT dan ITP reading/listening sudah berkutipan
  dan sudah diverifikasi, tetapi masih memakai kalimat pembuka seragam per jenis
  soal. Kalau mau diperkaya, tulis tangan lewat pola `HAND` seperti
  `_skrip/itp_explain.py`.

### Berkas baru di sesi ini

`qaudit.js` · `data/bank-13-swe-dasar.js` … `data/bank-18-unipma.js` ·
`data/lessons-03-tatabahasa.js` ·
`_skrip/build_bank13.py` · `_skrip/pbt_parse.py` · `_skrip/build_bank14.py` ·
`_skrip/itp_extract.py` · `_skrip/build_bank16.py` · `_skrip/itp_explain.py` ·
`_skrip/build_bank17.py` · `_skrip/unipma_ocr.py` · `_skrip/build_bank18.py`

---

## TITIK LANJUT (9 Sep 2026, sesi ke-4 lanjutan) — perapian materi

Tiga permintaan lanjutan dari pemilik proyek, semuanya sudah dikerjakan.

### 1. Penyebutan penerbit modul dihapus

Unit **"Tata Bahasa Dasar (POLMANBABEL)"** menjadi **"Tata Bahasa Dasar"**.
Sumber banknya berganti nama jadi *"Structure & Written Expression — Sari Mubaroh
(2021)"*, dan `source.id` berganti dari `polman-swe` jadi `swe-dasar`.
Berkasnya ikut diganti nama:

* `data/lessons-03-polman.js` → `data/lessons-03-tatabahasa.js`
* `data/bank-13-polman.js` → `data/bank-13-swe-dasar.js`

Keduanya sudah disesuaikan di `index.html` dan di `_skrip/build_bank13.py`.
**`id` tiap pelajaran tetap berawalan `pb-`** — sengaja tidak diubah supaya
progres belajar yang tersimpan di `localStorage` pengguna tidak hilang. Awalan
itu tidak pernah tampil di layar.

### 2. Unit "Pengenalan Tes & Strategi" dihapus

`data/lessons-04-orientasi.js` dihapus beserta ketiga topiknya (jenis TOEFL,
cara skor ITP dihitung, strategi waktu) dan tag `<script>`-nya di `index.html`.
Materi tinggal **36 topik dalam 7 unit**.

### 3. Setiap topik dipastikan punya contoh soal

Pemeriksaannya: hitung `steps` yang punya kunci `ex` di tiap pelajaran, lalu
hitung berapa soal di bank yang cocok dengan `themes` + `match` pelajaran itu.

Hasil awal: 8 pelajaran di `data/lessons-02-reading.js` baru punya **satu**
contoh soal (main-idea, detail-matching, tfng, inference, melengkapi,
vocab-context, listening, writing-speaking). Ketiga topik orientasi punya **nol**
— tetapi ketiganya memang dihapus.

Untuk kedelapan pelajaran itu ditambahkan **satu contoh soal kedua**, dipilih
dengan cara berikut supaya tidak asal tambah:

1. Semua soal di bank yang cocok dengan topik itu didaftar dulu, lalu
   **dikelompokkan per sub-tema**.
2. Contoh baru dibuat untuk **sub-tema yang belum terwakili contoh pertama**,
   dan isinya diambil dari materi bank yang sungguh ada:

| Pelajaran | Contoh pertama | Contoh kedua yang ditambahkan | Sub-tema di bank |
|---|---|---|---|
| Main Idea | gagasan utama paragraf | apa yang mendahului bacaan (*Overview Items*) | 24 soal |
| Detail & Matching | detail dalam satu kalimat | mencocokkan informasi ke bagian bacaan | 77 soal |
| True/False/Not Given | kasus **False** | kasus **Not Given** | 124 soal |
| Inference & Purpose | penarikan simpulan | soal **rujukan** (*the word "ones" refers to*) | 97 soal |
| Melengkapi | jawaban singkat dari teks | ringkasan dengan kotak pilihan A–D | 37 soal |
| Vocabulary in Context | kalimat buatan | butir asli bank Magoosh (*tolerable*) | 245 soal |
| Listening | detail tanggal | butir asli naskah ITP (*What does the woman imply?*) | 95 soal |
| Writing & Speaking | kalimat pembuka esai | menyusun kalimat (*Build a Sentence*) | 10 soal |

Hasil akhir: **36 dari 36 topik punya minimal 2 contoh soal**, dan tiap topik
punya **minimal 10 soal latihan** yang cocok di bank.

Skrip pemeriksanya bisa dijalankan ulang kapan saja:

```
node -e "global.window={};global.TOEFLDRILL={questions:[],passages:{},sources:{},addBank:function(b){var s=b.source||{};if(s.id)this.sources[s.id]=s;if(b.passages)for(var k in b.passages)this.passages[k]=b.passages[k];(b.questions||[]).forEach(q=>{q.sourceId=q.sourceId||s.id;this.questions.push(q)})}};const fs=require('fs');fs.readdirSync('data').filter(f=>f.endsWith('.js')).sort().forEach(f=>eval(fs.readFileSync('data/'+f,'utf8')));const L=window.TOEFLDRILL_LESSONS,Q=TOEFLDRILL.questions;L.forEach(l=>{const ex=(l.steps||[]).filter(s=>s.ex).length;const m=(l.match||[]).map(s=>s.toLowerCase());const n=Q.filter(q=>(l.themes||[]).indexOf(q.theme)>=0&&(!m.length||m.some(x=>String(q.subtheme||'').toLowerCase().indexOf(x)>=0))).length;console.log((ex>=2?'ok':'!!'),'ex='+ex,'soal='+n,'|',l.unit,'|',l.title)});"
```

**Aturan untuk pelajaran baru:** minimal 2 contoh soal per topik, dan `match`
harus benar-benar menangkap soal di bank — kalau hasilnya 0, `match`-nya salah,
bukan banknya yang kurang.

### Catatan teknis: menghapus berkas di folder pengguna

`device_bash` tidak boleh menghapus berkas secara bawaan (`rm` gagal dengan
*Operation not permitted*). Izin hapus harus diminta lebih dulu; sesudah
disetujui, `rm` dan `mv` berjalan normal untuk sisa sesi. Mengganti nama berkas
(`mv`) ternyata **tidak** butuh izin itu.

### Pemeriksaan ulang sesudah perubahan

`node validate.js`, `node qcheck.js`, dan `node qaudit.js` semuanya bersih.
Uji browser: 2.332 soal, 36 pelajaran, minimum 2 contoh soal per pelajaran,
urutan unit benar, tidak ada lagi penyebutan penerbit modul di mana pun,
**0 error konsol**.

---

## TITIK LANJUT (9 Sep 2026) — latihan soal per topik ditarik dari SELURUH bank

**Masalahnya.** Pemilik proyek menunjuk hal yang benar: yang dimaksud "latihan
soal" pada sebuah topik materi bukan dua contoh soal setelah penjelasan,
melainkan **kolam soal yang banyak dan setopik**. Sebelum perbaikan ini, tombol
latihan di tiap pelajaran hanya menarik soal lewat pencocokan `l.match` terhadap
**sub-tema**, padahal sub-tema di 18 bank sama sekali tidak seragam:

* Bank baru memberi label spesifik (`Agreement: Prepositional Phrase`).
* Bank lain memberi label umum yang tidak menyebut topiknya sama sekali —
  `ITP Structure` (30), `ITP Written Expression` (46), `Preview Test: Structure`
  (21), `Review Test H: Reading` (25), `Multiple Choice` (245), dan seterusnya.

Akibatnya banyak topik cuma menarik 10 soal (persis soal dari latihan modulnya
sendiri), dan **110 soal tidak masuk topik mana pun**.

### Yang dikerjakan

**1. `data/topics.js` — indeks topik lintas bank.** Dibuat oleh
`node _skrip/build_topics.js`. Isinya `{ id pelajaran: [id soal, ...] }`, yaitu
soal setopik yang **tidak** tertangkap `l.match` sehingga perlu ditambahkan.

Cara menggolongkannya berbeda untuk dua jenis soal:

* **Soal bacaan** digolongkan dari **batang soalnya** — pola yang sudah dipakai
  `_skrip/build_bank14.py` dipakai ulang di sini: *closest in meaning* →
  Vocabulary, *refers to* → Inference & Reference, *main idea / best title /
  paragraph precede* → Main Idea, *True/False/Not Given* → TFNG,
  *complete the summary* → Melengkapi, sisanya → Detail & Matching.
* **Soal tata bahasa** digolongkan dari **pembahasannya**, bukan dari batang
  soalnya. Ini keputusan penting: pembahasan seluruh bank berbahasa Indonesia
  dan hampir selalu menyebut kaidah yang diuji ("Sesudah <em>has</em> harus past
  participle", "Rangkaian paralelnya tiga kata benda"), sedangkan batang soalnya
  penuh kata yang menyesatkan. Percobaan pertama sempat ikut membaca batang soal
  dan langsung salah: kalimat yang kebetulan memuat *a number of* atau *little*
  masuk ke topik countable/uncountable padahal soalnya tentang artikel atau kata
  ganti. Setelah dibatasi ke pembahasan + sub-tema saja, contoh acaknya bersih.

**2. `index.html` memakai indeks itu sebagai tambahan, bukan pengganti.**
`lessonQuestions()` sekarang meloloskan soal bila **id-nya ada di indeks
topik** ATAU sub-temanya cocok seperti dulu. Berkasnya dimuat lewat satu baris
`<script src="data/topics.js">` sesudah berkas `lessons-*.js`.

**3. Empat pelajaran payung diperluas jadi seluruh temanya** (`match:[]`):
Menemukan Bagian yang Salah → 402 soal, Vocabulary in Context → 273,
Strategi Listening → 147, Menulis & Berbicara → 19.

**4. Tombol latihan tidak lagi mentok di 25 soal.** Sekarang ada tombol ketiga
**"Latihan semua N soal"** begitu kolamnya lebih dari 25. Sudah diuji dengan
sesi 705 soal — termuat, bisa dinavigasi, 0 error konsol.

### Hasilnya

| | Sebelum | Sesudah |
|---|---|---|
| Soal yang tidak masuk topik mana pun | 110 | **0** |
| Kolam latihan terkecil | 10 | **11** |
| Kolam latihan median | 20 | **51** |
| Kolam latihan terbesar | 479 | **705** |

Contoh pertumbuhannya: *Kesesuaian Subjek–Kata Kerja* 11 → 48,
*Bentuk Kata* 30 → 57, *Adjective Clause Connector* 27 → 51,
*Countable vs Uncountable* 18 → 49, *Menemukan Bagian yang Salah* 117 → 402,
*Detail, Scanning & Matching* 479 → 705.

Tujuh topik masih di bawah 20 soal (possessive pronoun, agreement kuantitas,
paired conjunction, past participle setelah have, base form setelah modal,
agreement certain words, writing & speaking). Itu bukan cacat indeks —
kaidahnya memang jarang diuji, dan bank ini belum punya lebih banyak.

### Aturan untuk sesi berikutnya

* **Setiap kali menambah bank, jalankan ulang `node _skrip/build_topics.js`.**
  Kalau tidak, soal barunya hanya akan terhubung ke topik lewat sub-tema.
* `node validate.js` sekarang ikut memeriksa indeksnya: id pelajaran dan id soal
  harus ada, tidak boleh ganda, tema soal harus cocok dengan pelajarannya, dan
  **tiap pelajaran wajib punya kolam ≥ 10 soal**.
* Kalau sebuah topik baru kolamnya 0 atau sangat kecil, yang salah hampir selalu
  `l.match` atau pola di `_skrip/build_topics.js`, bukan banknya.
