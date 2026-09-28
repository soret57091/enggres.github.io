# -*- coding: utf-8 -*-
"""Bank 12 — Barron's IELTS: blok soal yang kotak pilihannya rusak di OCR,
dipulihkan dengan membaca ulang halaman aslinya satu per satu.
Kunci tetap milik buku; opsi disusun agar sejenis dan sepanjang kunci."""
import json, io

Q=[]; rot=0
def add(qid,pid,sub,ref,instr,stem,opts,ex,fixed=False):
    global rot
    assert len(set(opts))==len(opts), qid
    cor=opts[0]; rest=opts[1:]
    if fixed:
        o=sorted(opts); pos=o.index(cor)
    else:
        pos=rot%len(opts); rot+=1
        o=rest[:pos]+[cor]+rest[pos:]
    Q.append({"id":qid,"theme":"reading","subtheme":sub,"ref":ref,"passageId":pid,
              "instruction":instr,"question":stem,"options":o,"answer":pos,"explain":ex})

# ============ AC2 27–32 : catatan Catastrophe vs Gradualist Theory ============
R="Barron's IELTS — Academic Practice Test 2, Reading"
I="Lengkapi catatan tentang kedua teori berikut berdasarkan bacaan."
S="Melengkapi Catatan/Ringkasan"
add('brz-ac2-27','AC2-P3',S,R,I,
 "<b>Catastrophe Theory</b> — First introduced by ______.",
 ["Georges Cuvier","James Hutton","Charles Darwin","Walter Alvarez"],
 "Kunci buku: <b>Georges Cuvier</b>, pencetus teori katastrofisme. James Hutton adalah pencetus teori gradualis.")
add('brz-ac2-28','AC2-P3',S,R,I,
 "<b>Catastrophe Theory</b> — Proposes that major ______ have given Earth its shape.",
 ["disasters","eruptions","migrations","discoveries"],
 "Kunci buku: <b>disasters</b>. Inti katastrofisme: bentuk Bumi dihasilkan oleh bencana-bencana besar yang mendadak.")
add('brz-ac2-29','AC2-P3',S,R,I,
 "<b>Catastrophe Theory</b> — Supports the idea that the Earth has a ______ history.",
 ["short","long","mysterious","definite"],
 "Kunci buku: <b>short</b>. Karena perubahan dianggap terjadi lewat bencana mendadak, Bumi tidak perlu berumur panjang. <i>long</i> justru pandangan teori gradualis.")
add('brz-ac2-30','AC2-P3',S,R,I,
 "<b>Gradualist Theory</b> — First introduced by ______.",
 ["James Hutton","Georges Cuvier","Charles Darwin","Walter Alvarez"],
 "Kunci buku: <b>James Hutton</b>. Cuvier adalah tokoh teori katastrofisme.")
add('brz-ac2-31','AC2-P3',S,R,I,
 "<b>Gradualist Theory</b> — Proposes that many ______ changes in the shape of the Earth happened over a long period of time.",
 ["small","short","sudden","definite"],
 "Kunci buku: <b>small</b>. Teori gradualis menekankan perubahan kecil yang menumpuk, bukan perubahan mendadak.")
add('brz-ac2-32','AC2-P3',S,R,I,
 "<b>Gradualist Theory</b> — …changes in the shape of the Earth happened over a ______ period of time.",
 ["long","short","brief","definite"],
 "Kunci buku: <b>long</b>. Perubahan kecil membutuhkan rentang waktu yang sangat panjang.")

# ============ AC3 14–19 : penny bloods vs dime novels ============
R="Barron's IELTS — Academic Practice Test 3, Reading"
I="Ciri berikut milik jenis bacaan yang mana?"
S="Mengelompokkan Ciri"
OPT=["Penny bloods","Dime novels","Keduanya (penny bloods dan dime novels)"]
for qid,st,k,ex in [
 ('brz-ac3-14',"They were popular in America.",1,"<b>Dime novels</b> adalah bacaan murah khas Amerika; penny bloods terbit di Inggris."),
 ('brz-ac3-15',"They were popular in Britain.",0,"<b>Penny bloods</b> adalah bacaan seharga satu penny yang populer di Inggris."),
 ('brz-ac3-16',"They showed members of the upper class as corrupt.",0,"Penggambaran kaum atas sebagai orang bejat adalah ciri <b>penny bloods</b> Inggris."),
 ('brz-ac3-17',"They were inexpensive.",2,"Harga murah adalah ciri <b>keduanya</b> — penny bloods satu penny, dime novels sepuluh sen."),
 ('brz-ac3-18',"They featured tales of the Wild West.",1,"Kisah Wild West adalah ciri khas <b>dime novels</b> Amerika."),
 ('brz-ac3-19',"They were popular among members of the working class.",2,"<b>Keduanya</b> sama-sama dibaca kalangan pekerja."),
]:
    Q.append({"id":qid,"theme":"reading","subtheme":S,"ref":R,"passageId":"AC3-P2",
              "instruction":I,"question":st,"options":OPT,"answer":k,
              "explain":"Kunci buku: <b>%s</b>. %s"%(OPT[k],ex)})

