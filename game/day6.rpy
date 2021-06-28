label day6_Kirana:
    
    scene kamar with dissolve
    "Hmm.. Sudah pagi ternyata"
    "Oiya, Sekarang hari libur kalau gitu aku bantu orang tuaku"

    scene dapur with dissolve
    mc "Pagi bu"
    show mom at center with dissolve:
        ypos 1.15
    mom "Pagi [mcFirst] "
    mom "Panggil ayahmu ada didepan rumah, bentar lagi makanan sudah siap"
    mc "ahh.. Okk"
    hide mom with dissolve

    scene depan rumah with dissolve
    mc "Yah, Kuy Makan \nMakanannya sudah siap"
    show dad at center with dissolve:
        ypos 1.2
    dad "Okk, bentar aku mau cuci tangan dulu"
    mc "Aku makan duluan"
    hide dad with dissolve

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Gimana ayahmu ?"
    mc "Bentar lagi kesini, kalau gitu aku makan duluan bu"
    show mom at center with dissolve:
        ypos 1.15
        xzoom -1
    show dad at center with moveinleft:
        xpos 0.65
        ypos 1.2
    dad "Mantapp,, ini \nBu Nasinya yang ini ?"
    mom "Iya yah yang itu nasinya"
    mc "Bu aku sudah selsai"
    hide dad with dissolve
    hide mom with dissolve
    play sound cuci_piring
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    window show dissolve
    show mom at center with dissolve:
        ypos 1.15
        xzoom -1
    show dad at center with dissolve:
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
    hide dad with dissolve
    hide mom with dissolve

    scene kamar with dissolve
    "Aku bersihkan kamarku dulu setelah itu ruangan lain"

    scene ruang tamu with dissolve
    #

    scene ruang keluarga with dissolve
    #

    scene kamar mandi with dissolve
    #

    scene dapur with dissolve
    #

    scene ruang keluarga
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

    scene depan rumah with dissolve
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Permisi"
    "~Knock Knock Knock~"
    mg2 "Permisii !!"
    "~Knock Knock Knock~"
    
    scene ruang keluarga
    show dad at center with dissolve:
        xpos 0.6
        ypos 1.2
    dad "Siapa itu bu ?"
    "~Knock Knock Knock~"
    show mom at center with dissolve:
        ypos 1.15
    mom "Mungkin tamu"
    hide dad with dissolve
    hide mom with moveoutleft

    scene depan rumah
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Permisii !"
    "~Knock Knock Knock~"
    show ardana_cas at center with moveinright:
        xpos 0.3
        ypos 1.2
    show mom at center with moveinright:
        ypos 1.15
    mom "Iyaa sebentar"
    mg2 "Halo Tante"
    mom "Oalah, kamu toh"
    show dad at center with moveinright:
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
    hide dad with moveoutright
    hide ardana_cas with moveoutright

    scene ruang keluarga
    show dad at center with moveinleft:
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
    hide dad with dissolve
    hide mom with dissolve

    scene depan kamar
    show ardana_cas at center with moveinleft:
        ypos 1.2
    mg2 "[mcFirst] ayo bangun aku dah sampai ini"
    "~Knock Knock~"
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
    
    scene depan kamar with dissolve
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

    scene ruang keluarga
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
    show dad at center with dissolve:
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
    hide dad with dissolve
    hide mom with dissolve
    hide ardana_cas with moveoutleft

    scene jalan_malam with dissolve
    mc "Tadi ada apa an emangnya ?"
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "ga ada apa-apa"
    mc "Dih, ga mau cerita"
    mg2 "Biarinnn.. Bwekk"
    mc "Awas saja kamu"
    hide ardana_cas with dissolve

    scene parkiran mall with dissolve
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

    scene section baju
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

    scene cafe_malam
    show ardana_cas at center with dissolve:
        ypos 1.2
    mg2 "Mau pesan apa ?"
    mc "Yakult Strawberry aja"
    mg2 "Okk dah kalau gitu"
    hide ardana_cas with moveoutleft
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
    "Sepertinya, [mg2_Last] sudah selsai memesan"
    show ardana_cas at center with moveinleft:
        ypos 1,2
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
    "Tiba-tiba sunyi dan mg2_Last menjadi serius"
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

    scene ruang tamu
    mc "Aku Pulang!"

    scene ruang keluarga
    show mom at center with dissolve:
        ypos 1.15
    mom "Gimana jalan-jalannya ?"
    mc "Ampas"
    mom "Ada apa ?"
    mc "Aku mau tidur duluan aja bu"
    mc "Soalnya capek"
    mom "Iya nak"
    show dad at center with dissolve:
        xpos 0.665
        ypos 1.2
    dad "Ada apa ?"
    mom "Kayaknya ada masalah"
    mom "Aduhh.. sudah mendingan gini jadi ada masalah lagi"
    dad "Semoga anak kita baik-baik saja bu"
    mom "Iyaa yah.. besok mari kita coba dengarkan permasalahannya"
    hide dad with dissolve
    hide mom with dissolve

    jump day7_Kirana

