# -*- coding: utf-8 -*-
"""Bank 09: Peterson's — latihan isian diubah jadi pilihan ganda.
Opsi = bentuk kata nyata dari akar yang sama (setara panjang & jenis)."""
import json, io

# (id, subtheme, ref, stem_with_______, [correct, d1, d2, d3], explain)
W = []
def w(i, sub, ref, stem, opts, ex): W.append((i, sub, ref, stem, opts, ex))

# ---------- EXERCISE 18.3 : Adjective vs Adverb / bentuk kata ----------
R='Exercise 18.3'; S='Bentuk Kata (Adjective/Adverb)'
w('pi-183-1',S,R,"In any animal community, herbivores ______ outnumber carnivores.",
  ["greatly","great","greater","greatest"],
  "Yang diterangkan kata kerja <i>outnumber</i>, jadi butuh <b>adverb</b>: <i>greatly</i>.")
w('pi-183-2',S,R,"Floods cause billions of dollars worth of property damage ______.",
  ["annually","annual","annuals","annualized"],
  "Keterangan waktu bagi kata kerja <i>cause</i> harus <b>adverb</b>: <i>annually</i> (= setiap tahun).")
w('pi-183-3',S,R,"______ airmail service in the United States began in 1918.",
  ["Regular","Regularly","Regularity","Regularize"],
  "Kata benda <i>service</i> diterangkan <b>adjective</b>: <i>regular airmail service</i>.")
w('pi-183-4',S,R,"Writer Ernest Hemingway was known for his ______ language and his lively dialogue.",
  ["simple","simply","simplest","simplicity"],
  "Di depan kata benda <i>language</i> dipakai <b>adjective</b>: <i>his simple language</i>.")
w('pi-183-5',S,R,"The tiny coral snake is ______ but deadly.",
  ["beautiful","beautifully","beauty","beautify"],
  "Setelah <i>to be</i>, pelengkap subjek berupa <b>adjective</b>, sejajar dengan <i>deadly</i>.")
w('pi-183-6a',S,R,"______, bauxite is found near the surface, so it is relatively simple to mine.",
  ["Generally","General","Generality","Generalize"],
  "Keterangan yang menerangkan seluruh kalimat memakai <b>adverb</b>: <i>Generally, …</i>")
w('pi-183-6b',S,R,"Generally, bauxite is found near the surface, so it is relatively ______ to mine.",
  ["simple","simply","simpler","simplicity"],
  "Setelah <i>is</i> + <i>relatively</i> tetap butuh <b>adjective</b> sebagai pelengkap: <i>is relatively simple</i>.")
w('pi-183-7',S,R,"The colony of New Hampshire was ______ separated from the Massachusetts Bay Colony in 1692.",
  ["permanently","permanent","permanence","permanency"],
  "Yang diterangkan kata kerja pasif <i>was separated</i>, jadi <b>adverb</b>: <i>permanently</i>.")
w('pi-183-8',S,R,"The most numerous and ______ distributed of all insectivorous animals are the shrews.",
  ["widely","wide","wider","width"],
  "<i>distributed</i> (participle) diterangkan <b>adverb</b>: <i>widely distributed</i>.")
w('pi-183-9',S,R,"The endocrine system functions in ______ relationship with the nervous system.",
  ["close","closely","closer","closeness"],
  "Di dalam frasa <i>in ___ relationship</i>, yang diterangkan kata benda <i>relationship</i> → <b>adjective</b>.")
w('pi-183-10',S,R,"A gap in the Coast Range of California provides ______ access to the San Francisco Bay Area.",
  ["easy","easily","easier","ease"],
  "<i>access</i> adalah kata benda, jadi penjelasnya <b>adjective</b>: <i>easy access</i>.")
w('pi-183-11',S,R,"Mushrooms are found in an ______ range of sizes, colors, and shapes.",
  ["incredible","incredibly","incredibility","incredulous"],
  "Yang diterangkan kata benda <i>range</i> → <b>adjective</b>. (<i>incredulous</i> berarti 'tidak percaya', bukan 'luar biasa'.)")
w('pi-183-12',S,R,"Some airplanes have an automatic pilot that is connected to the airplane’s controls and ______ keeps the plane on course.",
  ["automatically","automatic","automation","automate"],
  "Yang diterangkan kata kerja <i>keeps</i> → <b>adverb</b>: <i>automatically keeps</i>.")
w('pi-183-13a',S,R,"Hats may ______ social status or occupation, as well as being fashion items.",
  ["symbolize","symbolic","symbol","symbolically"],
  "Setelah modal <i>may</i> harus ada <b>kata kerja bentuk dasar</b>: <i>symbolize</i>.")
w('pi-183-13b',S,R,"Hats may symbolize social status or ______, as well as being fashion items.",
  ["occupation","occupational","occupationally","occupy"],
  "Sejajar dengan kata benda <i>status</i>, jadi harus <b>kata benda</b> juga: <i>occupation</i>.")
