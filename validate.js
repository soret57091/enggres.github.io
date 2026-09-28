/* Validator bank soal + materi — jalankan: node validate.js  (dari folder ini) */
global.window={};
global.TOEFLDRILL={questions:[],passages:{},sources:{},addBank:function(b){
  var s=b.source||{}; if(s.id)this.sources[s.id]=s;
  if(b.passages)for(var k in b.passages)this.passages[k]=b.passages[k];
  (b.questions||[]).forEach(q=>{q.sourceId=q.sourceId||s.id;this.questions.push(q);});}};
const fs=require('fs');
fs.readdirSync('data').filter(f=>f.endsWith('.js')).sort().forEach(f=>{
  try{ eval(fs.readFileSync('data/'+f,'utf8')); }
  catch(e){ console.log('SYNTAX ERROR di',f,':',e.message); process.exit(1); }});
const Q=TOEFLDRILL.questions, ids={}; var bad=0;
const err=(m,id)=>{console.log('  ✗',m,id);bad++;};
Q.forEach(q=>{
  if(ids[q.id]) err('id ganda',q.id); ids[q.id]=1;
  if(!q.explain) err('tanpa pembahasan',q.id);
  if(q.passageId&&!TOEFLDRILL.passages[q.passageId]) err('bacaan hilang',q.id);
  if(q.type==='open'){ if(q.options) err('open tapi ada options',q.id); return; }
  if(!q.options||q.options.length<2) return err('opsi kurang',q.id);
  if(typeof q.answer!=='number'||q.answer<0||q.answer>=q.options.length) err('kunci invalid',q.id);
  if(new Set(q.options).size!==q.options.length) err('opsi kembar',q.id);
});
const byT={},byS={},dist={};
Q.forEach(q=>{ byT[q.theme]=(byT[q.theme]||0)+1; byS[q.sourceId]=(byS[q.sourceId]||0)+1;
  if(q.type!=='open'){ dist[q.sourceId]=dist[q.sourceId]||{};
    const L='ABCD'[q.answer]; dist[q.sourceId][L]=(dist[q.sourceId][L]||0)+1; }});
console.log('TOTAL SOAL :',Q.length,' (terbuka:',Q.filter(q=>q.type==='open').length+')');
console.log('Per tema   :',JSON.stringify(byT));
console.log('Per sumber :',JSON.stringify(byS));
console.log('Bacaan     :',Object.keys(TOEFLDRILL.passages).length);
console.log('Sebaran kunci per sumber (harus relatif merata):');
for(const s in dist) console.log('  ',s,JSON.stringify(dist[s]));

/* ---------- materi belajar ---------- */
const LS = global.window.TOEFLDRILL_LESSONS || [];
if(LS.length){
  const lid={}; let lbad=0;
  const lerr=(m,id)=>{console.log('  ✗',m,id);lbad++;};
  LS.forEach(l=>{
    if(lid[l.id]) lerr('id pelajaran ganda',l.id); lid[l.id]=1;
    if(!l.unit||!l.title||!l.blurb) lerr('metadata pelajaran kurang',l.id);
    if(!l.steps||!l.steps.length) return lerr('pelajaran tanpa bagian',l.id);
    l.steps.forEach((st,i)=>{
      if(st.ex){
        const e=st.ex;
        if(!e.q||!e.o||!e.w) lerr('contoh soal tidak lengkap di bagian '+(i+1),l.id);
        else if(typeof e.a!=='number'||e.a<0||e.a>=e.o.length) lerr('kunci contoh soal invalid di bagian '+(i+1),l.id);
        else if(new Set(e.o).size!==e.o.length) lerr('opsi contoh soal kembar di bagian '+(i+1),l.id);
      } else if(!st.h) lerr('bagian tanpa isi: '+(i+1),l.id);
      if(!st.t) lerr('bagian tanpa judul: '+(i+1),l.id);
    });
  });
  const units={}; LS.forEach(l=>{units[l.unit]=(units[l.unit]||0)+1});
  console.log('\nMATERI     :',LS.length,'pelajaran');
  console.log('Per unit   :',JSON.stringify(units));
  console.log(lbad? 'MASALAH MATERI: '+lbad : 'MASALAH MATERI: 0 — bersih.');
  bad+=lbad;

  /* indeks topik (data/topics.js) */
  const TI = global.window.TOEFLDRILL_TOPICS;
  if(TI){
    const qid={}; Q.forEach(q=>qid[q.id]=q);
    const lid={}; LS.forEach(l=>lid[l.id]=l);
    let tbad=0, tot=0;
    for(const k in TI){
      if(!lid[k]){ console.log('  ✗ indeks topik menunjuk pelajaran yang tidak ada:',k); tbad++; continue; }
      const seen={};
      TI[k].forEach(id=>{
        tot++;
        if(!qid[id]){ console.log('  ✗ indeks topik menunjuk soal yang tidak ada:',k,id); tbad++; return; }
        if(seen[id]){ console.log('  ✗ id soal ganda dalam indeks topik:',k,id); tbad++; }
        seen[id]=1;
        if((lid[k].themes||[]).indexOf(qid[id].theme)<0){
          console.log('  ✗ tema soal tidak cocok dengan pelajarannya:',k,id,qid[id].theme); tbad++; }
      });
    }
    /* tiap pelajaran harus punya kolam latihan yang layak */
    LS.forEach(l=>{
      const m=(l.match||[]).map(s=>s.toLowerCase());
      const set={}; (TI[l.id]||[]).forEach(id=>set[id]=1);
      const n=Q.filter(q=> set[q.id] || ((l.themes||[]).indexOf(q.theme)>=0 &&
              (!m.length || m.some(x=>String(q.subtheme||'').toLowerCase().indexOf(x)>=0)))).length;
      if(n<10){ console.log('  ✗ kolam latihan terlalu kecil (<10):',l.id,n); tbad++; }
    });
    console.log('INDEKS TOPIK:',tot,'rujukan soal untuk',Object.keys(TI).length,'pelajaran');
    console.log(tbad? 'MASALAH INDEKS: '+tbad : 'MASALAH INDEKS: 0 — bersih.');
    bad+=tbad;
  }
}

console.log(bad? '\nMASALAH TOTAL: '+bad : '\nMASALAH TOTAL: 0 — bersih.');
