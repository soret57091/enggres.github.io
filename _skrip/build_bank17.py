# -*- coding: utf-8 -*-
"""
Bank 17 — Magoosh "Free TOEFL Practice Questions" (format TOEFL iBT).
Reading: 1 bacaan + 13 soal pilihan ganda (soal ke-14 bertipe tabel, dilewati).
Speaking & Writing: prompt terbuka.
Bagian Listening tidak dipakai karena audionya berupa tautan luar dan
naskahnya tidak disertakan di PDF — sama seperti listening C-Media.

Pembahasan disarikan dalam bahasa Indonesia dari penjelasan resmi Magoosh.
Jalankan: python3 _skrip/build_bank17.py
"""
import re, io, os, json, subprocess

PDF = os.path.expanduser("~/mnt/TOEFL IELTS/referensi 2/TOEFL_Practice_Questions.pdf")
TXT = "/tmp/magoosh.txt"

def raw():
    if not os.path.exists(TXT):
        subprocess.run(["pdftotext", PDF, TXT], check=False)
    t = io.open(TXT, encoding="utf-8", errors="replace").read()
    t = re.sub(r"[​‎‏­]", "", t)
    t = re.sub(r"\n?toefl\.magoosh\.com\s+\d+\n?", "\n", t)
    return t

PARA = ["Chickenpox is a highly contagious",
        "A vaccine against chickenpox was originally invented",
        "Strong belief in that view eroded",
        "Another reason that the chickenpox vaccine",
        "Today, use of the chickenpox vaccine is common"]

def passage():
    """PDF-nya memenggal baris di setiap kata bercetak tebal/miring, sehingga
    batas paragraf tidak bisa dikenali dari baris kosong. Seluruh teks
    disambung dulu jadi satu aliran, lalu dipenggal di pembuka paragraf
    yang sudah diketahui."""
    t = raw()
    i = t.index("History of the Chickenpox Vaccine")
    j = t.index("1. The word")
    flow = re.sub(r"\s+", " ", t[i:j].replace("History of the Chickenpox Vaccine", "", 1)).strip()
    pos = []
    for m in PARA:
        k = flow.index(m)
        pos.append(k)
    pos.append(len(flow))
    paras = [flow[pos[k]:pos[k + 1]].strip() for k in range(len(PARA))]
    txt = "\n\n".join(paras).replace("\u25a0", "\u25aa")
    txt = re.sub(r"\s+([,.;:!?])", r"\1", txt)
    txt = re.sub(r"([\u201c\u2018]) ", r"\1", txt)
    txt = re.sub(r" ([\u201d\u2019])", r"\1", txt)
    return txt

E = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
PID = "MG-chickenpox"

