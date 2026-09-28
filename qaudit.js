/* Pemeriksa kutipan pembahasan: potongan yang dikutip harus benar-benar ada
   di dalam bacaan/naskah yang dirujuk soal.  Jalankan: node qaudit.js  */
global.window = {};
global.TOEFLDRILL = {questions:[],passages:{},sources:{},addBank:function(b){
  var s=b.source||{}; if(s.id)this.sources[s.id]=s;
  if(b.passages)for(var k in b.passages)this.passages[k]=b.passages[k];
  (b.questions||[]).forEach(q=>{q.sourceId=q.sourceId||s.id;this.questions.push(q);});}};
const fs=require('fs');
fs.readdirSync('data').filter(f=>f.endsWith('.js')).sort().forEach(f=>eval(fs.readFileSync('data/'+f,'utf8')));
const Q=TOEFLDRILL.questions, P=TOEFLDRILL.passages;
const norm = s => String(s).replace(/<[^>]+>/g,'').replace(/&[a-z]+;/g,' ')
                 .replace(/[‘’]/g,"'").replace(/[“”]/g,'"')
                 .replace(/\s+/g,' ').trim().toLowerCase();
let cek=0, gagal=0, tanpa=0;
const contoh=[];
Q.forEach(q=>{
  const m = /(?:Kutipan pendukung[^:]*:|Bagian naskah yang mendukung:)\s*[“"]([^”"]{15,})[”"]/.exec(q.explain||'');
  if(!m){ if(q.passageId) tanpa++; return; }
  if(!q.passageId){ return; }
  cek++;
  let kut = norm(m[1]).replace(/…$/,'').trim();
  const teks = norm((P[q.passageId]||{}).text||'');
  const potong = kut.length>60 ? kut.slice(0,60) : kut;
  if(teks.indexOf(potong)<0){ gagal++; if(contoh.length<12) contoh.push([q.id,potong.slice(0,70)]); }
});
console.log('soal berkutipan :',cek);
console.log('kutipan tak cocok:',gagal);
console.log('soal berbacaan tanpa kutipan:',tanpa);
contoh.forEach(c=>console.log('   ✗',c[0],'|',c[1]));

/* kunci vs pembahasan: pembahasan harus menyebut huruf kuncinya */
let beda=0; const bd=[];
Q.forEach(q=>{
  if(q.type==='open'||typeof q.answer!=='number') return;
  const m=/<b>([A-D])\.\s/.exec(q.explain||'');
  if(m && 'ABCD'.indexOf(m[1])!==q.answer){ beda++; if(bd.length<10) bd.push(q.id+' kunci='+'ABCD'[q.answer]+' pembahasan='+m[1]); }
});
console.log('\npembahasan menyebut huruf lain dari kuncinya:',beda);
bd.forEach(x=>console.log('   ✗',x));

/* bacaan yatim & soal tanpa bacaan yang seharusnya punya */
const dipakai={}; Q.forEach(q=>{ if(q.passageId) dipakai[q.passageId]=1; });
const yatim=Object.keys(P).filter(k=>!dipakai[k]);
console.log('\nbacaan tak terpakai:',yatim.length, yatim.slice(0,8));
