/* Perbaikan bank-12 berdasarkan audit: satu pengecoh yang ikut benar,
   satu kunci yang bocor lewat batang soal tetangga, dan 17 kutipan pembahasan
   yang salah ambil (semua kutipan pengganti sudah dicocokkan ke teks bacaan). */
const fs=require('fs'), path=require('path');
const DIR=__dirname+'/data';

/* ---- kutipan pendukung yang benar ---- */
const QUOTE={
 'brz-ac2-31':"…adopted the idea that small changes on Earth occurred over a large expanse of time.",
 'brz-ac2-32':"The term deep time was used to describe the span in which gradual geological processes occurred, especially the formation of sedimentary rock.",
 'brz-ac3-15':"In America, dime novels typically centered on tales of the American Revolution and the Wild West, while British penny bloods (later called penny dreadfuls) told serial tales of horror or fictionalized versions of true crimes.",
 'brz-ac4-30':"Because New Caledonian crows are highly social and because tool design varies from area to area, most researchers assume the birds' tool use is cultural; that is, the tool use is learned from other crows.",
 'brz-ac4-31':"When Abel flew away with the hooked wire, Betty bent the straight wire and successfully lifted the bucket of food with her hook.",
 'brz-ac4-32':"A New Caledonian crow that had been captured in 2000 as a juvenile had invented a new tool from materials not found in her natural habitat without observing the behavior in other crows.",
 'brz-gt5-23':"Not having to deal with traffic, bus schedules, or other logistics of travel also saves the telecommuter a good deal of unnecessary stress.",
 'brz-gt5-24':"As a result, the telecommuter can approach work with more energy and more positive feelings.",
 'brz-gt5-26':"Another issue many telecommuters face is the distractions of home life. It can be hard to concentrate on work when family members are demanding attention.",
 'brz-gt5-27':"…some telecommuters find that spending their workday at home results in higher costs for electricity and heating.",
 'brz-gt6-3' :"Special prices for National Car Club members — 10 percent off our usual low prices!",
 'brz-gt6-4' :"Two convenient locations … To reserve your car, call us at: 432-555-0943 (airport) 432-555-7118 (train station)",
 'brz-gt6-7' :"Fast ‘n Frugal Car Rental • Compact and mid-sized cars • Vans • Small trucks • Rent by the day, week, or month",
 'brz-gt6-31':"…wells as deep as a mile or more can be drilled into underground reservoirs to tap steam and hot water that are used to run turbines and create energy. Power companies can then transmit this energy over power lines.",
 'brz-gt6-32':"While geothermal heat pumps are an emissions-free and reliable source of energy, the biggest disadvantage is that such systems are expensive to install.",
 'brz-gt6-34':"However, one does not need to live in the desert to take advantage of solar power. Cloudy Germany is the worldwide leader in the use of solar power.",
 'brz-gt6-35':"Some enterprising home-owners reduce the initial costs by purchasing inexpensive kits and setting up the system on their own.",
};
/* ---- alasan pengecoh per soal (menggantikan kalimat seragam) ---- */
const REASON={
 'brz-gt5-25':"Buku mencantumkan <b>A — feeling lonely</b> sebagai salah satu jawaban benar. <i>Missed staff meetings</i> justru bukan kerugian: bacaan menyebut telecommuter tetap datang ke kantor untuk menghadiri rapat.",
 'brz-gt5-26':"Buku mencantumkan <b>C — interruptions of work</b> sebagai salah satu jawaban benar. Yang mengganggu adalah keluarga di rumah, bukan rekan kerja, jadi <i>problems with colleagues</i> tidak disebut.",
 'brz-gt5-27':"Buku mencantumkan <b>E — more expenses at home</b> sebagai salah satu jawaban benar. Dua pilihan lain tidak disebut sebagai kerugian di dalam bacaan.",
};
/* ---- perbaikan batang soal & opsi ---- */
const STEM={
 'brz-ac2-31':"<b>Gradualist Theory</b> — Proposes that many ______ changes in the shape of the Earth happened gradually.",
};
const OPTSWAP={ 'brz-ac4-32':{'show her how to use':'take any interest in'} };