Q = [
 (1, "vocabulary", "Vocabulary in Context",
  'The word <b>tolerable</b> in the passage is closest in meaning to',
  ["sudden", "bearable", "infrequent", "unexpected"], 1,
  "<em>tolerable</em> berasal dari verb <em>to tolerate</em> — menahan sesuatu yang tidak enak tanpa berusaha menghentikannya. Padanan terdekatnya <b>B. bearable</b>, dari <em>to bear</em> yang artinya sama. Konteksnya juga menegaskan: <em>a high but tolerable level of discomfort</em> — kata sambung <em>but</em> menuntut lawan dari 'sangat parah'. <em>sudden</em> dan <em>unexpected</em> sama-sama bermakna negatif sehingga tidak menimbulkan kontras; <em>infrequent</em> memang terdengar melegakan tetapi maknanya 'jarang', bukan 'masih tertahankan'."),
 (2, "reading", "Detail",
  'According to paragraph 1, which of the following is true of the chickenpox virus?',
  ["It leads to a potentially deadly disease in adults.",
   "It is associated with a possibly permanent rash.",
   "It is easily transmittable by an infected individual.",
   "It has been virtually eradicated in the modern world."], 2,
  "Kalimat pertama menyebut cacar air <em>highly contagious</em> — mudah menular dari satu orang ke orang lain. Jawabannya <b>C</b>. A menggoda karena herpes zoster memang penyakit serius pada orang dewasa, tetapi itu dibahas di paragraf lain dan bacaannya tidak pernah menyebutnya mematikan. B bertentangan dengan <em>the disease can last for up to 14 days</em>. D memang disinggung, tapi di paragraf terakhir, bukan paragraf 1."),
 (3, "reading", "Paraphrase",
  'Which of the following best expresses the essential information in this sentence: <em>“The ailment was once considered to be a ‘rite of passage’ by parents in the U.S. and thought to provide children with greater and improved immunity to other forms of sickness later in life.”</em>',
  ["U.S. parents believed that having chickenpox benefited their children.",
   "U.S. parents believed that chickenpox led to immunity against most sickness.",
   "U.S. parents wanted to make sure that their children developed chickenpox.",
   "U.S. parents did not think that other vaccinations were needed after chickenpox."], 0,
  "Inti kalimatnya: orang tua di AS dulu menganggap cacar air justru <em>menguntungkan</em> anak. <b>A</b> merangkum itu tanpa menambah atau mengurangi. B melebih-lebihkan menjadi 'kebal terhadap hampir semua penyakit'; C menambahkan niat yang tidak ada di kalimat aslinya; D bicara soal vaksin lain yang sama sekali tidak disinggung."),
 (4, "reading", "Inference",
  'Which of the following can be inferred from paragraph 2 about the clinical trials for the chickenpox vaccine?',
  ["They took longer than expected.", "They cost a lot of money to complete.",
   "They took a long time to finish.", "They were ultimately successful."], 3,
  "Paragraf 2 menyebut uji klinis dimulai 1972 dan program vaksinasi massal berjalan di Jepang pada 1974 — artinya uji itu <b>berhasil</b>. Jawabannya <b>D</b>. A dan C menggoda karena ada angka '20 tahun', tetapi angka itu menyangkut lamanya persetujuan FDA di AS, bukan lamanya uji klinis. B tidak pernah disinggung."),
 (5, "vocabulary", "Vocabulary in Context",
  'The word <b>notion</b> in the passage is closest in meaning to',
  ["history", "findings", "fact", "belief"], 3,
  "<em>notion</em> berarti gagasan atau anggapan — <b>D. belief</b>. Konteksnya: orang tua <em>cited the notion that chickenpox did not constitute a serious enough disease</em>, yaitu sebuah pendapat, bukan kenyataan. Karena itu <em>fact</em> dan <em>findings</em> justru bertentangan dengan maksud paragrafnya, yang menjelaskan bahwa anggapan itu kemudian runtuh."),
 (6, "reading", "Detail",
  'According to paragraph 3, which of the following is true of <em>Varicella zoster</em>?',
  ["It typically attacks adults who are over 60 years old.",
   "It is linked to a serious disease that occurs more commonly in adults.",
   "It likely is not a serious enough threat to human health to require a vaccine.",
   "It is completely eradicated from the body after chickenpox occurs."], 1,
  "Paragraf 3 menerangkan kaitan <em>Varicella zoster</em> dengan herpes zoster (shingles), penyakit yang lebih berat dan menyerang orang dewasa. Jawabannya <b>B</b>. A salah karena bacaannya justru menyoroti risiko pada usia 30–40 tahun; C adalah anggapan lama yang dibantah paragraf ini; D bertentangan langsung dengan <em>remains dormant inside the body</em>."),
 (7, "reading", "Negative Fact",
  'According to paragraph 3, all of the following are true about the chickenpox virus EXCEPT:',
  ["It causes two distinct yet related ailments.",
   "People did not view it as a serious public health threat.",
   "It tended to quickly become dormant and remain inoperative over time.",
   "Vaccination against it would help prevent the onset of shingles."], 2,
  "Soal EXCEPT: tiga pilihan didukung paragraf 3, satu tidak. Bacaan memang menyebut virus itu <em>remains dormant</em>, tetapi tidak pernah mengatakan virusnya cepat tidur dan <b>tetap tidak aktif</b> — justru sebaliknya, virus itu bisa bangkit lagi menjadi shingles. Jadi jawabannya <b>C</b>."),
 (8, "reading", "Purpose",
  'The author uses <b>booster shots</b> as an example of',
  ["a scientifically approved medicine to eliminate chickenpox",
   "a preferred method of chickenpox rash and fever treatment",
   "a way to increase the effectiveness of the chickenpox vaccine",
   "a strategy for parents to avoid vaccinating their child altogether"], 2,
  "Kalimatnya berbunyi <em>booster shots of the vaccine elongated immunity and countered the perceived limits on the strength of the vaccine</em> — jadi suntikan penguat disebut sebagai cara <b>memperkuat</b> vaksinnya. Jawabannya <b>C</b>. Booster bukan obat untuk memusnahkan penyakit (A), bukan pengobatan ruam dan demam (B), dan justru bagian dari vaksinasi, bukan cara menghindarinya (D)."),
 (9, "vocabulary", "Vocabulary in Context",
  'The word <b>countered</b> in the passage is closest in meaning to',
  ["affirmed", "refuted", "supported", "defied"], 1,
  "<em>to counter</em> berarti membantah atau mematahkan — <b>B. refuted</b>. Yang dibantah di sini adalah anggapan bahwa vaksinnya lemah. <em>affirmed</em> dan <em>supported</em> justru berlawanan arti. <em>defied</em> berarti menantang atau melanggar, biasanya terhadap aturan atau orang, bukan terhadap sebuah anggapan."),
 (10, "reading", "Detail",
  'According to paragraph 4, many parents did not choose the chickenpox vaccine because',
  ["they believed that the virus was weak and not especially harmful",
   "they thought that scientists did not have enough data to reach a conclusion",
   "they were unsure about the utility of the vaccine given its expected duration",
   "they were convinced it was potentially very toxic, particularly for older children"], 2,
  "Paragraf 4 menyebut alasannya: vaksin itu dianggap <em>did not last long enough and did not confer a lifetime of immunity</em> — jadi keraguannya soal <b>daya tahan</b> kekebalannya. Jawabannya <b>C</b>. A adalah alasan yang dibahas di paragraf 2, bukan 4; B dan D tidak disebut sama sekali."),
 (11, "reading", "Detail",
  'According to paragraph 5, which of the following was true of the rates of chickenpox before the chickenpox vaccine became widely used?',
  ["It was 10 times higher.", "It was consistently rising.",
   "It declined over time.", "It fluctuated over several decades."], 0,
  "Paragraf terakhir menyebut angka 400.000 kasus per tahun sekarang, dari lebih 4.000.000 kasus sebelum vaksinasi meluas — sepuluh kali lipat. Jawabannya <b>A</b>. Bacaannya hanya memberi dua angka pembanding; ia tidak pernah berbicara tentang tren naik (B), turun bertahap (C), atau naik-turun (D) sebelum vaksinasi."),
 (12, "vocabulary", "Vocabulary in Context",
  'The word <b>prevalent</b> in the passage is closest in meaning to',
  ["dangerous", "widespread", "infectious", "contaminated"], 1,
  "<em>prevalent</em> berarti tersebar luas — <b>B. widespread</b>. Konteksnya: pada orang dewasa muda ruamnya <em>more painful and prevalent</em>, yaitu lebih sakit dan lebih menyebar di tubuh. <em>dangerous</em> dan <em>infectious</em> memang berkaitan dengan penyakit, tetapi bukan arti kata ini."),
 (13, "reading", "Sisipan Kalimat",
  'Look at the four squares [▪] that indicate where the following sentence could be added to the passage: <em>“Meanwhile, some continue to remain unconvinced, citing a supposed potential of the vaccine to do harm.”</em> Where would the sentence fit best?',
  ["Kotak A", "Kotak B", "Kotak C", "Kotak D"], 1,
  "Kalimat sisipan memuat dua petunjuk. Pertama, <em>Meanwhile</em> menandakan pergantian sudut pandang. Kedua, <em>some continue to remain unconvinced</em> harus muncul <b>sesudah</b> pandangan mayoritas dokter dan <b>sebelum</b> kalimat <em>Of course, many parents continue to think of the disease as an innocuous ailment</em> yang meneruskan gagasan tentang orang tua yang menolak. Posisi yang memenuhi keduanya adalah <b>kotak B</b>."),
]

