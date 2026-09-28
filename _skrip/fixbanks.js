/* Perbaikan menyeluruh bank soal berdasarkan hasil audit. */
const fs=require('fs'), path=require('path');
const DIR='/mnt/user-data/outputs/TOEFL-Drill-Web/data';
const ANASAZI=fs.readFileSync('/home/claude/anasazi.txt','utf8').trim();

const ANSWER_FIX={ 'pt-ex14-16':2, 'ptr-ex34_2-12':2, 'ptr-ex35_2-20':0, 'bb-l1-9':1 };
const NOTE_FIX={
 'pt-ex14-16':"Kalau <i>which</i> sudah menjadi objek klausa, objek <i>them</i> tidak boleh diulang: cukup <b>use</b>.",
 'ptr-ex34_2-12':"Bacaan menyatakan hammered dulcimer <i>“is shaped like a trapezoid”</i>. Bentuk tetesan air mata dan jam pasir adalah dulcimer Appalachian. <i>(Catatan: kunci di buku tertulis A — tampaknya salah cetak; bacaan jelas menyebut trapezoid.)</i>",
 'ptr-ex35_2-20':"Bacaan: <i>“passengers board aircraft from small terminals that are separated from the main terminals. Passengers reach the satellites by way of shuttle trains…”</i> — jadi kereta ulang-alik berangkat dari <b>terminal utama</b>.",
 'bb-l1-9':"Seharusnya <b>our friends in Bandung yesterday</b>. Keterangan waktu tidak boleh menyela kata kerja dan objeknya. Urutan yang benar: Subject + Verb + Complement + Modifier.",
 'ptr-ex37_2-6':"<i>This process</i> merujuk proses yang baru saja diuraikan di kalimat sebelumnya, yaitu <b>mineral concentration</b> — tahap akhir penambangan.",
 'bb-l4-1':"Kata sifat <i>various</i> harus diganti kata benda <b>variety</b>: <i>a remarkable variety of inventions</i>.",
};
const DROP=new Set(['bb-voc-9','i202-4-a','i202-5-j','i202-9-a','i202-9-g','i202-9-h',
                    'br-ac4-5','i202-5-f','br-ac5-11']);

const JOIN=[[/\bifyou\b/g,'if you'],[/\bcandothis\b/g,'can do this'],[/\balleviatethe\b/g,'alleviate the'],
 [/\bsunlightand\b/g,'sunlight and'],[/\btimesof\b/g,'times of'],[/\bFredAllen\b/g,'Fred Allen'],
 [/\bItis\b/g,'It is'],[/\bgroundfloor\b/g,'ground floor'],[/\bsecondfloor\b/g,'second floor'],
 [/\bthirdfloor\b/g,'third floor'],[/\bfourthfloor\b/g,'fourth floor'],
 [/\bwinterschedule\b/g,'winter schedule'],[/\banswersheet\b/g,'answer sheet'],[/\bonyour\b/g,'on your'],
 [/\bsomefriends\b/g,'some friends'],[/\bcurrentjob\b/g,'current job'],[/\bproducedfood\b/g,'produced food'],
 [/\btextfor\b/g,'text for'],[/\bmimms\b/g,'minutes'],[/\binorderto\b/g,'in order to'],
 [/\bLTamvery\b/g,'I am very'],[/\bTorna does\b/g,'Tornadoes'],[/,vas\b/g,'was'],[/\bImust\b/g,'I must'],
 [/\bthefollowing\b/g,'the following'],[/\bofthe\b/g,'of the'],[/\bIwas\b/g,'I was'],
 [/if the phra /g,'if the phrase describes '],
 [/­\s*/g,''],[/\bo f\b/g,'of'],[/\bin­\s*/g,'in'],
];
function joins(s){ JOIN.forEach(([a,b])=>s=s.replace(a,b)); return s; }
function sq(s){ return s.replace(/[ \t]+/g,' ').replace(/ ([,.;:?!])/g,'$1').trim(); }

