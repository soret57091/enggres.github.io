/* Perbaikan hasil audit untuk bank-09, bank-10, bank-11. */
const fs=require('fs'), path=require('path');
const DIR=__dirname+'/data';
const FILES=['bank-09-petersons-inline.js','bank-10-barron-completion.js','bank-11-barron-isian.js'];

/* --- 1. ganti opsi yang ternyata ikut benar --- */
const OPT_SWAP={
 'pi-183-4' :{'simplest':'simplify'},
 'pi-183-6b':{'simpler':'simplify'},
 'pi-183-9' :{'closer':'closing'},
 'pi-183-10':{'easier':'easiness'},
 'pi-193-1' :{'the other':'the others'},
 'pi-193-2' :{'the other':'the others'},
 'pi-194-6' :{'much':'a few'},
 'pi-195-6' :{'early':'soon'},
 'pi-195-12':{'lively':'liven'},
 'pi-251-3-2':{'for':'of'},
};
/* subject-verb agreement: 'to be' terlalu jelas salah → ganti bentuk perfect */
const SVA={'pi-201-1':'have been','pi-201-2':'have been','pi-201-3':'has been',
           'pi-201-4':'have been','pi-201-6':'has been','pi-201-7':'has been',
           'pi-201-8':'have been','pi-201-10':'has been','pi-201-11':'have been'};

/* --- 2. buang opsi yang juga benar menurut bacaan --- */
const OPT_DROP={'brx-ac6-30':['Paragraf D'],'brx-ac6-31':['Paragraf D']};

/* --- 3. label kano A/B/C diganti nama yang jelas (dipastikan dari bacaan) --- */
const KANO={'Kano A':'Kano kulit kayu (frame-and-bark canoe)',
            'Kano B':'Kano batang pohon (dugout)',
            'Kano C':'Kano papan (plank canoe / tomol)'};

/* --- 4. pembahasan True/False/Not Given yang berisi bukti --- */
const EXPL={
 'brx-ac4-14':"Bacaan: <i>“Native to the <b>Amazon and Orinoco River basins</b>…”</i> — bukan kawasan Teluk Meksiko. Kunci: <b>False</b>.",
 'brx-ac4-15':"Bacaan: <i>“it requires a <b>humid climate and regular rainfall</b>.”</i> Kunci: <b>True</b>.",
 'brx-ac4-16':"Bacaan: <i>“A mature tree may have as many as 6,000 flowers but will only produce about <b>twenty pods</b>.”</i> Dua puluh pod itu hasil satu <i>pohon</i>, bukan satu bunga. Kunci: <b>False</b>.",
 'brx-ac4-17':"Bacaan: <i>“the first cacao-based drink was probably produced by fermenting <b>the pulp</b> in the cacao pods to yield a beerlike beverage.”</i> Kunci: <b>True</b>.",
 'brx-ac4-18':"Bacaan hanya menyebut temuan bejana tembikar di Puerto Escondido berumur sekitar 3.100 tahun; <b>suhu minumannya tidak pernah disinggung</b>. Kunci: <b>Not Given</b>.",
 'bri-gt2-7':"Teks: <i>“Also available on the website is a variety of <b>international bread recipes</b>.”</i>",
};

/* --- 5. perbaikan pertanyaan --- */
const Q_FIX={
 'bri-gt1-36':"Double-hulled canoes were made by connecting two dugout canoes with ______.",
};

/* --- 6. bersihkan bacaan --- */
const PCUT=[
 /\s*WRITING TASK\s*1[\s\S]*$/i, /\s*WRITING TASK\s*2[\s\S]*$/i,
 /\s*You should spend about 40 minutes on this task[\s\S]*$/i,
 /\s*Practice Test \d\s+Candidate Name[\s\S]*$/i,
 /\s*INTERNATIONAL ENGLISH LANGUAGE[\s\S]*$/i,
 /\s*Questions?\s*\d[\d ]*[-‐-―−]\s*\d[\d ]*\s*(?:Which|Choose|Complete|Do the following|Answer the)[\s\S]*$/i,
 /\s*Which of the following are facts[\s\S]*$/i,
 /\s*SECTION\s*\d\s+QUESTIONS?\s*\d[\s\S]*$/i,
];
const FOOT=[[/\btraveling1\b/g,'traveling'],[/\bOrganize1\b/g,'Organize'],[/\bCategorize2\b/g,'Categorize'],
  [/\bModernization1\b/g,'Modernization'],[/\bskillful1\b/g,'skillful'],[/\bcolors1\b/g,'colors'],
  [/\bfall1\b/g,'fall'],[/\bPaleolithic1\b/g,'Paleolithic'],[/\bfossilized2\b/g,'fossilized'],
  [/\bArcheologists1\b/g,'Archeologists'],[/\btravel(l?)ed1\b/g,'travel$1ed'],
  [/\bcolors2\b/g,'colors'],[/\bfavorable2\b/g,'favorable'],[/\bsustainable 1\b/g,'sustainable'],
  [/\s*\d?British: ?\w+\s*/g,' ']];
