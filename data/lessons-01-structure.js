/* ============================================================
   MATERI BELAJAR — Bagian 1: Fondasi Kalimat (Structure)
   Dipakai oleh tab "Belajar dulu yuk" di index.html
   ============================================================ */
window.TOEFLDRILL_LESSONS = window.TOEFLDRILL_LESSONS || [];
window.TOEFLDRILL_LESSONS.push(

{ id:'inti-kalimat', unit:'Fondasi Kalimat', title:'Inti Kalimat: Subjek & Verb',
  blurb:'Sebelum apa pun: kenali mana subjek dan mana verb utama. Semua soal Structure berangkat dari sini.',
  themes:['structure','written'], match:['mengenali subjek','struktur kalimat','structure'],
  steps:[
  {t:'Kenapa ini yang pertama', h:`
    <p>Soal Structure TOEFL hampir selalu menguji satu hal: apakah kalimatnya <b>lengkap dan hanya punya satu inti</b>. Kalimat lengkap minimal punya <b>subjek</b> (pelaku/topik) dan <b>verb utama</b> (kata kerja yang ditandai waktu).</p>
    <ul>
      <li><b>The committee</b> <b>approved</b> the plan. → subjek + verb utama ✔</li>
      <li><b>Approving</b> the plan quickly. → tidak ada verb utama ✘</li>
      <li>In the middle of the night. → hanya frasa preposisi ✘</li>
    </ul>
    <p>Jadi begitu melihat titik-titik rumpang, tanya dulu: <em>yang hilang itu subjeknya, verb-nya, atau keduanya?</em></p>`},
  {t:'Tiga jebakan langganan', h:`
    <p><b>1. Frasa preposisi bukan subjek.</b> Kata setelah <em>of, in, with, along with</em> tidak bisa jadi subjek.<br>
    <em>The box of old letters</em> <b>was</b> found — subjeknya <em>box</em>, bukan <em>letters</em>.</p>
    <p><b>2. Bentuk -ing dan -ed sendirian bukan verb utama.</b> Butuh <em>be</em> atau <em>have</em>.<br>
    <em>The results published last year</em> ✘ → <em>The results <b>were</b> published last year</em> ✔</p>
    <p><b>3. Satu klausa hanya boleh punya satu verb utama.</b> Kalau ada dua, harus ada konjungsi atau salah satunya diubah jadi klausa/frasa.<br>
    <em>The engine failed the pilot landed safely</em> ✘ → <em>The engine failed, <b>so</b> the pilot landed safely</em> ✔</p>`},
  {t:'Cara kerja di soal', h:`
    <p>Langkah cepat yang bisa kamu pakai di setiap nomor:</p>
    <ul>
      <li>Tutup semua frasa preposisi dan klausa keterangan. Sisanya = tulang kalimat.</li>
      <li>Cek: ada subjek? ada verb utama bertanda waktu?</li>
      <li>Buang pilihan yang menambah subjek/verb kedua tanpa konjungsi, atau yang mengawali klausa tapi tidak pernah menutupnya.</li>
    </ul>`},
  {t:'Contoh soal', ex:{
    q:'______ was awarded the Nobel Prize in Physics in 1903 and in Chemistry in 1911.',
    o:['Because Marie Curie','Marie Curie','When Marie Curie','Marie Curie, who'],
    a:1,
    w:'Kalimat sudah punya verb utama (<b>was awarded</b>) tapi belum punya subjek. Yang dibutuhkan hanya frasa nomina: <b>Marie Curie</b>. A dan C menambah konjungsi sehingga kalimat jadi klausa keterangan tanpa induk; D menjadikan verb utama milik klausa adjektiva, jadi kalimat utamanya kehilangan predikat.'}},
  {t:'Contoh soal', ex:{
    q:'The instruments used by early surveyors ______ surprisingly accurate for their time.',
    o:['being','were','to be','which were'],
    a:1,
    w:'<em>used by early surveyors</em> hanya frasa participle yang menerangkan <em>instruments</em>, bukan verb utama. Jadi kalimat masih butuh verb utama: <b>were</b>. A dan C bukan verb bertanda waktu; D membuat seluruh kalimat jadi klausa tanpa induk.'}}
]},

{ id:'sv-agreement', unit:'Fondasi Kalimat', title:'Kesesuaian Subjek–Kata Kerja',
  blurb:'Verb ikut subjek inti, bukan kata yang paling dekat. Termasuk aturan each, the number of, dan gerund.',
  themes:['structure','written'], match:['kesesuaian subjek'],
  steps:[
  {t:'Aturan dasar', h:`
    <p>Verb menyesuaikan diri dengan <b>subjek inti</b>. Masalahnya, penulis soal suka menyelipkan kata di antara keduanya supaya kamu tertipu oleh kata terdekat.</p>
    <ul>
      <li>The <b>quality</b> of the recordings <b>is</b> poor. (bukan <em>are</em>)</li>
      <li>The <b>samples</b> in the second box <b>were</b> contaminated.</li>
    </ul>
    <p>Frasa penyela yang tidak mengubah bentuk verb: <em>along with, as well as, together with, in addition to, including</em>.<br>
    The director, as well as the actors, <b>was</b> present.</p>`},
  {t:'Daftar yang wajib hafal', h:`
    <ul>
      <li><b>each / every / either / neither / one of</b> + verb tunggal → <em>Each of the students <b>has</b> a locker.</em></li>
      <li><b>the number of</b> + verb tunggal · <b>a number of</b> + verb jamak → <em>The number of visitors <b>has</b> risen</em> / <em>A number of visitors <b>have</b> complained.</em></li>
      <li><b>Gerund atau klausa sebagai subjek</b> → tunggal. <em>Collecting rare stamps <b>is</b> expensive.</em></li>
      <li><b>either A or B / neither A nor B</b> → verb ikut yang <b>paling dekat</b>. <em>Neither the manager nor the clerks <b>were</b> informed.</em></li>
      <li><b>there is / there are</b> → ikut nomina sesudahnya. <em>There <b>are</b> several reasons.</em></li>
      <li>Nomina jumlah/ukuran sebagai satu kesatuan → tunggal. <em>Twenty miles <b>is</b> a long walk.</em></li>
    </ul>`},
  {t:'Contoh soal', ex:{
    q:'The list of participants and their affiliations ______ been posted outside the lecture hall.',
    o:['have','has','having','are'],
    a:1,
    w:'Subjek intinya <b>the list</b> (tunggal) — <em>of participants and their affiliations</em> cuma frasa preposisi. Verb yang benar <b>has</b> been posted. Kalau subjeknya benar-benar jamak barulah <em>have</em>.'}},
  {t:'Contoh soal', ex:{
    q:'Neither the coach nor the players ______ satisfied with the referee&rsquo;s decision.',
    o:['was','has been','were','is'],
    a:2,
    w:'Pada <em>neither ... nor ...</em>, verb mengikuti subjek yang paling dekat, yaitu <b>the players</b> (jamak) → <b>were</b>.'}}
]},

{ id:'klausa', unit:'Fondasi Kalimat', title:'Klausa: Independent, Adjective, Adverb, Noun',
  blurb:'Empat jenis klausa dan konjungsi yang mengawalinya — modal utama menjawab soal kalimat kompleks.',
  themes:['structure','written'], match:['clauses','klausa'],
  steps:[
  {t:'Peta klausa', h:`
    <p><b>Independent clause</b> bisa berdiri sendiri: <em>The rain stopped.</em></p>
    <p><b>Dependent clause</b> tidak bisa, dan ada tiga rasa:</p>
    <ul>
      <li><b>Adjective clause</b> — menerangkan nomina, diawali <em>who, whom, whose, which, that, where, when</em>.<br><em>The scientist <b>who discovered penicillin</b> was Scottish.</em></li>
      <li><b>Adverb clause</b> — menerangkan keseluruhan kalimat, diawali <em>although, because, since, while, when, if, unless, so that</em>.<br><em><b>Because the road was flooded</b>, the bus turned back.</em></li>
      <li><b>Noun clause</b> — menempati posisi subjek/objek, diawali <em>that, what, whether, how, why</em>.<br><em><b>What the survey revealed</b> surprised the researchers.</em></li>
    </ul>`},
  {t:'Menyambung dua independent clause', h:`
    <p>Hanya tiga cara yang sah:</p>
    <ul>
      <li>koma + <b>and, but, or, so, for, yet, nor</b> → <em>The engine stalled, <b>but</b> the crew stayed calm.</em></li>
      <li>titik koma → <em>The engine stalled; the crew stayed calm.</em></li>
      <li>titik koma + kata transisi + koma → <em>...stalled; <b>however</b>, the crew stayed calm.</em></li>
    </ul>
    <p><b>Jebakan klasik:</b> memakai dua konjungsi sekaligus. <em>Although it rained, <s>but</s> the match continued.</em> — pilih salah satu, bukan dua.</p>`},
  {t:'Adjective clause: yang sering diuji', h:`
    <ul>
      <li><b>who</b> untuk orang, <b>which</b> untuk benda, <b>that</b> untuk keduanya (tanpa koma).</li>
      <li><b>whose</b> = kepemilikan: <em>the author <b>whose</b> book won the prize</em>.</li>
      <li>Kalau relative pronoun berfungsi sebagai <b>objek</b>, boleh dihilangkan: <em>the book (that) I borrowed</em>. Kalau berfungsi sebagai <b>subjek</b>, tidak boleh: <em>the book <b>that</b> won the prize</em>.</li>
      <li>Setelah relative pronoun jangan ada subjek ganda: <em>the theory that <s>it</s> explains gravity</em> ✘</li>
    </ul>`},
  {t:'Contoh soal', ex:{
    q:'Although the storm had passed by noon, ______.',
    o:['but the roads were still closed','the roads were still closed','and the roads closed','closing the roads for hours'],
    a:1,
    w:'<em>Although ...</em> sudah menjadi adverb clause, jadi yang dibutuhkan adalah induk kalimat berupa independent clause: <b>the roads were still closed</b>. A menumpuk dua konjungsi, C menambah <em>and</em> yang tidak perlu, D hanya frasa tanpa verb utama.'}},
  {t:'Contoh soal', ex:{
    q:'The geologist ______ mapped the fault line published her results last spring.',
    o:['who she','which','who','whose'],
    a:2,
    w:'Yang dibutuhkan relative pronoun untuk <b>orang</b> yang berfungsi sebagai <b>subjek</b> di klausanya (<em>___ mapped the fault line</em>) → <b>who</b>. A menambah subjek ganda, B untuk benda, D butuh nomina sesudahnya.'}}
]},

{ id:'paralelisme', unit:'Fondasi Kalimat', title:'Paralelisme & Pasangan Korelatif',
  blurb:'Unsur yang disejajarkan harus berbentuk sama. Pasangan both…and, not only…but also punya aturan ketat.',
  themes:['structure','written'], match:['parallelism','paralelisme'],
  steps:[
  {t:'Bentuk sama sejajar', h:`
    <p>Kalau dua unsur atau lebih dihubungkan <em>and, or, but</em>, ketiganya harus satu jenis: semua nomina, semua gerund, semua infinitive, atau semua klausa.</p>
    <ul>
      <li>✔ The course teaches students <b>to plan</b>, <b>to draft</b>, and <b>to revise</b>.</li>
      <li>✘ The course teaches students to plan, to draft, and <s>revising</s>.</li>
      <li>✔ She is admired for her <b>patience</b>, her <b>humor</b>, and her <b>honesty</b>.</li>
    </ul>
    <p>Boleh menyebut <em>to</em> sekali saja asal konsisten: <em>to plan, draft, and revise</em>.</p>`},
  {t:'Pasangan korelatif', h:`
    <p>Kata pertama menentukan kata kedua, dan bentuk di kedua sisi harus cocok:</p>
    <ul>
      <li><b>both</b> A <b>and</b> B</li>
      <li><b>not only</b> A <b>but also</b> B</li>
      <li><b>either</b> A <b>or</b> B · <b>neither</b> A <b>nor</b> B</li>
      <li><b>between</b> A <b>and</b> B (bukan <em>between A or B</em>)</li>
      <li>perbandingan: <b>as</b> ... <b>as</b>, <b>more</b> ... <b>than</b> (bukan <em>more ... as</em>)</li>
    </ul>
    <p><em>The device is not only cheaper <b>but also</b> easier to repair.</em> — dua sisi sama-sama adjektiva komparatif.</p>`},
  {t:'Contoh soal', ex:{
    q:'The training program emphasizes safety, teamwork, and ______.',
    o:['to communicate clearly','communicating clearly','clear communication','communicate clearly'],
    a:2,
    w:'Dua unsur pertama nomina (<em>safety, teamwork</em>), jadi unsur ketiga juga harus nomina: <b>clear communication</b>. Pilihan lain infinitive/gerund/verb sehingga rangkaiannya tidak sejajar.'}},
  {t:'Contoh soal', ex:{
    q:'The new alloy is not only lighter than steel ______ resistant to corrosion.',
    o:['and also','but also','as well','however'],
    a:1,
    w:'Pasangan tetap <em>not only ... <b>but also</b> ...</em>. Bentuk di kedua sisi pun sejajar: adjektiva <em>lighter</em> dan <em>resistant</em>.'}}
]},

{ id:'preposisi', unit:'Fondasi Kalimat', title:'Preposisi: Waktu, Tempat & Kolokasi',
  blurb:'Topik paling banyak di bank soal. Sebagian bisa dinalar (waktu/tempat), sebagian harus dihafal sebagai pasangan kata.',
  themes:['structure','written'], match:['preposisi'],
  steps:[
  {t:'Waktu: in / on / at', h:`
    <ul>
      <li><b>in</b> — rentang panjang: <em>in 1998, in July, in the morning, in the 1920s, in two hours</em></li>
      <li><b>on</b> — hari & tanggal: <em>on Monday, on 3 May, on my birthday, on the weekend (AmE)</em></li>
      <li><b>at</b> — titik waktu: <em>at 6 p.m., at noon, at night, at the same time</em></li>
    </ul>
    <p>Pasangan lain yang sering muncul: <em><b>during</b> the lecture</em> (sepanjang), <em><b>for</b> three years</em> (durasi), <em><b>since</b> 2010</em> (titik awal), <em><b>by</b> Friday</em> (paling lambat), <em><b>until</b> Friday</em> (sampai).</p>`},
  {t:'Tempat & arah', h:`
    <ul>
      <li><b>in</b> ruang tertutup/wilayah: <em>in the lab, in Canada</em></li>
      <li><b>on</b> permukaan/garis: <em>on the wall, on the coast, on page 12</em></li>
      <li><b>at</b> titik/lokasi kegiatan: <em>at the entrance, at the conference</em></li>
      <li>arah: <b>to</b> (tujuan), <b>into</b> (masuk), <b>onto</b> (naik ke), <b>toward</b> (menuju), <b>through</b> (menembus), <b>across</b> (menyeberang), <b>along</b> (menyusuri)</li>
    </ul>`},
  {t:'Kolokasi yang wajib dihafal', h:`
    <p><b>Verb + preposisi:</b> depend <b>on</b>, consist <b>of</b>, result <b>in</b>, result <b>from</b>, rely <b>on</b>, account <b>for</b>, contribute <b>to</b>, refer <b>to</b>, object <b>to</b>, insist <b>on</b>, succeed <b>in</b>, differ <b>from</b>, comply <b>with</b>, benefit <b>from</b>.</p>
    <p><b>Adjektiva + preposisi:</b> aware <b>of</b>, capable <b>of</b>, similar <b>to</b>, different <b>from</b>, responsible <b>for</b>, famous <b>for</b>, interested <b>in</b>, based <b>on</b>, dependent <b>on</b>, familiar <b>with</b>, subject <b>to</b>.</p>
    <p><b>Nomina + preposisi:</b> reason <b>for</b>, increase <b>in</b>, effect <b>on</b>, cause <b>of</b>, solution <b>to</b>, demand <b>for</b>, lack <b>of</b>, attitude <b>toward</b>.</p>
    <p>Tanpa preposisi (sering jadi jebakan): <em>discuss</em>, <em>enter</em>, <em>approach</em>, <em>mention</em>, <em>lack</em>(v), <em>marry</em>. → <em>They discussed <s>about</s> the plan.</em> ✘</p>`},
  {t:'Contoh soal', ex:{
    q:'The sharp rise ______ fuel prices resulted ______ higher shipping costs.',
    o:['of / from','in / in','on / to','in / for'],
    a:1,
    w:'Pasangannya tetap: <b>a rise in</b> (kenaikan pada) dan <b>result in</b> (mengakibatkan). Kalau arah sebabnya dibalik, baru <em>result <b>from</b></em>: <em>Higher costs resulted from the rise.</em>'}},
  {t:'Contoh soal', ex:{
    q:'Most of the delegates arrived ______ the conference center ______ Sunday evening.',
    o:['in / at','at / on','to / in','at / in'],
    a:1,
    w:'Lokasi kegiatan sebagai titik → <b>at</b> the conference center; hari (Sunday) → <b>on</b> Sunday evening. Ingat: nama hari selalu <em>on</em>, meski disebut bagian harinya.'}}
]},

{ id:'bentuk-kata', unit:'Fondasi Kalimat', title:'Bentuk Kata: Adjective vs Adverb & Keluarga Kata',
  blurb:'Posisi kata di dalam kalimat menentukan bentuknya. Kenali sufiks dan tempat masing-masing.',
  themes:['structure','written'], match:['bentuk kata','pilihan kata'],
  steps:[
  {t:'Siapa menerangkan siapa', h:`
    <ul>
      <li><b>Adjective</b> menerangkan nomina, atau muncul setelah linking verb (<em>be, seem, become, appear, remain, feel</em>).<br><em>a <b>rapid</b> decline</em> · <em>the result seems <b>reliable</b></em></li>
      <li><b>Adverb</b> menerangkan verb, adjective, atau adverb lain.<br><em>declined <b>rapidly</b></em> · <em><b>remarkably</b> reliable</em></li>
    </ul>
    <p>Cek cepat: kalau kata itu menempel pada nomina → adjective. Kalau menerangkan bagaimana/kapan/seberapa → adverb.</p>`},
  {t:'Sufiks penanda keluarga kata', h:`
    <ul>
      <li>nomina: <em>-tion, -ment, -ness, -ity, -ance/-ence, -ism, -ure</em> → <em>analysis, statement, density, resistance</em></li>
      <li>adjektiva: <em>-ous, -ive, -al, -ful, -less, -able/-ible, -ic</em> → <em>various, productive, essential</em></li>
      <li>adverb: <em>-ly</em> → <em>essentially</em></li>
      <li>verba: <em>-ize, -ify, -en, -ate</em> → <em>stabilize, clarify, strengthen</em></li>
    </ul>
    <p>Waspadai kata yang bentuk adjektiva dan adverb-nya sama: <em>fast, hard, late, early, straight</em>. Dan yang berubah makna: <em>hardly</em> = hampir tidak, <em>lately</em> = belakangan ini.</p>`},
  {t:'Perbandingan', h:`
    <ul>
      <li>satu suku kata: <em>-er / -est</em> → <em>cheaper, cheapest</em></li>
      <li>tiga suku kata atau lebih: <em>more / most</em> → <em>more efficiently</em></li>
      <li>jangan dobel: <em><s>more cheaper</s></em> ✘</li>
      <li><em>the + comparative, the + comparative</em> → <em>The higher the altitude, the thinner the air.</em></li>
    </ul>`},
  {t:'Contoh soal', ex:{
    q:'The revised procedure works far more ______ than the one it replaced.',
    o:['efficient','efficiently','efficiency','efficiencies'],
    a:1,
    w:'Yang diterangkan adalah verb <b>works</b> (bagaimana cara kerjanya) → butuh adverb: <b>more efficiently</b>. <em>Efficient</em> adjektiva, dua sisanya nomina.'}},
  {t:'Contoh soal', ex:{
    q:'Despite the storm, the bridge remained ______ throughout the night.',
    o:['stably','stability','stable','stabilize'],
    a:2,
    w:'<em>remained</em> di sini linking verb, jadi yang mengikuti adalah adjektiva yang menerangkan subjek: <b>stable</b>. Setelah linking verb tidak dipakai adverb.'}}
]},

{ id:'verb-gerund', unit:'Fondasi Kalimat', title:'Verb, Participle, Gerund & Infinitive',
  blurb:'Kapan pakai -ing, kapan -ed, kapan to + verb. Termasuk frasa participle di awal kalimat.',
  themes:['structure','written'], match:['verb','participle','gerund','infinitive'],
  steps:[
  {t:'Participle: -ing vs -ed', h:`
    <p><b>-ing</b> = aktif, pelaku. <b>-ed/-en</b> = pasif, yang dikenai.</p>
    <ul>
      <li>the <b>developing</b> countries (negara yang sedang berkembang)</li>
      <li>the <b>developed</b> film (film yang dicetak)</li>
      <li>an <b>exciting</b> discovery / the <b>excited</b> audience</li>
    </ul>
    <p>Frasa participle di awal kalimat harus menerangkan <b>subjek induk</b>:<br>
    ✔ <em><b>Built</b> in 1885, the bridge is still in use.</em> (jembatannya yang dibangun)<br>
    ✘ <em>Built in 1885, engineers still admire the bridge.</em> (insinyurnya jadi yang dibangun)</p>`},
  {t:'Gerund atau infinitive?', h:`
    <ul>
      <li>setelah <b>preposisi</b> selalu gerund: <em>interested <b>in studying</b></em>, <em>capable <b>of solving</b></em></li>
      <li>verb yang diikuti <b>gerund</b>: enjoy, avoid, suggest, consider, mind, finish, keep, recommend, risk, deny</li>
      <li>verb yang diikuti <b>infinitive</b>: want, decide, hope, plan, agree, refuse, manage, fail, offer, seem</li>
      <li>verb + objek + infinitive: allow, ask, advise, force, encourage, persuade, remind</li>
      <li>setelah <b>make, let, have</b> dan modal → bentuk dasar tanpa <em>to</em>: <em>let him <b>go</b></em>, <em>must <b>be</b></em></li>
      <li><em>used to</em> + verb dasar (kebiasaan lampau) vs <em>be used to</em> + gerund (terbiasa)</li>
    </ul>`},
  {t:'Subjunctive & bentuk dasar', h:`
    <p>Setelah verb/adjektiva berkonotasi saran atau keharusan, klausa <em>that</em> memakai <b>bentuk dasar</b> tanpa perubahan:</p>
    <ul>
      <li>recommend, suggest, insist, demand, require, propose, request</li>
      <li>it is essential/necessary/important that ...</li>
    </ul>
    <p><em>The board recommended that the report <b>be</b> revised.</em> · <em>It is essential that she <b>attend</b> the hearing.</em></p>`},
  {t:'Contoh soal', ex:{
    q:'______ in 1885, the cantilever bridge is still carrying rail traffic today.',
    o:['Building','It was built','Built','To build'],
    a:2,
    w:'Yang dibutuhkan frasa participle pasif yang menerangkan subjek <em>the bridge</em> → <b>Built</b>. A menjadikan jembatan sebagai pelaku pembangunan, B menciptakan klausa kedua tanpa konjungsi, D menyatakan tujuan yang tidak logis.'}},
  {t:'Contoh soal', ex:{
    q:'The committee insisted that every applicant ______ a second interview.',
    o:['attends','attended','attend','to attend'],
    a:2,
    w:'<em>insist that</em> memicu subjunctive: verb dalam bentuk <b>dasar</b> tanpa -s, meskipun subjeknya tunggal → <b>attend</b>.'}}
]},

{ id:'kata-rancu', unit:'Fondasi Kalimat', title:'Kata Rancu: other, do/make, so/such, many/much',
  blurb:'Kelompok kata yang mirip tapi aturannya beda — porsinya besar di bank soal Structure.',
  themes:['structure','written'], match:['kata rancu'],
  steps:[
  {t:'another / other / others / the other', h:`
    <ul>
      <li><b>another</b> + nomina tunggal: <em>another reason</em> (satu lagi, tak tentu)</li>
      <li><b>other</b> + nomina jamak: <em>other reasons</em></li>
      <li><b>the other</b> = sisanya yang tertentu: <em>the other half</em></li>
      <li><b>others</b> berdiri sendiri (tanpa nomina): <em>Some agreed; others did not.</em></li>
      <li><b>each other / one another</b> = saling</li>
    </ul>`},
  {t:'do / make dan pasangan tetapnya', h:`
    <p><b>do</b> untuk kegiatan/tugas: <em>do research, do homework, do business, do a favor, do damage</em>.<br>
    <b>make</b> untuk menghasilkan/keputusan: <em>make a decision, make progress, make an effort, make a mistake, make arrangements, make noise</em>.</p>`},
  {t:'so / such / too / enough / as', h:`
    <ul>
      <li><b>so</b> + adjektiva/adverb + <em>that</em>: <em>so cold that the pipes froze</em></li>
      <li><b>such</b> + (a) + adjektiva + nomina + <em>that</em>: <em>such a cold night that ...</em></li>
      <li><b>too</b> + adjektiva + <em>to</em> = terlalu ... untuk: <em>too dense to float</em></li>
      <li>adjektiva + <b>enough</b> + <em>to</em> = cukup ...: <em>light enough to carry</em></li>
      <li><b>as ... as</b> untuk kesetaraan; <b>the same as</b>, <b>similar to</b>, <b>different from</b></li>
    </ul>`},
  {t:'many / much / few / little', h:`
    <ul>
      <li>bisa dihitung: <b>many, few, a few, fewer, number of</b> → <em>few species</em></li>
      <li>tidak bisa dihitung: <b>much, little, a little, less, amount of</b> → <em>little rainfall</em></li>
      <li><b>a few / a little</b> = ada sedikit (positif); <b>few / little</b> = hampir tidak ada (negatif)</li>
    </ul>`},
  {t:'Contoh soal', ex:{
    q:'There were ______ volunteers that the organizers had to cancel two of the sessions.',
    o:['such few','so few','too few','very few'],
    a:1,
    w:'Pola akibat memakai <em>so ... that</em>, dan <em>few</em> dipakai karena <em>volunteers</em> bisa dihitung → <b>so few</b>. <em>such</em> butuh nomina dengan adjektiva, <em>too few</em> tidak berpasangan dengan <em>that</em>, <em>very few</em> tidak membentuk pola akibat.'}},
  {t:'Contoh soal', ex:{
    q:'One group examined the fossils, while ______ recorded the measurements.',
    o:['other','the other','another','others'],
    a:1,
    w:'Ada dua kelompok yang tertentu; kelompok kedua = sisanya → <b>the other</b>. <em>other</em> butuh nomina jamak, <em>another</em> butuh nomina tunggal, <em>others</em> berarti beberapa yang tak tentu (bukan pasangan dari <em>one group</em>).'}}
]},

{ id:'urutan-inversi', unit:'Fondasi Kalimat', title:'Urutan Kata & Inversi',
  blurb:'Urutan adjektiva, posisi adverb, dan kapan verb pindah ke depan subjek.',
  themes:['structure','written'], match:['urutan kata','inversi','kata tambahan'],
  steps:[
  {t:'Urutan standar', h:`
    <p>Urutan netral: <b>subjek – verb – objek – keterangan cara – tempat – waktu</b>.<br>
    <em>The team presented the findings clearly at the seminar last week.</em></p>
    <p>Urutan adjektiva sebelum nomina: opini – ukuran – usia – bentuk – warna – asal – bahan.<br>
    <em>a remarkable small ancient bronze statue</em></p>
    <p>Adverb frekuensi (<em>always, often, never, rarely</em>) diletakkan sebelum verb utama tapi sesudah <em>be</em>:<br>
    <em>She <b>often</b> works late.</em> · <em>He is <b>always</b> punctual.</em></p>`},
  {t:'Kapan terjadi inversi', h:`
    <p>Verb bantu pindah ke depan subjek kalau kalimat dibuka oleh:</p>
    <ul>
      <li>adverbial negatif: <em><b>Never before had</b> the city seen such flooding.</em> · <em><b>Rarely does</b> he comment.</em></li>
      <li><em>not only</em> di awal: <em><b>Not only did</b> the price fall, but demand also rose.</em></li>
      <li><em>only</em> + keterangan: <em><b>Only after the war did</b> the industry recover.</em></li>
      <li><em>so/such ... that</em> di awal: <em><b>So severe was</b> the drought that crops failed.</em></li>
      <li>conditional tanpa <em>if</em>: <em><b>Had I known</b>, I would have called.</em></li>
      <li>keterangan tempat di awal (verb <em>be</em>/gerak): <em><b>On the hill stands</b> an old chapel.</em></li>
    </ul>`},
  {t:'Contoh soal', ex:{
    q:'Never before ______ such a detailed map of the ocean floor.',
    o:['scientists have produced','have scientists produced','scientists produced','producing scientists'],
    a:1,
    w:'Kalimat dibuka adverbial negatif <em>Never before</em>, jadi wajib inversi: auxiliary <b>have</b> mendahului subjek <em>scientists</em>, lalu participle <em>produced</em>.'}},
  {t:'Contoh soal', ex:{
    q:'______ the results been published earlier, the debate might have ended sooner.',
    o:['If','Had','Have','Having'],
    a:1,
    w:'Ini conditional ketiga yang <em>if</em>-nya dihilangkan, sehingga auxiliary maju ke depan: <b>Had</b> the results been published... Kalau memakai <em>If</em>, bentuknya <em>If the results had been published</em>.'}}
]}

);