w('pi-183-14',S,R,"Analgesics are used to ______ pain and reduce fever.",
  ["relieve","relief","relieved","relieving"],
  "Setelah <i>to</i> dan sejajar dengan <i>reduce</i> → <b>kata kerja bentuk dasar</b>: <i>relieve</i>.")
w('pi-183-15a',S,R,"A ______ of the Paiute tribe of Nevada, Sarah Winnemucca worked as a guide and an interpreter.",
  ["member","membership","members","memberships"],
  "Yang dimaksud orangnya, bukan status keanggotaan: <i>a <b>member</b> of the tribe</i>.")
w('pi-183-15b',S,R,"A member of the Paiute tribe of Nevada, Sarah Winnemucca worked as a guide and an ______.",
  ["interpreter","interpret","interpretation","interpretive"],
  "Sejajar dengan <i>a guide</i> (orang), jadi butuh kata benda pelaku: <b>interpreter</b>.")
w('pi-183-16a',S,R,"The earth’s ______ shell is divided into sections called plates, which are constantly in motion.",
  ["outer","out","outing","outward"],
  "Penjelas kata benda <i>shell</i> adalah <b>adjective</b>: <i>the outer shell</i>.")
w('pi-183-16b',S,R,"The earth’s outer shell is divided into sections called plates, which are ______ in motion.",
  ["constantly","constant","constancy","constants"],
  "Menerangkan frasa <i>in motion</i> (bagaimana bergeraknya) → <b>adverb</b>: <i>constantly in motion</i>.")

# ---------- EXERCISE 19.1 : do vs make ----------
R='Exercise 19.1'; S='Kata Rancu: do / make'
w('pi-191-1',S,R,"The tips of high-speed dental drills are ______ of tungsten steel and often contain diamonds.",
  ["made","done","making","doing"],
  "<i>be <b>made</b> of</i> = terbuat dari. <i>done</i> tidak dipakai untuk bahan.")
w('pi-191-2',S,R,"A cottage industry is a form of manufacturing ______ at home.",
  ["done","made","doing","making"],
  "Yang dimaksud 'pekerjaan yang dikerjakan' → <i><b>done</b> at home</i>. <i>made</i> menuntut objek berupa barang jadi.")
w('pi-191-3',S,R,"Margaret Mead ______ fundamental contributions to both the theory and fieldwork of anthropology.",
  ["made","did","done","do"],
  "Frasa tetap: <i><b>make</b> a contribution</i> → bentuk lampaunya <i>made</i>.")
w('pi-191-4',S,R,"Many universities receive grants to ______ research for the federal government.",
  ["do","make","did","made"],
  "Frasa tetap: <i><b>do</b> research</i> (melakukan penelitian).")
w('pi-191-5',S,R,"Research in genetics in the early nineteenth century ______ much to improve agriculture.",
  ["did","made","done","make"],
  "<i><b>do</b> much to…</i> = banyak berperan untuk… Kalimat lampau → <i>did</i>.")
w('pi-191-6',S,R,"Futurologists study current trends to ______ predictions about the future.",
  ["make","do","made","did"],
  "Frasa tetap: <i><b>make</b> a prediction</i>. Setelah <i>to</i> dipakai bentuk dasar.")
w('pi-191-7',S,R,"Filmmaker George Lucas has ______ many advances in the production of motion pictures, especially in the use of special effects.",
  ["made","done","did","do"],
  "<i><b>make</b> advances</i> = mencapai kemajuan. Setelah <i>has</i> dipakai past participle <i>made</i>.")
w('pi-191-8',S,R,"The distinction between wildflowers and weeds is one that is often difficult to ______.",
  ["make","do","made","done"],
  "Frasa tetap: <i><b>make</b> a distinction</i> (membuat pembedaan).")

# ---------- EXERCISE 19.2 : so / such / too / as ----------
R='Exercise 19.2'; S='Kata Rancu: so / such / too / as'
w('pi-192-1',S,R,"The mineral talc is ______ soft that it can be scratched with a fingernail.",
  ["so","such","too","as"],
  "Pola <b>so + adjective + that</b>. <i>such</i> dipakai bila diikuti kata benda.")
w('pi-192-2',S,R,"Oceanographers use robots and unmanned submarines to explore parts of the ocean that are ______ deep for people to explore safely.",
  ["too","so","as","such"],
  "Pola <b>too + adjective + for … to …</b> (terlalu … untuk …). Tidak ada <i>that</i>, jadi bukan <i>so</i>.")
w('pi-192-3',S,R,"______ much paper money was printed during the Revolutionary War that it became almost worthless.",
  ["So","Such","Too","As"],
  "Pola <b>so much/so many + noun + that</b>: <i>So much paper money … that …</i>")
w('pi-192-4',S,R,"The walking stick is an insect with ______ close resemblance to a twig that it escapes the notice of its enemies.",
  ["such a","so a","such","so"],
  "Pola <b>such a + adjective + noun + that</b>: <i>such a close resemblance … that …</i>")