/* ---- perbaikan teks bacaan ---- */
const PFIX=[
 ['GT6-S1', /Special prices for National Car Club members-\s*/,
            "Special prices for National Car Club members — 10 percent off our usual low prices! "],
 ['GT6-S1', /\s*Practice Test B\s*/, ' '],
];
const TYPO=[[/\bbehavior1\b/g,'behavior'],[/\bprofes sionally\b/g,'professionally'],
            [/\bfictionalized1\b/g,'fictionalized'],[/\bpaleontologists2\b/g,'paleontologists'],
            [/\bbehaviour1\b/g,'behaviour'],[/\bcolours2\b/g,'colours']];

const N=s=>s.replace(/\s+/g,' ').replace(/[’‘]/g,"'").replace(/[“”]/g,'"').replace(/[—–]/g,'-');
const esc=s=>s.replace(/</g,'&lt;').replace(/>/g,'&gt;');
const jss=x=>JSON.stringify(x);

/* muat semua bacaan lebih dulu untuk verifikasi kutipan */
const FILES=fs.readdirSync(DIR).filter(x=>x.endsWith('.js')).sort();
const ALLP={};
for(const f of FILES){ let b=null; global.TOEFLDRILL={addBank:x=>{b=x}};
  eval(fs.readFileSync(path.join(DIR,f),'utf8')); Object.assign(ALLP,b.passages||{}); }

let rep={pass:0,typo:0,quote:0,reason:0,stem:0,opt:0}, warn=[];
for(const f of FILES){
  let bank=null; global.TOEFLDRILL={addBank:x=>{bank=x}};
  const raw=fs.readFileSync(path.join(DIR,f),'utf8');
  const header=(raw.match(/^\/\*[\s\S]*?\*\//)||[''])[0];
  eval(raw);
  let touched=false;
  for(const k in (bank.passages||{})){
    let t=bank.passages[k].text, b0=t;
    for(const [pid,re,to] of PFIX) if(pid===k && re.test(t)){ t=t.replace(re,to); rep.pass++; }
    for(const [a,b] of TYPO) t=t.replace(a,b);
    if(t!==b0){ bank.passages[k].text=t.replace(/\s{2,}/g,' ').trim(); touched=true; rep.typo++; }
  }
  for(const q of bank.questions){
    if(STEM[q.id]){ q.question=STEM[q.id]; rep.stem++; touched=true; }
    if(OPTSWAP[q.id]){ const m=OPTSWAP[q.id]; const cor=q.options[q.answer];
      q.options=q.options.map(o=>m[o]!==undefined?m[o]:o);
      q.answer=q.options.indexOf(cor); rep.opt++; touched=true; }
    if(REASON[q.id]){
      const tail=(q.explain.match(/ Bagian bacaan yang mendukung:[\s\S]*$/)||[''])[0];
      q.explain=REASON[q.id]+tail; rep.reason++; touched=true;
    }
    if(QUOTE[q.id]){
      const head=q.explain.replace(/ Bagian bacaan yang mendukung:[\s\S]*$/,'').replace(/\.?$/,'.');
      q.explain=head+' Bagian bacaan yang mendukung: <i>“'+esc(QUOTE[q.id])+'”</i>';
      rep.quote++; touched=true;
      /* verifikasi: potongan terpanjang tanpa elipsis harus ada di bacaan */
      const src=N((ALLP[q.passageId]||{}).text||'');
      const frag=QUOTE[q.id].split(/…|\s\|\s/).map(s=>s.trim()).filter(s=>s.length>28);
      for(const fr of frag){ const parts=N(fr).split(' … ');
        for(const p2 of parts) if(src.indexOf(p2.replace(/^[^A-Za-z0-9]+/,''))<0) warn.push(q.id+' :: '+p2.slice(0,60)); }
    }
  }
  if(!touched) continue;
  const out=[header,'TOEFLDRILL.addBank({','source: '+jss(bank.source)+','];
  if(bank.passages&&Object.keys(bank.passages).length){ out.push('passages: {');
    for(const k in bank.passages) out.push(jss(k)+': { title:'+jss(bank.passages[k].title)+', text:'+jss(bank.passages[k].text)+' },');
    out.push('},'); }
  out.push('questions: [');
  for(const q of bank.questions){
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
console.log(rep);
console.log(warn.length? 'PERINGATAN kutipan tak ditemukan di bacaan:\n  '+warn.join('\n  ') : 'Semua kutipan pengganti terverifikasi ada di bacaan.');
