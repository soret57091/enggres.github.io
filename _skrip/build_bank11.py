# -*- coding: utf-8 -*-
"""Bank 11 — Barron's IELTS: soal isian kata/jawaban singkat diubah jadi pilihan ganda.
Opsi ditulis tangan: 4 pilihan sejenis dan sepanjang, semuanya masuk akal secara
tata bahasa, tetapi hanya satu yang didukung bacaan."""
import sys, re, json, io
sys.path.insert(0,'/home/claude')
import barron_parse as B

def cl(s):
    s=s.replace('­','')
    s=re.sub(r'(\w)-\s+(?=[a-z])',r'\1',s)
    s=re.sub(r'\s+',' ',s).strip()
    for pat in [r'^You should spend about \d+ (?:minutes|mimms) on Questions[^.]*\.\s*',
                r'^The following text has ?four sections[^.]*\.\s*',
                r'^Thefollowing text hasfour sections[^.]*\.\s*',
                r'^Choose the correct heading ?for each section[^.]*\.\s*',
                r'^Write the correct number[^.]*\.\s*',
                r'^There are more headings than sections[^.]*\.\s*',
                r'^(?:j?i{1,3}|iv|v|vi|vii|viii|ix|x)\s+[A-Z][^\n]{3,40}?(?=\s+(?:i{1,3}|iv|v|vi|vii|viii|ix|x)\s+[A-Z])']:
        for _ in range(9): s=re.sub(pat,'',s)
    return s.strip()

PSRC={}
for lab in ['AC2','AC5','AC6']:
    P,_,_=B.reading_blocks(lab)
    for k,v in P.items(): PSRC[k]=cl(v)
for lab in ['GT1','GT2']:
    for a,b,pid,pr in B.gt_sections(lab): PSRC[pid]=cl(pr)

CUT={'GT1-S2':'The Marcy Corporation','GT2-S1':'Presto Bread Machine'}
for pid,mark in CUT.items():
    if pid in PSRC:
        i=PSRC[pid].find(mark)
        if i>0: PSRC[pid]=PSRC[pid][i:]
TN={'AC':'Academic','GT':'General Training'}
def ref(lab): return "Barron's IELTS — %s Practice Test %s, Reading"%(TN[lab[:2]],lab[2])

SETS=[]
def S(lab,pid,sub,instr,items): SETS.append((lab,pid,sub,instr,items))
# item = (nomor, stem, [kunci, d1, d2, d3], penjelasan)

S('AC2','AC2-P1','Jawaban Singkat (Angka Tahun)',
  'Jawab pertanyaan berikut berdasarkan bacaan. Pilih satu angka tahun.',[
 (1,"When did Viking warriors raid an abbey on the coast of England?",
  ["793","841","866","870"],
  "Bacaan: <i>“During their first expedition, in <b>793</b>, a force of Viking warriors sacked the famed abbey at Lindisfarne, on England’s northeast coast.”</i>"),
 (2,"When was Eric the Red convicted of a crime?",
  ["980","998","870","866"],
  "Bacaan: <i>“In <b>980</b>, an Icelandic assembly found a man named Eric ‘the Red’ Ericson guilty of murder and sent him into exile.”</i> Tahun 998 adalah pelayaran anaknya, Leif Ericson."),
 (3,"When did Vikings establish a fort in Ireland?",
  ["841","844","866","870"],
  "Bacaan: <i>“in <b>841</b> founded Dublin, today a major Irish city, but originally a Viking fort.”</i> Tahun 844 adalah serbuan ke Portugal dan Spanyol."),
 (4,"When was a Viking chief granted lands by a king of France?",
  ["911","886","845","866"],
  "Bacaan: <i>“French King Charles III the Simple in <b>911</b> offered the Viking chief Rollo territories in northwest France.”</i> Tahun 845–886 adalah masa serangan ke Paris."),
 (5,"When did Viking warriors defeat an English king?",
  ["1066","998","911","886"],
  "Bacaan: <i>“in <b>1066</b>, under William, Duke of Normandy, defeated King Harold at the battle of Hastings in England.”</i>"),
])