w('pi-192-5',S,R,"At present, solar cells are ______ expensive and inefficient to be used in the commercial generation of electricity.",
  ["too","so","as","such"],
  "Pola <b>too + adjective + to + V</b> = terlalu … untuk …")
w('pi-192-6',S,R,"Acrylic plastics are very hard and are ______ clear as glass.",
  ["as","so","too","such"],
  "Perbandingan setara: <b>as + adjective + as</b>: <i>as clear as glass</i>.")
w('pi-192-7',S,R,"Founded in 1682, Norfolk developed ______ prosperous sea trade that it quickly became the largest town in the colony of Virginia.",
  ["such a","so a","such","so"],
  "Pola <b>such a + adjective + noun + that</b>: <i>such a prosperous sea trade that …</i>")
w('pi-192-8',S,R,"Continental islands are ______ close to continents that their plant and animal life are identical to life on the mainland.",
  ["so","so much","such","too"],
  "Pola <b>so + adjective + that</b>. <i>so much</i> hanya untuk kata benda tak terhitung.")

# ---------- EXERCISE 19.3 : another / other ----------
R='Exercise 19.3'; S='Kata Rancu: another / other'
w('pi-193-1',S,R,"Lightning is a rush of electrical current from a cloud to the ground or from one cloud to ______.",
  ["another","other","others","the other"],
  "<b>another</b> = satu lagi yang tidak tertentu (tunggal). Pasangan lazim: <i>from one … to another</i>.")
w('pi-193-2',S,R,"A ballet dancer’s techniques and skills are very different from those of ______ dancers.",
  ["other","another","others","the other"],
  "Di depan kata benda jamak (<i>dancers</i>) dipakai <b>other</b>; <i>another</i> hanya untuk tunggal.")
w('pi-193-3',S,R,"The commercial center of New York City, the island of Manhattan is joined to the ______ boroughs by bridges and tunnels.",
  ["other","another","others","the others"],
  "Setelah <i>the</i> dan sebelum kata benda jamak dipakai <b>other</b>: <i>the other boroughs</i>.")
w('pi-193-4',S,R,"The legal surrender of a criminal suspect from one state or country to ______ is called extradition.",
  ["another","other","others","the other"],
  "Pola <i>from one … to <b>another</b></i>; <i>another</i> berdiri sendiri sebagai kata ganti tunggal.")
w('pi-193-5',S,R,"Life expectancy for both males and females is higher in Hawaii than it is in any ______ state.",
  ["other","another","others","the other"],
  "Setelah <i>any</i> dipakai <b>other</b>: <i>any other state</i>.")
w('pi-193-6',S,R,"Rocky Mountain spotted fever is one type of disease that is carried by ticks, and Colorado tick fever is ______.",
  ["another","other","others","the other"],
  "Sebagai kata ganti tunggal tak tertentu ('satu lagi') dipakai <b>another</b>.")
w('pi-193-7',S,R,"The art of photography has often been influenced by—and has influenced—______ fine arts.",
  ["other","another","others","the other"],
  "Menerangkan kata benda jamak <i>fine arts</i> → <b>other</b>.")
w('pi-193-8',S,R,"______ than the cheetah, all cats have retractable claws.",
  ["Other","Another","Others","The other"],
  "Frasa tetap <b>other than</b> = selain. Tidak ada bentuk <i>another than</i>.")
w('pi-193-9',S,R,"Few ______ Supreme Court justices have had as much impact on American law as William O. Douglas.",
  ["other","another","others","the other"],
  "Setelah penentu <i>Few</i> + kata benda jamak dipakai <b>other</b>.")

# ---------- EXERCISE 19.4 : many/much/few/little, number/amount ----------
R='Exercise 19.4'; S='Kata Rancu: many / much / few / little'
w('pi-194-1',S,R,"______ industrial products can be made from soybeans.",
  ["Many","Much","Little","A little"],
  "<i>products</i> dapat dihitung dan jamak → <b>Many</b>. <i>Much/little</i> untuk benda tak terhitung.")
w('pi-194-2',S,R,"Desert plants compete fiercely for the ______ available water.",
  ["little","few","many","much"],
  "<i>water</i> tak terhitung, dan maknanya 'sedikit' → <b>little</b>. <i>few</i> hanya untuk benda terhitung.")
w('pi-194-3',S,R,"The American designer Louis Comfort Tiffany took ______ of his inspiration from nature.",
  ["much","many","few","little"],
  "<i>inspiration</i> tak terhitung dan maknanya 'banyak' → <b>much</b>.")
w('pi-194-4',S,R,"A ______ simple precautions can prevent accidents at home and on the job.",
  ["few","little","much","many"],
  "<i>precautions</i> terhitung jamak, dan <i>a</i> menuntut <b>few</b>: <i>a few precautions</i>.")
