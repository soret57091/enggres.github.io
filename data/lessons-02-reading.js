/* ============================================================
   MATERI BELAJAR — Bagian 2: Written Expression, Reading,
   Vocabulary, Listening, Writing & Speaking
   ============================================================ */
window.TOEFLDRILL_LESSONS = window.TOEFLDRILL_LESSONS || [];
window.TOEFLDRILL_LESSONS.push(

{ id:'written-expr', unit:'Written Expression', title:'Menemukan Bagian yang Salah',
  blurb:'Soal bergaris bawah: satu dari empat bagian salah. Ini urutan pemeriksaan yang paling cepat menemukannya.',
  themes:['written'], match:[],   /* seluruh soal bertema Written Expression */
  steps:[
  {t:'Bentuk soalnya', h:`
    <p>Empat bagian kalimat digarisbawahi; tugasmu memilih <b>satu</b> yang salah secara tata bahasa — bukan yang terdengar aneh, tapi yang benar-benar melanggar aturan.</p>
    <p>Jangan mencari makna. Kalimat soal boleh saja isinya membosankan atau janggal; yang dinilai murni strukturnya.</p>`},
  {t:'Checklist enam langkah', h:`
    <ol>
      <li><b>Subjek–verb agreement.</b> Tutup frasa penyela, cocokkan subjek inti dengan verb-nya.</li>
      <li><b>Bentuk kata.</b> Adjective di tempat adverb? Nomina di tempat verb? Lihat sufiksnya.</li>
      <li><b>Bentuk verb.</b> -ing/-ed sendirian tanpa <em>be</em>, tense yang bertabrakan dengan penanda waktu, verb setelah modal.</li>
      <li><b>Paralelisme.</b> Ada rangkaian <em>and/or</em>? Cek ketiga unsurnya sejenis.</li>
      <li><b>Preposisi & artikel.</b> Kolokasi (<em>depend on</em>), <em>a/an/the</em> pada nomina tunggal terhitung.</li>
      <li><b>Kata berlebih atau hilang.</b> Subjek ganda (<em>the theory it explains</em>), dobel komparatif (<em>more better</em>), dobel konjungsi (<em>although ... but</em>).</li>
    </ol>
    <p>Kalau setelah enam langkah masih ragu, pilih bagian yang paling menyimpang dari pola yang kamu kenal dan lanjut — jangan menahan waktu di satu nomor.</p>`},
  {t:'Contoh soal', ex:{
    q:'The number of <u>students</u> who <u>enrolls</u> in advanced statistics <u>has</u> increased <u>sharply</u> since 2015.',
    o:['students','enrolls','has','sharply'],
    a:1,
    w:'Relative pronoun <em>who</em> merujuk ke <em>students</em> (jamak), jadi verb di klausa itu harus <b>enroll</b>, bukan <em>enrolls</em>. Perhatikan bahwa <em>has increased</em> justru benar karena subjek induknya <em>the number of ...</em> (tunggal).'}},
  {t:'Contoh soal', ex:{
    q:'Although the equipment was outdated, <u>but</u> the technicians <u>managed</u> to complete the <u>repairs</u> <u>on time</u>.',
    o:['but','managed','repairs','on time'],
    a:0,
    w:'<em>Although</em> sudah menjadikan bagian pertama klausa keterangan, jadi <b>but</b> berlebih — cukup satu konjungsi. Tiga bagian lain sudah tepat.'}}
]},

{ id:'main-idea', unit:'Reading', title:'Main Idea, Judul Bagian & Overview',
  blurb:'Soal gagasan utama: yang dicari cakupan yang pas — tidak terlalu sempit, tidak terlalu luas.',
  themes:['reading'], match:['main idea','memilih judul','overview'],
  steps:[
  {t:'Di mana gagasan utama bersembunyi', h:`
    <p>Untuk teks akademik, gagasan utama biasanya ada di <b>kalimat pertama atau kedua paragraf pertama</b>, lalu ditegaskan lagi di kalimat penutup. Kalimat pertama tiap paragraf berikutnya memberi peta isinya.</p>
    <p>Teknik dua menit: baca kalimat pertama setiap paragraf, lalu kalimat terakhir paragraf terakhir. Dari situ kamu sudah bisa menebak jawaban main idea sebelum melihat pilihan.</p>`},
  {t:'Tiga bentuk pengecoh', h:`
    <ul>
      <li><b>Terlalu sempit</b> — benar, tapi hanya isi satu paragraf. Ini pengecoh paling sering dipilih.</li>
      <li><b>Terlalu luas</b> — bicara topik besar yang tidak dibahas seluas itu di teks.</li>
      <li><b>Benar tapi tidak disebut</b> — pernyataan yang masuk akal secara umum, namun tidak ada di teks.</li>
    </ul>
    <p>Untuk soal <em>memilih judul bagian</em> (headings), jawabannya harus mencakup <b>seluruh</b> paragraf, bukan hanya contoh atau angka yang menonjol di dalamnya.</p>`},
  {t:'Contoh soal', ex:{
    q:'Paragraf: <em>Wood was abundant in the North American colonies, and colonists used it for houses, tools, fuel, and ships. In Europe, by contrast, timber had grown scarce and expensive, so builders relied on stone and brick.</em><br><br>Gagasan utama paragraf itu adalah ...',
    o:['Rumah kolonial dibangun dari kayu','Melimpahnya kayu membuat teknologi kolonial berbeda dari Eropa','Eropa kehabisan hutan pada abad ke-18','Kapal kolonial lebih murah daripada kapal Eropa'],
    a:1,
    w:'B mencakup kedua sisi paragraf: kayu melimpah di koloni <em>dan</em> kontrasnya dengan Eropa. A dan D hanya satu detail (terlalu sempit); C menambah kesimpulan sebab yang tidak dinyatakan.'}},
  {t:'Contoh soal', ex:{
    q:'Kalimat pembuka sebuah bacaan: <em>Another reason that the chickenpox vaccine was not immediately accepted centred on the fear that its protection would not last a lifetime.</em><br><br>Paragraf <b>sebelum</b> paragraf ini paling mungkin membahas ...',
    o:['cara kerja vaksin cacar air di dalam tubuh','alasan lain mengapa orang tua menolak vaksin itu','sejarah penemuan virus cacar air','jumlah kasus cacar air di dunia saat ini'],
    a:1,
    w:'Kata <b>Another reason</b> mengunci jawabannya: kalau di sini disebut alasan <em>lain</em>, berarti paragraf sebelumnya sudah menyebut satu alasan. Soal jenis ini (yang menanyakan apa yang mendahului atau menyusul bacaan) selalu dijawab dari <b>kata sambung di kalimat pembuka atau penutup</b>, bukan dari isi tengahnya. A, C, dan D masuk akal sebagai topik, tetapi tidak ada penandanya di kalimat itu.'}}
]},

{ id:'detail-matching', unit:'Reading', title:'Detail, Scanning & Matching Information',
  blurb:'Soal detail dijawab dengan berburu kata kunci dan sinonimnya — bukan dengan membaca ulang semuanya.',
  themes:['reading'], match:['detail','scanning','informasi rinci','matching','mencocokkan','read in daily life','multiple choice'],
  steps:[
  {t:'Kata kunci yang layak diburu', h:`
    <p>Ambil dari pertanyaan kata yang <b>tidak mungkin diparafrase</b>: nama, angka, tahun, istilah teknis, nama tempat. Kata seperti <em>increase, important, people</em> hampir selalu diganti sinonim, jadi jangan dipakai sebagai jangkar.</p>
    <p>Setelah menemukan lokasinya, baca <b>satu kalimat sebelum dan sesudahnya</b> — jawaban sering berada di kalimat tetangga.</p>`},
  {t:'Urutan soal vs urutan teks', h:`
    <ul>
      <li><b>Detail / multiple choice / sentence completion</b>: umumnya <b>berurutan</b> mengikuti teks. Kalau nomor 5 kamu temukan di paragraf 3, nomor 6 hampir pasti sesudah titik itu.</li>
      <li><b>Matching information (paragraf mana yang memuat X)</b>: <b>tidak berurutan</b>, dan satu paragraf bisa terpakai lebih dari sekali. Kerjakan paling akhir, per paragraf, bukan per soal.</li>
      <li><b>Mengelompokkan ciri (matching features)</b>: buat tabel kecil di kertas — kolom nama/kategori, baris ciri.</li>
    </ul>`},
  {t:'Contoh soal', ex:{
    q:'Teks: <em>Dragonflies can hover, fly backward, and reach speeds of up to 30 miles per hour, a capability unmatched among insects of similar size.</em><br><br>Menurut teks, kemampuan capung yang tidak dimiliki insekta lain seukurannya adalah ...',
    o:['bertahan hidup di air','melayang dan terbang mundur pada kecepatan tinggi','berburu pada malam hari','bermigrasi jauh'],
    a:1,
    w:'Kata kunci yang diburu: <em>unmatched</em> / <em>30 miles per hour</em>. Kalimat itu menyebut tiga kemampuan (hover, fly backward, kecepatan) sebagai yang tak tertandingi → B. Pilihan lain tidak disebut di kalimat tersebut.'}},
  {t:'Contoh soal', ex:{
    q:'Bacaan punya empat bagian:<br><em>A. Bagaimana pengeras suara pertama dirakit di bengkel rumahan.<br>B. Mengapa penjualan radio melonjak setelah 1925.<br>C. Perselisihan paten antara dua produsen.<br>D. Pengaruh siaran radio terhadap kebiasaan keluarga di malam hari.</em><br><br>Bagian mana yang memuat informasi berikut: <b>sebuah sengketa hukum antarperusahaan</b>?',
    o:['Bagian A','Bagian B','Bagian C','Bagian D'],
    a:2,
    w:'Soal mencocokkan informasi tidak menuntut kamu membaca seluruh bacaan; ia menuntut kamu <b>menerjemahkan pernyataannya jadi kata kunci</b> lalu mencarinya. Di sini <em>sengketa hukum antarperusahaan</em> = <em>perselisihan paten antara dua produsen</em> → <b>C</b>. Perhatikan bahwa kata yang dipakai soal hampir tidak pernah sama persis dengan kata di bacaan — yang dicocokkan adalah maknanya.'}}
]},

{ id:'tfng', unit:'Reading', title:'True / False / Not Given (dan Yes/No/Not Given)',
  blurb:'Jenis soal terbanyak di bank IELTS. Kuncinya satu: bedakan “bertentangan” dari “tidak disebut”.',
  themes:['reading'], match:['true / false','yes / no','benar/salah'],
  steps:[
  {t:'Definisi yang harus dipegang', h:`
    <ul>
      <li><b>True / Yes</b> — pernyataan soal mengatakan hal yang <b>sama</b> dengan teks, meski kata-katanya berbeda.</li>
      <li><b>False / No</b> — teks mengatakan yang <b>berlawanan</b>. Harus ada kontradiksi yang bisa kamu tunjuk.</li>
      <li><b>Not Given</b> — teks <b>tidak membahasnya</b>, atau membahas sebagian saja sehingga kamu perlu berasumsi untuk memutuskan.</li>
    </ul>
    <p>Aturan praktis: kalau kamu harus berpikir “masuk akal, sih” — itu <b>Not Given</b>. Kalau kamu bisa menunjuk kalimatnya dan artinya bertabrakan — itu <b>False</b>.</p>
    <p>Bedanya True/False/Not Given dan Yes/No/Not Given hanya pada objeknya: yang pertama tentang <b>fakta</b> di teks, yang kedua tentang <b>pandangan penulis</b>.</p>`},
  {t:'Kata yang menentukan jawaban', h:`
    <p>Perhatikan pengubah kadar di pernyataan soal, karena di situlah jebakannya:</p>
    <ul>
      <li>mutlak: <em>all, only, never, always, the first, the most</em> — sering membuat pernyataan jadi <b>False</b> padahal teks menyebut “sebagian” atau “salah satu”.</li>
      <li>perbandingan: <em>more than, better than</em> — kalau teks tidak membandingkan, itu <b>Not Given</b>.</li>
      <li>sebab-akibat: <em>because, due to</em> — teks bisa menyebut dua fakta tanpa menyatakan hubungannya → <b>Not Given</b>.</li>
    </ul>`},
  {t:'Contoh soal', ex:{
    q:'Teks: <em>Some species of dragonfly migrate hundreds of kilometres, though the routes of most species remain unmapped.</em><br><br>Pernyataan: <b>All dragonfly species migrate long distances.</b>',
    o:['True','False','Not Given'],
    a:1,
    w:'Teks menyebut <em>some species</em>, pernyataan menyebut <em>all</em> — bertentangan langsung, jadi <b>False</b>. Kalau pernyataannya “rute migrasi capung sulit dipetakan”, itu True; kalau “capung bermigrasi lebih jauh daripada kupu-kupu”, itu Not Given karena teks tidak membandingkan.'}},
  {t:'Contoh soal', ex:{
    q:'Teks: <em>The first fire engines were pulled by hand, and it was not until the 1830s that horses were used to draw them.</em><br><br>Pernyataan: <b>Horse-drawn fire engines were more effective than hand-pulled ones.</b>',
    o:['True','False','Not Given'],
    a:2,
    w:'Teks hanya menyebut <em>urutan waktunya</em> — ditarik tangan dulu, baru kuda sejak 1830-an. Ia tidak pernah <b>membandingkan keefektifan</b> keduanya. Jadi jawabannya <b>Not Given</b>, bukan True. Ini jebakan paling sering: pembaca menambahkan kesimpulan yang masuk akal (kuda tentu lebih cepat) padahal soal ini hanya menanyakan apa yang <em>tertulis</em>. Aturannya: kalau pernyataan memuat perbandingan, sebab, atau penilaian yang tidak ada kalimatnya di teks → Not Given.'}}
]},

{ id:'inference', unit:'Reading', title:'Inference, Purpose & Reference',
  blurb:'Tiga jenis soal yang menuntut satu langkah di luar kalimat — tapi hanya satu langkah.',
  themes:['reading','listening'], match:['inference','purpose','reference','rhetorical','paraphrase','negative fact'],
  steps:[
  {t:'Inference: satu langkah saja', h:`
    <p>Jawaban inferensi harus bisa kamu buktikan dari teks dengan satu langkah penalaran. Kalau butuh dua atau tiga asumsi tambahan, itu pengecoh.</p>
    <p>Penanda soal: <em>it can be inferred, the author implies, the passage suggests</em>.</p>
    <p>Pilih jawaban yang <b>paling hati-hati</b>. Pernyataan yang berlebihan (<em>proves, always, the only</em>) hampir selalu salah pada tipe ini.</p>`},
  {t:'Purpose: kenapa penulis menyebutnya', h:`
    <p>Soal <em>Why does the author mention X?</em> tidak menanyakan apa itu X, tapi <b>fungsinya</b> di paragraf: memberi contoh, membandingkan, membantah anggapan, memperkenalkan sebab.</p>
    <p>Jawabnya dengan melihat kalimat <b>sebelum</b> X: biasanya di situ klaim yang X-nya jadi bukti.</p>`},
  {t:'Reference: cari yang cocok logika & bentuk', h:`
    <p>Soal <em>The word “it/they/this” refers to ...</em>. Ganti kata rujukan dengan tiap pilihan lalu baca ulang kalimatnya. Yang benar harus cocok dua-duanya: tunggal/jamak dan makna.</p>
    <p>Rujukan biasanya nomina terdekat <b>sebelum</b> kata itu yang berperan sebagai subjek atau objek utama, bukan nomina di dalam frasa preposisi.</p>`},
  {t:'Contoh soal', ex:{
    q:'Teks: <em>Early colonists rarely bothered to season timber before building. Houses therefore shifted and cracked within a decade, and repairs became a routine part of household life.</em><br><br>Dari paragraf itu dapat disimpulkan bahwa ...',
    o:['kolonis tidak tahu cara mengeringkan kayu','biaya perbaikan rumah menjadi hal yang lumrah diperhitungkan','rumah kolonial dibangun dari kayu keras','kayu di koloni berkualitas rendah'],
    a:1,
    w:'Teks menyatakan perbaikan menjadi rutin, jadi satu langkah kesimpulannya: penghuni menganggapnya hal biasa → B. A menuduh ketidaktahuan (teks hanya bilang “rarely bothered”), C dan D menambah informasi yang tidak ada.'}},
  {t:'Contoh soal', ex:{
    q:'Teks: <em>Hotels were distinctively American facilities that made conventions possible. The growing custom of regularly assembling representatives of all kinds of groups &mdash; political, commercial, professional, and learned <b>ones</b> &mdash; in turn supported the multiplying hotels.</em><br><br>Kata <b>ones</b> merujuk pada ...',
    o:['hotels','conventions','groups','representatives'],
    a:1,
    w:'Soal rujukan dijawab dengan satu cara: <b>masukkan tiap pilihan ke posisi kata itu</b> lalu baca ulang. <em>political, commercial, professional, and learned <b>conventions</b></em> — masuk akal dan sejajar dengan daftar sebelumnya. <em>hotels</em> tidak bisa disifati <em>learned</em>; <em>groups</em> sudah disebut sendiri tepat sebelumnya sehingga tidak perlu diganti kata ganti; <em>representatives</em> ada di kalimat lain. Kata rujukan hampir selalu menunjuk ke belakang, ke kata benda terdekat yang cocok bentuk tunggal/jamaknya.'}}
]},

{ id:'melengkapi', unit:'Reading', title:'Melengkapi Ringkasan, Catatan & Kalimat',
  blurb:'Isian dari teks: jawabannya kata persis dari bacaan, dan harus lolos uji tata bahasa.',
  themes:['reading','vocabulary'], match:['melengkapi','complete the words','jawaban singkat'],
  steps:[
  {t:'Aturan mainnya', h:`
    <ul>
      <li>Batas jumlah kata harus dipatuhi (<em>NO MORE THAN TWO WORDS</em>). Melebihi = salah, meski maknanya benar.</li>
      <li>Kata harus <b>diambil apa adanya</b> dari teks — tidak diubah bentuknya, tidak diparafrase.</li>
      <li>Angka boleh ditulis dengan angka; kata sambung seperti <em>a/the</em> ikut dihitung sebagai kata.</li>
    </ul>`},
  {t:'Prediksi dulu, cari kemudian', h:`
    <p>Sebelum melihat teks, tentukan dari rumpangnya: yang dibutuhkan <b>nomina, verba, angka, atau adjektiva?</b> Prediksi ini menghemat waktu dan mencegah salah bentuk kata.</p>
    <p>Ringkasan biasanya mengikuti urutan teks dan hanya mencakup <b>satu bagian</b> bacaan. Temukan paragraf awalnya, lalu kerjakan rumpang berurutan dari sana.</p>
    <p>Terakhir, baca ulang kalimatmu utuh. Kalau tata bahasanya pincang (<em>a research</em>, <em>increase of 5 percent were</em>), jawabannya kemungkinan salah bentuk.</p>`},
  {t:'Contoh soal', ex:{
    q:'Teks: <em>The bridge was financed entirely by private subscription, and its total cost reached £48,000 — nearly double the original estimate.</em><br><br>Isian: <em>Pembangunan jembatan dibiayai oleh ______ .</em> (tidak lebih dari dua kata)',
    o:['the government','private subscription','local investors','£48,000'],
    a:1,
    w:'Diambil persis dari teks: <b>private subscription</b> — dua kata, sesuai batas. <em>£48,000</em> menjawab pertanyaan lain (biaya), dua pilihan lainnya tidak ada di teks.'}},
  {t:'Contoh soal', ex:{
    q:'Teks: <em>Crows are able to recognise individual human faces, and they pass that recognition on to their offspring, which behave warily towards a person they have never met.</em><br><br>Ringkasan: <em>Burung gagak mengenali wajah manusia satu per satu dan mewariskan pengenalan itu kepada ______ .</em><br><br>Pilih dari kotak: <em>A. peneliti &nbsp; B. anak-anaknya &nbsp; C. kawanan lain &nbsp; D. manusia asing</em>',
    o:['A. peneliti','B. anak-anaknya','C. kawanan lain','D. manusia asing'],
    a:1,
    w:'Kunci soal ringkasan adalah <b>mencocokkan kata di kotak dengan kata di teks yang maknanya sama</b>, bukan mencari kata yang sama persis. <em>offspring</em> = <b>anak-anaknya</b> → B. Perhatikan juga tata bahasanya: rumpang itu berada sesudah <em>kepada</em>, jadi yang masuk harus pihak penerima. <em>Manusia asing</em> memang muncul di teks (<em>a person they have never met</em>) tetapi perannya berbeda — ia yang diwaspadai, bukan yang mewarisi.'}}
]},

{ id:'vocab-context', unit:'Vocabulary', title:'Vocabulary in Context',
  blurb:'Bukan soal hafalan kamus: makna yang dicari adalah makna kata di kalimat itu.',
  themes:['vocabulary'], match:[],   /* seluruh soal bertema Vocabulary */
  steps:[
  {t:'Tiga sumber petunjuk', h:`
    <ul>
      <li><b>Konteks kalimat.</b> Tutup kata yang ditanya, lalu isi sendiri dengan kata yang kamu rasa pas. Baru cocokkan ke pilihan.</li>
      <li><b>Penanda hubungan.</b> <em>but, however, although</em> menandakan makna berlawanan dengan kalimat sebelumnya; <em>that is, such as, in other words</em> menandakan definisi atau contoh yang mengulang maknanya.</li>
      <li><b>Bentuk kata.</b> Akar dan afiks menyempitkan pilihan: <em>in-/un-/dis-</em> (negasi), <em>pre-/post-</em> (waktu), <em>-ology</em> (ilmu), <em>-ify</em> (menjadikan).</li>
    </ul>`},
  {t:'Jebakan makna umum', h:`
    <p>Pengecoh favorit penulis soal adalah <b>makna paling umum</b> dari kata itu, padahal di kalimat tersebut maknanya berbeda.</p>
    <p><em>The colony <b>observed</b> the treaty for a decade.</em> → di sini <em>observed</em> = mematuhi, bukan mengamati.<br>
    <em>Her account of the voyage</em> → <em>account</em> = laporan, bukan rekening.</p>
    <p>Selalu uji ulang: masukkan pilihanmu ke kalimat aslinya dan baca utuh. Kalau kalimatnya jadi janggal, ganti.</p>`},
  {t:'Contoh soal', ex:{
    q:'<em>Although the two reports were issued by different agencies, their conclusions were virtually <b>identical</b>.</em><br><br>Kata <b>identical</b> paling dekat maknanya dengan ...',
    o:['the same','opposite','detailed','official'],
    a:0,
    w:'<em>Although</em> menandakan kontras antara “lembaga berbeda” dan “kesimpulan yang ...”, jadi yang masuk adalah kemiripan penuh → <b>the same</b>. <em>Opposite</em> justru menghapus kontras yang dibangun kalimat itu.'}},
  {t:'Contoh soal', ex:{
    q:'<em>Individuals infected with chickenpox can expect to experience a high but <b>tolerable</b> level of discomfort and a fever as the disease works its way through the system.</em><br><br>Kata <b>tolerable</b> paling dekat maknanya dengan ...',
    o:['sudden','bearable','infrequent','unexpected'],
    a:1,
    w:'Dua alat yang selalu bisa dipakai. <b>Struktur kata:</b> <em>tolerable</em> berasal dari <em>to tolerate</em> (menahan), dan <em>bearable</em> dari <em>to bear</em> yang artinya sama. <b>Konteks:</b> kata sambung <em>but</em> menuntut lawan dari <em>high</em> yang bernada negatif, jadi yang dicari adalah kata bernada meredakan. <em>sudden</em> dan <em>unexpected</em> sama-sama negatif sehingga tidak menimbulkan kontras; <em>infrequent</em> terdengar melegakan tetapi artinya jarang, bukan tertahankan.'}}
]},

{ id:'listening', unit:'Listening', title:'Strategi Listening (dengan Transkrip)',
  blurb:'Bank soal ini memakai transkrip sebagai pengganti audio — pakai untuk melatih perburuan penanda jawaban.',
  themes:['listening'], match:[],    /* seluruh soal bertema Listening */
  steps:[
  {t:'Kata penanda arah bicara', h:`
    <p>Dalam percakapan dan kuliah, jawaban hampir selalu menempel pada penanda:</p>
    <ul>
      <li>penekanan: <em>the key point is, what matters here, remember that</em></li>
      <li>urutan: <em>first, next, finally, to begin with</em></li>
      <li>kontras & koreksi diri: <em>but, actually, in fact, sorry — I meant</em></li>
      <li>contoh: <em>for instance, such as, take ... for example</em></li>
    </ul>
    <p>Pada koreksi diri, jawaban yang benar adalah yang <b>disebut terakhir</b> — angka atau nama pertama sengaja dipasang sebagai pengecoh.</p>`},
  {t:'Cara berlatih dengan transkrip', h:`
    <ol>
      <li>Baca pertanyaannya dulu, prediksi jenis jawaban (angka, nama, alasan, tempat).</li>
      <li>Baca transkrip <b>sekali saja</b>, seolah audio: jangan berhenti mengulang kalimat.</li>
      <li>Tandai kalimat tempat jawaban ditemukan, lalu bandingkan dengan pembahasan.</li>
      <li>Untuk soal <em>Choose a Response</em>, perhatikan fungsi ucapannya: menawarkan, mengeluh, meminta izin — jawaban harus merespons fungsi itu, bukan mengulang kata-katanya.</li>
    </ol>
    <p>Detail teknis yang sering salah: ejaan nama (didiktekan huruf per huruf), angka (<em>thirteen</em> vs <em>thirty</em>), tanggal, dan satuan.</p>`},
  {t:'Contoh soal', ex:{
    q:'Transkrip: <em>Student: I&rsquo;d like to register for the field trip on the 14th. — Staff: The 14th is full, but we&rsquo;ve added a second group on the 21st.</em><br><br>Kapan mahasiswa itu bisa mengikuti kunjungan lapangan?',
    o:['tanggal 14','tanggal 21','tanggal 14 dan 21','tidak bisa mengikuti'],
    a:1,
    w:'Kata <em>but</em> menandai koreksi arah: tanggal 14 penuh, ditambahkan kelompok kedua pada tanggal <b>21</b>. Tanggal 14 dipasang sebagai pengecoh karena disebut lebih dulu.'}},
  {t:'Contoh soal', ex:{
    q:'Naskah: <em>Pria: Have you seen my calculator? It was right here a minute ago. &mdash; Wanita: Did you look under your book? I&rsquo;m always losing things that way.</em><br><br>Apa maksud perkataan wanita itu?',
    o:['Dia menghilangkan kalkulator pria itu','Dia akan meminjamkan kalkulatornya','Kalkulator itu mungkin ada di bawah buku','Pria itu tidak akan sempat mencarinya'],
    a:2,
    w:'Bagian Listening jarang menanyakan apa yang <em>diucapkan</em>; yang ditanyakan hampir selalu apa yang <b>dimaksudkan</b>. Di sini pertanyaan wanita itu bukan pertanyaan sungguhan melainkan saran: kalkulatornya mungkin tertutup buku. Pola yang wajib dikenali: <em>Did you look…?</em>, <em>Why don&rsquo;t you…?</em>, dan <em>Have you tried…?</em> semuanya berarti saran. Pilihan A membalik siapa yang kehilangan; B menambah tawaran yang tidak ada; D mengambil kata <em>a minute ago</em> di luar konteks.'}}
]},

{ id:'writing-speaking', unit:'Writing & Speaking', title:'Menulis & Berbicara Terstruktur',
  blurb:'Soal terbuka tidak dinilai otomatis, jadi yang kamu latih adalah kerangkanya.',
  themes:['writing','speaking'], match:[],   /* seluruh soal Writing & Speaking */
  steps:[
  {t:'Kerangka esai argumen', h:`
    <p>Empat paragraf, kira-kira 280–320 kata:</p>
    <ol>
      <li><b>Pendahuluan</b> — parafrase pertanyaan + posisimu dalam satu kalimat tegas.</li>
      <li><b>Alasan 1</b> — kalimat topik, penjelasan, satu contoh konkret.</li>
      <li><b>Alasan 2</b> — pola sama; boleh mengakui sisi lawan lalu membantahnya.</li>
      <li><b>Penutup</b> — ulangi posisi dengan kata lain, tanpa informasi baru.</li>
    </ol>
    <p>Yang paling menaikkan nilai bukan kata sulit, tapi <b>kalimat topik yang jelas</b> dan contoh yang spesifik.</p>`},
  {t:'Email & deskripsi data', h:`
    <p><b>Email/surat:</b> sebut tujuan di kalimat pertama, satu paragraf per keperluan, tutup dengan permintaan tindakan yang jelas. Jaga konsistensi nada — formal semua atau santai semua.</p>
    <p><b>Deskripsi grafik/tabel:</b> satu kalimat parafrase judul, satu kalimat <em>overview</em> berisi pola besar (naik, turun, stabil, timpang), lalu dua paragraf detail dengan angka pembanding. Jangan memberi opini.</p>`},
  {t:'Speaking: struktur 45 detik', h:`
    <p>Pakai pola <b>PREP</b>: <em>Point</em> (posisi, 1 kalimat) – <em>Reason</em> (alasan, 1–2 kalimat) – <em>Example</em> (contoh pribadi, 2 kalimat) – <em>Point</em> (tutup, 1 kalimat).</p>
    <p>Latihan yang efektif: rekam dirimu, lalu hitung berapa kali kamu berhenti. Target awal bukan sempurna, tapi <b>tanpa jeda panjang</b>.</p>`},
  {t:'Contoh soal', ex:{
    q:'Prompt: <em>Some people prefer to study alone; others prefer to study in groups. Which do you prefer, and why?</em><br><br>Kalimat pembuka mana yang paling kuat?',
    o:['There are many advantages and disadvantages of both sides of this issue.','I prefer studying in groups because explaining ideas out loud forces me to notice what I do not understand.','Studying is very important for students in the modern world today.','In my opinion, both ways are good depending on the situation and the person.'],
    a:1,
    w:'B langsung menyatakan posisi <b>dan</b> alasan spesifik — persis yang dituntut prompt. A dan D menunda posisi, C kalimat pembuka umum yang tidak menambah apa pun (dan memakan waktu bicara).'}},
  {t:'Contoh soal', ex:{
    q:'Susun kalimat yang benar dari potongan berikut, untuk menjawab pertanyaan <em>Why did you choose this university?</em><br><br><em>because / I chose / it offers / this university / a research programme / in my field</em>',
    o:['I chose this university because it offers a research programme in my field.','I chose because this university it offers a research programme in my field.','Because I chose this university it offers a research programme in my field.','This university I chose because a research programme it offers in my field.'],
    a:0,
    w:'Rangka yang dinilai penguji selalu sama: <b>posisi &rarr; penghubung &rarr; alasan yang khusus</b>. A memenuhi ketiganya dan susunan klausanya benar (S + V + O, lalu <em>because</em> + S + V + O). B menaruh <em>because</em> sebelum objek klausa induk; C menjadikan seluruh kalimat klausa keterangan tanpa induk; D mengacak urutan subjek-verb-objek. Untuk speaking, kalimat pertama seperti A sudah cukup — sisa waktumu dipakai untuk satu contoh nyata, bukan untuk memperpanjang pembukaan.'}}
]}

);
