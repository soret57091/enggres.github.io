/* ============================================================
   Membuat data/topics.js — indeks "soal ini milik topik apa".

   Kenapa perlu: sub-tema di 18 bank tidak seragam. Banyak bank
   memakai label umum ("ITP Structure", "Preview Test: Reading",
   "Multiple Choice", "Review: ...") sehingga soalnya tidak bisa
   dirutekan ke topik materi hanya lewat sub-tema. Indeks ini
   menggolongkan tiap soal dari isinya sendiri — batang soal,
   pilihan, dan pembahasannya — lalu dipakai index.html sebagai
   TAMBAHAN atas pencocokan sub-tema yang sudah ada.

   Jalankan: node _skrip/build_topics.js   (dari folder proyek)
   ============================================================ */
global.window = {};
global.TOEFLDRILL = {questions:[],passages:{},sources:{},addBank:function(b){
  var s=b.source||{}; if(s.id)this.sources[s.id]=s;
  if(b.passages)for(var k in b.passages)this.passages[k]=b.passages[k];
  (b.questions||[]).forEach(q=>{q.sourceId=q.sourceId||s.id;this.questions.push(q);});}};
const fs = require('fs');
fs.readdirSync('data').filter(f=>f.endsWith('.js') && f!=='topics.js').sort()
  .forEach(f=>eval(fs.readFileSync('data/'+f,'utf8')));
const Q = TOEFLDRILL.questions, L = window.TOEFLDRILL_LESSONS || [];

const flat = s => String(s||'').replace(/<[^>]+>/g,' ').replace(/&[a-z]+;/g,' ')
                   .replace(/\s+/g,' ').toLowerCase();

/* ---------- 1. soal bacaan: digolongkan dari batang soalnya ---------- */
function readingTopic(st){
  if(/closest in meaning|best be replaced|paling dekat maknanya|sinonim|synonym/.test(st)) return 'vocab-context';
  if(/\brefers? to\b|merujuk (pada|ke)/.test(st))                                          return 'inference';
  if(/true|false|not given|ya \/ tidak|yes\/no/.test(st))                                  return 'tfng';
  if(/main (idea|topic|subject|purpose)|mainly discuss|primarily concerned|best title|"?judul"?|gagasan utama|paling tepat untuk (bagian|section)|(precede|follow)s? the passage|paragraph .*(precede|follow)/.test(st)) return 'main-idea';
  if(/complete the (summary|notes|sentence|table)|melengkapi|isian|no more than|______/.test(st)) return 'melengkapi';
  if(/can be inferred|it is implied|the author (implies|suggests|mentions)|why does the author|in order to|purpose of|most likely|probably|except|not mentioned|attitude|tone/.test(st)) return 'inference';
  return 'detail-matching';
}

/* ---------- 2. soal tata bahasa: digolongkan dari pembahasannya ---------- */
/* pembahasan seluruh bank berbahasa Indonesia dan hampir selalu menyebut
   kaidah yang diuji, jadi itulah penanda yang paling dapat diandalkan.   */