w('pi-194-5a',S,R,"In a formal debate, the same ______ of people speak for each team, and both teams are granted an equal amount of time in which to make their arguments.",
  ["number","amount","numbers","amounts"],
  "<i>people</i> dapat dihitung → <b>number of</b>. <i>amount of</i> untuk benda tak terhitung.")
w('pi-194-5b',S,R,"In a formal debate, the same number of people speak for each team, and both teams are granted an equal ______ of time in which to make their arguments.",
  ["amount","number","amounts","numbers"],
  "<i>time</i> tak terhitung → <b>amount of time</b>.")
w('pi-194-6',S,R,"Bats do ______ damage to people, livestock, or crops.",
  ["little","few","many","much"],
  "<i>damage</i> tak terhitung; tanpa <i>a</i>, <b>little</b> berarti 'sedikit sekali'.")
w('pi-194-7',S,R,"Even small ______ of zinc can have a significant effect on the growth of plants.",
  ["amounts","numbers","amount","number"],
  "<i>zinc</i> tak terhitung → <b>amounts of</b>; bentuknya jamak karena didahului <i>small</i> tanpa penentu tunggal.")

# ---------- EXERCISE 19.5 : kata rancu campuran ----------
R='Exercise 19.5'; S='Kata Rancu Campuran'
w('pi-195-1',S,R,"In 1941, nylon was first used to make stockings, and the year ______ it was first used to make toothbrush bristles.",
  ["before","ago","past","back"],
  "<b>before</b> menghitung mundur dari titik waktu di kalimat (1941); <i>ago</i> hanya dihitung dari saat sekarang.")
w('pi-195-2',S,R,"The Missouri River is about ______ as long as the Colorado River.",
  ["twice","double","doubled","twofold"],
  "Perbandingan kelipatan memakai <b>twice as … as</b>. <i>double</i> tidak dipakai dalam pola ini.")
w('pi-195-3',S,R,"Catherine Esther Beecher established schools in Connecticut and Ohio, and ______ founded the American Women’s Educational Association.",
  ["afterward","after","aftermath","afters"],
  "Yang dibutuhkan <b>adverb</b> 'sesudah itu' → <i>afterward</i>. <i>after</i> adalah preposisi/konjungsi, harus diikuti objek.")
w('pi-195-4',S,R,"______ antibiotics are antibacterial agents, but some are effective against fungal, protozoal, or yeast infections.",
  ["Most","Almost","Mostly","Utmost"],
  "Di depan kata benda dipakai <b>Most</b>. <i>Almost</i> adalah adverb dan tidak boleh langsung menerangkan kata benda.")
w('pi-195-5',S,R,"At 8 weeks of ______, red foxes begin to get their adult markings.",
  ["age","old","older","aged"],
  "Frasa tetap <b>at … weeks of age</b>. <i>old</i> dipakai pada pola <i>8 weeks old</i>.")
w('pi-195-6',S,R,"Chuck Berry was one of the ______ and most influential performers of rock music.",
  ["earliest","soonest","early","sooner"],
  "Untuk urutan waktu dalam sejarah dipakai <b>early/earliest</b>; <i>soon</i> berarti 'sebentar lagi'.")
w('pi-195-7',S,R,"Long before Columbus, various thinkers believed that the earth was ______.",
  ["round","around","rounded","roundly"],
  "Sebagai pelengkap subjek setelah <i>was</i> dibutuhkan <b>adjective</b> <i>round</i>; <i>around</i> adalah preposisi.")
w('pi-195-8',S,R,"Apricots, ______ smaller than peaches, are known for their delicate taste.",
  ["somewhat","some","something","somehow"],
  "Yang diterangkan bentuk perbandingan <i>smaller</i>, jadi butuh adverb <b>somewhat</b> (= agak).")
w('pi-195-9',S,R,"Huge radio telescopes aimed into space may someday ______ us whether intelligent life exists elsewhere in the universe.",
  ["tell","say","speak","talk"],
  "Hanya <b>tell</b> yang boleh langsung diikuti objek orang: <i>tell us</i>. <i>say</i> butuh <i>to</i>.")
w('pi-195-10',S,R,"Except for humans and apes, all mammals can produce vitamin C in their livers, so they ______ suffer from a lack of it.",
  ["never","ever","always","often"],
  "Karena mereka bisa memproduksi sendiri, maknanya 'tidak pernah' → <b>never</b>. <i>ever</i> tidak berdiri sendiri dalam kalimat positif.")
w('pi-195-11',S,R,"One of Canada’s most beautiful botanical gardens is Butchart Gardens ______ Victoria, British Columbia.",
  ["near","nearly","nearness","nearest"],
  "Yang dibutuhkan preposisi tempat <b>near</b> (= dekat). <i>nearly</i> berarti 'hampir'.")
w('pi-195-12',S,R,"When the Hopi Indians perform the Snake Dance, the dancers handle ______ rattlesnakes.",
  ["live","alive","lively","liveliness"],
  "Di depan kata benda dipakai <b>live</b>; <i>alive</i> hanya boleh sesudah kata kerja, dan <i>lively</i> berarti 'lincah'.")