S('AC5','AC5-P3','Melengkapi Ringkasan',
  'Lengkapi ringkasan bacaan berikut dengan pilihan yang tepat.',[
 (28,"Camouflage helps animals hide from both ______.",
  ["predators and prey","hunters and scavengers","enemies and rivals","males and females"],
  "Bacaan: <i>“Animals that use camouflage to conceal themselves from their enemies, <b>predator and prey</b> alike…”</i> — jadi kamuflase dipakai baik oleh pemangsa maupun mangsa."),
 (29,"Animals pass on their ______ through their genes.",
  ["protective coloring","hunting instincts","seasonal behavior","body temperature"],
  "Bacaan: <i>“Creatures with some type of <b>protective coloring</b> pass along the genes responsible…”</i>"),
 (30,"In background matching, an animal’s appearance helps it ______ with its environment.",
  ["blend in","stand out","move about","catch up"],
  "Bacaan: <i>“…all sorts of wildlife use background matching, also known as crypsis, to <b>blend in</b> with their surroundings.”</i>"),
 (31,"The arctic fox and snowshoe hare are examples of animals that ______ with the seasons.",
  ["alter their coloring","change their habitat","increase their weight","reduce their activity"],
  "Bacaan: <i>“Some animals have the ability to <b>alter their coloring</b> as their environment changes seasonally…”</i> — rubah artik berbulu putih di musim dingin dan cokelat saat hangat."),
 (32,"Many animals use a different strategy, having camouflage that helps them disguise themselves ______.",
  ["on many backgrounds","in one setting","at all times","from every angle"],
  "Bacaan: <i>“a somewhat more effective strategy involves having a camouflage that works <b>on many backgrounds</b>, blending in with all, but not perfectly matching any of them.”</i>"),
 (33,"Animals with disruptive coloration have markings such as ______ that make it difficult for a predator to discern the shape of the body.",
  ["stripes or spots","scales or feathers","horns or claws","fur or bristles"],
  "Bacaan: <i>“Disruptive coloration uses a pattern such as <b>stripes or spots</b> to disrupt the body’s outline.”</i>"),
 (34,"Although zebras are black and white, they can hide in tall grass because their major predator is ______.",
  ["color-blind","near-sighted","slow-moving","far-ranging"],
  "Warna hitam-putih zebra tetap menyatu dengan rerumputan hijau-kuning karena singa, pemangsa utamanya, <b>buta warna</b>."),
 (35,"______ is a type of camouflage that helps hide animals that are seen from above or below.",
  ["Countershading","Background matching","Disruptive coloration","Mimicry"],
  "Empat jenis kamuflase dalam bacaan: background matching, disruptive coloration, <b>countershading</b>, dan mimicry. Yang bekerja untuk pandangan dari atas atau bawah adalah <b>countershading</b>."),
 (36,"Penguins, for example, have ______, which help them blend in with the dark water from the point of view of an observer standing above.",
  ["black backs","white bellies","thick feathers","short wings"],
  "Dilihat dari atas, <b>punggung hitam</b> penguin menyatu dengan air laut yang gelap. Perut putihnya justru berfungsi bila dilihat dari bawah."),
])

S('AC6','AC6-P2','Melengkapi Kalimat',
  'Lengkapi kalimat berikut sesuai isi bacaan.',[
 (22,"People often believe that Paleolithic art consisted only of ______.",
  ["cave paintings","stone tools","animal bones","clay figures"],
  "Bacaan: <i>“many people assume that the art of early hunters and gatherers was limited to <b>cave paintings</b>.”</i>"),
 (23,"Ice Age artists used pointed tools to make ______ and sculptures on rocks.",
  ["engravings","pigments","torches","quadrangles"],
  "Bacaan: <i>“created <b>engravings</b> by scratching designs into rock with pointed tools, as well as creating low-relief sculptures.”</i>"),
 (24,"As well as pictures of animals, ______ are common in most sites.",
  ["geometrical designs","written symbols","painted numbers","carved letters"],
  "Bacaan: <i>“In addition to animal images, most sites also have <b>geometrical designs</b>, including dots and quadrangles.”</i>"),
 (25,"Pictures of ______ were sometimes made by wetting the palm with paint.",
  ["hands","horses","bison","faces"],
  "Bacaan: <i>“Images of <b>hands</b>, created either by wetting the palm of the hand with paint and pressing the hand onto rock…”</i>"),
 (26,"It is unusual to see an image of a ______ in European cave art.",
  ["full human","wild horse","cave bear","large bison"],
  "Bacaan: <i>“However, <b>full images of humans</b> are rare in the European caves.”</i> Kuda dan bison justru paling sering muncul."),
 (27,"Rather than being symbolic, paintings of animals are ______ images.",
  ["detailed, realistic","simple, abstract","small, faded","rough, primitive"],
  "Bacaan: <i>“Most of the animal images… are <b>detailed, realistic</b> portrayals of an individual animal species, not simply an abstract symbol.”</i>"),
])