# ============ AC4 28–33 : ringkasan kecerdasan burung gagak ============
R="Barron's IELTS — Academic Practice Test 4, Reading"
I="Lengkapi ringkasan bacaan berikut."
S="Melengkapi Catatan/Ringkasan"
add('brz-ac4-28','AC4-P3',S,R,I,
 "Jane Goodall’s work in 1960 showed that ______ were not the only ones to make tools.",
 ["humans","chimpanzees","corvids","primates"],
 "Kunci buku: <b>humans</b>. Temuan Goodall justru memperlihatkan simpanse ikut membuat alat, jadi manusia bukan satu-satunya.")
add('brz-ac4-29','AC4-P3',S,R,I,
 "New Caledonian crows make tools in order to retrieve the ______ that they eat in the wild.",
 ["grubs","twigs","leaves","spears"],
 "Kunci buku: <b>grubs</b> (larva serangga) — itulah makanan yang dicungkil dengan alat. <i>twigs</i> dan <i>leaves</i> adalah bahan alatnya, bukan makanannya.")
add('brz-ac4-30','AC4-P3',S,R,I,
 "Scientists believe that generally these birds ______ how to make tools.",
 ["learn from other birds","are born knowing","discover by accident","copy from humans"],
 "Kunci buku: <b>learn from other birds</b> — kemampuan itu diturunkan lewat belajar dari sesamanya, bukan bawaan lahir.")
add('brz-ac4-31','AC4-P3',S,R,I,
 "Scientists observed Betty use pieces of wire to make ______, which she used to retrieve food.",
 ["hooks","spears","twigs","leaves"],
 "Kunci buku: <b>hooks</b>. Betty membengkokkan kawat menjadi kait.")
add('brz-ac4-32','AC4-P3',S,R,I,
 "The interesting thing is that other crows did not ______ the tools.",
 ["teach her how to make","try to take away","help her to bend","show her how to use"],
 "Kunci buku: <b>teach her how to make</b> — Betty menemukannya sendiri, tidak diajari gagak lain.")
add('brz-ac4-33','AC4-P3',S,R,I,
 "Once the scientists saw Betty make a tool, they tried to get her to ______ the behavior, which she did successfully.",
 ["repeat","modify","explain","forget"],
 "Kunci buku: <b>repeat</b>. Para ilmuwan meminta Betty mengulang perilaku itu, dan ia berhasil.")

# ============ GT5 21–27 : telecommuting ============
R="Barron's IELTS — General Training Practice Test 5, Reading"
S="Informasi Rinci (pilih satu)"
ADV_OK=[("A","reduced travel expenses"),("D","more time to spend with the family"),
        ("E","a more relaxed life"),("G","an improved attitude toward work")]
ADV_NO=["salary increases","a better employer–employee relationship","more time for personal business"]
for i,(L,txt) in enumerate(ADV_OK):
    add('brz-gt5-%d'%(21+i),'GT5-S2',S,R,
        "Pilih SATU keuntungan telecommuting yang memang disebutkan dalam bacaan.",
        "Which of the following advantages of telecommuting are mentioned in the passage?",
        [txt]+ADV_NO,
        "Buku mencantumkan <b>%s — %s</b> sebagai salah satu jawaban benar. Kenaikan gaji, hubungan atasan–bawahan, dan waktu untuk urusan pribadi tidak disebut sebagai keuntungan."%(L,txt))
DIS_OK=[("A","feeling lonely"),("C","interruptions of work"),("E","more expenses at home")]
DIS_NO=["missed staff meetings","problems with colleagues"]
for i,(L,txt) in enumerate(DIS_OK):
    add('brz-gt5-%d'%(25+i),'GT5-S2',S,R,
        "Pilih SATU kerugian telecommuting yang memang disebutkan dalam bacaan.",
        "Which of the following disadvantages of telecommuting are mentioned in the passage?",
        [txt]+DIS_NO,
        "Buku mencantumkan <b>%s — %s</b> sebagai salah satu jawaban benar. Bacaan justru menyebut telecommuter tetap datang ke kantor untuk rapat, jadi rapat yang terlewat bukan kerugian yang disebutkan."%(L,txt))