const foot=s=>{FOOT.forEach(([a,b])=>s=s.replace(a,b));return s.replace(/\s{2,}/g,' ').trim();};

const jss=x=>JSON.stringify(x);
let rep={opt:0,drop:0,kano:0,expl:0,q:0,pass:0,ref:0,foot:0};
for(const f of FILES){
  const raw=fs.readFileSync(path.join(DIR,f),'utf8');
  const header=(raw.match(/^\/\*[\s\S]*?\*\//)||[''])[0];
  let bank=null; global.TOEFLDRILL={addBank:b=>{bank=b;}}; eval(raw);
  const P=bank.passages||{};
  for(const k in P){
    let t=foot(P[k].text);
    for(const re of PCUT){const m=t.match(re); if(m&&m.index>600){t=t.slice(0,m.index); rep.pass++;}}
    P[k].text=t.trim();
  }
  const out=[];
  for(const q of bank.questions){
    if(q.ref){const b=q.ref; q.ref=q.ref.replace(/^(Peterson’s TOEFL — )(?:Peterson’s TOEFL — )+/,'$1'); if(q.ref!==b)rep.ref++;}
    if(OPT_SWAP[q.id]){const m=OPT_SWAP[q.id];
      q.options=q.options.map(o=>{if(m[o]!==undefined){rep.opt++; return m[o];} return o;});}
    if(SVA[q.id]){const i=q.options.indexOf('to be');
      if(i>=0 && !q.options.includes(SVA[q.id])){q.options[i]=SVA[q.id]; rep.opt++;}}
    if(OPT_DROP[q.id]){const cor=q.options[q.answer];
      q.options=q.options.filter(o=>!OPT_DROP[q.id].includes(o));
      q.answer=q.options.indexOf(cor); rep.drop++;}
    if(q.id.startsWith('brx-gt1-')&&q.options.some(o=>KANO[o])){
      const cor=q.options[q.answer];
      q.options=q.options.map(o=>KANO[o]||o); q.answer=q.options.indexOf(KANO[cor]||cor);
      q.instruction="Jenis kano mana yang cocok dengan keterangan berikut?"; rep.kano++;}
    if(EXPL[q.id]){q.explain=EXPL[q.id]; rep.expl++;}
    if(Q_FIX[q.id]){q.question=Q_FIX[q.id]; rep.q++;}
    q.options=q.options.map(o=>{const n=foot(o); if(n!==o)rep.foot++; return n;});
    q.question=foot(q.question); q.explain=foot(q.explain);
    if(new Set(q.options).size!==q.options.length||q.answer<0) {console.log('DIBUANG',q.id);continue;}
    out.push(q);
  }
  const lines=[header,'TOEFLDRILL.addBank({','source: '+jss(bank.source)+','];
  if(Object.keys(P).length){lines.push('passages: {');
    for(const k in P) lines.push(jss(k)+': { title:'+jss(P[k].title)+', text:'+jss(P[k].text)+' },');
    lines.push('},');}
  lines.push('questions: [');
  for(const q of out){
    const p=['id:'+jss(q.id),'theme:'+jss(q.theme),'subtheme:'+jss(q.subtheme),'ref:'+jss(q.ref)];
    if(q.passageId)p.push('passageId:'+jss(q.passageId));
    p.push('\n instruction:'+jss(q.instruction),'\n question:'+jss(q.question),
           '\n options:'+jss(q.options)+', answer:'+q.answer,'\n explain:'+jss(q.explain));
    lines.push('{'+p.join(', ')+'},');
  }
  lines.push(']\n});');
  fs.writeFileSync(path.join(DIR,f),lines.join('\n')+'\n');
  console.log(f,'->',out.length,'soal');
}
console.log(rep);
