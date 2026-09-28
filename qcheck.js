global.window={};
/* Pemeriksa mutu pengecoh: keseimbangan panjang opsi & pola yang membocorkan kunci. */
const fs=require('fs'),path=require('path');
global.TOEFLDRILL={questions:[],passages:{},sources:{},addBank:function(b){
  const s=b.source||{}; if(s.id)this.sources[s.id]=s;
  Object.assign(this.passages,b.passages||{});
  (b.questions||[]).forEach(q=>{q.sourceId=q.sourceId||s.id;this.questions.push(q);});}};
for(const f of fs.readdirSync('data').filter(x=>x.endsWith('.js')).sort())
  eval(fs.readFileSync(path.join('data',f),'utf8'));
const Q=TOEFLDRILL.questions.filter(q=>q.type!=='open'&&q.options);
let lop=[],longest=0,shortest=0,dup=[],ids=new Set(),dupid=[];
const bySrc={};
for(const q of Q){
  if(ids.has(q.id))dupid.push(q.id); ids.add(q.id);
  const L=q.options.map(o=>o.length), mx=Math.max(...L), mn=Math.min(...L);
  const ans=L[q.answer];
  (bySrc[q.sourceId]=bySrc[q.sourceId]||{n:0,lop:0,long:0,short:0}).n++;
  if(mx>=25 && mx>mn*2.2){ lop.push([q.sourceId,q.id,L.join('/')]); bySrc[q.sourceId].lop++; }
  if(q.options.length>2 && ans===mx && mx>mn*1.6 && mx>=20){ longest++; bySrc[q.sourceId].long++; }
  if(q.options.length>2 && ans===mn && mn*1.6<mx && mx>=20){ shortest++; bySrc[q.sourceId].short++; }
  if(new Set(q.options.map(o=>o.toLowerCase().trim())).size!==q.options.length) dup.push(q.id);
}
console.log('Soal pilihan ganda :',Q.length);
console.log('ID ganda           :',dupid.length, dupid.slice(0,5));
console.log('Opsi kembar        :',dup.length, dup.slice(0,5));
console.log('Set opsi timpang   :',lop.length,'(opsi terpanjang > 2,2x terpendek)');
console.log('Kunci = opsi TERPANJANG :',longest,'   Kunci = opsi TERPENDEK :',shortest,
            '  (kalau salah satu jauh lebih banyak, pengecoh membocorkan kunci)');
console.log('\nper sumber:');
for(const s in bySrc){const b=bySrc[s];
  console.log(`  ${s.padEnd(20)} n=${String(b.n).padStart(4)}  timpang=${String(b.lop).padStart(3)}  kunci-terpanjang=${String(b.long).padStart(3)}  kunci-terpendek=${String(b.short).padStart(3)}`);}
console.log('\ncontoh set timpang:'); lop.slice(0,12).forEach(x=>console.log('  ',x.join(' | ')));