const G = [
 ['inti-kalimat',   /verb utama|kehilangan (subjek|predikat)|tidak punya (subjek|verb)|belum punya (subjek|verb)|dua verb|butuh subjek|tanpa induk|klausa tanpa induk|kalimat ini tidak punya/],
 ['sv-agreement',   /kesesuaian subjek|subject[- ]verb|subjeknya\b[^.]{0,45}(tunggal|jamak)|verb-?nya (harus|seharusnya)|menyesuaikan diri dengan subjek|verb (tunggal|jamak)|subjek (tunggal|jamak)|selalu tunggal, jadi verb/],
 ['pb-agree-prep',  /frasa preposisi[^.]{0,70}(subjek|verb|penyela|ditutup)|hanya (frasa|keterangan) penyela|penyela\b/],
 ['pb-agree-quant', /ungkapan kuantitas|sesudah\s+of\s+ada|(all|most|half|some|none) of the [a-z]+\b[^.]{0,30}(tunggal|jamak|uncountable)/],
 ['pb-agree-certain',/\b(each|every|everybody|everyone|everything|somebody|someone|nobody|no one|anybody|anyone|nothing)\b[^.]{0,55}(tunggal|singular)|selalu tunggal/],
 ['klausa',         /klausa (adjektiva|keterangan|nomina|induk)|noun clause|adjective clause|adverb clause|connector|penghubung|konjungsi|relative pronoun|dua klausa/],
 ['pb-coordinate',  /coordinate connector|koma sebelum coordinate|penghubung setara|dua klausa lengkap[^.]{0,60}(koma|penghubung|and|but|or|so|yet)|butuh (penghubung|konjungsi)|tanpa penghubung/],
 ['pb-adverb-clause',/adverb clause|klausa keterangan|\b(because|although|while|since|unless|whether|when|before|after|though|whereas)\b[^.]{0,50}(klausa|connector|koma)/],
 ['pb-noun-clause', /noun clause|klausa nomina|menjadi (subjek|objek) dari (verb|kalimat)|objek (dari )?preposisi/],
 ['pb-adj-clause',  /adjective clause|klausa adjektiva|\b(who|whom|which|that|whose)\b[^.]{0,50}(menerangkan|klausa|connector)/],
 ['paralelisme',    /paralel|sebentuk|rangkaian paralel|korelatif|\bboth\b[^.]{0,25}\band\b|\beither\b[^.]{0,25}\bor\b|\bneither\b[^.]{0,25}\bnor\b|not only[^.]{0,25}but also/],
 ['pb-parallel-coord',/rangkaian paralel|(kiri|kanan)[^.]{0,40}\b(and|but|or)\b|paralel[^.]{0,45}\b(and|but|or)\b|samakan:/],
 ['pb-parallel-paired',/pasangan(nya)? (konjungsi|tepat|salah|itu)|\bboth\b[^.]{0,25}\band\b|\beither\b[^.]{0,25}\bor\b|\bneither\b[^.]{0,25}\bnor\b|not only[^.]{0,25}but also|korelatif/],
 ['preposisi',      /preposisi(nya)? (keliru|tepat|yang benar)|kolokasi|ungkapannya\b|preposition|setelah preposisi|sesudah preposisi/],
 ['bentuk-kata',    /(harus|seharusnya|butuh|dibutuhkan|wajib)[^.]{0,45}(adverb|adjective|kata sifat|kata keterangan)|menerangkan kata benda|penerang(nya)? (harus|wajib)|keluarga kata|bentuk kata/],
 ['pb-adj-adv',     /(harus|seharusnya|butuh|dibutuhkan|wajib)[^.]{0,45}(adverb|adjective|kata sifat|kata keterangan)|menerangkan (kata benda|kata kerja|kata sifat|verb)|adverb yang menerangkan|adjective yang menerangkan/],
 ['verb-gerund',    /participle|gerund|infinitive|bentuk dasar|verb bantu|\bmodal\b/],
 ['pb-participle',  /participle|aktif[^.]{0,25}pasif|pasif[^.]{0,25}participle|kalimatnya (aktif|pasif)/],
 ['pb-pp-have',     /sesudah\s+(have|has|had|having|should have|will have|would have)\b|(have|has|had|having)\s+(wajib|harus)[^.]{0,30}past participle|past participle[^.]{0,45}\bhave\b/],
 ['pb-participle-be',/sesudah\s+(be|is|are|was|were|been|being)\b|kalimatnya pasif|kalimat(nya)? aktif|bentuknya pasif/],
 ['pb-modal-base',  /\bmodal\b|bentuk dasar (verb|kata kerja)?|sesudah\s+(can|could|may|might|shall|should|will|would|must)\b/],
 ['kata-rancu',     /countable|uncountable|terhitung|\b(many|much|few|little|fewer|less)\b|\banother\b|\bother\b|\bdo\b \/ \bmake\b|so \/ such/],
 ['pb-countable',   /countable|uncountable|(bisa|tak|tidak) (di)?hitung|terhitung|\b(many|much|few|little|fewer|less|amount of|number of)\b/],
 ['pb-noun-jamak',  /kata benda (tunggal|jamak)|bentuk jamak|menuntut (bentuk )?jamak|menuntut (kata benda )?tunggal|jamak tak beraturan|artikel\s+an?\b/],
 ['pb-pronoun-so',  /object pronoun|subject pronoun|kata ganti (objek|subjek|orang)|pronoun/],
 ['pb-possessive',  /possessive|kepemilikan|\bits\b[^.]{0,35}apostrof|\btheir\b[^.]{0,25}\btheirs\b|bentuk possessive/],
 ['urutan-inversi', /inversi|urutan kata|terbalik|memaksa inversi|kalimat tanya[^.]{0,35}tidak boleh/],
];

