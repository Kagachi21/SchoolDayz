label day7_Kirana:

    play music istirahat fadein 1.0
    window hide dissolve
    scene sky2 with dissolve
    show day7 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day7 with dissolve
    window show dissolve
    
    scene kamar with dissolve
    stop sound fadeout 1.0
    "Haa.. kemarin benar benar heboh tak kusangka bisa sampai segitunya"
    "Grup di Hp pun ramai masih membahas jalan-jalan ke pantai"
    "Hmmm.. Anak-anak ternyata masih belum tau kejadian kemarin"
    "Padhal mereka tinggal bilang ke lainnya"
    play sound telpon fadein 1.0
    window hide dissolve
    pause 3.0
    window show dissolve
    "Haaa... ngapain si Nada Nelpon"
    stop sound fadeout 1.0
    na "Halo lur"
    mc "Ada apa ?"
    na "Kamu ga jadi ikut ?"
    mc "Ga, kenapa lur ?"
    na "Pasti gara-gara tadi malam"
    mc "Ternyata sudah diceritain ya ?"
    na "Iyaa, sama si [kk]"
    na "yahh,, itu emang tidak sepenuhnya salahmu"
    na "Aku kalau jadi kamu pasti marah juga lah tiba-tiba ungkit masa kelam hahahha"
    mc "Apa aku harus ikut ?"
    na "Ikut saja, kalau ada masalah tenang brader ada aku hahaha"
    mc "Hadeh... okk lah"
    mc "Berangkat kapan ini ?"
    na "Sebentar lagi brader"
    mc "Okk kumpul dimana ntar ?"
    na "Di alun alun"
    mc "Okk"

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Kamu mau kemana ?"
    mc "Berangkat jalan-jalan"
    mom "Kamu gapapa ?"
    mc "Gapapa bu, cuma kemarin terjadi yaa agak gimana gitu ?"
    show dad_uni at center with dissolve:
        xpos 0.665
        ypos 1.2
    dad "Cerita aja gapapa"
    dad "Ayah dan Ibu selalu mendengarkanmu"
    mc "Sigh.. Jadi kemarin setelah dari mall pergi ke cafenya"
    mc "Tiba-tiba [mg2_Last] tanya tentangku dulu"
    mc "Aku sudah ga mau ngulik masa lalu malah dibahas sama dia jadi aku emosi terus aku pulang pesen kojek"
    ai "Hoo.. Jadi begitu"
    mom "Kamu memang ga salah, [mom] selalu mendukungmu tapi [mg2_Last] tidak sepenuhnya salah mungkim ada alasannya"
    dad "Terus gimana itu si [mg2_Last]"
    mc "Ntahlah, aku ga tau"
    mom "Sudah-sudah nanti makin badmood loh pagi-pagi masa anak ibu sudah badmood padahal kamu sudah kembali jadi ceria"
    mc "hahah Iya bu"
    dad "Kalau gitu kita makan aja"
    mc "Okie Selamat makan"
    hide dad_uni with dissolve
    hide mom with dissolve

    scene depan_rumah
    show mom at center with dissolve:
        ypos 1.15
    show dad_uni at center with dissolve:
        xpos 0.665
        ypos 1.2
    dad "Hadapi saja terobos.. Anak Ayah kuat sudah lebih baik daripada yang dulu"
    mom "Abaikan saja klo ada yang mengganggumu \nHajar saja.."
    mc "Terima kasih yah bu, kalau gitu aku berangkat"
    ai "Iyaa hati-hati nak"
    hide dad_uni with dissolve
    hide mom with dissolve

    scene central_park with dissolve
    show nada_cas at center with dissolve:
        ypos 1.2
    na "Oeee oeee [mcFirst]"
    mg2 "...."
    kk "Sudahlah, [mg2_Last]"
    mc "Ini aku yang terakhir apa gimana ?"
    na "Ga, nunggu [skce1] dan [ol]"
    hide nada_cas with dissolve
    mc "Ah..okk"
    wkk "Kalau gitu kita tunggu di FoodCourt aja kuy"
    skco2 "Gass kan"
    kk "Eii.. bilang dulu ke [skce1] dan [ol] nanti kita ke FoodCourt mereka nyariin"
    wkk "Ehh,,, Iyaa yaa ahhaha"
    wkk "Oiyaa,, [mg2_Last] kabarin [ol] aku kabarin si [skce1]"
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Iyaa ya kukabarin"
    hide ardana_cas with dissolve
    mc "....."

    scene foodcourt with dissolve
    kk "Kalian pesan apa ?"
    show nada_cas at center with dissolve:
        ypos 1.2
    na "Aku Jus mangga aja"
    mc "Aku Es Jeruk"
    wkk "Milkshake Oreo"
    skco2 "Es Coklat"
    kk "Okk.. Kalau kamu na ?"
    show ardana_cas at center with dissolve:
        xpos 0.7
        ypos 1.2
    mg2 "Terserah dah"
    kk "Okk random yaa"
    mg2 "Jus Jambu aja dah"
    na "Sekalian pesan Snack Kentang goreng sama Tempe Goreng"
    na "Nunggu mereka pasti lama jadi sekalian nyamil lah"
    wkk "Benar juga"
    skco2 "Beli 3 Kentang gitu 2 Tempe kayaknya cukup"
    kk "Hai hai klo gitu aku mesan dulu"
    wkk "Sudah siap kamera belum ?"
    mg2 "Sudah dong"
    skco2 "Mantap!!"
    kk "Aku sudah pesan tinggal tunggu aja"
    kk "omonng-omong gimana mereka berdua ?"
    mg2 "[ol] baru bangun tapi sebentar lagi berangkat"
    wkk "Kalau [skce1] sudah OTW"
    kk "Okk dah kalau gitu"
    $ ifc = "Ibu-Ibu FoodCourt"
    ifc "ini Pesenannya"
    kk "Terima Kasih bu"
    na "Skuy Libas hahaha"
    na "[mcFirst] Kentangnya bro dimakan jangan lupa"
    mc "Okk"
    hide nada_cas with dissolve
    hide ardana_cas with dissolve
    "~Kami pun menikmati pesanan kami sambil menunggu teman kami~"
    "~Tak Lama kemudian [ol] dan [skce1] datang~"
    ol "Maaf, aku kebablas tidurnya heheh tadi malam habis nonton Drakor"
    show ardana_cas at center with dissolve:
        xpos 0.7
        ypos 1.2
    mg2 "Ihh.. Kamu nih"
    ol "hehehe"
    skce1 "Aku tadi masih bantu bantuin ibu"
    skco2 "Kitaa Gass ga ini apa kalian mau pesan dulu ?"
    ol "Langsung gas aja aku juga sudah makan"
    skce1 "Aku juga sudah makan"
    show nada_cas at center with dissolve:
        ypos 1.2
    na "Kalau gitu gass kita berangkat"
    wkk "Let's Goo"
    hide nada_cas with moveoutleft
    hide ardana_cas with moveoutleft

    stop music fadeout 1.0
    play music pantai fadein 1.0

    scene parkir with dissolve
    ol "Yeay,, Akhirnya sampai juga"
    wkk "Mantap emang"

    scene pantai with dissolve
    bl "Segarnya aroma pantai ini"
    bl "Kita foto dulu atau gimana ?"
    show nada_cas at center with dissolve:
        ypos 1.2
    na "Ganti baju dulu lahh, tapi klo mau foto duluan sih gapapa"
    bl "Mending kita foto duluan saja jadi ada Awal datang sama akhir"
    skce1 "Boleh itu gass keun"
    skco2 "Cari tempat dulu kuy yang cocok buat foto"
    kk "Sini kayaknya cocok cepat sini sini"
    kk "Aku ga sabar mau basah-basahan hahahah"
    bl "Sudah siap kan ?"
    na "Sudah lah"
    hide nada_cas with moveoutleft
    $ sm = "Semuanya"
    sm "Cheesseeee~"
    window hide dissolve
    play sound ambil_foto
    pause 3.0
    stop sound fadeout 1.0
    window show dissolve
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Okk dah kalau gitu skuy ganti baju.. main basah-basahan kita"
    bl "Yuukk!!"
    skce1 "Tunggu akuu!!"
    ol "Aku juga mau ikut oee"
    hide ardana_cas with moveoutright
    wkk "[kk] kamu ga ikut mereka ganti baju ?"
    kk "Aku pake baju ini aja sudah aman kok"
    show nada_cas at center with dissolve:
        ypos 1.2
    na "Wihhh.. Segarnya airnya kuy renang [mcFirst]"
    mc "Okk wait buka baju"
    mc "Gass"
    skco2 "Aku juga ikutan oee"
    hide nada_cas with moveoutleft
    kk "Kamu ga ikut renang ama mereka ?"
    wkk "Bentar lagi, kita bahas dulu cara dekatin mereka berdua lagi"
    kk "Kamu tauu ?"
    wkk "HAhahah,, kelihatan dari wajah mereka berdua"
    kk "Iyaa juga sih lebih canggung sekarang"
    kk "gimana kalau aku saja yang jaga barang-barang kita"
    kk "Nanti gantian aku mau renang juga lah, nanti kan si [mg2_Last] main-main juga kan"
    kk "Kalau bisa kamu dekatin jadi misal mereka berdua dekat kalian ajak yang lainnya pergi"
    wkk "Boleh juga idenya bisaa nihh dicobaa"
    wkk "yaudah aku kesana dulu mau bilang ke anak-anak suruh ikut aku misal [mg2_Last] sudah datang"
    wkk "Yuhuuuu.. Sea I'm coming"
    show nada_cas at center with dissolve:
        ypos 1.2
    na "Hahah segar kan"
    hide nada_cas with dissolve
    kk "Enaknya lihat mereka"
    show ardana_cas at center with moveinright:
        ypos 1.2
    mg2 "[kk] kamu ga renang ?"
    kk "Aku jaga barang-barang dulu"
    kk "Sana dah kalau mau renang nanti gantian yang jaga hehehe"
    mg2 "Kenapa, ga kita berdua saja yang jaga ?"
    kk "Aku aja cukup sana main dulu sambil dinginkan kepalamu itu"
    mg2 "Okie [kk]"
    hide ardana_cas with moveoutleft
    ol "Kami duluann [kk]"
    kk "Iyaa"

    scene pantai with dissolve
    wkk "Kuy kuy ntr lagi ikut aku, explore kita"
    skco2 "Gasskeun"
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Mainn duluan nih bocah hahahha"
    show nada_cas at center with dissolve:
        xpos 0.3
        ypos 1.2
    na "Sini kau"
    "~cepyar~"
    mg2 "Awas kau nada"
    hide ardana_cas with moveoutleft
    na "Pfft,, serbu para ciwi-ciwi gaes"
    hide nada_cas with moveoutright
    skco2 "Lets goo"
    wkk "Kuyy kitaa kaburr pergii"
    mc "Lahh ?"
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "...."
    mc "...."
    ol "yang lain mana ?"
    mg2 "Kabur mereka"
    bl "hohoho sisa 1 disini,, serbuu!!!"
    ol "Gogogogogo"
    mc "Eh eh kok jadi aku"
    mc "Gyahhh.. Blurp~ Blurp~"
    $ all_girls = "[ol], [mg2_Last], [skce1], dan [bl]"
    all_girls "HAhahhahaha"
    hide ardana_cas with dissolve

    scene pantai_siang with dissolve
    kk "Kayaknya berjalan lancarr.."
    wkk "yoo"
    kk "Astaga, kaget aku"
    wkk "Gimana ?"
    kk "Kelihatannya lancar sih"
    wkk "Hahah benar kan syukurlah kalau mendingan"

    scene pantai_siang with dissolve
    "Aku rasa hari fokus bersenang-senang saja lah meskipun ada beberapa problem sama [mg2_Last]"
    "Ga begitu buruk juga, jadi gini rasanya ada teman yang ngesupport juga"
    "Kami pun bergantian yang menjaga barang, bermain di pantai hingga sore pun menyenangkan"

    scene pantai_sore with dissolve
    bl "Kuy foto lagi, foto kenangan diakhir mengunjungi pantai"
    kk "Gas gas berangkat"
    wkk "[ol]... [ol].... ppstt nanti pulang sama yang lainnya aja"
    ol "ehh,, Kenapa ?"
    wkk "Gapapa,, biar [mcFirst] sama [mg2_Last]"
    ol "Iya deh, yang penting pulang hahaha"
    bl "Kalian ini ngomong mulu ga siap-siap"
    wkk "hehehh maaf-maaf"
    bl "1... 2... 3..."
    skce1 "Cepat sini lari lari"
    window hide dissolve
    play sound ambil_foto
    pause 3.0
    stop sound fadeout 1.0
    window show dissolve
    show nada_cas at center with dissolve:
        ypos 1.2
    na "Yokk,, pulang yok pulang"
    hide nada_cas with moveoutleft

    scene parkir_sore with dissolve
    wkk "[mg2_Last] pulangmu bareng [mcFirst]"
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Lah,, kenapa ?"
    mc "...."
    wkk "Soalnya aku langsung pulang beda arah juga kan"
    mg2 "hnnggh.. iya dehh"
    hide ardana_cas with dissolve
    wkk "[mcFirst] kamu ga masalah kan ?"
    mc "Iya gapapa"
    wkk "ppstt psst... [kk]"
    kk "Apa ?"
    wkk "Giamana mantap kan idenya ?"
    kk "Boleh-boleh"
    show nada_cas at center with dissolve:
        ypos 1.2
    na "kalau gitu skuy Pulang"
    hide nada_cas with dissolve
    mc "...."

    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    scene jalan_sore with dissolve
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "[mcFirst] Maaf Yaa yang kemarin"
    mc "Hahh !?"
    mg2 "Maaff yang Kemarin"
    mc "Ohh.."
    mg2 "Aku juga udah berlebihan nanyain hal yang sensitif"
    mg2 "Bodohnya aku, aku minta maaf yaa.. Hiks... Hikss.."
    mc "Ahh..Iyaa.."
    mc "Aku juga minta maaf kayaknya kemarin aku juga berlebihan"
    mg2 "Kamu ga salah kok"
    mg2 "Aku jika ditanyai hal sensitif begitu terus maksa pasti bakalan marah hehe"
    mc "...."
    mc "dah dah.. kita baikan ?"
    mg2 "Huum Hehehhe"
    hide ardana_cas with dissolve

    scene depan_rumah_kirana_sore with dissolve
    mc "Ini rumahmu kan ?"
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Iyaa.. mau mampir ?"
    mc "Ga usah aku pulang dulu aja"
    mg2 "Iyaa.. Hati-hati dijalan yaa"
    mc "Hooh.. iyaa"
    mg2 "bai bai"
    hide ardana_cas with dissolve

    scene ruang_tamu_sore with dissolve
    mc "Aku Pulangg"
    play sound laridilorong fadein 1.0
    window hide dissolve
    pause 3.0
    show mom at center with moveinright:
        ypos 1.15
    window show dissolve
    stop sound fadeout 1.0
    mom "Gimana kamu gapapa ?"
    mc "Aman buu,, ada Nada juga"
    mom "Syukurlahh"
    mc "Ayah.. kemana bu ?"
    mom "Ayahmu nonton tv"
    mc "ohh.. Iya udah aku mau tidur dulu ya bu"
    mc "aku agak capek bu hehhe"
    mom "Iyaa.."
    hide mom with dissolve

    scene kamar_sore with dissolve
    "Huuu Capeknyaaa"
    "Hmm... Kitaa jadi baikan huh"
    "Dahlah aku tidur aja"

    scene kamar_malam with dissolve
    play sound telpon fadein 1.0
    window hide dissolve
    pause 3.0
    window show dissolve
    "Huhh. siapa ini ?"
    "Ahh.. [mg2_Last]"
    stop sound fadeout 1.0
    mc "Ada apa ?"
    mg2 "Hoo Sudah bangun kukira masih tidur"
    mc "Kamu telpon aku jadi bangun"
    mg2 "Hehehehe masih capek"
    mc "Ga terlalu sih tapi masih ingin tidur"
    mg2 "Yaudah.. tidur lagi sana"
    mg2 "Ketemu besokk"
    mc "Iyaa Iyaa"
    mg2 "Bai bai"
    mc "Bai"
    "Huu ? kalau gitu aku tidur lagi aja capek beneran ternyata"

    stop music fadeout 1.0
    play music pagi fadein 1.0
    scene sky with dissolve
    "~Bonus~" with dissolve
    "Kami berdua pun jadian dan lulus bersama lalu bekerja di tempat yang sama"
    "Kami Berdua juga Menikah dan hidup bahagia"

    stop music fadeout 1.0

    jump credits
    
    return

# label day7_Miselia:

 #label day7_Airin:

