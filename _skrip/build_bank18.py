# -*- coding: utf-8 -*-
"""
Bank 18 — "Soal Pelatihan TOEFL Mahasiswa" (Test TOEFL-Like UNIPMA / P2B UNIPMA),
yaitu Diagnostic Pre-Test (Paper) Section 2: Structure & Written Expression.

PDF-nya berupa pindaian tanpa lembar kunci. Karena itu:
  * Section 1 (Listening) TIDAK dipakai — tidak ada audio maupun naskahnya.
  * Section 3 (Reading, 50 soal) TIDAK dipakai — tanpa kunci, terlalu banyak
    untuk ditetapkan sendiri dengan aman. Bacaannya tetap ada di PDF kalau
    suatu saat kuncinya ditemukan.
  * Section 2 dipakai: kuncinya ditetapkan ulang dari kaidah tata bahasanya,
    dan setiap pembahasan menyebutkan perbaikannya secara eksplisit sehingga
    kunci dan pembahasan saling memeriksa.
  * Soal 40 dibuang karena kalimatnya tidak memuat kesalahan tata bahasa yang
    bisa dipastikan — lebih baik hilang daripada salah.

Naskah soal dan letak garis bawahnya diambil dari OCR 300 dpi
(_skrip/unipma_ocr.py): tiap huruf penanda A-D dipasangkan dengan kata di
atasnya berdasarkan koordinat.

Jalankan: python3 _skrip/build_bank18.py
"""
import io, json

E = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------------- Structure 1-15 ----------------
ST = [
 (1, "The North Pole ______ a latitude of 90 degrees north.",
  ["it has", "is having", "which is having", "has"], 3,
  "Kalimat ini butuh satu verb utama saja. <b>D. has</b> menyediakannya. A menambah subjek kedua, C mengawali klausa adjektiva sehingga kalimat kehilangan predikat, dan B memakai bentuk continuous untuk verb kepemilikan yang tidak lazim."),
 (2, "The city of Beverly Hills is surrounded on ______ the city of Los Angeles.",
  ["its sides", "the sides are", "it is the side of", "all sides by"], 3,
  "Kalimatnya pasif, jadi pelakunya diperkenalkan dengan <em>by</em>: <b>D. all sides by</b> — <em>surrounded on all sides by the city of Los Angeles</em>. B dan C menambahkan verb kedua tanpa penghubung."),
 (3, "______ greyhound, can achieve speeds up to thirty-six miles per hour.",
  ["The", "The fastest", "The fastest dog", "The fastest dog, the"], 3,
  "Yang dibutuhkan subjek beserta aposisinya yang diapit koma: <b>D. The fastest dog, the</b> → <em>The fastest dog, the greyhound, can achieve…</em>. Pilihan lain meninggalkan koma penutup aposisi tanpa pasangan pembuka."),
 (4, "Marmots spend their time foraging among meadow plants and flowers or ______ on rocky cliffs.",
  ["gets sun", "sunning", "the sun", "sunny"], 1,
  "Setelah <em>or</em> harus sebentuk dengan <em>foraging</em>, yaitu gerund: <b>B. sunning</b>. A verb bertanda waktu, C kata benda, D kata sifat — ketiganya merusak paralelisme."),
 (5, "The greenhouse effect occurs ______ heat radiated from the Sun.",
  ["when does the Earth’s atmosphere trap", "does the Earth’s atmosphere trap",
   "when the Earth’s atmosphere traps", "the Earth’s atmosphere traps"], 2,
  "Dibutuhkan connector klausa keterangan diikuti klausa berurutan biasa: <b>C. when the Earth’s atmosphere traps</b>. A memakai pola tanya, B dan D tidak punya penghubung sehingga kalimat berisi dua verb tanpa connector."),
 (6, "The Rose Bowl, ______ place on New Year’s Day, is the oldest postseason collegiate football game in the United States.",
  ["takes", "it takes", "which takes", "took"], 2,
  "Bagian yang diapit dua koma adalah klausa adjektiva, jadi butuh connector: <b>C. which takes</b>. A dan D menjadikan kalimat punya dua verb utama; B menambah subjek kedua tanpa penghubung."),
 (7, "Experiments ______ represent a giant step into the medicine of the future.",
  ["using gene therapy", "use gene therapy", "they use", "gene therapy uses"], 0,
  "Verb utamanya sudah ada (<em>represent</em>), jadi yang boleh disisipkan hanyalah frasa penerang <em>Experiments</em>: <b>A. using gene therapy</b>. Tiga pilihan lain menambahkan verb bertanda waktu kedua."),
 (8, "______ off the Hawaiian coastline are living, others are dead.",
  ["While some types of coral reefs", "Some types of coral reefs",
   "There are many types of coral reefs", "Coral reefs"], 0,
  "Ada dua klausa (<em>… are living</em> dan <em>others are dead</em>) yang harus dihubungkan. <b>A. While some types of coral reefs</b> menjadikan yang pertama klausa keterangan sekaligus menyiapkan kontras dengan <em>others</em>."),
 (9, "Nimbostratus clouds are thick, dark gray clouds ______ forebode rain.",
  ["what", "which", "what they", "which they"], 1,
  "Yang dibutuhkan connector klausa adjektiva yang sekaligus menjadi subjeknya: <b>B. which</b>. <em>what</em> tidak dipakai untuk klausa adjektiva; C dan D menambah subjek kedua."),
 (10, "Some economists now suggest that home equity loans are merely a new trap to push consumers beyond ______.",
  ["they can afford", "they can afford it", "what is affordable", "able to afford"], 2,
  "Setelah preposisi <em>beyond</em> dibutuhkan objek berupa nomina atau noun clause: <b>C. what is affordable</b>. A dan B klausa tanpa connector; D bukan frasa nomina."),
 (11, "People who reverse the letters of words ______ to read suffer from dyslexia.",
  ["when trying", "if they tried", "when tried", "if he tries"], 0,
  "Kalimat ini sudah punya verb utama (<em>suffer</em>) dan verb klausa adjektiva (<em>reverse</em>), jadi yang boleh masuk hanya klausa keterangan tereduksi: <b>A. when trying</b>. B dan D menambah verb bertanda waktu; C memakai bentuk pasif yang maknanya keliru."),
 (12, "Featured at the Henry Ford Museum ______ of antique cars dating from 1865.",
  ["is an exhibit", "an exhibit", "an exhibit is", "which is an exhibit"], 0,
  "Frasa participle di depan kalimat memaksa inversi: verb dulu, baru subjeknya — <b>A. is an exhibit</b> (<em>Featured at the Henry Ford Museum is an exhibit of antique cars…</em>). B tidak punya verb, C memakai urutan biasa yang tidak cocok setelah pembuka terbalik, D mengawali klausa adjektiva tanpa induk."),
 (13, "Rubber ______ from vulcanized silicones with a high molecular weight is difficult to distinguish from natural rubber.",
  ["is produced", "producing", "that produces", "produced"], 3,
  "Verb utama kalimat adalah <em>is difficult</em>, jadi bagian ini hanya boleh berupa frasa participle pasif yang menerangkan <em>Rubber</em>: <b>D. produced</b>. A dan C menambah verb bertanda waktu kedua; B memberi makna aktif yang keliru."),
 (14, "______ appears considerably larger at the horizon than it does overhead is merely an optical illusion.",
  ["The Moon", "That the Moon", "When the Moon", "The Moon which"], 1,
  "Ada dua verb utama (<em>appears</em> dan <em>is</em>) sehingga dibutuhkan dua subjek: <b>B. That the Moon</b> — <em>the Moon</em> subjek dari <em>appears</em>, dan seluruh noun clause <em>That the Moon appears…</em> menjadi subjek dari <em>is</em>."),
 (15, "According to the World Health Organization, ______ any of the six most dangerous diseases to break out, it could be cause for quarantine.",
  ["were", "they were", "there were", "were they"], 0,
  "Ini kalimat pengandaian tanpa <em>if</em>, yang dibentuk dengan inversi: verb bantu di depan subjeknya — <b>A. were</b> (<em>Were any of the six most dangerous diseases to break out…</em>). B, C, dan D menyisipkan subjek tambahan padahal subjeknya sudah ada, yaitu <em>any of the six most dangerous diseases</em>."),
]

# ---------------- Written Expression 16-39 ----------------
# (kalimat, [(teks_bergaris_bawah, huruf)], indeks kunci, pembahasan)
WE = [
 (16, "On <u>the floor</u><sup>A</sup> of the Pacific Ocean <u>is</u><sup>B</sup> hundreds of <u>flat-topped</u><sup>C</sup> mountains <u>more than</u><sup>D</sup> a mile beneath sea level.",
  ["the floor", "is", "flat-topped", "more than"], 1,
  "Kalimatnya terbalik: keterangan tempat di depan, subjek di belakang verb. Subjek sebenarnya <em>hundreds of … mountains</em> (jamak), jadi <b>B. is</b> harus jadi <em>are</em>."),
 (17, "Because of the flourish <u>with which</u><sup>A</sup> John Hancock signed the Declaration of Independence, <u>his name</u><sup>B</sup> <u>become</u><sup>C</sup> <u>synonymous</u><sup>D</sup> with signature.",
  ["with which", "his name", "become", "synonymous"], 2,
  "Kalimatnya bercerita tentang masa lampau, jadi verb utamanya harus bentuk lampau. <b>C. become</b> seharusnya <em>became</em>."),
 (18, "Segregation in <u>public</u><sup>A</sup> schools <u>was declare</u><sup>B</sup> <u>unconstitutional</u><sup>C</sup> by the Supreme Court <u>in 1954</u><sup>D</sup>.",
  ["public", "was declare", "unconstitutional", "in 1954"], 1,
  "Setelah <em>was</em> harus past participle. <b>B. was declare</b> seharusnya <em>was declared</em>."),
 (19, "Sirius, the Dog Star, is <u>the most brightest</u><sup>A</sup> star in the sky, with <u>an absolute magnitude</u><sup>B</sup> about <u>twenty-three times</u><sup>C</sup> <u>that</u><sup>D</sup> of the Sun.",
  ["the most brightest", "an absolute magnitude", "twenty-three times", "that"], 0,
  "Superlatif tidak boleh ditandai dua kali. <b>A. the most brightest</b> seharusnya <em>the brightest</em>."),
 (20, "Killer whales <u>tend</u><sup>A</sup> to <u>wander</u><sup>B</sup> in family clusters that hunt, play, and <u>resting</u><sup>C</sup> <u>together</u><sup>D</sup>.",
  ["tend", "wander", "resting", "together"], 2,
  "Rangkaian paralelnya tiga verb: <em>hunt, play, and …</em>. <b>C. resting</b> seharusnya <em>rest</em>."),
 (21, "<u>Some of</u><sup>A</sup> the most <u>useful</u><sup>B</sup> resistor <u>material</u><sup>C</sup> are carbon, metals, and <u>metallic</u><sup>D</sup> alloys.",
  ["Some of", "useful", "material", "metallic"], 2,
  "Verb-nya jamak (<em>are</em>) dan pelengkapnya juga jamak, jadi subjeknya harus jamak. <b>C. material</b> seharusnya <em>materials</em>."),
 (22, "The <u>community</u><sup>A</sup> of Bethesda, Maryland, was <u>previous</u><sup>B</sup> <u>known</u><sup>C</sup> <u>as</u><sup>D</sup> Darcy’s Store.",
  ["community", "previous", "known", "as"], 1,
  "Yang diterangkan adalah <em>known</em>, sebuah participle yang berlaku sebagai kata sifat, jadi penerangnya harus adverb. <b>B. previous</b> seharusnya <em>previously</em>."),
 (23, "Alloys of gold and copper <u>have been</u><sup>A</sup> <u>widely</u><sup>B</sup> <u>using</u><sup>C</sup> in <u>various types</u><sup>D</sup> of coins.",
  ["have been", "widely", "using", "various types"], 2,
  "Kalimatnya pasif — paduan logam itu <em>dipakai</em>. Setelah <em>have been</em> harus past participle: <b>C. using</b> seharusnya <em>used</em>."),
 (24, "J.H. Pratt used <u>group therapy</u><sup>A</sup> <u>early</u><sup>B</sup> in this century <u>when</u><sup>C</sup> he brought tuberculosis patients together to discuss <u>its</u><sup>D</sup> disease.",
  ["group therapy", "early", "when", "its"], 3,
  "Penyakit yang dimaksud sudah jelas dari konteks dan bukan milik siapa pun. <b>D. its</b> seharusnya <em>the</em> (atau <em>their</em> kalau mengacu ke para pasien)."),
 (25, "The United States <u>has import</u><sup>A</sup> <u>all</u><sup>B</sup> carpet wools in recent years <u>because</u><sup>C</sup> domestic wools are <u>too fine</u><sup>D</sup> and soft for carpets.",
  ["has import", "all", "because", "too fine"], 0,
  "Setelah <em>has</em> harus past participle. <b>A. has import</b> seharusnya <em>has imported</em>."),
 (26, "Irving Berlin <u>wrote</u><sup>A</sup> “Oh How I Hate to Get Up in the Morning” <u>while serving</u><sup>B</sup> <u>in a</u><sup>C</sup> U.S. Army <u>during</u><sup>D</sup> World War I.",
  ["wrote", "while serving", "in a", "during"], 2,
  "Nama satuan tentara yang sudah tertentu memakai <em>the</em>. <b>C. in a</b> seharusnya <em>in the</em> U.S. Army."),
 (27, "Banks are <u>rushing</u><sup>A</sup> to merge because consolidations <u>enable them</u><sup>B</sup> to slash <u>theirs</u><sup>C</sup> costs and <u>expand</u><sup>D</sup>.",
  ["rushing", "enable them", "theirs", "expand"], 2,
  "Bentuk possessive yang diikuti kata benda adalah <em>their</em>, bukan <em>theirs</em>. <b>C. theirs</b> seharusnya <em>their</em> costs."),
 (28, "<u>That</u><sup>A</sup> water has a very high specific heat <u>means</u><sup>B</sup> that without a large temperature change water can add <u>or lose</u><sup>C</sup> a large <u>number</u><sup>D</sup> of heat.",
  ["That", "means", "or lose", "number"], 3,
  "<em>heat</em> tak terhitung, jadi kata kuncinya bukan <em>number</em>. <b>D. number</b> seharusnya <em>amount</em>."),
 (29, "Benny Goodman was <u>equally</u><sup>A</sup> talented as both a jazz <u>performer</u><sup>B</sup> <u>as well as</u><sup>C</sup> a <u>classical musician</u><sup>D</sup>.",
  ["equally", "performer", "as well as", "classical musician"], 2,
  "Pasangan konjungsi <em>both</em> hanya boleh dipasangkan dengan <em>and</em>. <b>C. as well as</b> seharusnya <em>and</em>."),
 (30, "The state seal <u>still used</u><sup>A</sup> in Massachusetts <u>designed</u><sup>B</sup> by Paul Revere, <u>who</u><sup>C</sup> also designed <u>the first</u><sup>D</sup> Continental currency.",
  ["still used", "designed", "who", "the first"], 1,
  "Kalimat ini kehilangan verb utama yang bertanda waktu, dan maknanya pasif. <b>B. designed</b> seharusnya <em>was designed</em>."),
 (31, "Quarter horses were developed in eighteenth-century Virginia <u>to race</u><sup>A</sup> on <u>courses short</u><sup>B</sup> of about a quarter of <u>a mile</u><sup>C</sup> in <u>length</u><sup>D</sup>.",
  ["to race", "courses short", "a mile", "length"], 1,
  "Dalam bahasa Inggris kata sifat mendahului kata benda. <b>B. courses short</b> seharusnya <em>short courses</em>."),
 (32, "<u>No longer</u><sup>A</sup> <u>satisfied</u><sup>B</sup> with the <u>emphasis</u><sup>C</sup> of the Denishawn School, Martha Graham has <u>moved</u><sup>D</sup> to the staff of the Eastman School in 1925.",
  ["No longer", "satisfied", "emphasis", "moved"], 3,
  "Keterangan waktu lampau yang tertentu (<em>in 1925</em>) tidak boleh dipakai dengan present perfect. <b>D. has moved</b> seharusnya <em>moved</em>."),
 (33, "William Hart was <u>an act</u><sup>A</sup> best <u>known</u><sup>B</sup> for <u>his</u><sup>C</sup> roles <u>as</u><sup>D</sup> western heroes in silent films.",
  ["an act", "known", "his", "as"], 0,
  "Yang dimaksud adalah pelakunya, bukan perbuatannya. <b>A. an act</b> seharusnya <em>an actor</em>."),
 (34, "<u>Prior to</u><sup>A</sup> an extermination program <u>earlier</u><sup>B</sup> this century, <u>alive</u><sup>C</sup> wolves roamed <u>across nearly</u><sup>D</sup> all of North America.",
  ["Prior to", "earlier", "alive", "across nearly"], 2,
  "<em>alive</em> hanya dipakai sesudah verb (<em>the wolves are alive</em>), tidak boleh mendahului kata benda. <b>C. alive</b> seharusnya <em>live</em> wolves."),
 (35, "<u>During</u><sup>A</sup> the 1960s the Berkeley campus of the University of California <u>came</u><sup>B</sup> to national attention as a <u>result</u><sup>C</sup> its radical <u>political</u><sup>D</sup> activity.",
  ["During", "came", "result", "political"], 2,
  "Ungkapannya <em>as a result <b>of</b></em>. <b>C. result</b> kehilangan preposisi <em>of</em>."),
 (36, "<u>Artist</u><sup>A</sup> Gutzon Borglum designed the Mount Rushmore Memorial and worked on <u>project</u><sup>B</sup> from 1925 <u>until</u><sup>C</sup> <u>his</u><sup>D</sup> death in 1941.",
  ["Artist", "project", "until", "his"], 1,
  "Kata benda tunggal yang bisa dihitung dan sudah tertentu menuntut penentu. <b>B. project</b> seharusnya <em>the project</em>."),
 (37, "It is proving less <u>costly</u><sup>A</sup> and more <u>profitably</u><sup>B</sup> for drugmakers to <u>market</u><sup>C</sup> <u>directly</u><sup>D</sup> to patients.",
  ["costly", "profitably", "market", "directly"], 1,
  "Rangkaian paralelnya dua kata sifat setelah <em>is proving</em>: <em>less costly and more …</em>. <b>B. profitably</b> adverb; seharusnya <em>profitable</em>."),
 (38, "Sapphires <u>weighing</u><sup>A</sup> <u>as</u><sup>B</sup> much as two <u>pounds</u><sup>C</sup> have on occasion <u>mined</u><sup>D</sup>.",
  ["weighing", "as", "pounds", "mined"], 3,
  "Batu safirnya <em>ditambang</em>, jadi kalimatnya pasif dan <em>been</em> tidak boleh hilang. <b>D. mined</b> seharusnya <em>been mined</em>."),
 (39, "<u>Like snakes</u><sup>A</sup>, lizards can be <u>found</u><sup>B</sup> on all <u>others</u><sup>C</sup> continents <u>except</u><sup>D</sup> Antarctica.",
  ["Like snakes", "found", "others", "except"], 2,
  "<em>others</em> berdiri sendiri sebagai kata ganti dan tidak boleh diikuti kata benda. <b>C. others</b> seharusnya <em>other</em> continents."),
]

def build():
    qs = []
    for n, stem, opts, ans, ex in ST:
        qs.append({"id": "up-st-%d" % n, "theme": "structure", "subtheme": "Diagnostic Pre-Test: Structure",
                   "ref": "Section 2 no.%d" % n,
                   "instruction": "Pilih kata atau frasa yang paling tepat melengkapi kalimat.",
                   "question": E(stem), "options": [E(o) for o in opts],
                   "answer": ans, "explain": ex})
    for n, html, opts, ans, ex in WE:
        qs.append({"id": "up-we-%d" % n, "theme": "written", "subtheme": "Diagnostic Pre-Test: Written Expression",
                   "ref": "Section 2 no.%d" % n,
                   "instruction": "Pilih bagian bergaris bawah yang harus diperbaiki.",
                   "question": html, "options": [E(o) for o in opts],
                   "answer": ans, "explain": ex})
    bank = {"source": {"id": "unipma", "name": "UNIPMA — Soal Pelatihan TOEFL Mahasiswa (Diagnostic Pre-Test)",
                       "test": "TOEFL PBT"},
            "questions": qs}
    out = "/* dibuat oleh _skrip/build_bank18.py — jangan diedit tangan */\nTOEFLDRILL.addBank(\n"
    out += json.dumps(bank, ensure_ascii=False, indent=1) + "\n);\n"
    io.open("data/bank-18-unipma.js", "w", encoding="utf-8").write(out)
    d = {}
    for q in qs:
        d["ABCD"[q["answer"]]] = d.get("ABCD"[q["answer"]], 0) + 1
    print("bank-18-unipma.js:", len(qs), "soal | sebaran", d)

if __name__ == "__main__":
    build()