w('pi-195-13',S,R,"Approximately 85 ______ of the bauxite produced in the United States is mined in Arkansas.",
  ["percent","percentage","percentile","percentages"],
  "Setelah angka dipakai <b>percent</b>; <i>percentage</i> dipakai tanpa angka (<i>a large percentage of</i>).")
w('pi-195-14',S,R,"Artist Clementine Hunter continued to paint until she was more than 100 years ______.",
  ["old","age","aged","older"],
  "Pola umur: <b>… years old</b>. <i>of age</i> harus memakai <i>of</i>.")
w('pi-195-15',S,R,"The period immediately ______ the Civil War is known as Reconstruction.",
  ["after","afterward","aftermath","afters"],
  "Diikuti objek <i>the Civil War</i>, jadi butuh preposisi <b>after</b>, bukan adverb <i>afterward</i>.")
w('pi-195-16',S,R,"The ______ familiar type of pump in use today is the piston pump.",
  ["most","almost","mostly","utmost"],
  "Bentuk superlatif adjective dibentuk dengan <b>most</b>: <i>the most familiar</i>.")

# ---------- EXERCISE 20.1 : Subject-Verb Agreement ----------
R='Exercise 20.1'; S='Kesesuaian Subjek-Kata Kerja'
w('pi-201-1',S,R,"Ethics ______ the study of moral duties, principles, and values.",
  ["is","are","being","to be"],
  "<i>Ethics</i> nama bidang ilmu: berakhiran -s tetapi <b>tunggal</b> → <i>is</i>.")
w('pi-201-2',S,R,"The first bridge to be built with electric lights ______ the Brooklyn Bridge.",
  ["was","were","being","to be"],
  "Subjeknya <i>The first bridge</i> (tunggal); <i>to be built with electric lights</i> hanya keterangan → <b>was</b>.")
w('pi-201-3',S,R,"There ______ two types of calculus, differential and integral.",
  ["are","is","being","to be"],
  "Pada pola <i>There + be</i>, kata kerja mengikuti kata benda sesudahnya: <i>two types</i> (jamak) → <b>are</b>.")
w('pi-201-4',S,R,"George Gershwin, together with his brother Ira, ______ the creator of the first musical comedy to win a Pulitzer Prize.",
  ["was","were","being","to be"],
  "Frasa <i>together with …</i> tidak mengubah jumlah subjek; subjeknya tetap tunggal → <b>was</b>.")
w('pi-201-5',S,R,"In a chess game, the player with the white pieces always ______ first.",
  ["moves","move","moving","to move"],
  "Subjek <i>the player</i> tunggal; <i>with the white pieces</i> hanya frasa preposisi → <b>moves</b>.")
w('pi-201-6',S,R,"Earth and Pluto ______ the only two planets believed to have a single moon.",
  ["are","is","being","to be"],
  "Dua subjek digabung <i>and</i> → jamak → <b>are</b>.")
w('pi-201-7',S,R,"A number of special conditions ______ necessary for the formation of a geyser.",
  ["are","is","being","to be"],
  "<b>A number of</b> + kata benda jamak selalu diikuti kata kerja jamak. (Bandingkan <i>the number of … is</i>.)")
w('pi-201-8',S,R,"Each of the Ice Ages ______ more than a million years long.",
  ["was","were","being","to be"],
  "<i>Each</i> selalu dianggap <b>tunggal</b>, meski diikuti <i>of the Ice Ages</i>.")
w('pi-201-9',S,R,"The battery, along with the alternator and starter, ______ up the electrical system of a car.",
  ["makes","make","making","to make"],
  "Sisipan <i>along with …</i> di antara koma tidak menambah subjek; subjeknya <i>The battery</i> → <b>makes</b>.")
w('pi-201-10',S,R,"Teeth ______ covered with a hard substance called enamel.",
  ["are","is","being","to be"],
  "<i>Teeth</i> adalah bentuk jamak tak beraturan dari <i>tooth</i> → <b>are</b>.")
w('pi-201-11',S,R,"The more-or-less rhythmic succession of economic booms and busts ______ referred to as the business cycle.",
  ["is","are","being","to be"],
  "Inti subjeknya <i>succession</i> (tunggal); <i>of economic booms and busts</i> hanya keterangan → <b>is</b>.")

# ---------- EXERCISE 21.1 : Participles ----------
R='Exercise 21.1'; S='Participle (-ing / -ed)'
w('pi-211-1',S,R,"The largest ______ insects are found in tropical rain forests.",
  ["known","knowing","knew","to know"],
  "Serangga itu 'dikenal' (pasif) → <b>past participle</b> <i>known</i>.")
