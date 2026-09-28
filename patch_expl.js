/* Menambahkan kutipan pendukung untuk 10 pembahasan terakhir + membetulkan
   beberapa salah baca OCR yang tidak tertangkap penyambung kata otomatis. */
const fs=require('fs'), path=require('path');
const DIR=__dirname+'/data';
const ADD={
 'brx-ac1-7' :"Dragonflies and damselflies both lay their eggs on or just below the surface of the water in a pond or stream.",
 'brx-ac1-8' :"The babies emerge from the eggs in the form of nymphs.",
 'brx-ac1-10':"They have a special lip that they can extend far forward in order to grab their prey when it comes close.",
 'brx-ac1-12':"They have two sets of wings that can move independently of each other. This gives them great maneuverability in the air.",
 'brx-ac1-13':"…they catch their prey while flying. They can hover, make sharp turns, and fly backward.",
 'brx-gt4-37':"Sometimes, light therapy is used in combination with antidepressant medication and individual psychotherapy.",
 'brx-gt4-39':"People who have a tendency to suffer from SAD are encouraged to go outside every day during the winter months and to exercise regularly.",
 'brx-gt4-40':"Sometimes, light therapy is used in combination with antidepressant medication and individual psychotherapy.",
 'brz-ac3-17':"The industrial revolution facilitated the growth of literacy, making it easier to print and transport publications in large quantities, thus providing inexpensive entertainment for the masses.",
 'brz-gt5-25':"Unfortunately, even the most independent worker can start to feel isolated over time.",
};
const TYPO=[[/\bindependendy\b/g,'independently'],[/\bman age\b/g,'manage'],[/\bunder stand\b/g,'understand'],
 [/\bmaneuverability1\b/g,'maneuverability'],[/\bcanoea\b/g,'canoe — a'],[/\bunder standing\b/g,'understanding'],
 [/\bhimlisten ing\b/g,'him — listening'],[/\brumors2\b/g,'rumors'],[/\bcolors1\b/g,'colors']];
const fixT=s=>{TYPO.forEach(([a,b])=>s=s.replace(a,b));return s;};
let n=0;
for(const f of fs.readdirSync(DIR).filter(x=>x.endsWith('.js')).sort()){
  let bank=null; global.TOEFLDRILL={addBank:x=>{bank=x}};
  const raw=fs.readFileSync(path.join(DIR,f),'utf8');
  const header=(raw.match(/^\/\*[\s\S]*?\*\//)||[''])[0];
  eval(raw);
  let touched=false;
  for(const k in (bank.passages||{})){const b=bank.passages[k].text;const a=fixT(b);if(a!==b){bank.passages[k].text=a;touched=true;}}
  for(const q of bank.questions){
    if(ADD[q.id]){ q.explain=q.explain.replace(/\.?$/,'.')+' Bagian bacaan yang mendukung: <i>“'+ADD[q.id]+'”</i>'; n++; touched=true; }
    const be=q.explain, bq=q.question; q.explain=fixT(q.explain); q.question=fixT(q.question);
    if(q.options) q.options=q.options.map(fixT);
    if(be!==q.explain||bq!==q.question) touched=true;
  }
  if(!touched) continue;
  const jss=x=>JSON.stringify(x);
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
console.log('pembahasan ditambah kutipan:',n);