# ============ GT6 31–36 : energi panas bumi & surya ============
R="Barron's IELTS — General Training Practice Test 6, Reading"
GEO_OK=[("B","is used to run power plants"),("C","costs a good deal of money to set up"),
        ("E","is used for cooling as well as heating buildings")]
GEO_NO=["is easiest to use where there is a plentiful supply of groundwater",
        "requires electricity to power the heat pump"]
for i,(L,txt) in enumerate(GEO_OK):
    add('brz-gt6-%d'%(31+i),'GT6-S3',S,R,
        "Pilih SATU keterangan tentang energi panas bumi yang memang disebutkan dalam bacaan.",
        "Which of the following facts about geothermal energy are mentioned in the passage?",
        [txt]+GEO_NO,
        "Buku mencantumkan <b>%s — %s</b> sebagai salah satu jawaban benar."%(L,txt))
SOL_OK=[("A","can be used even in areas without intense sunlight"),
        ("C","does not have to be installed by a professional"),
        ("D","the amount of power generated fluctuates with the amount of exposure to the sun")]
SOL_NO=["the panels are usually installed on the roof of the house",
        "is often used by farmers to power electric fences"]
for i,(L,txt) in enumerate(SOL_OK):
    add('brz-gt6-%d'%(34+i),'GT6-S3',S,R,
        "Pilih SATU keterangan tentang energi surya yang memang disebutkan dalam bacaan.",
        "Which of the following facts about solar energy are mentioned in the passage?",
        [txt]+SOL_NO,
        "Buku mencantumkan <b>%s — %s</b> sebagai salah satu jawaban benar."%(L,txt))

# ============ GT4 1–7 : mencocokkan kesempatan menjadi relawan ============
R="Barron's IELTS — General Training Practice Test 4, Reading"
S4="Mencocokkan Informasi"
VOL=["Performing for nursing home residents","The Citizen’s Park Cleanup Committee",
     "Tutoring at Mayfield Elementary School","Assisting at the Mayfield Free Clinic",
     "Serving meals at the Mayfield Shelter"]
for n,st,k,ex in [
 (1,"is only free in the evening?",4,"Bacaan: <i>“The Mayfield Shelter serves hot dinners to the homeless <b>every evening</b>.”</i>"),
 (2,"is interested in health care?",3,"Bacaan: <i>“The Mayfield Free Clinic… Volunteers will complete patient intake forms, educate the patients about clinic services.”</i>"),
 (3,"plays the guitar and sings?",0,"Bacaan: <i>“Do you like to perform? Do you have a <b>special talent</b> that’s just waiting for an audience?”</i>"),
 (4,"enjoys spending time outdoors?",1,"Bacaan: <i>“picking up trash, repairing equipment, pulling weeds, and <b>planting flowers</b>”</i> — semuanya kegiatan di luar ruang."),
 (5,"likes to cook?",4,"Bacaan: <i>“the shelter needs volunteers to help with <b>preparing and serving meals</b>.”</i>"),
 (6,"only has one day a month free?",1,"Bacaan: <i>“Committee members spend <b>the last Saturday of each month</b> at a different city park.”</i>"),
 (7,"enjoys young children?",2,"Bacaan: <i>“Mayfield Elementary School needs people to help with their afterschool program. Volunteers will <b>tutor children</b> in reading and math.”</i>"),
]:
    Q.append({"id":"brz-gt4-%d"%n,"theme":"reading","subtheme":S4,"ref":R,"passageId":"GT4-S1",
      "instruction":"Kesempatan menjadi relawan mana yang paling cocok?",
      "question":"Which opportunity is most appropriate for a person who "+st,
      "options":VOL,"answer":k,
      "explain":"Kunci buku: <b>%s</b>. %s"%(VOL[k],ex)})