const STEMCUT=[
 /\s*SECTION\s*\d\s+QUESTIONS?\s*\d/i, /\s*Questions?\s*\d[\d ]*\s*(?:and|[-‐-―−])\s*\d/,
 /\s*Practice Test \d\s+Candidate Name/i, /\s*Candidate Name and Number/i,
 /\s*INTERNATIONAL ENGLISH LANGUAGE/i, /\s*WRITING TASK/i,
 /\s*You (?:should spend|are advised to spend) about \d+ minutes/i,
 /\s*Write (?:the correct letter|your answers|ONE WORD)/i, /\s*Choose (?:FIVE|THREE|the correct)/i,
];
function cutStem(s){
  for(const re of STEMCUT){ const m=s.match(re); if(m && m.index>25) s=s.slice(0,m.index); }
  s=s.replace(/\s+[A-Z]\s*$/,'').replace(/\s*[|—-]?\s*r?\s*\d{2,3}\s*\|?\s*$/,'');
  return sq(s);
}
function cutExpl(s){
  const cuts=[/\s*s\.\s*\)\s*Mengenali Subjek/, /\s*e\s+Membalikkan Urutan/, /\s*\d{1,2}\.\s*Jawaban\s*\d?[A-D]/,
              /\s*[A-Z]\.\)\s+[A-Z]/, /\s*©\s*Bentuk Kata/];
  for(const re of cuts){ const m=s.match(re); if(m && m.index>40) s=s.slice(0,m.index); }
  if(s.length>900){ const c=s.lastIndexOf('. ',900); s=s.slice(0,c>300?c+1:900); }
  return sq(s);
}
const PCUT_HEAD=[
 /^You should spend about \d+ (?:minutes|mimms) on Questions[^.]*\.\s*/i,
 /^Questions?\s*\d[\d\-‐-―\s]*[.:]?\s*/,
 /^Read the (?:text|information|passage)[^.]*\.\s*/i,
 /^reading passage below\.\s*/i, /^below\.\s*/i,
];
const PCUT_TAIL=[
 /\s*WRITING TASK 1[\s\S]*$/i, /\s*You should spend about 40 minutes on this task[\s\S]*$/i,
 /\s*Questions?\s*\d[\d ]*[-‐-―]\s*Complete the chart[\s\S]*$/i,
 /\s*WORD DEFINITIONS[\s\S]*$/i, /\s*Exercise \d\.\d\.\s*(?:Listen|Dictation)[\s\S]*$/i,
 /\s*\d{3}\s+IELTS Practice Exams[\s\S]*$/i, /\s*AUDIOSCRIPTS for Listen\s*ing[\s\S]*$/i,
];
function cleanPassage(t){
  let s=joins(t);
  for(const re of PCUT_HEAD){ s=s.replace(re,''); }
  for(const re of PCUT_TAIL){ s=s.replace(re,''); }
  s=s.replace(/\s*\d{3}\s+IELTS Practice Exams\s*/g,' ')
     .replace(/\s*on page \d+\s*/g,' ')
     .replace(/\s*IELTS Practice Exams\s*/g,' ');
  return sq(s);
}

const jss=x=>JSON.stringify(x);
let report={fixAns:0,fixExpl:0,drop:0,stem:0,expl:0,pass:0};
for(const f of fs.readdirSync(DIR).filter(x=>x.endsWith('.js')).sort()){
  const raw=fs.readFileSync(path.join(DIR,f),'utf8');
  const header=(raw.match(/^\/\*[\s\S]*?\*\//)||[''])[0];
  let bank=null;
  global.TOEFLDRILL={addBank:b=>{bank=b;}};
  eval(raw);
  const P=bank.passages||{};
  for(const k in P){
    const before=P[k].text; const after=cleanPassage(before);
    if(after!==before) report.pass++;
    P[k].text=after;
  }
  if(P['EX34.2-P1']) P['EX34.2-P1'].text=ANASAZI;
  const qs=[];
  for(const q of bank.questions||[]){
    if(DROP.has(q.id)){ report.drop++; continue; }
    if(q.id in ANSWER_FIX){ q.answer=ANSWER_FIX[q.id]; report.fixAns++; }
    if(q.id in NOTE_FIX){ q.explain=NOTE_FIX[q.id]; report.fixExpl++; }
    if(q.question){ const b=q.question; q.question=cutStem(joins(b)); if(q.question!==b) report.stem++; }
    if(q.options) q.options=q.options.map(o=>sq(joins(o)).replace(/^_+\s*/,''));
    if(q.explain){ const b=q.explain; q.explain=cutExpl(joins(b)); if(q.explain!==b) report.expl++; }
    if(q.instruction) q.instruction=sq(q.instruction);
    if(q.type!=='open'){
      if(!q.options||q.options.length<2||new Set(q.options).size!==q.options.length
         ||q.answer==null||q.answer<0||q.answer>=q.options.length
         ||q.options.some(o=>!o)||(q.question||'').length<12){ report.drop++; continue; }
    }
    qs.push(q);
  }
  const out=[header, 'TOEFLDRILL.addBank({',
    'source: '+jss(bank.source)+','];
  if(Object.keys(P).length){
    out.push('passages: {');
    for(const k in P) out.push(jss(k)+': { title:'+jss(P[k].title)+', text:'+jss(P[k].text)+' },');
    out.push('},');
  }
  out.push('questions: [');
  for(const q of qs){
    const parts=['id:'+jss(q.id),'theme:'+jss(q.theme)];
    if(q.subtheme) parts.push('subtheme:'+jss(q.subtheme));
    if(q.ref) parts.push('ref:'+jss(q.ref));
    if(q.type) parts.push('type:'+jss(q.type));
    if(q.passageId) parts.push('passageId:'+jss(q.passageId));
    if(q.instruction) parts.push('\n instruction:'+jss(q.instruction));
    parts.push('\n question:'+jss(q.question));
    if(q.options) parts.push('\n options:'+jss(q.options)+', answer:'+q.answer);
    parts.push('\n explain:'+jss(q.explain));
    out.push('{'+parts.join(', ')+'},');
  }
  out.push(']\n});');
  fs.writeFileSync(path.join(DIR,f), out.join('\n')+'\n');
  console.log(f,'->',qs.length,'soal');
}
console.log(report);