label day6_Miselia:

    scene ruang keluarga
    mc "Wah ibu , sudah mateng aja nih"
    mom "Iya nak , nanti sarapan dulu ya , sana mandi dulu"
    mc "Bu,terimakasih ya sudah memasakan mc makanan yang enak enak setiap pagi"
    dad "Memang ibumu ini the best nak, makanya bapak milih ibumu hehhe"
    mom "Haduh. sama sama , itu sudah kewajiban ibu , sebagai ibumu dan istri ayahmu"
    mc "Hehe, tapi pasti ibu cape ya , tunggu mc jadi orang sukses ya bu , mc janji akan bahagiain ibu dan bapak"
    mom "Iya nak, doa ibu selalu menyertaimu. Ya sudah, makan dulu gih, kalo kurang nambah aja "
    mc"Wah rasanya enak banget bu"
    mom"Alhamdulillah , syukurlah kalo kamu suka nak"
    mc"Bu , aku beraangkat dulu ya , alhamdulillah sudah kenyang , jadi bikin tambah semangat buat belajar hehe"
    mom "Kamu ini bisa aja , yasudah hati hati di jalan ya nak , yang rajin semangat ya. kalau adaapa apa wa ibu ya"

    scene jalan raya
    sa "Nak , sini duduk di depan aja , masih ada bangku kosong khusus buat kamu "
    mc "Baik pak"

    scene lorong Kelas
    mg1 "Mc...."
    mc "Hei .. iya , kamu kok tumben brangkatnya siang?"
    mg1 "Iya , aku dianterin sama mama ku tadi , macet tau di Mastrip"
    mg1 "Kamu udah ngerjain PR belum ?"

    scene kelas 
    mc "Pr apa ? emang ada ya ?"
    mg1 "Iya pr dari Bu sendra , yang kita suruh ngeragkum materi virus tu"
    mc "Oh iya , sudah dong , kamu sudah juga ?"
    mg1 "Iya sama aku juga sudah kok"
    sr "Selamat pagi anak anak, bagaimana kabar hari ini ? semoga baik baik saja ya"
    kk "Pagi bu, Alhamdulillah sehat bu"
    sr "Oh iya , kemaren ibu meminta untuk merangkum materi virus ya ? apa sudah siap untuk di presentasikan?"
    sk "Sudah bu"
    sr "Kalau begitu ibu tunjukk,, mmm kali ini yang maju Mc ya !"
    mc "Baik bu sendra"

    "Materi presentasi virus"

    mg1 "Mc kamu mau ke kantin ga ? ayo bareng kalo mau"
    mc "Iya bentar , aku beresin barangku dulu"

    scene kantin
    mc "Kamu mau beli apa ? minum apa makanan?"
    mg1 "Aku mau beli minuman aja deh di kantinya Bu nunung"
    mc "Oh yaudah aku beli pentol dulu ya"
    mg1 "Kamu ngerasa ga sih , kalau pelajaran makin hari makin susah?"
    mc "Sebenernya bukan tambah sulit sih, cuman ya kita kurang belajar aja"
    mg1 "Hmm, aku tu ya agak maales tau kalo disuruh belajar , kadang cuman aku buka aja nih LKS nya terus yaudah aku tutup lagi haaha"
    mc "Kamu ni, coba dikit dikit biasain suka baca "
    mg1 "Hahaha, iya kalo kamu , gatau mager aja tu kalo disuruh belajar"
    mc "Eh ayo balik ke kelas , tar lagi bel nih"
    mg1 "Iya ayo"

    scene kelas 
    sr "Selamat siang , Assalamualaikum wr. wb"
    sk "Selamat siang bu,Waalaikumsalam wr.wb"
    sr "Anak anak , hari ini Bu sendra akan memberikan kuis ya"
    st "Waduh bu, saya belum belajar kok sudah kuis lagi"
    sr "Hei sinta , namanya latihan kerjakan sendiri sendiri ya , jangan ada yang nyonto"
    st "Iya buuuu"

    "Kuis Virus"
    sr "Okey , karen waktunya sudah habis , dan sudah menunjukkan waktu pulang, silahkan berkemas kemas ya , hai hati di jlan , dan selamat siang aasalamualaikum wr.wb"
    sk "Iya buu, waalaikumsalam wr.wb"

    scene lorong
    mg1 "Kamu mau pulang bareng aku ?"
    mc "Engga sel aku di jemput sama bapakku kok, makasih tawarannya ya"
    mg1"Oalah, yauda deh kalo gitu aku duuluan ke parkiran ya"
    mc "Iyaa kamu hti hati ya "

    scene jalan raya 
    dad "Gimana sekolah kamu nak?"
    mc "Alhamdulillah pak, lancar tadi"    
    dad "Apa kamu masih sering di jaili nak sama orang lain?"
    mc "Hm.. engga kok pak , aman aku di sekolaah"
    dad "Jangan bohong sama bapak ya , cerita ke bapak kalo ada apa apa nak."
    mc "Iya pak, mc bakalan cerita kok"
    dad "Kamu mau es degan ga ?"
    mc "Boleh pak, bungkus aja sekalian buat ibu juga "
    dad "Oke yasudah ayo kita beli"

    scene warung
    $ ij = "Ibu penjual degan"
    dad "Buk , bungkus es degan nya 3 ya "
    ij "Iya pak, tunggu sebentar ya , mau pake susu semua ?"
    mc "Oh tidak bu , yang satu pakai jeruk nipis ya"
    ij "Oke nak"

    scene jalan raya 
    mc "Ayo pak kita jalan"
    dad "Oke nak"

    scene ruang keluarga 
    mom "Wah kalian bungkus apa ini ?"
    mc "Itu buk, tadi ayah kepengen es degan , jdi bungkus deh"
    dad "Loh , kok ayah orang kamu gitu lo yang pengen hehehe"
    mom "Sudah- sudah , mending kalian segera gantui baju, biar ibu yang nyiapin es degannya"

    jump day7_Miselia

