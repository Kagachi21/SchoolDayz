label day6_Kirana:
    
    play music pagi fadein 1.0
    window hide dissolve
    scene sky2 with dissolve
    show day6 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day6 with dissolve
    window show dissolve

    scene kamar with dissolve
    "Hmm.. Sudah pagi ternyata"
    stop sound fadeout 1.0
    play sound burung_terbang fadein 1.0
    window hide dissolve
    pause 3.0
    window show dissolve
    "Oiya, Sekarang hari libur kalau gitu aku bantu orang tuaku"

    scene dapur with dissolve
    mc "Pagi bu"
    show mom at center with dissolve:
        ypos 1.15
    mom "Pagi [mcFirst] "
    mom "Panggil ayahmu ada didepan rumah, bentar lagi makanan sudah siap"
    mc "ahh.. Okk"
    hide mom with dissolve

    scene depan_rumah with dissolve
    mc "Yah, Kuy Makan \nMakanannya sudah siap"
    show dad_cas at center with dissolve:
        ypos 1.2
    dad "Okk, bentar aku mau cuci tangan dulu"
    mc "Aku makan duluan"
    hide dad_cas with dissolve

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Gimana ayahmu ?"
    mc "Bentar lagi kesini, kalau gitu aku makan duluan bu"
    show mom at center with dissolve:
        ypos 1.15
        xzoom -1
    show dad_cas at center with moveinleft:
        xpos 0.65
        ypos 1.2
    dad "Mantapp,, ini \nBu Nasinya yang ini ?"
    mom "Iya yah yang itu nasinya"
    mc "Bu aku sudah selsai"
    hide dad_cas with dissolve
    hide mom with dissolve
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(15.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    show mom at center with dissolve:
        ypos 1.15
        xzoom -1
    show dad_cas at center with dissolve:
        xpos 0.65
        ypos 1.2
    dad "Ga tambah kamu ?"
    mc "Ga, sudah kenyang tadi ambilnya sudah kebanyakan"
    mc "Aku mau bersih-bersih dulu"
    mom "Ga usah, biar ibu saja"
    mc "gapapa, aku ga ada kerjaan soalnya bu"
    mc "Ibu Istirahat saja"
    dad "aku aja kalau gitu"
    mc "Ayah bersihin bagian luar aja"
    dad "Ahh.. Okk"
    hide dad_cas with dissolve
    hide mom with dissolve

    scene kamar with dissolve
    play sound sapu fadein 1.0
    "Aku bersihkan kamarku dulu setelah itu ruangan lain"
    stop sound fadeout 1.0

    scene ruang_tamu with dissolve
    play sound sapu fadein 1.0
    "Sisa Ruang Keluarga, Kamar Mandi, dan dapur"
    stop sound fadeout 1.0

    scene ruang_keluarga with dissolve
    play sound sapu fadein 1.0
    "Sisa Kamar Mandi, dan dapur"
    stop sound fadeout 1.0

    scene kamar_mandi with dissolve
    play sound gosok fadein 1.0
    "Sisa Dapur"
    stop sound fadeout 1.0

    scene dapur with dissolve
    play sound sapu fadein 1.0
    "Sebentar lagi selesai Fyuhh ~"
    stop sound fadeout 1.0

    scene ruang_keluarga_siang with dissolve
    mc "Bu, sudah aku bersihkan bagian dalamnya \nKalau gitu, aku tidur duluan"
    show mom at center with dissolve:
        ypos 1.15
    mom "Iyaa"
    mc "[cat] mana bu ?"
    mom "Kayaknya diluar sama [dad]"
    mc "Ohh.. Okk"
    hide mom with dissolve

    scene kamar_siang with dissolve
    "Siapin baju buat nanti malam sekalian dah"
    "Nanti malam biar langsung berangkat"
    "~Menyiapkan baju~"
    "Done, saatnya tidur"

    stop music fadeout 1.0
    play music sore fadein 1.0

    scene depan_rumah_malam with dissolve
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Permisi"
    play sound ketuk_pintu fadein 1.0
    "Knock Knock Knock"
    stop sound fadeout 1.0
    mg2 "Permisii !!"
    play sound ketuk_pintu fadein 1.0
    "Knock Knock Knock"
    stop sound fadeout 1.0
    
    scene ruang_keluarga_malam with dissolve
    show dad_cas at center with dissolve:
        xpos 0.6
        ypos 1.2
    dad "Siapa itu bu ?"
    play sound ketuk_pintu fadein 1.0
    "Knock Knock Knock"
    stop sound fadeout 1.0
    show mom at center with dissolve:
        ypos 1.15
    mom "Mungkin tamu"
    hide dad_cas with dissolve
    hide mom with moveoutleft

    scene depan_rumah_malam with dissolve
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Permisii !"
    play sound ketuk_pintu fadein 1.0
    "Knock Knock Knock"
    stop sound fadeout 1.0
    show ardana_cas at center with moveinright:
        xpos 0.3
        ypos 1.2
    mom "Iyaa sebentar"
    mg2 "Halo Tante"
    show mom at center with moveinright:
        ypos 1.15
    mom "Oalah, kamu toh"
    show dad_cas at center with moveinright:
        xpos 0.65
        ypos 1.2
    dad "Siapa bu ?"
    mg2 "halo Om"
    dad "Hooo, kamu temannya [mcFirst] yang katanya tante ya"
    mg2 "Hehehe Iyaa om, Tante cerita tah om ?"
    mom "Iyaa aku ceritain hahha"
    mg2 "Ihh tante dasar"
    dad "dah dah, silahkan masuk dulu kayaknya [mcFirst] masih tidur"
    dad "Sekalian bangunin yaa hahah"
    mg2 "Waduh gapapa nih om ?"
    dad "Bangunin aja hehehe"
    mom "nanti kalau mau cari tante atau om ada di ruang keluarga"
    mg2 "Okk Om Te"
    mg2 "Permisi~"
    ai "Silahkan"
    hide mom with moveoutright
    hide dad_cas with moveoutright
    hide ardana_cas with moveoutright

    scene ruang_keluarga_malam with dissolve
    show dad_cas at center with moveinleft:
        xpos 0.65
        ypos 1.2
    show mom at center with moveinleft:
        ypos 1.15
    dad "Cantik juga ya bu hahah.. ga nyangka anak kita yang dulunya pendiam dan trauma sosial"
    dad "Tiba-tiba bawa pulang cewe cantik"
    mom "Hahaha.. Ayah bisa aja"
    mom "Kita doain aja yang terbaik untuk mereka"
    dad "Iya bu, btw, mereka masih temanan ?"
    mom "Iyaa yah, kan ga langsungan pasti masih ada proses kayak kita dulu heheh"
    dad "Ahh.. ibu bisa saja"
    hide dad_cas with dissolve
    hide mom with dissolve

    scene kamar_malam with dissolve
    show ardana_cas at center with moveinleft:
        ypos 1.2
    mg2 "[mcFirst] ayo bangun aku dah sampai ini"
    play sound ketuk_pintu fadein 1.0
    "Knock Knock Knock"
    stop sound fadeout 1.0
    mg2 "Bangunn !!"
    mg2 "Ihh.. ga mau bangun"
    hide ardana_cas with dissolve

    scene kamar_malam with dissolve
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Meoooww Meoooww"
    mc "Ummm.. "
    cat "meoow Meooww"
    hide cat with moveoutbottom
    mc "Hmmm.. ada apa ? loh kok [cat] bisa disini"
    mc "Ehh,, iyaa lupa ga kututup tadii hahah"
    "Bangun!!~"
    mc "Siapa itu kok ga asing banget ?"
    
    scene kamar_malam with dissolve
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Bangun!"
    "~Klek~"
    mg2 "Bang--"
    mc "Apa sih berisik-berisik ? sampai teriak-teriak lagi"
    mc "Loh,, kok tiba-tiba kamu ada disini"
    hide ardana_cas
    show ardana_cas_emosi at center:
        ypos 1.2
    mg2 "Dih.. padahal aku bangunin kamu"
    mg2 "Lah,, kamu lupa ? katanya mau temani aku malam ini"
    mc "Padahal kamu sendiri yang minta temani"
    mg2 "Dasar.. Hmmph"
    mc "Ahh.. Okk klo gitu aku mau salin dulu"
    mg2 "Iyaa.. jangan lama-lama"
    hide ardana_cas_emosi with moveoutleft

    scene ruang_keluarga_malam with dissolve
    show ardana_cas_emosi at center with moveinleft:
        ypos 1.2
    mg2 "Ihh.. si [mcFirst]"
    show mom at center with dissolve:
        xpos 0.35
        ypos 1.15
    mom "Kenapa ?"
    mom "Gimana sudah bangun [mcFirst] ?"
    mg2 "Sudah te"
    mg2 "Masa dibangunin jadi marah-marah"
    show dad_cas at center with dissolve:
        xpos 0.65
        ypos 1.2
    dad "Hahahaha"
    mg2 "Ihh.. Om malah ketawa - ketawa"
    dad "Maaf-Maaf, tapi [mcFirst] jarang kayak gitu"
    ai "Terima kasih ya, [mcFirst] jadi lebih mendingan daripada dulu"
    hide ardana_cas_emosi
    show ardana_cas at center:
        ypos 1.2
    mg2 "Ehh... Terima kasih apa om te ?"
    ai "Hahaha,, gapapa terima kasih telah menjadi teman [mcFirst]"
    mg2 "Ealah,, ga masalah te"
    mc "Hei.. Ayo berangkat aku dah siap nih"
    mc "ibu ma ayah cerita apa ? kok senyum-senyum gitu"
    ai "Ohh gapapa.. sana dah berangkat"
    mg2 "Kalau gitu aku pamit dulu om te"
    mm2 "Kami Berangkat dulu"
    ai "Iya Hati - Hati dijalan"
    hide dad_cas with dissolve
    hide mom with dissolve
    hide ardana_cas with moveoutleft

    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    scene jalan_malam with dissolve
    mc "Tadi ada apa an emangnya ?"
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "ga ada apa-apa"
    mc "Dih, ga mau cerita"
    mg2 "Biarinnn.. Bwekk"
    mc "Awas saja kamu"
    hide ardana_cas with dissolve

    scene parkiran_mall_malam with dissolve
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Yeayy sudah sampai"
    mc "Kalau gitu aku nunggu disini saja"
    mg2 "Ihh.. ya masuk lah"
    mc "Iya-iya aku masuk juga"
    hide ardana_cas with dissolve

    scene mall_malam with dissolve
    mc "Ini kita mau kemana ?"
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Bantuin pilihin baju jadi kita ke bagian baju dulu"
    mg2 "Soalnya ada promo hehehhe"
    mc "Iya iya ayo kesana"
    hide ardana_cas with dissolve

    scene section_baju_malam with dissolve
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Lihat-lihat banyak yang promo"
    mg2 "Yang ini bagus tak ?"
    #show Baju
    mc "Umm. Mayan sih yang ini"
    mg2 "Kalau yang ini gimana bagus tak ?"
    mc "Yang ini lebih mending yang tadi"
    mc "Ohh yang ini menurutku bagus tapi ga ada promo"
    mg2 "Hmm... Cari yang promo lah"
    mc "Iya iyaa"
    mg2 "Inii nihh kyknya bagus"
    mc "Mayan juga tapi bagusan yang tadi"
    mg2 "ihh.. Mayan mulu"
    mc "Hmm.. Kan kamu yang minta pendapat"
    mc "Yaudah,, aku diam aja kalau gitu"
    mg2 "Hehehehe.. canda canda"
    mg2 "Ayo cari lagi"
    "~Setelah 2 Jam Kemudian~"
    mc "[mg2_Last] sini dulu"
    mg2 "Apaa ?"
    mc "Ini bagus bajunya menurutku ada promo jugaa"
    mg2 "Iyaa ini juga bagus kalau gitu aku ambil ini saja"
    mg2 "Ternyata Promonya beli 1 gratis 1"
    mc "Yaudah cari lagi"
    mg2 "Bentar, aku tanya ke mbak - mbaknya"
    $ psb = "Pelayan Mall Bagian Baju"
    mg2 "Permisi kak"
    psb "Iyaa ada apa kak ?"
    mg2 "Mau tanya promo itu kak"
    mg2 "Kan itu Promo beli 1 gratis 1 tapi disebelahnya ada pakaian laki - laki juga"
    mg2 "Itu masuk ke promo beli 1 gratis 1 juga kak ?"
    psb "Iya kak itu masuk ke promo itu juga jadi misal kakak beli baju cewe gratis 1 nya bisa ambil baju cowo kak"
    psb "Tapi nanti harganya pake harga yang mahal kak misal lebih mahal baju yang cowo jadi pakai harga baju yang cowo kak"
    mg2 "Ohh,, Terima kasih kak"
    psb "sama - sama kak"
    mc "Tanya apaan emangnya sudah jelas beli 1 gratis 1 itu"
    mg2 "Oh,, gapapa"
    mg2 "ini kayaknya Bagus buat kamu bajunya"
    mc "Hee.. gausah, itu ga include promo aku juga ga mau beli baju"
    mg2 "Gapapa, Ambil ini apa gimana ?"
    mg2 "Soalnya menurutku ini bagus"
    mc "Sigh.. iyaa dah itu aja kalau kamu memaksa"
    mg2 "Okk ini aja kalau gitu tinggal bayar saja"
    mg2 "Ini kak minta notanya"
    psb "Iya kak sebentar saya buatin dulu"
    psb "Sudah kak, ini notanya"
    mg2 "Makasih kak"
    $ ks = "Kasir Bagian Baju"
    mg2 "Ini Kak"
    ks "Sebentar kak, saya scan notanya"
    "~Tiit Tiit~"
    mg2 "Berapa kak totalnya ?"
    ks "Rp. 159.000 kak"
    mc "hee.. ini aku bayar separuhnya juga"
    mg2 "Gausah, biar aku saja"
    mc "Lah,, kalau gitu aku ga mau ambil bajunya"
    mg2 "Ihh.. Iya iya"
    mc "Ini Rp. 79.500"
    mg2 "Iyaa kalau gitu aku bayar"
    mg2 "ini kak uangnya"
    ks "Uangnya pas ya. Terima kasih banyak kak"
    mg2 "Sama-sama kak"
    mc "Kalau gitu mau kemana lagi ini ?"
    mg2 "Mampir cafe dulu dong kan aku bilang mau traktir"
    mc "Okk dah"
    hide ardana_cas with dissolve

    scene cafe_malam with dissolve
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Mau pesan apa ?"
    mc "Yakult Strawberry aja"
    mg2 "Okk dah kalau gitu"
    hide ardana_cas with moveoutleft
    stop music fadeout 1.0
    play music sore fadein 1.0
    kk "Loh ada [mcFirst] juga"
    mc "lahh ada kamu"
    kk "Hahahah ga nyangka ketemu disini"
    kk "Sama siapa ?"
    mc "sama [mg2_Last]"
    kk "Iya loh, kalian dekat banget aku kira kalian jadian"
    mc "Mana ada ?"
    kk "hahahaha.. Oiya, besok jadi kemana ?"
    mc "Kurang tau juga kayaknya bakalan ke pantai"
    kk "Boleh tuh kalau gitu aku kabarin yang lain juga sama bikin grupnya"
    mc "btw,, kamu sama siapa kesini ?"
    kk "Sama temen-temen rumah hahaha cuma numpang WiFi aja soalnya kenceng disini"
    kk "Mau gabung kumpul dengan ku ?"
    mc "Ga dah, paling aku ga lama-lama disini"
    kk "Okk Kalau gitu selamat bersenang-senang"
    mc "Okk lur"
    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    "Sepertinya, [mg2_Last] sudah selsai memesan"
    show ardana_cas at center with moveinleft:
        ypos 1.2
    mg2 "Tadi kamu ngomong sama siapa ?"
    mc "Aku ngomong sama [kk]"
    mg2 "Ehh.. [kk] ada disini juga"
    mc "Iyaa itu coba lihat yang rame"
    mg2 "Ealah,, ehh.. ini ada grup buat besok"
    mc "Iyaa tadi dia sudah bilang kalau mau buat"
    mc "sana dah kasih tau mau kemana besok"
    mg2 "Ohh iyaa yaa bentar aku chat dulu"
    psc "Ini kak Minuman dan snacknya"
    mc "Banyak amat pesennya ?"
    mg2 "heheheh.. aku lapar karena tadi waktu belanja"
    mc "Astaga.. hahahha"
    stop music fadeout 1.0
    play music bertengkar fadein 1.0
    "Tiba-tiba sunyi dan [mg2_Last] menjadi serius"
    mg2 "Oiyaa, aku mau tanya kamu lulusan SMP XXX kan ?"
    mc "Ga tau aku"
    mg2 "Kamu dulu yang sering kena bully kan ? yang katanya [ad] waktu itu"
    #Sound Sedih
    mc "Kau ngomong apa ?"
    mg2 "Jujur aja"
    mc "Sigh.. Kalau gitu aku pulang dulu"
    mc "Ini Kuncinya sama karcis parkirnya"
    mg2 "Ehh.. tunggu jangan pulang"
    mc "Lahh Terus Kenapa ?!?! serah serah aku dong"
    mc "Memang dulu aku dibully sewaktu SMP Emang aku lulusan sana"
    mc "Selama 3 tahun dibully terus-terusan para guru cuma menghiraukan saja supaya image sekolah ga buruk"
    mc "Makin lama makin jadi"
    mc "Yaaa,, aku pernah masuk rumah sakit dulu karena dibully"
    mc "Mulai dari didorong di tangga, Kursi dikasih paku, Di Sepatu ada Pakunya, masih banyak lagi"
    mc "Ntah kenapa mereka membullyku ? aku juga ga tau !!"
    mc "yang awal masuk sekolah tahun pertama baik saja-saja"
    mc "Tiba-tiba mereka jadi membullyku karena aku tidak memberikan jawaban saat ujian"
    mc "Aku menolak mereka yang ngemis uang padaku karena menurutku itu buruk"
    mc "itulah kenapa aku pindah rumah dengan beli rumah biasa saja ?! aku ga mau kelihatan kaya juga karena ujung-ujungnya dimanfaatkan"
    mc "Kamu tahu !! yang ada malah mereka makin menjadi membully ku"
    mc "Selama aku smp aku sering berobat dan aku selalu diam karena aku takut !!"
    mc "Semuanya hanya mengabaikan dan aku dikucilkan"
    mc "Iyaa aku pernah lihat kamu yang hanya diam dan memberi tatapan sombong"
    mc "Nth kenapa kau tiba-tiba jadi baik sekali"
    mc "Merasa Bersalah waktu kejadian SMP ha !!"
    mc "Tau gitu aku ga ikut atau bawa kendaraan sendiri"
    mg2 "Sudah kuduga itu kamu"
    mg2 "Maaf, aku waktu SMP ga membantumu"
    mg2 "Maaf, waktu itu aku mengabaikanmu ketika kamu membutuhkan pertolongan saat dibully"
    mc "Dah,, lah dah lewat juga buat apa ? kalau gitu aku pulang aja lah tuh baju ambil aja"
    mg2 "Tunggu dulu.. Jangan pulang"
    mc "Ini Uang Minumannya Byee"
    mg2 "Jangan gitu.. Hueeee Hikss.. Hikks.."
    kk "Ehh [mcFirst] jangan gitu ini ditempat umum"
    kk "Aku ga tau permasalahannya kenapa tiba tiba begitu ?"
    kk "[mg2_Last] juga sudah minta maaf.. besok juga mau jalan-jalan"
    mc "Sudahlah aku ga peduli. dia dulu yang mulai "
    mc "Aku Pulang duluan Bye"
    kk "Haaa ?! Kembali sini"
    mg2 "Hikss... Hikss.. Aku salah ya ?"
    kk "Aku ga tau permasalahanmu tapi kamu ga sepenuhnya salah kok"
    mg2 "Besok jalan-jalan gimana untuk besok ? Hikss.. Hiks.."
    kk "Sudah-sudah, untuk besok kalau [mcFirst] ga ikut bilang aja waktu kumpul-kumpul kalau dia sakit"
    mg2 "Iyaa"
    mg2 "Sekarang aku jadi ga mood makan ini semua"
    mg2 "[kk] kamu habisin ya sama teman-temanmu"
    mg2 "Kalau gitu aku pulang duluan"
    mg2 "Terima kasih [kk]"
    kk "Iya sama-sama hati-hati dijalan"
    hide ardana_cas with moveoutleft

    stop music fadeout 1.0
    play music jarak fadein 1.0

    scene ruang_tamu_malam with dissolve
    mc "Aku Pulang!"

    scene ruang_keluarga_malam with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Gimana jalan-jalannya ?"
    mc "Ampas"
    mom "Ada apa ?"
    mc "Aku mau tidur duluan aja bu"
    mc "Soalnya capek"
    mom "Iya nak"
    show dad_cas at center with dissolve:
        xpos 0.665
        ypos 1.2
    dad "Ada apa ?"
    mom "Kayaknya ada masalah"
    mom "Aduhh.. sudah mendingan gini jadi ada masalah lagi"
    dad "Semoga anak kita baik-baik saja bu"
    mom "Iyaa yah.. besok mari kita coba dengarkan permasalahannya"
    hide dad_cas with dissolve
    hide mom with dissolve

    stop music fadeout 1.0

    jump day7_Kirana

    return

# label day6_Miselia:

label day6_Airin:

    play music pagi fadein 1.0
    window hide dissolve
    scene sky2 with dissolve
    show day6 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day6 with dissolve
    window show dissolve
    
    scene kamar with dissolve
    "Sudah Pagi Ternyata, sebaiknya aku bergegas menuju sekolah"
    stop sound fadeout 1.0
    play sound burung_terbang fadein 1.0
    window hide dissolve
    pause 3.0
    window show dissolve
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Meoowww Meooww Meooww"
    mc "Hooamm.. Sudah bangun ternyata"
    mc "Jam Berapa ini ?"
    cat "meooww meooww"
    mc "Hoo jam 5.45"
    cat "Meooww"
    mc "Mau Keluar ternyata hahahha.."
    mc "Kuy ke dapur"
    cat "Nyaaaa"
    hide cat with dissolve

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.2
    mom "Makanannya belum siap"
    mc "Aku mau ngasih makan [cat] dulu setelah itu mandi"
    show mom at center with moveinleft:
        xpos 0.7
        ypos 1.2
        xzoom -1
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Nyaaaa"
    mc "Makann yang banyakk [cat]"
    cat "Nyaaaa Nyaaa Nyaaa"
    hide cat with dissolve

    scene kamar with dissolve
    "Okay,, sudah siap semuanya, tinggal ke dapur terus makan"

    scene dapur with dissolve
    mc "Sudah, siapp makanannya bu ?"
    show mom at center with dissolve:
        ypos 1.2
    mom "Sudah siap dong"
    mc "Ayah dimana ?"
    mom "Ayah didepan rumah lagi siram-siram bunga"
    mc "Okk Kalau gitu aku panggil ayah dulu untuk makan"
    hide mom with dissolve

    scene depan_rumah with dissolve
    mc "Yah, sarapan dulu.. makanan sudah siap"
    show dad_cas at center with dissolve:
        ypos 1.2
    dad "Hooo.. Sebentar lagi kesana makan duluan aja gapapa"
    mc "Okk yah"
    hide dad_cas with dissolve 

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.2
    mom "Dimana ayah ?"
    mc "Katanya duluan aja, sebentar lagi kesini"
    mc "Aku duluan aja kalau gitu bu makannya"
    mc "Mau berangkat ke sekolah soalnya"
    mom "Iyaa,, bawa bekal ga ?"
    mc "Tidak usah bu"
    mc "Soalnya nanti pulangnya sebentar saja"
    mom "Kalau gitu uang sangu saja ya"
    mc "Iyaa Bu"
    mom "Bentar ibu ambil dulu yaa"
    hide mom with moveoutright
    #Sound Meninggalkan MC
    mc "Lohh.. kakiku ada apa ini ?"
    mc "Ternyata [cat] toh"
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Meoooww"
    mc "Mau makan lagii tah ?"
    cat "Nyyaaa"
    mc "Okie deh kalau gitu aku isi ulang lagi ya"
    cat "Nyaa"
    hide cat with dissolve
    show mom at center with moveinright:
        ypos 1.2
    mom "Ini Uangnya"
    mc "Makasih bu.."
    mc "Aku berangkat dulu bu"
    mom "Hati - hati dijalan"
    hide mom with dissolve

    stop music fadeout 1.0
    play music jalan_jalan fadein 1.0

    scene jalan with dissolve
    "Tumben ga kelihatan [mg3_First] apa aku terlalu pagi ?"
    "Terbiasa berangkat bersama pagi-pagi jadi ada yang kurang"

    scene gerbang_sekolah with dissolve
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Halo Bro"
    mc "Oh Hi"
    na "mau mampir beli jajan dulu ?"
    mc "ga usah, langsung ke kelas aja"
    mc "Kan hari ini mapelnya ga sebanyak hari lainnya"
    na "Oh iya ya"
    hide nada_alma with dissolve

    scene kelas with dissolve
    "[mg3_First] Ternyata belum datang memang aku berangkatnya terlalu pagi"
    "Kalau gitu aku belajar dulu lah"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Dah bel masuk aja, harus siap nih"
    mc "Hahahah sans aja"
    hide nada_alma with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat pagi anak-anak"
    sk "Pagi bu"
    sr "Kemarin kan ada tugas, apakah sudah selsai semua ?"
    sk "Sudah selesai bu Senda"
    sr "Kalau gitu ibu panggil random yang maju duluan"
    sr "Okay, selanjutnya kelompok 4 maju"
    hide bu_senda with dissolve
    wkk "Kalau gitu kami mulai presentasinya" with dissolve
    $ _skipping = False
    show nada_alma at center with dissolve:
        ypos 1.2
    na "KINGDOM ANIMALIA (HEWAN)" with dissolve
    na "Hewan merupakan kelompok makhluk hidup yang hidup dengan cara memakan makhluk hidup lain" with dissolve
    na "Perbedaan utama antara hewan dan tumbuhan adalah pada dinding sel yang dimilikinya" with dissolve
    na "Sel-sel tumbuhan memiliki dinding sel, sedangkan sel-sel hewan tidak mempunyai dinding sel" with dissolve
    na "Kingdom animalia dapat dikelompokkan menjadi dua bagian berdasarkan ada tidaknya tulang belakang, yaitu:" with dissolve
    hide nada_alma with dissolve
    bl "Hewan Tidak Bertulang Belakang (Avertebrata): Avertebrata adalah jenis hewan yang tidak mempunyai tulang belakang atau tulang punggung" with dissolve
    bl "Struktur pembentuk atau morfologi seperti sistem pernapasan, sistem peredaran darah pada hewan avertebrata biasanya lebih sederhana dibandingkan hewan vertebrata" with dissolve
    bl "Terdapat 5 kelompok makhluk hidup yang termasuk ke dalam hewan avertebrata yaitu:" with dissolve
    wkk "Porifera (Hewan Berpori): merupakan hewan yang memiliki pori-pori dengan bentuk tubuh seperti spons" with dissolve
    wkk "Hewan jenis ini biasanya hidup di perairan, warna tubuhnya juga bermacam-macam seperti merah, kuning,dan hijau" with dissolve
    wkk "Contoh: Spongilla, Euspongia, Poerion, dan Scypha. Coelenterata (Hewan Berongga)" with dissolve
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Coeloenterata merupakan hewan berongga, memiliki tentakel untuk menangkap mangsa, pada permukaan tentakel terdapat sel beracun yang menyengat" with dissolve
    mg3 "Bentuk tubuh colenterata ada yang berbentuk polip yang melekat di tempat hidupnya dan ada yang berbentuk medusa yang dapat bergerak aktif di dalam air" with dissolve
    mg3 "Contoh: ubur-ubur, bunga karang, obelia, hydra dan anemon." with dissolve
    hide airin_alma with dissolve
    mc "Vermes (Cacing) merupakan hewan yang bertubuh lunak, tak bercabang, dansimetris bilateral" with dissolve
    mc "Vermes dapat dibagi menjadi 3 kelompok berdasarkan bentuk tubuhnya yaitu cacing pipih (Platyhelminthes), cacing gilig (Nemathelminthes) tubuhnya bulat" with dissolve
    mc "panjang dan tidak bersegmen, Annelida tubuhnya beruas-ruas seperti cincin" with dissolve
    mc "Contoh: cacing hati, cacing perut, dan lintah." with dissolve
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Mollusca (Hewan bertubuh lunak): Memiliki tubuh yang lunak, banyak lendir dan terbungkus oleh mantel" with dissolve
    na "Ada juga yang memiliki cangkang untuk menutup dan melindungi tubuh." with dissolve
    na "Contohnya cumi-cumi, gurita, siput, kerang, tiram, dan remis" with dissolve
    hide nada_alma with dissolve
    wkk "Arthropoda (Hewan berbuku-buku) Hewan jenis ini pada bagian tubuhnya bisa dibagi menjadi 3 yaitu kepala, dada dan perut" with dissolve
    wkk "Tubuh arthropoda diselubungi oleh zat kitin yang keras, mempunyai indera yang peka terhadap bau, sentuhan, dan memiliki mta faset (beribu-ribu mata kecil)" with dissolve
    wkk "Contoh: serangga (insecta) seperti belalang, udang-udangan (Crustacea) seperti kepiting, laba-laba (Arachnoidea) seperti kalajengking, dan lipan (Myriapoda) seperti kelabang." with dissolve
    bl "Hewan Bertulang Belakang (Vertebrata) Hewan bertulang belakang (Vertebrata) adalah kelompok hewan yang memiliki tulang belakang atau tulang punggung" with dissolve
    bl "Dari segi keragaman hewan vertebrata lebih sedikit jenisnya dibandingkan hewan avertebrata" with dissolve
    bl "Tubuh hewan vertebrata dapat dibagi menjadi tiga bagian yaitu kepala, badan, dan ekor" with dissolve
    bl "Hewan vertebrata dapat dibagi menjadi 5 kelompok, antara lain:" with dissolve
    bl "Pisces (Ikan), contohnya ikan mas, ikan pari, dan lain-lain."
    mg3 "Amphibia, hewan yang mampu hidup di dua alam darat dan air, contohnya katak." with dissolve
    mg3 "Reptilia, hewan yang berjalan dengan cara merayap, contohnya kura-kura, ular, dan buaya." with dissolve
    mc "Aves (Unggas), hewan yang tubuhnya tertutup oleh bulu, contohnya burung merpati dan ayam" with dissolve
    mc "Mamalia (Hewan Menyusui), hewan yang beranak dan memiliki kelenjar susu, contohnya sapi, kambing, kera, dan orang utan." with dissolve
    $ _skipping = True

    "Setelah semua presentasi selesai Bu Senda Memberikan Soal untuk dikerjakan pada kami semua"
    stop music fadeout 1.0
    play music jalan_jalan2 fadein 1.0

    "~SOAL~" with dissolve
    #Initialize score
    $ quiz6_klasifikasi_score = 0

    label quiz6_klasifikasi:
        $ quick_menu = False

        "1. Berikut ini yang bukan termasuk variasi dalam spesies adalah …."
        menu:
            "A. cara reproduksi":
                $ quiz6_klasifikasi_score += 10
            "B. jenis makanan":
                $ quiz6_klasifikasi_score += 0
            "C. bentuk tubuh":
                $ quiz6_klasifikasi_score += 0
            "D. ukuran tubuh":
                $ quiz6_klasifikasi_score += 0

        "2. Spesies adalah unit dasar dari klasifikasi biologi. Alasan dua individu yang berbeda dikelompokkan dalam satu spesies yang sama adalah …."
        menu:
            "A. mempunyai kesamaan nenek moyang":
                $ quiz6_klasifikasi_score += 0
            "B. mempunyai banyak perbedaan":
                $ quiz6_klasifikasi_score += 0
            "C. dapat saling kawin dan menghasilkan keturunan fertil":
                $ quiz6_klasifikasi_score += 0
            "D. dapat saling kawin dan menghasilkan keturunan fertil":
                $ quiz6_klasifikasi_score += 10 

        "3. Kata maniculata dari nama Latin Felis manuculata domesticus menunjukkan …."
        menu:
            "A. kelas":
                $ quiz6_klasifikasi_score += 0
            "B. Spesies":
                $ quiz6_klasifikasi_score += 0
            "C. genus":
                $ quiz6_klasifikasi_score += 10
            "D. Divisi":
                $ quiz6_klasifikasi_score += 0

        "4. Klasifikasi makhluk hidup dapat didasarkan pada … \n (1) warna kulit (3) ukuran tubuh \n (2) bentuk tubuh (4) cacat tubuh"
        menu:
            "A. Jika (1), (2), dan (3) benar":
                $ quiz6_klasifikasi_score += 10
            "B. Jika (1) dan (3) benar":
                $ quiz6_klasifikasi_score += 0
            "C. Jika (2) dan (4) benar":
                $ quiz6_klasifikasi_score += 0
            "D. Jika (4) saja benar":
                $ quiz6_klasifikasi_score += 0
            
        "5. Ilmu yang mempelajari prinsip dan pengelompokan makhluk hidup disebut …. \n (1) sistematik (3) taksonomi \n (2) takson (4) botani"
        menu:
            "A. Jika (1), (2), dan (3) benar":
                $ quiz6_klasifikasi_score += 0
            "B. Jika (1) dan (3) benar":
                $ quiz6_klasifikasi_score += 10
            "C. Jika (2) dan (4) benar":
                $ quiz6_klasifikasi_score += 0
            "D. Jika semuanya salah":
                $ quiz6_klasifikasi_score += 0

        "6. Mencandra suatu masalah berarti melakukan langkah-langkah mengidentifikasi dan …. \n (1) merumuskan (3) menyimpulkan \n (2) membuat diskripsi (4) memberi nama"
        menu:
            "A. Jika (1), (2), dan (3) benar":
                $ quiz6_klasifikasi_score += 0
            "B. Jika (1) dan (3) benar":
                $ quiz6_klasifikasi_score += 0
            "C. Jika (2) dan (4) benar":
                $ quiz6_klasifikasi_score += 10
            "D. Jika semuanya salah":
                $ quiz6_klasifikasi_score += 0

        "7. Metode yang merupakan dasar dari klasifikasi adalah …. \n (1) survei (3) deskriptif \n (2) kualitatif (4) empiris"
        menu:
            "A. Jika (1), (2), dan (3) benar":
                $ quiz6_klasifikasi_score += 0
            "B. Jika (1) dan (3) benar":
                $ quiz6_klasifikasi_score += 0
            "C. Jika (2) dan (4) benar":
                $ quiz6_klasifikasi_score += 0
            "D. Jika (4) saja benar":
                $ quiz6_klasifikasi_score += 10

        "8. Di bawah ini yang tidak termasuk sistem dalam metode rasional adalah …. \n (1) sistem praktis (3) sistem natural \n (2) sistem artifisial (4) sistem modern"
        menu:
            "A. Jika semuanya salah":
                $ quiz6_klasifikasi_score += 10
            "B. Jika (1) dan (3) benar":
                $ quiz6_klasifikasi_score += 0
            "C. Jika (2) dan (4) benar":
                $ quiz6_klasifikasi_score += 0
            "D. Jika (4) saja benar":
                $ quiz6_klasifikasi_score += 0

        "" (multiple=2)
        "9. Berikut ini yang merupakan pernyataan yang salah adalah …. \n
        (1) Dua atau lebih spesies dengan ciri-ciri tertentu dikelompokkan membentuk takson genus
        \n
        (2) Beberapa famili dengan ciri tertentu dikelompokkan untuk membentuk takson ordo
        \n
        (3) Beberapa genus yang memiliki ciri-ciri tertentu dikelompokkan untuk membentuk takson famili
        \n
        (4) Beberapa kelas yang memiliki ciri-ciri tertentu dikelompokkan untuk membentuk kingdom" (multiple=2)
        menu:
            "A. Jika (1), (2), dan (3) benar":
                $ quiz6_klasifikasi_score += 10
            "B. Jika (1) dan (3) benar":
                $ quiz6_klasifikasi_score += 0
            "C. Jika (2) dan (4) benar":
                $ quiz6_klasifikasi_score += 0
            "D. Jika (4) saja benar":
                $ quiz6_klasifikasi_score += 0

        "10. Di bawah ini yang merupakan nama Latin hewan adalah …. \n(1) Musa paradisiaca (3) Phaseolus vulgaris \n (2) Schistocerca americana (4) Canis familiaris"
        menu:
            "A. Jika (1), (2), dan (3) benar":
                $ quiz6_klasifikasi_score += 0
            "B. Jika (1) dan (3) benar":
                $ quiz6_klasifikasi_score += 0
            "C. Jika (2) dan (4) benar":
                $ quiz6_klasifikasi_score += 10
            "D. Jika semuanya salah":
                $ quiz6_klasifikasi_score += 0

        "Jawaban : 
            \n
            1. A \ \ \ \ 3. C \ \ \ \ 5. B \ \ \ \ 7. D \ \ \ \ 9. A
            \n  
            2. D \ \ \ \ 4. A \ \ \ \ 6. C \ \ \ \ 8. A \ \ \ \ 10. C"

        "Nilaiku adalah [quiz6_klasifikasi_score]"

    # Check the quiz 1 score
    if quiz6_klasifikasi_score >= 75:
        # Win
        $ quick_menu = True
        show bu_senda at center with dissolve:
            ypos 1.2
        sr "Bagi yang sudah kalian boleh istirahat sampai bel pulang berbunyi"
        sk "Baik bu.."
        # Did he win? Yes.
        #$ quiz4_win = True
        #$ quiz4_lose = False   
    else:
        # Lose
        show bu_senda at center with dissolve:
            ypos 1.2
        sr "Bagi yang nilainya jelek kalian bisa mengulang"
        menu:
            "Mengulang":
                $ quiz6_klasifikasi_score = 0
                jump quiz6_klasifikasi
            "Biarin":
                "Kalian gagal sebagai murid"
                "~END~"
                return

    hide bu_senda with dissolve
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Sudah selsai ?"
    mc "Sudah lah, mudah ini"
    mg3 "Dihh,, sombong"
    mc "pfftt"
    mg3 "Malah ketawa, oiyaa nanti malam kita jalan - jalan kuy"
    mc "Boleh aja sih"
    mg3 "okk dah berangkat"
    show airin_alma at center with moveinright:
        xpos 0.3
        ypos 1.2
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Sihuyy mau kemana ini ?"
    mg3 "Ihh.. apaan ?"
    na "Hahahhaah jalan-jalan cie"
    mg3 "Astaga.."
    hide nada_alma with dissolve
    hide airin_alma with dissolve
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Bel Sudah berbunyi kalau yang sudah dikumpulin tugasnya"
    hide bu_senda with dissolve
    sk "Baik bu.."
    mc "Nada titip kumpulin kedepan lah"
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Okk dah"
    hide nada_alma with dissolve
    "Setelah itu semuanya pada ngumpulin tugasnya ke Bu Senda"
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Terima kasih anak-anak \nKalau gitu kalian boleh pulang"
    hide bu_senda with moveoutright
    sk "Yeaayyy"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Ke atap ?"
    mc "Mau latihan ? \nBoleh"
    show nada_alma at center with dissolve:
        xpos 0.7
        ypos 1.2
    na "Bro Pulang duluan"
    hide nada_alma with moveoutright
    kk "Pulang duluan gaes"
    mc "Ohh.. okk"
    hide airin_alma with dissolve

    scene atap_siang with dissolve
    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Aku Mulaii.. dengarkan lohh yaa yang ini sedikit spesial"
    mc "Iyaa"
    stop music fadeout 1.0
    $ _skipping = False
    play music nyanyi fadein 1.0
    "~Mendengarkan Nyanyian~"
    window hide dissolve
    $ renpy.pause(15.0, hard=True)
    window show dissolve
    $ _skipping = True
    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    mc "Seperti biasa bagus.. Oiyaa,, alasanmu ?"
    mg3 "Heheh nanti saja"
    mc ".... \nokk dah"
    mc "Kalau gitu mari kita pulang"
    mg3 "haii.."
    hide airin_alma with dissolve

    stop music fadeout 1.0
    play music pagi fadein 1.0
    scene depan_rumah_siang with dissolve
    mc "Aku duluan"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Iyaa.. jangan lupa nanti malam"
    mc "Iyaa.. \nhati-hati dijalan"
    mg3 "Iyaa.."
    hide airin_alma with moveoutleft

    scene ruang_tamu_siang with dissolve
    mc "Aku Pulangg!!!"
    mc "tumben [cat] ga datang"

    scene ruang_keluarga_siang with dissolve
    mc "Ternya [cat] tidur toh Hahahaha"
    show mom at center with dissolve:
        ypos 1.2
    mom "Iyaa tadi habis makan banyak lalu main sama ibu"
    mc "OIyaa, bu aku langsung tidur saja nanti malam soalnya mau keluar"
    mom "Wiihh.. sama siapa ?"
    mc "sama [mg3_First]"
    mom "Sihuyyy.."
    mc "Ahh.. ibu bisa saja yaudah aku tidur dulu ya bu"
    mom "heheh ibu canda doang.. \niyaa sana dah tidur duluan"
    hide mom with dissolve

    scene kamar_siang with dissolve
    "Saatnya tidur Hahahah bisa-bisanya semuanya cie cie padahal ga ada apa-apa"

    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    scene kamar_malam with dissolve
    show airin_casual with dissolve:
        ypos 1.2
    mg3 "Banguunnn !!! Banguunnn !!! Banguunnn !!!"
    mc "Hmmm... "
    mg3 "Banguunn !!! Bangunnn !!!"
    mc "Hoaamm.. Loh kok kamu tiba-tiba ada disini ?"
    mg3 "Ini sudah malam"
    mc "Ahh iya kah ? \n Kalau gitu aku mau siap-siap dulu"
    mg3 "Kutunggu di ruang keluarga ya ?"
    mc "Iyaaa.."
    hide airin_casual with moveoutright
    "Setelah 20 Menit Kemudian aku pun sudah siap"

    scene ruang_keluarga_malam with dissolve
    mc "Ayo berangkat !!"
    show airin_casual at center with dissolve:
        ypos 1.2
    mg3 "Ihh.. Lama banget kayak cewe"
    mc "Mana ada ?"
    mg3 "Tuh,, buktinya lama"
    mc "Kamu aja yang terburu-buru"
    mg3 "Kan sudah malam"
    show airin_casual at center with dissolve:
        xpos 0.3
        ypos 1.2
    show mom at center with dissolve:
        xpos 0.6
        ypos 1.15
        xzoom -1
    show dad_cas at center with dissolve:
        xpos 0.75
        ypos 1.2
    mom "[dad] lihat mereka berdebat"
    dad "Keren.. Calon Mantu sudah bisa mendominasi"
    mc "Astaga.. Kuy Berangkat"
    mg3 "Awwawawa.. iyaa"
    hide airin_casual with moveoutleft
    hide mom with dissolve
    hide dad_cas with dissolve

    scene depan_rumah_malam with dissolve
    mc "ini mau kemana emangnya ?"
    show airin_casual at center with dissolve:
        ypos 1.2
    mg3 "Jalan-Jalan"
    mc "Sigh.. Jalan kaki ?"
    mg3 "Iyaa kan namanya jalan-jalan sambil cerita"
    hide airin_casual with dissolve
    mc "Iyaa juga yaa"

    scene jalan_malam with dissolve
    stop music fadeout 1.0
    play music istirahat fadein 1.0
    show airin_casual with dissolve:
        ypos 1.2
    mc "Oiyaa, ceritain dong alasanmu"
    mg3 "Ihh.. kamu dulu lahh"
    mc "Sighh.. tapi beneran cerita juga lah"
    mg3 "Iyaaa"
    mc "Semuanya berawal dari masuk pertama kali SMP. Semuanya baik-baik saja"
    mg3 "Terus ?"
    mc "Ada murid Idola 1 sekolah.. \nawal-awalnya baik-baik saja.. \ntiba-tiba dia mulai membully hal sekitar ntah karena apa ?"
    mg3 "Dia Bully siapa itu ?"
    mc "Dia bully cewe cakep tapi introvert lalu karena aku tak tahan \naku menolongnya dari situlah berawal aku selalu dibully menggantikan dia yang awalnya kebully"
    mc "Makin lama makin dibully dan diasingkan dari murid yang ada di kelas \ndan tiba-tiba ada laki yang sok kuat membully ku karena dibelakang dia memiliki bantuan"
    mc "Jadi mereka selalu membullyku bersamaan dengan cewe tersebut \naku dan cewe itu hanya bisa diam di kelas.. ntah kenapa bisa begitu"
    mc "Mungkin karena mereka punya backup an kuat di belakangnya \nKepala sekolahnya juga busuk dan guru bp nya"
    mc "Cewe yang sebelumnya kubantu pernah membantuku balik tapi mereka membalas lagi \nhingga dia akhirnya ketakutan"
    mg3 "Parah juga,, kenapa kamu ga bilang ortumu ?"
    mc "Aku awalnya selalu menyembunyikan dari ortuku karena ga ingin membuatnya khawatir"
    mc "Makin lama bullynya makin keras hingga bisa hampir merenggut nyawa di sekolah itu. \nyang baik hanya guru di UKS selalu membiarkanku masuk kelas terlambat"
    mc "Pada kelas 3 SMP akhirnya aku ketahuan ortuku dan mereka mengadu, terus pihak sekolah bilang mereka tidak apa-apa dan itu cuma bercanda"
    mc "Ortuku tak terima, karena memukul itu juga ga baik akhirnya ortuku memutuskan dengan jalur hukum"
    mc "Aku melarang ortuku, karena aku ga mau ngerepotin ortuku juga. sebenarnya untuk masalah uang ga masalah \ntapi ga mau bikin repot juga"
    mg3 "Hiks.. Hikss. selama ini kamu SMP menahan beban besar gitu \nJadi, itu alasanmu tidak mau berteman dengan yang lainnya"
    mc "Ya bisa jadi begitu,, Setelah itu kami memutuskan untuk Home School \nYahh,, aku masih merasa trauma dengan apa yang terjadi"
    mc "Aku sebenarnya ga mau mengingatnya"
    mg3 "Maafkan aku hiks hiks membuatmu mengingat kejadian ini"
    mc "Gapapa, tapi sekarang aku merasa lebih baik karena kalian"
    mg3 "Terima kasih,, sebenarnya aku hampir sama sepertimu"
    mg3 "Yeayy,, sudah hampir sampai"
    hide airin_casual with dissolve

    scene central_park_malam with dissolve
    show airin_casual at center with dissolve:
        ypos 1.2
    mc "Kamu kenapa ?"
    mg3 "Beli jajan dulu sama minuman terus cari kursi biar enak"
    mc "Hmm.. Okk"
    "Setelah itu kami memutuskan bersenang-senang dulu di alun-alun"
    mg3 "Fuhhh.. Capeknya"
    mc "Tadi apa yang ingin kamu bilang ?"
    mg3 "Oiyaa,, Alasan aku sering bernyanyi terus \nJadi, dulu sewaktu SMP aku artis solo dengan nama artis Deline"
    mc "Ahh.. aku pernah tau dengan nama itu"
    mg3 "Aku juga ikut semacam Solo Paduan suara seperti itu lah \nAwalnya baik-baik saja, ga ada masalah sama sekali"
    mg3 "Tiba-tiba ada suatu kasus, Produserku adalah seorang pedofil parah, dan aku ga suka itu"
    mg3 "Aku jadi korban dari produser itu awalnya dia hanya meraba-meraba dan makin lama dia mulai ingin memperkosaku"
    mg3 "Lalu, aku melawan dan lari \ntiba-tiba muncul berita yang tidak benar akhirnya aku dikecam oleh teman-temanku"
    mg3 "Tetangga sekitarku pun juga begitu \nYah,, aku baik-baik saja karena masih memiliki paduan suara ini"
    mg3 "Tapi aku ga menyangka di paduan suara aku juga di bully \npara anggota pria tersebut melakukan sexual harrastment"
    mg3 "Terus-menerus hingga aku trauma namun sekarang sudah lebih baik tapi masih ada sisa sedikit sebenarnya"
    mc "Sigh.. kenapa dunia bisa begitu kejam kepada kita ?"
    mg3 "Mungkin ini sebuah cobaan ?"
    mc "Bisa jadi hahahaha"
    hide airin_casual with dissolve

    "Setelah pembicaraan berat kami pun bersenang-senang lagi \nLalu kami pun pulang kerumah"

    stop music fadeout 1.0
    play music pagi fadein 1.0
    scene sky with dissolve
    "~Bonus~" with dissolve
    "Setelah lulus [mg3_First] melanjutkan karir bernyanyinya dan sukses"
    "[mg3_First] pun kuliah di Universitas Rapard"
    "Sedangkan aku melanjutkan kuliah di Universitas Poxpord"
    "Setelah Lulus Kuliah kami menikah dan memiliki anak perempuan yang lucu"

    stop music fadeout 1.0

    jump credits

    return 