S('GT1','GT1-S2','Melengkapi Kalimat',
  'Lengkapi kalimat berikut sesuai isi teks (Marcy Corporation).',[
 (21,"All ______ must participate in an orientation session.",
  ["new employees","department heads","part-time workers","company visitors"],
  "Teks: <i>“All <b>new employees</b> at the Marcy Corporation are required to attend an orientation session during their first month of employment.”</i>"),
 (22,"The ______ will take place in the company conference room.",
  ["next orientation session","annual staff meeting","monthly training class","yearly budget review"],
  "Teks: <i>“The <b>next orientation session</b> will be held on March 21 in the company conference room.”</i>"),
 (23,"The manual should be read before ______.",
  ["attending the orientation","signing the contract","meeting the supervisor","starting the first day"],
  "Teks: <i>“Employees are requested to read the employee manual and submit the signed statement prior to <b>attending the orientation</b>.”</i>"),
 (24,"The employee manual contains information about the company’s ______.",
  ["procedures and policies","products and services","salaries and bonuses","clients and partners"],
  "Teks: <i>“…has been provided to inform our employees about the company’s <b>procedures and policies</b>.”</i>"),
 (25,"The signed statement should be submitted to ______.",
  ["the employee’s supervisor","the Human Resources office","the orientation trainer","the company president"],
  "Teks: <i>“the statement below should be signed and returned to <b>the employee’s supervisor</b> by the date noted below.”</i> Human Resources hanya menerima <i>pertanyaan</i> tentang isi manual, bukan pernyataannya."),
 (26,"______ will answer questions about the content of the manual.",
  ["Human Resources","The supervisor","The president","The trainer"],
  "Teks: <i>“If there are any questions regarding the content of the manual, they should be submitted in writing to <b>Human Resources</b>.”</i>"),
 (27,"The due date for the signed statement is ______.",
  ["March 15","March 21","March 12","March 25"],
  "Teks: <i>“Please submit by: <b>March 15</b>.”</i> Tanggal 21 Maret adalah hari sesi orientasinya."),
])

S('GT1','GT1-S3','Melengkapi Ringkasan',
  'Lengkapi ringkasan bacaan tentang kano berikut.',[
 (35,"Polynesians turned dugout canoes into outrigger canoes by attaching ______ to them.",
  ["parallel floats","wooden sails","stone weights","bark panels"],
  "Bacaan: <i>“Outriggers have one or more <b>parallel floats</b> attached to a dugout canoe with poles for increased stability.”</i>"),
 (36,"Double-hulled canoes were made by connecting two outrigger canoes with ______.",
  ["a platform","a strong rope","a large sail","a wooden frame"],
  "Bacaan: <i>“Double-hulled canoes have <b>a platform</b> between two parallel dugouts.”</i>"),
 (37,"Because they could travel over ______ of ocean in these canoes, Polynesians were able to inhabit islands all across the Pacific Ocean.",
  ["huge expanses","narrow channels","shallow reefs","short stretches"],
  "Bacaan: <i>“could sail… across <b>huge expanses</b> of ocean, and in this way the Polynesian people spread throughout the Pacific.”</i>"),
 (38,"In West Africa, large war canoes were used to carry ______.",
  ["many fighters","heavy cargo","trade goods","large families"],
  "Bacaan: <i>“In West Africa, large war canoes capable of transporting <b>many fighters</b>…”</i>"),
 (39,"Today, ______ canoes are made of modern materials such as aluminum, fiberglass, and plastic.",
  ["recreational","ceremonial","commercial","traditional"],
  "Kano zaman sekarang dari aluminium, fiberglass, dan plastik dipakai untuk <b>rekreasi</b>, bukan lagi untuk perang atau upacara."),
 (40,"These modern canoes are similar in form to ______ canoes.",
  ["birch-bark","plank","war","dugout"],
  "Bentuk kano rekreasi modern meniru kano <b>kulit kayu birch</b> buatan penduduk asli Amerika Utara."),
])

S('GT2','GT2-S1','Jawaban Singkat',
  'Jawab pertanyaan berikut sesuai isi teks (Presto Bread Machine).',[
 (5,"How long does it take to bake raisin bread?",
  ["three hours","four hours","two hours","one hour"],
  "Teks: <i>“Your bread will be ready in <b>three hours</b> for white or raisin bread or four hours for whole wheat bread.”</i>"),
 (6,"How often should you clean the inside of the machine?",
  ["after each use","once a week","every three months","before each use"],
  "Teks: <i>“It is important to clean the inside of the machine <b>after each use</b>.”</i>"),
 (7,"According to these instructions, where can you find bread recipes from around the world?",
  ["on the website","in the booklet","on the machine","in the box"],
  "Resep dari berbagai negara disebutkan tersedia <b>di situs web</b>; buku resep yang disertakan hanya memuat resep dasar."),
])