label day6_Airin:

    scene bg jendela kamar terlihat burung
    "Sudah Pagi Ternyata, sebaiknya aku bergegas menuju sekolah"

    scene kamar
    cat "Meoowww Meooww Meooww"
    mc "Hooamm.. Sudah bangun ternyata"
    mc "Jam Berapa ini ?"
    cat "meooww meooww"
    mc "Hoo jam 5.45"
    cat "Meooww"
    mc "Mau Keluar ternyata hahahha.."
    mc "Kuy ke dapur"
    cat "Nyaaaa"

    scene dapur 
    mom "Makanannya belum siap"
    mc "Aku mau ngasih makan [cat] dulu setelah itu mandi"
    cat "Nyaaaa"
    mc "Makann yang banyakk [cat]"
    cat "Nyaaaa Nyaaa Nyaaa"

    scene kamar mandi 
    "Aku lupa mau siapin buat sekolah, sudahlah nanti saja"

    scene kamar
    "Okay,, sudah siap semuanya, tinggal ke dapur terus makan"

    scene dapur
    mc "Sudah, siapp makanannya bu ?"
    mom "Sudah siap dong"
    mc "Ayah dimana ?"
    mom "Ayah didepan rumah lagi siram-siram bunga"
    mc "Okk Kalau gitu aku panggil ayah dulu untuk makan"

    scene depan rumah
    mc "Yah, sarapan dulu.. makanan sudah siap"
    dad "Hooo.. Sebentar lagi kesana makan duluan aja gapapa"
    mc "Okk yah"

    scene dapur 
    mom "Diamana ayah ?"
    mc "Katanya duluan aja, sebentar lagi kesini"
    mc "Aku duluan aja kalau gitu bu makannya"
    mc "Mau berangkat ke sekolah soalnya"
    mom "Iyaa,, bawa bekal ga ?"
    mc "Tidak usah bu"
    mc "Soalnya nanti pulangnya sebentar saja"
    mom "Kalau gitu uang sangu saja ya"
    mc "Iyaa Bu"
    mom "Bentar ibu ambil dulu yaa"
    #Sound Meninggalkan MC
    mc "Lohh.. kakiku ada apa ini ?"
    mc "Ternyata [cat] toh"
    cat "Meoooww"
    mc "Mau makan lagii tah ?"
    cat "Nyyaaa"
    mc "Okie deh kalau gitu aku isi ulang lagi ya"
    cat "Nyaa"
    mom "Ini Uangnya"
    mc "Makasih bu.."
    mc "Aku berangkat dulu bu"
    mom "Hati - hati dijalan"

    scene jalan
    "Tumben ga kelihatan [mg3_First] apa aku terlalu pagi ?"
    "Terbiasa berangkat bersama pagi-pagi jadi ada yang kurang"

    scene gerbang_sekolah
    na "Halo Bro"
    mc "Oh Hi"
    na "mau mampir beli jajan dulu ?"
    mc "ga usah, langsung ke kelas aja"
    mc "Kan hari ini mapelnya ga sebanyak hari lainnya"
    na "Oh iya ya"

    scene kelas
    "[mg3_First] Ternyata belum datang memang aku berangkatnya terlalu pagi"
    "Kalau gitu aku belajar dulu lah"
    "~Ding Dong~"
    na "Dah bel masuk aja, harus siap nih"
    mc "Hahahah sans aja"
    sr "Selamat pagi anak-anak"
    sk "Pagi bu"
    sr "Kemarin kan ada tugas, apakah sudah selsai semua ?"
    sk "Sudah selesai bu Senda"
    sr "Kalau gitu ibu panggil random yang maju duluan"
    sr "Okay, selanjutnya kelompok 4 maju"
    "~Presentasi~"
    "Setelah semua presentasi selesai Bu Senda Memberikan Soal untuk dikerjakan pada kami semua"

    #Initialize score
    $ quiz6_klasifikasi_score = 0

    label quiz6_klasifikasi:

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

        "10. Di bawah ini yang merupakan nama Latin hewan adalah …. \n (1) Musa paradisiaca (3) Phaseolus vulgaris \n (2) Schistocerca americana (4) Canis familiaris"
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
        # Win
        sr "Bagi yang sudah kalian boleh istirahat sampai bel pulang berbunyi"
        sk "Baik bu.."
        # Did he win? Yes.
        #$ quiz4_win = True
        #$ quiz4_lose = False   
    else:
        # Lose
        sr "Bagi yang nilainya jelek kalian bisa mengulang"
        menu:
            "Lanjut":
                $ quiz6_klasifikasi_score = 0
                jump quiz6_klasifikasi
            "Biarin":
                "Kalian gagal sebagai murid"
                "~END~"
                return

    mg3 "Fuuuhh.. Akhirnya sudah selesai \n Oiyaa,, aku ke [mcFirst] dulu"
    mg3 "Sudah selsai ?"
    mc "Sudah lah, mudah ini"
    mg3 "Dihh,, sombong"
    mc "pfftt"
    mg3 "Malah ketawa, oiyaa nanti malam kita jalan - jalan kuy"
    mc "Boleh aja sih"
    mg3 "okk dah berangkat"
    na "Sihuyy mau kemana ini ?"
    mg3 "Ihh.. apaan ?"
    na "Hahahhaah jalan-jalan cie"
    mg3 "Astaga.."
    "~Ding Dong~"
    sr "Bel Sudah berbunyi kalau yang sudah dikumpulin tugasnya"
    sk "Baik bu.."
    mc "Nada titip kumpulin kedepan lah"
    na "Okk dah"
    "Setelah itu semuanya pada ngumpulin tugasnya ke Bu Senda"
    sr "Terima kasih anak-anak \n Kalau gitu kalian boleh pulang"
    sk "Yeaayyy"
    mg3 "Ke atap ?"
    mc "Mau latihan ? \n Boleh"
    na "Bro Pulang duluan"
    kk "Pulang duluan gaes"
    mc "Ohh.. okk"

    scene atap_siang
    mg3 "Aku Mulaii.. dengarkan lohh yaa"
    mc "Iyaa"
    "~Mendengarkan~"
    "Baguss.. Enak didengerin"
    "~Sudah Mendengarkan~"
    mc "Seperti biasa bagus.. Oiyaa,, alasanmu ?"
    mg3 "Heheh nanti saja"
    mc ".... \n okk dah"
    mc "Kalau gitu mari kita pulang"
    mg3 "haii.."

    scene depan rumah
    mc "Aku duluan"
    mg3 "Iyaa.. jangan lupa nanti malam"
    mc "Iyaa.. \n hati-hati dijalan"
    mg3 "Iyaa.."

    scene ruang tamu
    mc "Aku Pulangg!!!"
    mc "tumben [cat] ga datang"

    scene ruang keluarga
    mc "Ternya [cat] tidur toh Hahahaha"
    mom "Iyaa tadi habis makan banyak lalu main sama ibu"
    mc "OIyaa, bu aku langsung tidur saja nanti malam soalnya mau keluar"
    mom "Wiihh.. sama siapa ?"
    mc "sama [mg3_First]"
    mom "Sihuyyy.."
    mc "Ahh.. ibu bisa saja yaudah aku tidur dulu ya bu"
    mom "heheh ibu canda doang.. \n iyaa sana dah tidur duluan"

    scene kamar_siang
    "Saatnya tidur Hahahah bisa-bisanya semuanya cie cie padahal ga ada apa-apa"

    scene kamar_malam
    mg3 "Banguunnn !!! Banguunnn !!! Banguunnn !!!"
    mc "Hmmm... "
    mg3 "Banguunn !!! Bangunnn !!!"
    mc "Hoaamm.. Loh kok kamu tiba-tiba ada disini ?"
    mg3 "Ini sudah malam"
    mc "Ahh iya kah ? \n Kalau gitu aku mau siap-siap dulu"
    mg3 "Kutunggu di ruang keluarga ya ?"
    mc "Iyaaa.."
    "Setelah 20 Menit Kemudian aku pun sudah siap"

    scene ruang keluarga
    mc "Ayo berangkat !!"
    mg3 "Ihh.. Lama banget kayak cewe"
    mc "Mana ada ?"
    mg3 "Tuh,, buktinya lama"
    mc "Kamu aja yang terburu-buru"
    mg3 "Kan sudah malam"
    mom "[dad] lihat mereka berdebat"
    dad "Keren.. Calon Mantu sudah bisa mendominasi"
    mc "Astaga.. Kuy Berangkat"
    mg3 "Awwawawa.. iyaa"

    scene depan rumah
    mc "ini mau kemana emangnya ?"
    mg3 "Jalan-Jalan"
    mc "Sigh.. Jalan kaki ?"
    mg3 "Iyaa kan namanya jalan-jalan sambil cerita"
    mc "Iyaa juga yaa"

    scene jalan_malam
    mc "Oiyaa, ceritain dong alasanmu"
    mg3 "Ihh.. kamu dulu lahh"
    mc "Sighh.. tapi beneran cerita juga lah"
    mg3 "Iyaaa"
    mc "Semuanya berawal dari masuk pertama kali SMP. Semuanya baik-baik saja"
    mg3 "Terus ?"
    mc "Ada murid Idola 1 sekolah.. \n awal-awalnya baik-baik saja.. \n tiba-tiba dia mulai membully hal sekitar ntah karena apa ?"
    mg3 "Dia Bully siapa itu ?"
    mc "Dia bully cewe cakep tapi introvert lalu karena aku tak tahan \n aku menolongnya dari situlah berawal aku selalu dibully menggantikan dia yang awalnya kebully"
    mc "Makin lama makin dibully dan diasingkan dari kelas \n dan tiba-tiba ada laki yang sok kuat membully ku karena dibelakang dia bantuan"
    mc "Jadi mereka selalu membullyku bersamaan dengan cewe tersebut \n dikelas hanya bisa diam ntah kenapa bisa begitu"
    mc "Mungkin karena mereka punya backup an kuat di belakangnya \n Kepala sekolahnya juga busuk dan guru bp nya"
    mc "Cewe yang sebelumnya kubantu pernah membantuku balik tapi mereka membalas lagi \n hingga dia akhirnya ketakutan"
    mg3 "Parah juga,, kenapa kamu ga bilang ortumu ?"
    mc "Aku awalnya selalu menyembunyikan dari ortuku karena ga ingin membuatnya khawatir"
    mc "Makin lama bullynya makin keras hingga bisa merenggut nyawa di sekolah itu yang baik hanya guru di UKS selalu membiarkanku masuk kelas terlambat"
    mc "Pada kelas 3 SMP akhirnya aku ketahuan ortuku dan mereka mengadu terus pihak sekolah bilang mereka tidak apa-apa dan itu cuma bercanda"
    mc "Ortuku tak terima, karena memukul itu juga ga baik akhirnya ortuku memutuskan dengan jalur hukum"
    mc "Aku berhentiin ortuku, karena aku ga mau ngerepotin ortuku juga. sebenarnya untuk masalah uang ga masalah \n tapi ga mau bikin repot juga"
    mg3 "Hiks.. Hikss. selama ini kamu SMP menahan beban besar gitu \n Jadi, itu alasanmu tidak mau berteman dengan yang lainnya"
    mc "Ya bisa jadi begitu,, Setelah itu kami memutuskan untuk Home School \n Yahh,, aku masih merasa trauma dengan apa yang terjadi"
    mc "Aku sebenarnya ga mau mengingatnya"
    mg3 "Maafkan aku hiks hiks membuatmu mengingat kejadian ini"
    mc "Gapapa, tapi sekarang aku merasa lebih baik karena kalian"
    mg3 "Terima kasih,, sebenarnya aku hampir sama sepertimu"
    mg3 "Yeayy,, sudah hampir sampai"

    scene alun-alun_malam
    mc "Kamu kenapa ?"
    mg3 "Beli jajan dulu sama minuman terus cari kursi biar enak"
    mc "Hmm.. Okk"
    "Setelah itu kami memutuskan bersenang-senang dulu di alun-alun"
    mg3 "Fuhhh.. Capeknya"
    mc "Tadi apa yang ingin kamu bilang ?"
    mg3 "Oiyaa,, Alasan aku sering bernyanyi terus \n Jadi, dulu sewaktu SMP aku artis solo dengan nama artis Deline"
    mc "Ahh.. aku pernah tau dengan nama itu"
    mg3 "Aku juga ikut semacam Solo Panduan suara seperti itu lah \n Awalnya baik-baik saja, ga ada masalah sama sekali"
    mg3 "Tiba-tiba ada suatu kasus, Produserku adalah seorang pedofil parah, yang gila aku ga suka"
    mg3 "Aku jadi korban dari produser itu awalnya dia hanya meraba-meraba dan makin lama dia mulai ingin memperkosaku"
    mg3 "Lalu, aku melawan dan lari \n tiba-tiba muncul berita yang tidak benar akhirnya aku dikecam oleh teman-temanku"
    mg3 "Tetangga sekitarku pun juga begitu \n Yah,, aku baik-baik saja karena masih memiliki panduan suara ini"
    mg3 "Tapi aku ga menyangka di panduan suara aku juga di bully \n para anggota pria tersebut melakukan sexual harrastment"
    mg3 "Terus-menerus hingga aku trauma namun sekarang sudah lebih baik tapi masih ada sisa sedikit sebenarnya"
    mc "Sigh.. kenapa dunia bisa begitu kejam kepada kita ?"
    mg3 "Mungkin ini sebuah cobaan ?"
    mc "Bisa jadi hahahaha"

    "Setelah pembicaraan berat kami pun bersenang-senang lagi \n Lalu kami pun pulang kerumah"
    return 