w('pi-211-2',S,R,"A hummingbird’s heart beats at the ______ rate of 615 beats per minute.",
  ["astonishing","astonished","astonish","to astonish"],
  "<i>rate</i> yang <b>menimbulkan</b> rasa takjub → present participle <i>astonishing</i>. <i>astonished</i> dipakai untuk yang merasakannya.")
w('pi-211-4',S,R,"At the peak of his jump, a pole vaulter performs a series of ______ body motions to clear the bar.",
  ["twisting","twisted","twist","to twist"],
  "Gerakan itu yang <b>melakukan</b> putaran (aktif) → <i>twisting body motions</i>.")
w('pi-211-5',S,R,"Anyone ______ under conditions that cause a heavy loss of perspiration can suffer heat exhaustion.",
  ["working","worked","work","to work"],
  "<i>Anyone</i> yang bekerja (aktif) → present participle <b>working</b> sebagai penjelas di belakang.")
w('pi-211-6',S,R,"A mosquito ______ with blood is carrying twice its own body weight.",
  ["filled","is filled","fills","to fill"],
  "Kalimat sudah punya kata kerja utama <i>is carrying</i>, jadi penjelas subjek berupa <b>past participle</b>: <i>filled with blood</i>.")
w('pi-211-8',S,R,"Sun spots occur in cycles, with the greatest number generally ______ every eleven years.",
  ["appearing","are appearing","appear","appeared"],
  "Setelah pola <i>with + noun</i> dipakai <b>present participle</b>, bukan kata kerja bertakrif.")

# ---------- EXERCISE 22.1 : Infinitive / Gerund / Simple form ----------
R='Exercise 22.1'; S='Infinitive / Gerund / Bentuk Dasar'
w('pi-221-1',S,R,"Sports parachutes are relatively easy ______.",
  ["to control","controlling","controlled","control"],
  "Setelah pola <i>adjective + </i> dipakai <b>infinitive</b>: <i>easy to control</i>.")
w('pi-221-2',S,R,"Sleeve bearings let pistons ______ back and forth.",
  ["move","to move","moving","moved"],
  "Kata kerja <i>let</i> diikuti objek + <b>bentuk dasar</b> tanpa <i>to</i>.")
w('pi-221-3',S,R,"One of the most important steps in ______ a motion picture is film editing.",
  ["producing","to produce","produced","produce"],
  "Setelah preposisi <i>in</i> harus dipakai <b>gerund</b>: <i>in producing</i>.")
w('pi-221-4',S,R,"An opera singer is required ______ a powerful and beautiful voice.",
  ["to have","having","had","have"],
  "<i>be required</i> selalu diikuti <b>infinitive</b>: <i>is required to have</i>.")
w('pi-221-5',S,R,"The Wampanoag Indians taught the Pilgrims how ______ corn.",
  ["to grow","growing","grown","grow"],
  "Pola <i>question word + infinitive</i>: <b>how to grow</b>.")
w('pi-221-6',S,R,"Frogs and certain kinds of birds use their tongues ______ insects.",
  ["to catch","catching","caught","catch"],
  "<b>Infinitive of purpose</b> (untuk apa alat itu dipakai): <i>use their tongues to catch</i>.")
w('pi-221-7',S,R,"Modems permit computers ______ with one another over telephone lines.",
  ["to communicate","communicating","communicated","communicate"],
  "<i>permit</i> diikuti objek + <b>infinitive</b>: <i>permit computers to communicate</i>.")
w('pi-221-8',S,R,"Smells can be more effective than any other sensory stimuli in vividly ______ back memories.",
  ["bringing","to bring","brought","bring"],
  "Setelah preposisi <i>in</i> dipakai <b>gerund</b>: <i>in vividly bringing back</i>.")
w('pi-221-9',S,R,"Isadora Martinez invented a knee transplant that allows people with severe arthritis ______ their knees easily.",
  ["to bend","bending","bent","bend"],
  "<i>allow</i> diikuti objek + <b>infinitive</b>: <i>allows people to bend</i>.")
w('pi-221-10',S,R,"A sudden sound can make a golfer ______ a shot.",
  ["miss","to miss","missing","missed"],
  "<i>make</i> (kausatif) diikuti objek + <b>bentuk dasar</b> tanpa <i>to</i>.")
w('pi-221-11',S,R,"Heavy spring snows may cause the branches of trees ______.",
  ["to snap","snapping","snapped","snap"],
  "<i>cause</i> diikuti objek + <b>infinitive</b>: <i>cause the branches to snap</i>.")
w('pi-221-12',S,R,"Modern race cars store fuel in rubber bladders that are almost impossible ______.",
  ["to rupture","rupturing","ruptured","rupture"],
  "Pola <i>adjective + infinitive</i>: <i>impossible to rupture</i>.")