OPEN = [
 ("mg-sp-1", "speaking", "Independent Speaking (Task 1)",
  "Describe a teacher who was important to you and why he or she was important. Be sure to include specific examples in your response.",
  "Waktu persiapan 15 detik, waktu bicara 45 detik. Rangka jawaban yang aman: (1) sebut siapa gurunya dan mata pelajarannya dalam satu kalimat; (2) berikan <b>dua</b> alasan mengapa ia penting; (3) untuk salah satu alasan, ceritakan satu peristiwa nyata yang singkat dan konkret — penguji menilai pengembangan gagasan, dan satu contoh nyata jauh lebih bernilai daripada tiga alasan umum; (4) tutup dengan satu kalimat tentang pengaruhnya sampai sekarang. Jangan menghabiskan waktu pada pembukaan; mulailah menjawab di detik pertama."),
 ("mg-wr-1", "writing", "Independent Writing",
  "Some parents forbid young children from owning smartphones (cell phones with Internet access), while others disagree and believe that they are important tools for keeping in touch. Which point of view do you think is better, and why?",
  "30 menit, sasaran minimal 300 kata. Susunan yang dinilai baik: paragraf pembuka yang menyatakan pendirianmu dengan jelas (jangan menggantung di tengah); dua atau tiga paragraf isi, masing-masing satu alasan yang dibuka kalimat topik lalu didukung contoh nyata; satu paragraf yang mengakui sisi pandangan lawan lalu menjelaskan mengapa pendirianmu tetap lebih kuat; dan penutup singkat. Yang paling sering menurunkan nilai bukan tata bahasa, melainkan alasan yang diulang-ulang tanpa contoh. Sisakan tiga menit terakhir untuk memeriksa bentuk kata kerja, kata benda jamak, dan kata sambung antarparagraf."),
]

