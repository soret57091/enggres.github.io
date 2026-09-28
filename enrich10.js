/* Melengkapi pembahasan bank-10 yang masih berbunyi "Kunci buku: X"
   dengan kutipan pendukung dari bacaannya sendiri. */
const fs=require('fs'), path=require('path');
const DIR=__dirname+'/data';
const FILES=fs.readdirSync(DIR).filter(x=>x.endsWith('.js')).sort();

/* muat seluruh korpus dulu supaya bacaan dari bank lain ikut terbaca */
const ALLP={};
for(const f of FILES){ let b=null; global.TOEFLDRILL={addBank:x=>{b=x}};
  eval(fs.readFileSync(path.join(DIR,f),'utf8')); Object.assign(ALLP,b.passages||{}); }

const STOP=new Set(('a an the of to in on at for and or but is are was were be been being that this these those '+
 'with by from as it its they them their he she his her which who what when where how why not no yes '+
 'di ke dari yang pada dan atau untuk bagian mana keterangan berikut disebutkan judul paling tepat adalah').split(' '));
const words=s=>(s.toLowerCase().match(/[a-z']{3,}/g)||[]).filter(w=>!STOP.has(w));

function paras(text){
  /* {huruf: teks} — mengenali penanda paragraf "\nA\n" maupun " A " di tengah kalimat */
  const out={};
  let m, re=/(?:^|\n|\.\s|\s)\s*([A-H])\s*(?:\n|\s)(?=[A-Z(])/g, marks=[];
  while((m=re.exec(text))!==null) marks.push([m.index+m[0].indexOf(m[1]), m[1], re.lastIndex]);
  /* hanya rantai berurutan mulai A */
  const chain=[]; let want='A';
  for(const mk of marks){ if(mk[1]===want){ chain.push(mk); want=String.fromCharCode(want.charCodeAt(0)+1); } }
  for(let i=0;i<chain.length;i++){
    const end = i+1<chain.length ? chain[i+1][0] : text.length;
    out[chain[i][1]] = text.slice(chain[i][2], end).replace(/\s+/g,' ').trim();
  }
  return out;
}
const sentences=t=>t.replace(/\s+/g,' ').split(/(?<=[.!?])\s+(?=[A-Z“"(])/).filter(s=>s.length>25);

function best(text, probe){
  const pw=words(probe); if(!pw.length) return null;
  let bs=null, bsc=0;
  for(const s of sentences(text)){
    const sw=new Set(words(s));
    let sc=0; for(const w of pw) if(sw.has(w)) sc++;
    const norm=sc/Math.sqrt(s.length/60);
    if(sc>=2 && norm>bsc){ bsc=norm; bs=s; }
  }
  return bs;
}
const clip=(s,n=230)=>{ s=s.replace(/\s+/g,' ').trim(); if(s.length<=n) return s;
  const c=s.lastIndexOf(' ',n); return s.slice(0,c>60?c:n)+'…'; };
const esc=s=>s.replace(/</g,'&lt;').replace(/>/g,'&gt;');

let done=0, skip=0;
for(const f of FILES){
  if(!/bank-(10|12)/.test(f)) continue;
  let bank=null; global.TOEFLDRILL={addBank:x=>{bank=x}};
  const raw=fs.readFileSync(path.join(DIR,f),'utf8');
  const header=(raw.match(/^\/\*[\s\S]*?\*\//)||[''])[0];
  eval(raw);
  const P=Object.assign({}, ALLP, bank.passages||{});
  for(const q of bank.questions){
    if(/Bagian bacaan yang mendukung|Bacaan: <i>|Teks: <i>/.test(q.explain)) continue;
    const src=(P[q.passageId]||{}).text||''; if(!src){ skip++; continue; }
    const cor=q.options[q.answer];
    let quote=null;
    const mp=cor.match(/^(?:Paragraf|Bagian)\s+([A-H])$/);
    const ms=q.question.match(/<b>(?:Section|Paragraph)\s+([A-H])<\/b>/);
    if(mp||ms){
      const pp=paras(src), L=(mp?mp[1]:ms[1]);
      if(pp[L]) quote=clip(pp[L],250);
    }
    if(!quote){
      const generic=/Which of the following|Which car rental|Which opportunity/.test(q.question);
      const probe = generic ? (cor+' '+cor) : (q.question.replace(/<[^>]+>/g,' ')+' '+cor);
      quote=best(src,probe); if(quote) quote=clip(quote);
    }
    if(!quote){ skip++; continue; }
    if(/Judul yang paling tepat untuk <b>(?:Section|Paragraph)/.test(q.question) && !/pada bacaan/.test(q.question)){
      const title=(src.split(/\n|\.\s/)[0]||'').replace(/\s+/g,' ').trim().slice(0,45);
      if(title && title.length>6 && /^[A-Z]/.test(title))
        q.question=q.question.replace(/ adalah …$/,' pada bacaan <i>'+esc(title)+'</i> adalah …');
    }
    q.explain=q.explain.replace(/\.?$/,'.')+' Bagian bacaan yang mendukung: <i>“'+esc(quote)+'”</i>';
    done++;
  }
  const jss=x=>JSON.stringify(x);
  const out=[header,'TOEFLDRILL.addBank({','source: '+jss(bank.source)+','];
  if(bank.passages&&Object.keys(bank.passages).length){ out.push('passages: {');
    for(const k in bank.passages) out.push(jss(k)+': { title:'+jss(bank.passages[k].title)+', text:'+jss(bank.passages[k].text)+' },');
    out.push('},'); }
  out.push('questions: [');
  for(const q of bank.questions){
    const p=['id:'+jss(q.id),'theme:'+jss(q.theme),'subtheme:'+jss(q.subtheme),'ref:'+jss(q.ref)];
    if(q.passageId)p.push('passageId:'+jss(q.passageId));
    p.push('\n instruction:'+jss(q.instruction),'\n question:'+jss(q.question),
           '\n options:'+jss(q.options)+', answer:'+q.answer,'\n explain:'+jss(q.explain));
    out.push('{'+p.join(', ')+'},');
  }
  out.push(']\n});');
  fs.writeFileSync(path.join(DIR,f),out.join('\n')+'\n');
}
console.log('pembahasan diperkaya:',done,'| tidak ketemu kutipan:',skip);