# ---------- EXERCISE 25.1 : Preposisi ----------
# (kalimat, [(jawaban, [pengecoh x3], penjelasan), ...])
PREPS = [
 ("Wage rates depend %1 part %2 the general prosperity %3 the economy.", [
   ("in",["on","at","for"],"Frasa tetap <b>in part</b> = 'sebagian'."),
   ("on",["in","of","to"],"Kata kerja <i>depend</i> selalu berpasangan dengan <b>on</b>."),
   ("of",["for","in","to"],"Hubungan milik/atribut memakai <b>of</b>: <i>the prosperity of the economy</i>."),
 ]),
 ("%1 an injection to be effective %2 tetanus, it must be administered %3 72 hours %4 the injury.", [
   ("For",["To","In","On"],"Pola <b>For + subjek + to + V</b> untuk menyatakan tujuan/syarat."),
   ("against",["on","to","with"],"<i>effective <b>against</b></i> dipakai untuk melawan penyakit atau kuman."),
   ("within",["by","after","during"],"<b>within</b> 72 hours = dalam tenggat tidak lebih dari 72 jam."),
   ("of",["for","to","with"],"<i>within 72 hours <b>of</b> …</i> — <i>of</i> menandai titik acuan waktunya."),
 ]),
 ("The invention %1 the hand-cranked freezer opened the door %2 commercial ice-cream production, and %3 then, the ice-cream industry has grown %4 a 4-billion-dollar-a-year industry.", [
   ("of",["for","in","to"],"<i>the invention <b>of</b> something</i> — penemu memakai <i>by</i>, benda yang ditemukan memakai <i>of</i>."),
   ("to",["for","at","on"],"Ungkapan tetap <b>open the door to</b> = membuka jalan bagi."),
   ("since",["for","from","by"],"<b>since then</b> berpasangan dengan <i>has grown</i> (present perfect)."),
   ("into",["in","to","onto"],"<i>grow <b>into</b></i> = berkembang menjadi."),
 ]),
 ("%1 the time %2 the Revolutionary War, the North American colonies were merely a long string %3 settlements %4 the Atlantic Coast %5 Maine and Georgia.", [
   ("At",["On","In","By"],"Frasa tetap <b>at the time of</b> = pada masa."),
   ("of",["in","for","with"],"<i>the time <b>of</b> the war</i> — <i>of</i> menghubungkan waktu dengan peristiwanya."),
   ("of",["with","for","in"],"<i>a string <b>of</b> settlements</i> — <i>of</i> menyatakan isi dari kumpulan itu."),
   ("along",["among","across","between"],"<b>along</b> = memanjang mengikuti garis pantai."),
   ("between",["from","among","around"],"<b>between</b> selalu berpasangan dengan <i>and</i>: <i>between Maine and Georgia</i>."),
 ]),
 ("The probability %1 two people %2 a group %3 ten people having birthdays %4 the same day is about one %5 twenty.", [
   ("of",["for","in","to"],"<i>the probability <b>of</b> something</i>."),
   ("in",["on","at","of"],"<i><b>in</b> a group</i> = di dalam suatu kelompok."),
   ("of",["for","in","with"],"<i>a group <b>of</b> ten people</i>."),
   ("on",["in","at","for"],"Hari tertentu memakai <b>on</b>: <i>on the same day</i>."),
   ("in",["of","to","by"],"Perbandingan peluang memakai <b>in</b>: <i>one in twenty</i>."),
 ]),
 ("Showboats were floating theaters that tied up %1 towns %2 the Ohio and Mississippi Rivers to bring entertainment and culture %3 the people %4 the frontier.", [
   ("at",["in","by","from"],"<b>at</b> menandai titik persinggahan: <i>tied up at towns</i>."),
   ("on",["in","at","by"],"Kota di tepi sungai memakai <b>on</b>: <i>towns on the Mississippi</i>."),
   ("to",["at","for","into"],"<i>bring something <b>to</b> someone</i>."),
   ("on",["in","at","along"],"Ungkapan tetap <b>on the frontier</b> = di daerah perbatasan."),
 ]),
 ("Scrimshaw, the practice %1 carving ornate designs on ivory, was first practiced %2 sailors working %3 sail needles while %4 long sea voyages.", [
   ("of",["for","in","to"],"<i>the practice <b>of</b> + V-ing</i>."),
   ("by",["of","with","from"],"Pelaku pada kalimat pasif ditandai <b>by</b>."),
   ("with",["by","in","on"],"Alat yang dipakai ditandai <b>with</b>: <i>working with sail needles</i>."),
   ("on",["in","at","by"],"<i><b>on</b> a voyage</i> = sedang dalam pelayaran."),
 ]),
 ("%1 order %2 an object to be visible, light must travel %3 that object %4 a person’s eyes.", [
   ("In",["On","At","For"],"Pola tetap <b>in order for … to …</b> = agar …"),
   ("for",["to","of","with"],"Dalam pola <i>in order <b>for</b> + subjek + to + V</i>, subjeknya didahului <i>for</i>."),
   ("from",["for","of","out"],"Titik asal ditandai <b>from</b>."),
   ("to",["at","into","onto"],"Titik tujuan ditandai <b>to</b>: <i>travel from … to …</i>"),
 ]),
 ("%1 the 1930s and 1940s, when train travel was %2 its peak, passengers could look forward %3 wonderful meals %4 trains.", [
   ("In",["On","At","By"],"Dekade memakai <b>in</b>: <i>in the 1930s</i>."),
   ("at",["on","in","to"],"Ungkapan tetap <b>at its peak</b> = pada puncaknya."),
   ("to",["for","at","on"],"<i>look forward <b>to</b></i> — <i>to</i> di sini preposisi, diikuti kata benda atau V-ing."),
   ("on",["in","at","by"],"Berada di dalam kendaraan besar memakai <b>on</b>: <i>meals on trains</i>."),
 ]),
 ("%1 the 1960s, op art, which was based %2 scientific theories %3 optics, employed patterns %4 lines and colors that seemed to change shape as the viewer looked %5 them.", [
   ("In",["Since","On","At"],"Kalimatnya lampau sederhana (<i>employed</i>), jadi dipakai <b>In the 1960s</b>; <i>since</i> menuntut present perfect."),
   ("on",["in","at","of"],"Ungkapan tetap <b>be based on</b>."),
   ("of",["for","in","about"],"<i>theories <b>of</b> optics</i> = teori tentang optika."),
   ("of",["in","with","from"],"<i>patterns <b>of</b> lines and colors</i> — <i>of</i> menyatakan bahan penyusun pola."),
   ("at",["on","in","to"],"<i>look <b>at</b></i> = memandang."),
 ]),
 ("The first national convention devoted %1 the issue %2 women’s rights, organized partly %3 Elizabeth Cady Stanton, was held %4 her hometown %5 Seneca Falls, New York, %6 1848.", [
   ("to",["for","on","with"],"<i>be devoted <b>to</b></i> = dikhususkan untuk."),
   ("of",["with","for","about"],"<i>the issue <b>of</b> women’s rights</i>."),
   ("by",["of","from","with"],"Pelaku pada bentuk pasif <i>organized</i> ditandai <b>by</b>."),
   ("in",["on","at","into"],"Tempat berupa kota memakai <b>in</b>: <i>held in her hometown</i>."),
   ("of",["in","at","near"],"<i>her hometown <b>of</b> Seneca Falls</i> — <i>of</i> untuk aposisi nama tempat."),
   ("in",["on","at","by"],"Tahun memakai <b>in</b>: <i>in 1848</i>."),
 ]),
]

