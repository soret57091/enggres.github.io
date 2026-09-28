/* Menyambung kata yang terpecah oleh OCR ("cam ouflage" -> "camouflage").
   Aman: hanya disambung bila (a) bentuk gabungannya memang muncul sebagai satu
   kata di tempat lain dalam korpus, dan (b) salah satu penggalannya bukan kata
   Inggris yang berdiri sendiri. */
const fs=require('fs'), path=require('path');
const DIR=__dirname+'/data';
const files=fs.readdirSync(DIR).filter(x=>x.endsWith('.js')).sort();

let banks=[];
for(const f of files){
  let bank=null; global.TOEFLDRILL={addBank:b=>{bank=b;}};
  eval(fs.readFileSync(path.join(DIR,f),'utf8'));
  banks.push({f,bank});
}
/* kosakata: semua kata utuh di seluruh korpus */
const vocab=new Map();
const eat=s=>{ (String(s||'').toLowerCase().match(/[a-z]+/g)||[]).forEach(w=>vocab.set(w,(vocab.get(w)||0)+1)); };
for(const {bank} of banks){
  for(const k in (bank.passages||{})) eat(bank.passages[k].text);
  for(const q of bank.questions||[]){ eat(q.question); (q.options||[]).forEach(eat); }
}
const isWord=w=>(vocab.get(w)||0)>=3;

let joined=0, samples=[];
function fix(text){
  const s=String(text||'');
  const parts=s.split(/(\s+)/);            // pertahankan spasi asli
  for(let i=0;i+2<parts.length;i+=2){
    const a=parts[i], b=parts[i+2];
    if(!a||!b||!/\s/.test(parts[i+1]||'')) continue;
    const ma=a.match(/^(.*?)([A-Za-z]{2,})$/), mb=b.match(/^([a-z]{2,})(.*)$/);
    if(!ma||!mb) continue;
    const la=ma[2].toLowerCase(), lb=mb[1], j=la+lb;
    if(j.length<6) continue;
    if((vocab.get(j)||0)<2) continue;
    if(isWord(la)&&isWord(lb)) continue;
    joined++; if(samples.length<200) samples.push(ma[2]+' '+mb[1]+' -> '+ma[2]+mb[1]);
    parts[i]=ma[1]+ma[2]+mb[1]+mb[2]; parts[i+1]=''; parts[i+2]='';
  }
  return parts.join('').replace(/[ \t]{2,}/g,' ');
}
for(const {f,bank} of banks){
  const P=bank.passages||{};
  for(const k in P) P[k].text=fix(P[k].text);
  const jss=x=>JSON.stringify(x);
  const raw=fs.readFileSync(path.join(DIR,f),'utf8');
  const header=(raw.match(/^\/\*[\s\S]*?\*\//)||[''])[0];
  const out=[header,'TOEFLDRILL.addBank({','source: '+jss(bank.source)+','];
  if(Object.keys(P).length){out.push('passages: {');
    for(const k in P) out.push(jss(k)+': { title:'+jss(P[k].title)+', text:'+jss(P[k].text)+' },');
    out.push('},');}
  out.push('questions: [');
  for(const q of bank.questions||[]){
    const p=['id:'+jss(q.id),'theme:'+jss(q.theme)];
    if(q.subtheme)p.push('subtheme:'+jss(q.subtheme));
    if(q.ref)p.push('ref:'+jss(q.ref));
    if(q.type)p.push('type:'+jss(q.type));
    if(q.passageId)p.push('passageId:'+jss(q.passageId));
    if(q.instruction)p.push('\n instruction:'+jss(q.instruction));
    p.push('\n question:'+jss(q.question));
    if(q.options)p.push('\n options:'+jss(q.options)+', answer:'+q.answer);
    p.push('\n explain:'+jss(q.explain));
    out.push('{'+p.join(', ')+'},');
  }
  out.push(']\n});');
  fs.writeFileSync(path.join(DIR,f),out.join('\n')+'\n');
}
console.log('kata tersambung:',joined);
console.log(samples.join('\n'));