const idx = {};
L.forEach(l => idx[l.id] = []);
const themesOf = id => (L.find(l=>l.id===id)||{}).themes || [];

let nR = 0, nG = 0;
Q.forEach(q => {
  const st = flat(q.question), ex = flat(q.explain), sub = flat(q.subtheme);
  const hay = sub + ' ' + st + ' ' + flat((q.options||[]).join(' ')) + ' ' + ex;

  if (q.theme === 'reading' || q.theme === 'vocabulary') {
    let t = readingTopic(st);
    /* soal bertema reading yang batangnya berbunyi seperti soal kosakata tetap
       harus punya rumah — kalau temanya tidak cocok, jatuhkan ke topik umum. */
    if (!idx[t] || themesOf(t).indexOf(q.theme) < 0) t = 'detail-matching';
    if (idx[t] && themesOf(t).indexOf(q.theme) >= 0) { idx[t].push(q.id); nR++; }
  }
  if (q.theme === 'structure' || q.theme === 'written') {
    G.forEach(([id, re]) => {
      if (!idx[id]) return;
      if (themesOf(id).indexOf(q.theme) < 0) return;
      /* diuji pada PEMBAHASAN + sub-tema saja. Batang soal sengaja tidak
         dipakai: kata seperti "a number of" atau "little" sering muncul di
         kalimatnya tanpa ada hubungannya dengan kaidah yang diuji. */
      if (re.test(ex) || re.test(sub)) { idx[id].push(q.id); nG++; }
    });
  }
});

/* buang yang sudah tertangkap sub-tema supaya berkasnya ramping */
L.forEach(l => {
  const m = (l.match||[]).map(s=>s.toLowerCase());
  const byMatch = new Set(Q.filter(q =>
      (l.themes||[]).indexOf(q.theme) >= 0 &&
      (!m.length || m.some(x => flat(q.subtheme).indexOf(x) >= 0))
    ).map(q=>q.id));
  idx[l.id] = [...new Set(idx[l.id])].filter(id => !byMatch.has(id));
});

const out = '/* dibuat oleh _skrip/build_topics.js — jangan diedit tangan.\n'
  + '   Indeks tambahan: id pelajaran -> daftar id soal setopik yang\n'
  + '   TIDAK tertangkap oleh pencocokan sub-tema di berkas lessons-*.js. */\n'
  + 'window.TOEFLDRILL_TOPICS = ' + JSON.stringify(idx) + ';\n';
fs.writeFileSync('data/topics.js', out);

console.log('penggolongan bacaan :', nR, '| penggolongan tata bahasa :', nG);
console.log('data/topics.js ditulis,', (out.length/1024).toFixed(0), 'KB\n');
L.forEach(l => {
  const m = (l.match||[]).map(s=>s.toLowerCase());
  const a = Q.filter(q => (l.themes||[]).indexOf(q.theme)>=0 &&
              (!m.length || m.some(x=>flat(q.subtheme).indexOf(x)>=0))).length;
  console.log(String(a).padStart(4), '+', String(idx[l.id].length).padStart(4),
              '=', String(a+idx[l.id].length).padStart(4), '|', l.unit, '|', l.title);
});