def build():
    qs = []
    for n, theme, sub, stem, opts, ans, ex in Q:
        qs.append({"id": "mg-rd-%d" % n, "theme": theme, "subtheme": sub,
                   "ref": "Reading Section no.%d" % n, "passageId": PID,
                   "question": stem, "options": [E(o) for o in opts],
                   "answer": ans, "explain": ex})
    for qid, theme, sub, prompt, guide in OPEN:
        qs.append({"id": qid, "theme": theme, "subtheme": sub, "type": "open",
                   "ref": "Magoosh — " + sub, "question": E(prompt), "explain": guide})
    bank = {"source": {"id": "magoosh", "name": "Magoosh — Free TOEFL Practice Questions", "test": "TOEFL iBT"},
            "passages": {PID: {"title": "History of the Chickenpox Vaccine", "text": passage()}},
            "questions": qs}
    out = "/* dibuat oleh _skrip/build_bank17.py — jangan diedit tangan */\nTOEFLDRILL.addBank(\n"
    out += json.dumps(bank, ensure_ascii=False, indent=1) + "\n);\n"
    io.open("data/bank-17-magoosh.js", "w", encoding="utf-8").write(out)
    d = {}
    for q in qs:
        if "answer" in q: d["ABCD"[q["answer"]]] = d.get("ABCD"[q["answer"]], 0) + 1
    print("bank-17-magoosh.js:", len(qs), "soal (terbuka %d)" % len(OPEN), "| sebaran", d)
    print("panjang bacaan:", len(passage()), "char, paragraf:", passage().count("\n\n") + 1)

if __name__ == "__main__":
    build()