S('GT2','GT2-S2','Melengkapi Kalimat',
  'Lengkapi kalimat berikut sesuai isi teks (Job Interview Success).',[
 (15,"Wearing ______ clothes makes a better impression during the job interview.",
  ["conservative","expensive","comfortable","colorful"],
  "Teks: <i>“<b>Conservative</b> colors and styles always convey a more trustworthy image.”</i>"),
 (16,"Practice answering questions ahead of time so that you feel ______ during the interview.",
  ["calm","proud","tired","curious"],
  "Teks: <i>“Think of questions that you will probably be asked, and prepare answers for them. This will help you be <b>calm</b> when you are at the actual interview.”</i>"),
 (17,"If traveling to the interview by bus, make sure you know ______ ahead of time.",
  ["the schedules","the fares","the drivers","the seats"],
  "Teks: <i>“If by bus or subway, check <b>the schedules</b> the day before.”</i>"),
 (18,"You will be ______ for the interview if you plan your trip beforehand.",
  ["on time","in doubt","at ease","on foot"],
  "Teks: <i>“Careful planning will ensure that you will make a good impression by arriving <b>on time</b>.”</i>"),
 (19,"Use your ______ to convey an attitude of confidence.",
  ["voice","resume","clothes","hands"],
  "Teks: <i>“Speaking with a firm, clear <b>voice</b> is one of the best ways to give an impression of self-assurance.”</i>"),
 (20,"Show what you know by asking ______.",
  ["the right questions","for a tour","about the salary","for more time"],
  "Teks: <i>“asking <b>the right questions</b> shows that you are knowledgeable about the company.”</i>"),
])

S('GT6','GT6-S3','Melengkapi Ringkasan',
  'Lengkapi ringkasan bacaan tentang energi hijau berikut.',[
 (28,"These days, people are interested in reducing their consumption of ______.",
  ["fossil fuels","solar power","hot water","power lines"],
  "Bacaan: <i>“people everywhere are becoming increasingly concerned about using <b>fossil fuels</b>.”</i>"),
 (29,"They are looking at sources of ______ to supply their power needs.",
  ["alternative energy","greenhouse gas","underground steam","electric current"],
  "Bacaan: <i>“The ideal <b>alternative energy</b> source would be sustainable, clean, and reliable.”</i>"),
 (30,"People want sources that are ______, do not cause pollution, and can be consistently depended on.",
  ["sustainable","expensive","nonrenewable","imported"],
  "Bacaan: <i>“would be <b>sustainable</b> (the supply will not be exhausted), clean (no emissions), and reliable.”</i>"),
])

qs=[]; rot=0
for lab,pid,sub,instr,items in SETS:
    for n,stem,opts,ex in items:
        assert len(opts)==4 and len(set(opts))==4, (lab,n)
        cor=opts[0]; rest=opts[1:]
        pos=rot%4; rot+=1
        o=rest[:pos]+[cor]+rest[pos:]
        qs.append({"id":"bri-%s-%d"%(lab.lower(),n),"theme":"reading","subtheme":sub,
                   "ref":ref(lab),"passageId":pid,"instruction":instr,
                   "question":stem,"options":o,"answer":pos,"explain":ex})

NEED={q['passageId'] for q in qs}
HAVE_IN_BANK10={'GT1-S3','GT6-S3'}
src={"id":"barron-isian","name":"Barron's IELTS Practice Exams (Isian Kata → Pilihan Ganda)","test":"IELTS"}
def jss(x): return json.dumps(x,ensure_ascii=False)
out=["/* Bank 11 — Barron's IELTS: soal isian kata & jawaban singkat menjadi pilihan ganda.",
     "   Setiap set opsi ditulis tangan: sejenis, sepanjang, hanya satu yang didukung bacaan. */",
     "TOEFLDRILL.addBank({","source: "+jss(src)+",","passages: {"]
for pid in sorted(NEED-HAVE_IN_BANK10):
    txt=PSRC.get(pid,'')
    assert len(txt)>500, (pid,len(txt))
    out.append(jss(pid)+": { title:"+jss("Barron's IELTS — bacaan")+", text:"+jss(txt)+" },")
out.append("},"); out.append("questions: [")
for q in qs:
    out.append("{id:%s, theme:%s, subtheme:%s, ref:%s, passageId:%s,\n instruction:%s,\n question:%s,\n options:%s, answer:%d,\n explain:%s},"%(
        jss(q['id']),jss(q['theme']),jss(q['subtheme']),jss(q['ref']),jss(q['passageId']),
        jss(q['instruction']),jss(q['question']),jss(q['options']),q['answer'],jss(q['explain'])))
out.append("]\n});")
io.open('/mnt/user-data/outputs/TOEFL-Drill-Web/data/bank-11-barron-isian.js','w',encoding='utf-8').write("\n".join(out)+"\n")
from collections import Counter
print('soal',len(qs),'| kunci',Counter(q['answer'] for q in qs))
for pid in sorted(NEED-HAVE_IN_BANK10): print(' ',pid,len(PSRC.get(pid,'')),'|',PSRC.get(pid,'')[:70])