# ---- rakit ----
qs=[]
rot=0
def emit(qid, sub, ref, stem, opts, ex):
    global rot
    correct=opts[0]; rest=opts[1:]
    pos=rot % len(opts); rot+=1
    o=rest[:pos]+[correct]+rest[pos:]
    qs.append({"id":qid,"theme":"structure","subtheme":sub,"ref":"Peterson’s TOEFL — "+ref,
               "instruction":"Pilih kata atau frasa yang tepat untuk melengkapi kalimat.",
               "question":stem,"options":o,"answer":pos,"explain":ex})

for (i,sub,ref,stem,opts,ex) in W:
    assert len(set(opts))==len(opts), i
    emit(i,sub,ref,stem,opts,ex)

for si,(tpl,blanks) in enumerate(PREPS,1):
    for bi,(ans,dis,ex) in enumerate(blanks,1):
        stem=tpl
        for j,(a2,_,_) in enumerate(blanks,1):
            stem=stem.replace('%%%d'%j, '______' if j==bi else a2)
        emit('pi-251-%d-%d'%(si,bi),'Preposisi','Peterson’s TOEFL — Exercise 25.1',
             stem,[ans]+dis,ex)

src={"id":"petersons-inline","name":"Peterson’s Master TOEFL (Latihan Isian → Pilihan Ganda)","test":"TOEFL"}
def jss(x): return json.dumps(x,ensure_ascii=False)
out=["/* Bank 09 — Peterson’s: latihan isian diubah menjadi pilihan ganda.",
     "   Opsi disusun dari bentuk kata nyata seakar agar panjang & jenisnya setara. */",
     "TOEFLDRILL.addBank({","source: "+jss(src)+",","questions: ["]
for q in qs:
    out.append("{id:%s, theme:%s, subtheme:%s, ref:%s,\n instruction:%s,\n question:%s,\n options:%s, answer:%d,\n explain:%s},"%(
        jss(q["id"]),jss(q["theme"]),jss(q["subtheme"]),jss(q["ref"]),jss(q["instruction"]),
        jss(q["question"]),jss(q["options"]),q["answer"],jss(q["explain"])))
out.append("]\n});")
io.open('/mnt/user-data/outputs/TOEFL-Drill-Web/data/bank-09-petersons-inline.js','w',encoding='utf-8').write("\n".join(out)+"\n")
from collections import Counter
print("total soal:",len(qs))
print("sebaran kunci:",Counter(q["answer"] for q in qs))
print("per subtema:",Counter(q["subtheme"] for q in qs))