# ============ GT6 1–7 : mencocokkan iklan penyewaan mobil ============
R="Barron's IELTS — General Training Practice Test 6, Reading"
CAR=["Good Deal Car Rentals","Fast ‘n Frugal Car Rental","Dollar Dan’s Rent-a-Car"]
for n,st,k,ex in [
 (1,"has the lowest price for a compact car?",2,"Dollar Dan’s $35/hari (≈ $245 seminggu) lebih murah daripada $375 dan $350 seminggu di dua tempat lain."),
 (2,"accepts payments in cash?",0,"Bacaan: <i>“Payment by <b>cash</b> or credit card”</i>. Fast ‘n Frugal menulis <i>No cash, please</i>; Dollar Dan’s hanya kartu kredit."),
 (3,"offers a discount?",1,"Bacaan: <i>“Special prices for National Car Club members—<b>10 percent off</b> our usual low prices!”</i>"),
 (4,"is convenient for people arriving by plane?",0,"Hanya Good Deal yang punya kantor di <b>bandara</b> (432-555-0943 airport)."),
 (5,"is always open?",2,"Bacaan: <i>“We’re open <b>twenty-four hours/day, seven days/week</b>.”</i>"),
 (6,"does not require a reservation?",2,"Bacaan: <i>“There’s <b>no need to reserve</b> a car at Dollar Dan’s.”</i>"),
 (7,"has vehicles suitable for moving furniture?",1,"Hanya Fast ‘n Frugal yang menyewakan <b>vans</b> dan <b>small trucks</b>."),
]:
    Q.append({"id":"brz-gt6-%d"%n,"theme":"reading","subtheme":S4,"ref":R,"passageId":"GT6-S1",
      "instruction":"Perusahaan penyewaan mobil mana yang dimaksud?",
      "question":"Which car rental agency "+st,"options":CAR,"answer":k,
      "explain":"Kunci buku: <b>%s</b>. %s"%(CAR[k],ex)})

# ============ AC3 2,3,5,6 : memilih judul bagian ============
R="Barron's IELTS — Academic Practice Test 3, Reading"
HEAD=["Scanning the Brain and Chest","The Role of Computers","The CT Scan Is Invented",
      "The High Cost of CT Scans","Emergency Room Care","Faster and More Comfortable",
      "How Doctors Use CT Scans","The Patient Is Photographed","Enhancing Scan Images with Dyes"]
for n,sec,cor,dis,rom in [
 (2,"Section B","Faster and More Comfortable",["The High Cost of CT Scans","Emergency Room Care","The Role of Computers"],"vii"),
 (3,"Section C","The Patient Is Photographed",["Scanning the Brain and Chest","How Doctors Use CT Scans","Emergency Room Care"],"ix"),
 (5,"Section E","How Doctors Use CT Scans",["The Patient Is Photographed","Scanning the Brain and Chest","The Role of Computers"],"viii"),
 (6,"Section F","Enhancing Scan Images with Dyes",["Scanning the Brain and Chest","The High Cost of CT Scans","How Doctors Use CT Scans"],"x"),
]:
    add("brz-ac3-%d"%n,"AC3-P1","Memilih Judul Bagian",R,
        "Pilih judul yang paling sesuai dengan isi bagian tersebut.",
        "Judul yang paling tepat untuk <b>%s</b> pada bacaan <i>The CT Scanner</i> adalah …"%sec,
        [cor]+dis, "Kunci buku: <b>%s — %s</b>."%(rom,cor))

src={"id":"barron-pulih","name":"Barron's IELTS Practice Exams (Blok Pulihan → Pilihan Ganda)","test":"IELTS"}
def jss(x): return json.dumps(x,ensure_ascii=False)
out=["/* Bank 12 — Barron's IELTS: blok soal yang kotak pilihannya rusak di hasil OCR,",
     "   dipulihkan dengan membaca ulang halaman aslinya. Bacaan memakai id yang sudah",
     "   didefinisikan di bank-06 dan bank-10. */",
     "TOEFLDRILL.addBank({","source: "+jss(src)+",","questions: ["]
for q in Q:
    out.append("{id:%s, theme:%s, subtheme:%s, ref:%s, passageId:%s,\n instruction:%s,\n question:%s,\n options:%s, answer:%d,\n explain:%s},"%(
        jss(q['id']),jss(q['theme']),jss(q['subtheme']),jss(q['ref']),jss(q['passageId']),
        jss(q['instruction']),jss(q['question']),jss(q['options']),q['answer'],jss(q['explain'])))
out.append("]\n});")
io.open('/mnt/user-data/outputs/TOEFL-Drill-Web/data/bank-12-barron-pulih.js','w',encoding='utf-8').write("\n".join(out)+"\n")
from collections import Counter
print('soal',len(Q),'| kunci',Counter(q['answer'] for q in Q))
