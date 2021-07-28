label day5_Kirana:

    play music pagi fadein 1.0
    window hide dissolve
    scene sky2 with dissolve
    show day5 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day5 with dissolve
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
    hide cat with moveoutbottom
    mc "Hooamm.. Sudah bangun ternyata"
    mc "Jam Berapa ini ?"
    show cat at center with moveinbottom:
        ypos 0.775
    cat "meooww meooww"
    mc "Hoo jam 5.45"
    cat "Meooww"
    mc "Mau Keluar ternyata hahahha.."
    mc "Kuy ke dapur"
    cat "Nyaaaa"
    hide cat with dissolve

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Makanannya belum siap"
    mc "Aku mau ngasih makan [cat] dulu setelah itu mandi"
    hide mom with dissolve
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Nyaaaa"
    hide cat with moveoutbottom
    mc "Makann yang banyakk [cat]"
    show cat_happy at center with dissolve:
        ypos 0.75
    cat "Nyaaaa Nyaaa Nyaaa"
    hide cat_happy with dissolve

    scene kamar_mandi with dissolve
    play sound mandi fadein 1.0
    "Aku lupa mau siapin buat sekolah, sudahlah nanti saja"
    stop sound fadeout 1.0

    scene kamar with dissolve
    "Okay,, sudah siap semuanya, tinggal ke dapur terus makan"

    scene dapur with dissolve
    mc "Sudah, siapp makanannya bu ?"
    show mom at center with dissolve:
        ypos 1.15
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
        ypos 1.15
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
    hide mom with moveoutright
    #Sound Meninggalkan MC
    mc "Lohh.. kakiku ada apa ini ?"
    mc "Ternyata [cat] toh"
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Meoooww"
    mc "Mau makan lagii tah ?"
    cat "Nyyaaa"
    hide cat with moveoutbottom
    mc "Okie deh kalau gitu aku isi ulang lagi ya"
    show cat_happy at center with dissolve:
        ypos 0.775
    cat "Nyaaaa~~"
    hide cat_happy with dissolve
    show mom at center with moveinright:
        ypos 1.15
    mom "Ini Uangnya"
    mc "Makasih bu.."
    hide mom with dissolve
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    mc "Aku berangkat dulu bu"
    show mom at center with dissolve:
        ypos 1.15
    mom "Hati - hati dijalan"
    hide mom with dissolve

    stop music fadeout 1.0
    play music jalan_jalan fadein 1.0

    scene gerbang_sekolah with dissolve
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Halo Bro"
    mc "Oh Hi"
    na "mau mampir beli jajan dulu ?"
    mc "ga usah, langsung ke kelas aja"
    mc "Kan hari ini mapelnya ga sebanyak hari lainnya"
    na "Oh iya ya"
    hide nada_alma with moveoutleft

    scene kelas with dissolve
    "[mg2_Last] Ternyata belum datang"
    "Kalau gitu aku belajar dulu lah"
    "~Tak Lama Kemudian~"
    show ardana_alma at center with moveinright:
        ypos 1.2
    mg2 "Wihh,, datang duluan langsung belajar"
    mc "...."
    mg2 "Kemarin, gimana kerkelnya ?"
    mc "Kemarin, waktu kerkel 2 anak tidak datang jadi aku sama [bl] saja yang mengerjakan"
    mc "si [st] katanya jalan-jalan ke mall kalau [ad] nthlah ga bisa dihubungi"
    mc "Nthlah, ntr waktu presentasi gimana mereka itu"
    mg2 "Biarin saja sudah yang penting tugasnya sudah selesai"
    mg2 "Misal yang dapat nilai lebih bagus pasti kamu sama [bl]"
    hide ardana_alma with dissolve
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
    $ _skipping = False
    mc "Klasifikasi Virus dibagi menjadi 3 yaitu:" with dissolve
    mc "Berdasarkan Tempat Hidupnya" with dissolve
    bl "Berdasarkan Molekul yang Menyusun Asam Nukleat dan Berdasarkan Punya Tidaknya Selubung Virus" with dissolve
    mc "Berdasarkan tempat hidupnya ada 3 yaitu:" with dissolve
    mc "Virus bakteri (bakteriofage)"
    mc "Bakteriofage merupakan virus yang dapat menggandakan dirinya sendiri dengan menyerbu bakteri" with dissolve
    mc "Dibandingkan dengan kebanyakan virus , virus ini sangat kompleks serta mempunyai beberapa bagian berbeda yang diatut secara cermat" with dissolve
    mc "Virus bakteriofage mula-mula ditemukan oleh ilmuwan Perancis, D’Herelle. Bentuk luar terdiri atas kepala yang berbentuk heksagonal, leher, serta ekor" with dissolve
    mc "Bagian dalam kepala mengandung dua pilihan DNA . Bagian leher berfungsi untuk memasukkan DNA irus ke dalam sel inangnya" with dissolve
    mc "Virus tumbuhan" with dissolve
    mc "Virus yang berparasit pada sel tumbuhan . Contoh virus yang parasit pada tumbuhan : Tobacco Mozaic Virus (TMV0 serta Beet Yellow Virus (BYV)" with dissolve
    mc "Virus Hewan" with dissolve
    mc "Virus yang berparasit pada sel hewan. Contoh virus yang ada pada hewan : virus Poliomylitis, virus Vaccina, dan virus Influenza." with dissolve
    mc "Selanjutnya" with dissolve
    bl "Berdasarkan Molekul yang Menyusun Asam Nukleat dibedakan menjadi 3 yaitu:" with dissolve
    bl "DNA pita tunggal (DNA ss) DNA pita ganda, (DNA ds), RNA iota tunggal (RNA ss), dan RNA pita ganda (RNA ds)" with dissolve
    bl "Selanjutnya" with dissolve
    bl "Berdasarkan Punya Tidaknya Selubung Virus Dapat dibedakan menjadi dua tipe, yaitu:" with dissolve
    bl "Virus yang memiliki selubung atau sampul (enveloped virus)" with dissolve
    bl "Virus ini meiliki nukleokapsid yang dibungkus oleh membrane. Membrane terdiri dari dua lipid serta protein, (biasanya glikoprotein)" with dissolve
    bl "Membrane ini berfungsi sebagai struktur yang pertama-tama berinteraksi. Contoh Herpesvirus, Corronavirus, dan Orthomuxovirus" with dissolve
    bl "Virus yang tidak memiliki selubung" with dissolve
    bl "Hanya memiliki capsid(protein) serta asam nukleat(naked virus). Contoh: Reovirus, Papovirus, dan Adenovirus" with dissolve
    bl "Selanjutnya" with dissolve
    mc "Perkembangbiakan Virus dibagi menjadi 2 macam yaitu:" with dissolve
    mc "Daur Litik \nFase yang dilalui daur litik sebagai berikut:" with dissolve
    mc "1. Virus menempel pada dinding sel bakteri \n2. DNA virus dimasukkan ke dalam dinding sel bakteri yang telah dilubangi dan dilarutkan oleh enzim virus." with dissolve
    mc "3. DNA virus melakukan transkripsi di dalam sel bakteri dan menggunakan metabolik bakteri untuk menghasilkan komponen atau struktur virus seperti kapsid, ekor, serabut ekor, dan kepala" with dissolve
    mc "Virus baru yang tebentuk dalam satu kali daur litik dapat mencapai 200-1000 virus" with dissolve
    mc "4. Virus baru yang terbentuk akan mengeluarkan enzim lisozim untuk melisiskan dan menghancurkan dinding sel bakteri agar dapat menginfeksi dan mengulangi daur litik pada sel bakteri lainnya" with dissolve
    mc "Untuk menghasilkan virus baru pada satu kali daur litik, membutuhkan waktu hanya dalam 20 menit" with dissolve
    mc "Selanjutnya" with dissolve
    bl "Daur Lisogenik" with dissolve
    bl "Tidak semua virus yang masuk ke dalam dinding sel makhluk hidup dapat langsung menghancurkan dan melisiskan dinnding tersebut" with dissolve
    bl "DNA virus yang masuk dalam bakteri akan menjadi bagian dari DNA inang melalui rekombinasi" with dissolve
    bl "Namun, meskipun sudah menjadi bagian DNA inang, virus tidak langsung mengambil alih metabolisme sel inang tersebut" with dissolve
    bl "Daur seperti itulah yang disebut dengan daur lisogenik. Berikut fase yang dilakukan oleh virus pada daur lisogenik:" with dissolve
    bl "1. Virus hidup pada tempat yang spesifik di permukaan sel bakteri untuk dapat melisiskan dinding sel tersebut dan melakukan penetrasi materi genetik ke dalam tubuh sel bakteri." with dissolve
    bl "2. DNA virus kemudian menyisip kedalam DNA bakteri dan membentuk profage." with dissolve
    bl "3. Jika bakteri membelah diri, maka profage di dalam sel tersebut juga akan ikut membelah. Sehingga nantinya jumlah bakteri yang mengandung profage juga akan semakin banyak" with dissolve
    bl "Jika lingkungan mendukung, virus akan mengalami pematangan dan akan memasuki keadaan litik."
    bl "4. Virus baru terbentuk dan siap menyerang sel lainnya." with dissolve
    bl "Selanjutnya" with dissolve
    mc "Per-" with dissolve
    stop music fadeout 1.0
    play music jarak fadein 1.0
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Kok mulai tadi kalian berdua saja yang presentasi ? \nCoba giliran [st] dan [ad] yang menjelaskan"
    st "Hmm.. Per.. Peran Virus.. Ada berapa ya ?"
    st "Hehehhehehe"
    sk "Hahahahahhaha"
    sr "Astaga, kelihatan [st] ga ikut belajar kelompok"
    st "Hehhehehe.. Maaf, bu.. \nSaya menyesal"
    sr "Kalau gitu coba [ad]"
    ad "Aduhh.. bu.."
    sr "Kenapa ? \nPerut sakit ?"
    ad "Iyaa.. Bu.."
    sr "Alasann saja \nKalian Berdua setelah pulang sekolah harus ke ruang guru"
    $ sta = "Shinta dan Ardi"
    sta "Iya bu.."
    st "Aduhh.. gimana nih ? \nKena Hukum kita"
    ad "Salahmu nih.. ngajak aku jalan-jalan"
    st "Aku ga tau kalau bakal gini"
    ad "Yaudah, kalau gitu.. \nmau gimana lagi ?"
    sr "Ssstt.. kalian berdua \nAyo [mcFirst] dan [bl] lanjutkan presentasi kalian"
    stop music fadeout 1.0
    play music jalan_jalan2 fadein 1.0
    hide bu_senda with dissolve
    mc "Peran Virus bagi Kehidupan" with dissolve
    mc "A. Virus yang Menguntungkan:" with dissolve
    mc "1.Untuk membuat antitoksin. \n2. Untuk melemahkan bakteri. \n3. Untuk reproduksi vaksin." with dissolve
    bl "B. Virus yang Merugikan:" with dissolve
    bl "1. Menyebabkan penyakit pada manusia. \n2. Menyebabkan penyakit pada hewan. \n3. Menyebabkan penyakit pada tumbuhan." with dissolve
    bl "Sekian dari kelompok kami ~ Terima kasih telah memperhatikan presentasi kami" with dissolve
    "Setelah semuanya presentasi selesai Bu Senda Memberikan Soal untuk dikerjakan pada kami semua" 
    $ _skipping = True

    "~SOAL~" with dissolve

    #Initialize score
    $ quiz5_score = 0

    label quiz5:
        
        $ quick_menu = False

        "1. Ciri khas virus yang tidak terdapat pada organisme lain adalah…."
        menu:
            "A. memiliki DNA dan RNA":
                $ quiz5_score += 0
            "B. bentuknya beraneka ragam":
                $ quiz5_score += 0
            "C. hanya dapat berkembang biak dalam satu sel hidup":
                $ quiz5_score += 8
            "D. bersifat parasit":
                $ quiz5_score += 0

        "2. Bentuk virus yang menyerang bakteri (bakteriofage) adalah…."
        menu:
            "A. tumor pada hewan":
                $ quiz5_score += 0
            "B. flu burung":
                $ quiz5_score += 0
            "C. Bentuk T":
                $ quiz5_score += 8
            "D. polio":
                $ quiz5_score += 0 

        "Yang termasuk asam inti RNA adalah.." (multiple=2)
        "3. Macam-macam virus diantaranya:
            \n
            (1) Simplexvirus
            \n
            (2) Bakteriofag
            \n
            (3) Lyssavirus
            \n
            (4) Enterovirus
            \n
            (5) Ortohepadnavirus" (multiple=2)
        menu:
            "A. Semuanya Benar":
                $ quiz5_score += 0
            "B. 3,4, dan 5":
                $ quiz5_score += 8
            "C. 1,2,3, dan 4":
                $ quiz5_score += 0
            "D. 2,3, dan 5":
                $ quiz5_score += 0
        
        "4. Virus tidak dapat masuk dalam kelompok makhluk hidup karena .... "
        menu:
            "A. virus dapat bergerak ":
                $ quiz5_score += 0
            "B. virus dapat melakukan pembuahan ":
                $ quiz5_score += 0
            "C. virus dapat berkembang biaki":
                $ quiz5_score += 0
            "D. virus dapat dikristalkan":
                $ quiz5_score += 8
        
        "5. Ukuran virus sangat kecil, yaitu .... "
        menu:
            "A. 20 – 300 milimikron":
                $ quiz5_score += 8
            "B. <10 milimikron":
                $ quiz5_score += 0
            "C. 1 – 3 milimikron":
                $ quiz5_score += 0
            "D. 10 milimikron ":
                $ quiz5_score += 0

        "6. Virus mengambil alih fungsi DNA bakteri. Tujuan tindakan virus ini adalah...."
        menu:
            "A. mensintesis protein dan membuat struktur tubuh virus yang baru ":
                $ quiz5_score += 8
            "B. agar DNA bakteri melakukan replikasi sebagai persiapan pembelahan sel ":
                $ quiz5_score += 0
            "C. untuk mengaktifkan inti sel bakteri hingga dapat memproduksi enzim baru ":
                $ quiz5_score += 0
            "D. melipatgandakan bakteri":
                $ quiz5_score += 0

        "7. Bagian yang tidak dimiliki oleh virus adalah .... "
        menu:
            "A. selubung protein":
                $ quiz5_score += 8
            "B. membran sel":
                $ quiz5_score += 0
            "C. inti sel":
                $ quiz5_score += 0
            "D. organel sel":
                $ quiz5_score += 0

        "8. Ekor virus menempel pada dinding bakteri terjadi pada tahap ..."
        menu:
            "A. sintesis":
                $ quiz5_score += 0
            "B. injeksi ":
                $ quiz5_score += 0
            "C. melebur":
                $ quiz5_score += 0
            "D. adsorpsi":
                $ quiz5_score += 8

        "9. Dalam suatu larutan terdapat virus dan bakteri. Cara memisahkan bakteri dan virus tersebut adalah .... "
        menu:
            "A. memasukkan antibiotik ke dalam larutan agar bakteri mati ":
                $ quiz5_score += 0
            "B. menyaring larutan menggunakan saringan biasa agar virus dapat lolos":
                $ quiz5_score += 0
            "C. menyaring larutan menggunakan saringan keramik ":
                $ quiz5_score += 8
            "D. memasukkan sel hidup untuk inang virus ":
                $ quiz5_score += 0

        "10. Virus yang hanya menyerang kera dan manusia dengan gejala pendarahan di dalam dan di luar tubuh disebut dengan virus .... "
        menu:
            "A. demam berdarah r":
                $ quiz5_score += 0
            "B. kanker ":
                $ quiz5_score += 0
            "C. ebola":
                $ quiz5_score += 8
            "D. hepatitis ":
                $ quiz5_score += 0

        "11. Penyakit cacar air disebabkan oleh virus .... "
        menu:
            "A. E. coli ":
                $ quiz5_score += 0
            "B. Variola ":
                $ quiz5_score += 0
            "C. Mata belek ":
                $ quiz5_score += 0
            "D. Varisela":
                $ quiz5_score += 8

        "12. Sintesis DNA virus terjadi di dalam .... "
        menu:
            "A. di alam bebas ":
                $ quiz5_score += 0
            "B. tubuh inang ":
                $ quiz5_score += 8
            "C. tubuh virus dan inang ":
                $ quiz5_score += 0
            "D. ekor virus ":
                $ quiz5_score += 0

        show virusd5 at center with dissolve:
            ypos 0.725
        "13. Perhatikan tabel di atas ini!
        \nPasangan yang tepat antara virus dan peranan yang merugikan pada manusia adalah ...."
        menu:
            "A. 1B - 2A - 3D - 4E - 5C":
                $ quiz5_score += 8
            "B. 1C - 2A - 3D - 4B - 5E":
                $ quiz5_score += 0
            "C. 1D - 2B - 3A - 4E - 5C":
                $ quiz5_score += 0
            "D. 1B - 2A - 3D - 4E - 5C":
                $ quiz5_score += 0
        hide virusd5 with dissolve

        "14. Virus diamati dengan jelas apabila menggunakan..."
        menu:
            "A. lup":
                $ quiz5_score += 0
            "B. mikroskop fase kontras":
                $ quiz5_score += 0
            "C. mikroskop binokuler":
                $ quiz5_score += 0
            "D. mikroskop elektron":
                $ quiz5_score += 8

        "15. Jenis virus dan penyakit yang ditimbulkannya yang benar adalah..."
        menu:
            "A. Virus RNA - hepatitis A":
                $ quiz5_score += 0
            "B. Virus DNA - influenza":
                $ quiz5_score += 0
            "C. Rabdovirus - Rabies":
                $ quiz5_score += 8
            "D. Virus non B - hepatitis B":
                $ quiz5_score += 0

        "Jawaban : 
            \n
            1. C \ \ \ \ 3. B \ \ \ \ 5. A \ \ \ \ 7. A \ \ \ \ 9. C \ \ \ \ 11. D \ \ \ \ 13. A \ \ \ \ 15. C
            \n
            2. C \ \ \ \ 4. D \ \ \ \ 6. A \ \ \ \ 8. D \ \ \ \ 10. C \ \ \ \ 12. B \ \ \ \ 14. D"

        $ quiz5_score_total = quiz5_score - 20

        "Nilaiku adalah [quiz5_score_total]"

    # Check the quiz 1 score
    if quiz5_score_total >= 75:
        # Win
        $ quick_menu = True
        "Setelah Kemarin ngerangkum dan mengerjakan soal jadi lebih mudah"
        # Did he win? Yes.
        #$ quiz5_win = True
        #$ quiz5_lose = False   
    else:
        # Lose
        sr "Yang nilainya jelek seperti biasa silahkan jika ingin mengulang"
        sk "Baikk buu!!"
        menu:
            "Mengulang":
                $ quick_menu = True
                sr "yang mengulang silahkan dikerjakan lagi soalnya"
                $ quiz5_score = 0
                jump quiz5
            "Ga usah ngulang!":
                "Anda gagal sebagai murid"
                "~END~"
                return

    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    sk "Sudah Bel Pulang Yeay!!"
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Yaudah kalau gitu anak-anak. Kelasnya saya akhiri sekarang"
    sk "Baik bu.."
    sr "[st] dan [ad] Harap ikut Ibu ke ruang guru"
    sta "Baik bu.."
    hide bu_senda with moveoutright
    show ardana_alma at center with dissolve:
        ypos 1.2 
    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    mg2 "Kuy Pulang"
    mc "Aku yang ambil sepedamu atau gimana ?"
    mg2 "Iyaa dah kamu aja, aku tunggu di depan gerbang aja"
    mc "Kuncinya ?"
    mg2 "Ini"
    hide ardana_alma with moveoutright

    scene gerbang_sekolah_siang with dissolve
    show ardana_alma at center with dissolve:
        ypos 1.2
    mg2 "[mcFirst]!!" with vpunch
    mc "Skuy Naik, kamu mampir rumahku juga ga ?"
    mg2 "Woiya dong, kangen masakan tante hahaha"
    mc "Dasar kau ini"
    hide ardana_alma with moveoutleft

    scene jalan_siang with dissolve
    show ardana_alma at center with dissolve:
        ypos 1.2
    mg2 "Besok kamu ada dirumah ga ?"
    mc "Ada, kenapa emangnya ?"
    mg2 "Kuy, Jalan-jalan"
    mc "hah ?"
    mg2 "...."
    mg2 "Nanti saja pas sampe rumahmu kita bahas"
    mc "...."
    mc "Oh Ok"
    hide ardana_alma with dissolve

    scene depan_rumah_siang with dissolve
    mc "Tadi kamu mau bahas apa ?"
    show ardana_alma at center with dissolve:
        ypos 1.2
    mg2 "Ihh Masuk dulu lah"
    hide ardana_alma with moveoutright
    mc "Yaudah, aku parkir dulu"

    scene ruang_tamu_siang with dissolve
    mc "Aku Pulang"
    show ardana_alma at center with moveinright:
        ypos 1.2
    mg2 "Permisi Tante"
    mg2 'Kok Sepi ?'
    mc "Pasti [mom] di ruang keluarga"
    hide ardana_alma with dissolve

    stop music fadeout 1.0
    play music sore fadein 1.0
    scene ruang_keluarga_siang with dissolve
    show ardana_alma at center with moveinright:
        ypos 1.2
    mg2 "Halo Tante"
    show ardana_alma at center with moveinleft:
        xpos 0.55
        ypos 1.2
    show mom at center with dissolve:
        xpos 0.4
        ypos 1.15
    mom "Lahh,, ada kamu toh"
    mg2 "iya te hehehe"
    mom "Lama, ga kesini"
    mg2 "Ga kesempatan tante buat mampir, berhubung hari ini pulangnya lebih cepat jadi yaa mampir"
    mg2 "Lama ga ngicipin makanan tante"
    mg2 "Eh,, mau main sama [cat] aja kok te hehehe"
    mom "Astaga.. Kamu ini hahahah Jujur aja kalau kangen sama masakannya tante"
    mg2 "Hehehehe"
    mom "Ngomong-ngomong [mcFirst] mana ?"
    mg2 "lagi salin baju tante"
    mom "Oalah,, aku tadi pagi masak masih ada sisa banyak nih, mau ?"
    mg2 "Wah Mau tante"
    mom "Langsung ambil saja di meja makan ya ajak [mcFirst] makan juga"
    mg2 "Okie Tante"
    mom "kalau gitu tante mau tidur dulu"
    mom "Soalnya tante capek"
    mg2 "Okie tante"
    hide mom with moveoutright
    hide ardana_alma with moveoutright

    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    scene kamar_siang with dissolve
    play sound ketuk_pintu fadein 1.0
    "Knock Knock Knock"
    stop sound fadeout 1.0
    show ardana_alma at center with moveinleft:
        ypos 1.2
    mg2 "[mcFirst] Ayo makan"
    mc "Okk Aku keluar"
    hide ardana_alma with dissolve

    scene dapur_siang with dissolve
    show ardana_alma at center with dissolve:
        ypos 1.2
    mg2 "Umm.. Enaknyaa"
    mc "Oiya, ada apa tadi ?"
    mg2 "Ahh,, Iya aku hampir lupa"
    mg2 "Besok free ga ? kalau free, jalan-jalan kuy"
    mc "Ada siapa aja ?"
    mg2 "Ada [na], [bl], [wkk], [kk], [skce1], [ol], dan [skco2]"
    mg2 "Meskipun aku belum ngabarin semuanya"
    mc "Mana bisa begitu ?"
    mc "Kabarin dulu lah"
    mg2 "heheheh Iya iya, bentar aku kabarin dulu"
    mg2 "Semuanya bisa ikut, tinggal nentuin tempat"
    mc "Besok emangnya mau kemana ?"
    mg2 "Kalau sama anak-anak itu besok Lusanya"
    mg2 "Kalau besok kuy, ikut aku ke mall malamnya"
    mc "hmmm.. "
    mg2 "Ayoo ikut, ntr ku traktir hahahah"
    mc "Okk kalau gitu"
    mg2 "yeayyy"
    mg2 "[cat] Yeayy"
    show ardana_alma at center with moveinleft:
        xpos 0.7
        ypos 1.2
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Nyaaa ? "
    hide cat with dissolve
    mc "...."
    hide ardana_alma with dissolve

    scene depan_rumah_sore with dissolve
    show ardana_alma at center with dissolve:
        ypos 1.2
    mg2 "Tante masih tidur ya ?"
    mc "Iyaa masih tidur"
    mg2 "Kalau gitu titip salam ke tante ya"
    mc "Okk dah"
    mg2 "Aku pulang dulu"
    mc "Hati-hati dijalan"
    mg2 "Iyaa"
    hide ardana_alma with moveoutleft

    stop music fadeout 1.0
    play music sore fadein 1.0

    scene ruang_keluarga_sore with dissolve
    "Fuhh.. Capeknyaa, tidur dulu aja lah "

    scene kamar_malam with dissolve
    "Hoaamm.. sudah malam ternyata"
    "Laparnyaa,, mungkin ibu sudah menyipkan makanannya"
    
    scene dapur_malam with dissolve
    mc "Loh sudah pulang yah"
    show dad_cas at center with dissolve:
        ypos 1.2
    dad "Hooo.. tadi kamu ngajak cewe yang waktu itu lagi"
    dad "Sayangnya ayah baru pulang sekarang padahal ingin tahu cewenya yang mana ?"
    mc "Astaga.. tapi besok kesini lagi malam-malam minta temenin belanja"
    dad "Wihh Kerenn"
    show dad_cas at center with moveinright:
        xpos 0.65
        ypos 1.2
    show mom at center with dissolve:
        ypos 1.15
        xzoom -1
    mom "Sudah sudah makan dulu ini makanan sudah siap"
    dad "Okie doki bu hahha"
    mom "Astaga,, hahah"
    mc "Ayah kyknya habis kerasukan sesuatu bu"
    mom "Iyaa sepertinya"
    dad "yaa gimana besok ga sabar pengen lihat temenmu hahahha"
    mc "dah dah Lanjut makan lagi"
    hide dad_cas with dissolve
    hide mom with dissolve
    "Kami pun lanjut makan, Setelah itu aku pergi kembali tidur lagi"

    stop music fadeout 1.0

    jump day6_Kirana

    return

label day5_Miselia:

    play music pagi fadein 1.0
    window hide dissolve
    scene sky2 with dissolve
    show day5 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day5 with dissolve
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
    hide cat with moveoutbottom
    mc "Hooamm.. Sudah bangun ternyata"
    mc "Jam Berapa ini ?"
    show cat at center with moveinbottom:
        ypos 0.775
    cat "meooww meooww"
    mc "Hoo jam 5.45"
    cat "Meooww"
    mc "Mau Keluar ternyata hahahha.."
    mc "Kuy ke dapur"
    cat "Nyaaaa"
    hide cat with dissolve

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Makanannya belum siap"
    mc "Aku mau ngasih makan [cat] dulu setelah itu mandi"
    hide mom with dissolve
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Nyaaaa"
    hide cat with moveoutbottom
    mc "Makann yang banyakk [cat]"
    show cat_happy at center with dissolve:
        ypos 0.75
    cat "Nyaaaa Nyaaa Nyaaa"
    hide cat_happy with dissolve

    scene kamar_mandi with dissolve
    play sound mandi fadein 1.0
    "Aku lupa mau siapin buat sekolah, sudahlah nanti saja"
    stop sound fadeout 1.0

    scene kamar with dissolve
    "Okay,, sudah siap semuanya, tinggal ke dapur terus makan"

    scene dapur with dissolve
    mc "Sudah, siapp makanannya bu ?"
    show mom at center with dissolve:
        ypos 1.15
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
        ypos 1.15
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
    hide mom with moveoutright
    #Sound Meninggalkan MC
    mc "Lohh.. kakiku ada apa ini ?"
    mc "Ternyata [cat] toh"
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Meoooww"
    mc "Mau makan lagii tah ?"
    cat "Nyyaaa"
    hide cat with moveoutbottom
    mc "Okie deh kalau gitu aku isi ulang lagi ya"
    show cat_happy at center with dissolve:
        ypos 0.775
    cat "Nyaaaa~~"
    hide cat_happy with dissolve
    show mom at center with moveinright:
        ypos 1.15
    mom "Ini Uangnya"
    mc "Makasih bu.."
    hide mom with dissolve
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    mc "Aku berangkat dulu bu"
    show mom at center with dissolve:
        ypos 1.15
    mom "Hati - hati dijalan"
    hide mom with dissolve

    stop music fadeout 1.0
    play music jalan_jalan fadein 1.0

    scene gerbang_sekolah with dissolve
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Halo Bro"
    mc "Oh Hi"
    na "mau mampir beli jajan dulu ?"
    mc "ga usah, langsung ke kelas aja"
    mc "Kan hari ini mapelnya ga sebanyak hari lainnya"
    na "Oh iya ya"
    hide nada_alma with moveoutleft

    scene kelas with dissolve
    "[mg1_Last] Ternyata belum datang"
    "Kalau gitu aku belajar dulu lah"
    "~Tak Lama Kemudian~"
    show miselia_alma at center with moveinright:
        ypos 1.2
    mg1 "Wihh,, datang duluan langsung belajar"
    mc "...."
    mg1 "Kemarin, gimana kerkelnya ?"
    mc "Kemarin, waktu kerkel 2 anak tidak datang jadi aku sama [bl] saja yang mengerjakan"
    mc "si [st] katanya jalan-jalan ke mall kalau [ad] nthlah ga bisa dihubungi"
    mc "Nthlah, ntr waktu presentasi gimana mereka itu"
    mg1 "Biarin saja sudah yang penting tugasnya sudah selesai"
    mg1 "Misal yang dapat nilai lebih bagus pasti kamu sama [bl]"
    hide miselia_alma with dissolve
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
    mc "Kalau gitu kami akan mempresentasikan Materi Fungi"
    mc "Penggunaan manusia jamur untuk persiapan makanan atau pelestarian dan keperluan lainnya sangat luas dan memiliki sejarah panjang" with dissolve
    mc "Studi tentang dampak menggunakan historis dan sosiologis dari jamur ini dikenal sebagai ethnomycology" with dissolve
    mc "Baru-baru ini, metode telah dikembangkan untuk rekayasa genetika jamur, yang memungkinkan rekayasa metabolik spesies jamur" with dissolve
    mc "Sebagai contoh, modifikasi genetik dari spesies ragi yang mudah tumbuh pada tingkat yang cepat dalam fermentasi besar" with dissolve
    mc "Berikut ini beberapa manfaat lain dari beragam jenis jamur:"
    bl "Spesies Zygomycetes berguna dalam pembuatan makanan misalnya Rhizopus. Beberapa spesies anggota Zygomycetes antara lain Rhizopus sp, Pliobolus sp dan Muncor sp" with dissolve
    bl "Peran Ascomycotina dalam Kehidupan."
    bl "Berperan dalam Fermentasi: Misal pada Proses pembuatan tape, yaitu jamur Aspergillus oryzae, Proses pembuatan roti, yaitu jamur Saccharomyces cereviceae" with dissolve
    bl "Proses pembuatan kecap, yaitu jamur Aspergillus wentii, Proses pembuatan oncom," with dissolve
    bl "yaitu Neurospora sithophila, Proses pembuatan keju oleh Penicellium camemberti dan Penicellium requoforti, terakhir Proses pembuatan alcohol oleh Saccharomyces ovale" with dissolve
    mc "Bidang Medis: Alexander Flemming adalah orang pertama yang mengetahui khasiat penisilin," with dissolve
    mc "yaitu zat antibiotik yang dihasilkan oleh jamur jenis Penicillium notatum dan Penicillium chrysogenum" with dissolve
    mc "Namun demikian obat (antibiotik) tersebut baru dikembangkan secara besar-besaran setelah Perang Dunia II" with dissolve
    mc "Jamur ini dapat tumbuh dimana-mana, terutama pada buah yang telah ranum dan tampak sebagai noda hijau atau biru." with dissolve
    mc "Bidang Pertanian: Tidak disangsikan lagi, bahwa jamur sebagai organisme saprofit sangat penting dalam membantu mengembalikan kesuburan tanah" with dissolve
    mc "Jamur-jamur saprofit menghancurkan kayu daun-daunan sehingga menjadi mineral kembali." with dissolve
    bl "Dam-" with dissolve
    stop music fadeout 1.0
    play music jarak fadein 1.0
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Kok mulai tadi kalian berdua saja yang presentasi ? \nCoba giliran [st] dan [ad] yang menjelaskan"
    st "Hmm.. Per.. Peran Virus.. Ada berapa ya ?"
    st "Hehehhehehe"
    sk "Hahahahahhaha"
    sr "Astaga, kelihatan [st] ga ikut belajar kelompok"
    st "Hehhehehe.. Maaf, bu.. \nSaya menyesal"
    sr "Kalau gitu coba [ad]"
    ad "Aduhh.. bu.."
    sr "Kenapa ? \nPerut sakit ?"
    ad "Iyaa.. Bu.."
    sr "Alasann saja \nKalian Berdua setelah pulang sekolah harus ke ruang guru"
    $ sta = "Shinta dan Ardi"
    sta "Iya bu.."
    st "Aduhh.. gimana nih ? \nKena Hukum kita"
    ad "Salahmu nih.. ngajak aku jalan-jalan"
    st "Aku ga tau kalau bakal gini"
    ad "Yaudah, kalau gitu.. \nmau gimana lagi ?"
    sr "Ssstt.. kalian berdua \nAyo [mcFirst] dan [bl] lanjutkan presentasi kalian"
    stop music fadeout 1.0
    play music jalan_jalan2 fadein 1.0
    hide bu_senda with dissolve
    $ _skipping = False
    bl "DAMPAK NEGATIF JAMUR (FUNGI)"
    bl "Aspergillus nidulans dan Aspergillus niger adalah jenis jamur yang sering hidup pada saluran telinga tengah dan menimbulkan penyakit yang dikenal dengan otomikos." with dissolve
    bl "Di samping itu jamur golongan Deuteromycetes sering menimbulkan penyakit kulit yang disebut dermatomikos." with dissolve
    bl "Jamur parasit pada hewan contohnya adalah Aspergillus fumigatus. Jamur ini hidup dan menimbulkan penyakit paru-paru burung." with dissolve
    bl "Secara umum, penyakit infeksi karena Aspergillus dikenal dengan aspergilosis." with dissolve
    bl "Jamur parasit pada tanaman budidaya, misalnya Phytophthora infestans, dikenal juga sebagai jamur lanas sebagai parasit pada tanaman kentang." with dissolve
    bl "Jamur ini menyebabkan busuknya pucuk atau daun-daun tanaman kentang. Jenis jamur lanas lainnya adalah Phytophthora nicotianae, parasit pada daun tembakau" with dissolve
    bl "Sedang Phytophthora palmifora parasit pada tanaman kelapa." with dissolve
    mc "Jamur yang menghasilkan racun, walau banyak jamur yang enak dimakan, namun tidak sedikit pula yang mengandung racun penyebab kematian baik pada ternak maupun pada manusia" with dissolve
    mc "Contoh: Aspergillus flavus, yang menghasilkan racun aflatoksin, Amanita phaloides menghasilkan racun falin, yang dapat merusak sel-sel darah merah." with dissolve
    mc "Sekian dari kelompok kami.. Mohon Maaf jika ada kesalahan mohon dimaklumi"
    "Setelah semuanya presentasi selesai Bu Senda Memberikan Soal untuk dikerjakan pada kami semua" 
    $ _skipping = True
    "~SOAL~"

    $ quiz_fungi5_score = 0

    label quiz_fungi5:
        $ quick_menu = False

        "1. Berikut ini yang bukan merupakan ciri-ciri jamur Basidiomycota adalah …."
        menu:
            "A. hifa bersekat melintang":
                $ quiz_fungi5_score += 0
            "B. reproduksi seksual menghasilkan basidium":
                $ quiz_fungi5_score += 0
            "C. reproduksi aseksual dengan konidia":
                $ quiz_fungi5_score += 0
            "D. merupakan jamur makroskopik":
                $ quiz_fungi5_score += 10

        "2. Talus yang berbentuk seperti kerak adalah ciri lumut kerak yang bertipe …."
        menu:
            "A. Fruktikosa":
                $ quiz_fungi5_score += 0
            "B. Foliosa":
                $ quiz_fungi5_score += 0
            "C. Krustosa":
                $ quiz_fungi5_score += 10
            "D. Variola":
                $ quiz_fungi5_score += 0

        "3. Di bawah ini yang bukan merupakan manfaat lumut kerak bagi manusia adalah …."
        menu:
            "A. dibuat obat":
                $ quiz_fungi5_score += 0
            "B. dibuat kertas lakmus":
                $ quiz_fungi5_score += 0
            "C. penambah rasa atau aroma":
                $ quiz_fungi5_score += 0
            "D. bahan cat tembok":
                $ quiz_fungi5_score += 10

        "4. tubuh buah yang berbentuk seperti mangkok tempat dihasilkannya spora disebut…"
        menu:
            "A. askus":
                $ quiz_fungi5_score += 10
            "B. stolon":
                $ quiz_fungi5_score += 0
            "C. basidium":
                $ quiz_fungi5_score += 0
            "D. konidium":
                $ quiz_fungi5_score += 0
            
        "5. Di bawah ini yang merupakan pernyataan yang benar adalah …."
        menu:
            "A. askogonium mengandung dua inti":
                $ quiz_fungi5_score += 0
            "B. inti askogonium berpindah tempat ke anteridium":
                $ quiz_fungi5_score += 0
            "C. askus dapat terbentuk dari hifa haploid":
                $ quiz_fungi5_score += 0
            "D. anteridium mengandung inti yang haploid":
                $ quiz_fungi5_score += 10

        "6. Di bawah ini yang merupakan pernyataan yang benar perbedaaan jamur Basidiomycota dan Lichenes"
        menu:
            "A. pencernaan makananannya":
                $ quiz_fungi5_score += 0
            "B. Basdiomycota = jamurnya memiliki tudung buah dan Lichenes = hasil simbiosis antara jumur basidio atau asco dengan chlorophyta atau cyanobacteria":
                $ quiz_fungi5_score += 10
            "C. reproduksi aseksualnya":
                $ quiz_fungi5_score += 0
            "D. reproduksi seksualnya":
                $ quiz_fungi5_score += 0

        "7. Jenis Ascomycota yang dapat mengubah ampas kacang menjadi oncom adalah.."
        menu:
            "A. Aspergillus Niger":
                $ quiz_fungi5_score += 0
            "B. Ustilago maydis":
                $ quiz_fungi5_score += 0
            "C. Puccinia graminis":
                $ quiz_fungi5_score += 0
            "D. Neurospora sitophyla":
                $ quiz_fungi5_score += 10

        "8. Pernyataan dibawah ini tentang sifat-sifat dari jamur yang benar adalah"
        menu:
            "A. Tidak berklorofil dan prokariotik":
                $ quiz_fungi5_score += 0
            "B. Tidak berklorofil dan eukariotik":
                $ quiz_fungi5_score += 10
            "C. Tidak berklorofil dan autotrof":
                $ quiz_fungi5_score += 0
            "D. berklorofil dan eukariotik":
                $ quiz_fungi5_score += 0

        show fungid5 at truecenter with dissolve
        "9. Haustorium ditunjukkan oleh nomor..."
        menu:
            "A. 1":
                $ quiz_fungi5_score += 0
            "B. 2":
                $ quiz_fungi5_score += 10
            "C. 3":
                $ quiz_fungi5_score += 0
            "D. 4":
                $ quiz_fungi5_score += 0
        hide fungid5 with dissolve

        "10. Dalam siklus hidup jamur, spora yang jatuh di tempat yang lembab akan membentuk…"
        menu:
            "A. Protalium":
                $ quiz_fungi5_score += 0
            "B. Arkegonium":
                $ quiz_fungi5_score += 0
            "C. Miselium":
                $ quiz_fungi5_score += 10
            "D. Protonema":
                $ quiz_fungi5_score += 0

        "Jawaban : 
            \n
            1. D \ \ \ \ 3. D \ \ \ \ 5. D \ \ \ \ 7. D \ \ \ \ 9. B
            \n
            2. C \ \ \ \ 4. A \ \ \ \ 6. B \ \ \ \ 8. B \ \ \ \ 10. C"

        "Nilaiku adalah [quiz_fungi5_score]"

    # Check the quiz 1 score
    if quiz_fungi5_score >= 75:
        # Win
        $ quick_menu = True
        "Setelah Kemarin ngerangkum dan mengerjakan soal jadi lebih mudah"
        # Did he win? Yes.
        #$ quiz_fungi5_win = True
        #$ quiz_fungi5_lose = False   
    else:
        # Lose
        sr "Yang nilainya jelek seperti biasa silahkan jika ingin mengulang"
        sk "Baikk buu!!"
        menu:
            "Mengulang":
                sr "yang mengulang silahkan dikerjakan lagi soalnya"
                $ quiz_fungi5_score = 0
                jump quiz_fungi5
            "Ga usah ngulang!":
                "Anda gagal sebagai murid"
                "~END~"
                return

    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    sk "Sudah Bel Pulang Yeay!!"
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Yaudah kalau gitu anak-anak. Kelasnya saya akhiri sekarang"
    sk "Baik bu.."
    sr "[st] dan [ad] Harap ikut Ibu ke ruang guru"
    sta "Baik bu.."
    hide bu_senda with moveoutright
    show miselia_alma at center with dissolve:
        ypos 1.2 
    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    mg1 "Kuy Pulang"
    mc "Aku yang ambil sepedamu atau gimana ?"
    mg1 "Iyaa dah kamu aja, aku tunggu di depan gerbang aja"
    mc "Kuncinya ?"
    mg1 "Ini"
    hide miselia_alma with moveoutright

    scene gerbang_sekolah_siang with dissolve
    show miselia_alma at center with dissolve:
        ypos 1.2
    mg1 "[mcFirst]!!" with vpunch
    mc "Skuy Naik, kamu mampir rumahku juga ga ?"
    mg1 "Lihat aja nanti"
    mc "okk dah"
    hide miselia_alma with moveoutleft

    scene depan_rumah_sore with dissolve
    mg1 "Kayaknya aku ga bisa mampir dah"
    mg1 "mungkin Next time"
    mc "Okk dah klo gitu"
    mc "Hati-hati dijalan"
    mg1 "Iyaa.."
    hide miselia_alma with moveoutleft
    
    stop music fadeout 1.0
    play music sore fadein 1.0

    scene ruang_keluarga_sore with dissolve
    "Fuhh.. Capeknyaa, tidur dulu aja lah "

    scene kamar_malam with dissolve
    "Hoaamm.. sudah malam ternyata"
    "Laparnyaa,, mungkin ibu sudah menyipkan makanannya"
    
    scene dapur_malam with dissolve
    show dad_cas at center with moveinright:
        xpos 0.65
        ypos 1.2
    show mom at center with dissolve:
        ypos 1.15
        xzoom -1
    mom "makan dulu ini makanan sudah siap"
    dad "Okie doki bu hahha"
    mom "Astaga,, hahah"
    mc "Ayah kyknya habis kerasukan sesuatu bu"
    mom "Iyaa sepertinya"
    dad "yaa gimana besok ga sabar pengen lihat temenmu hahahha"
    mc "dah dah Lanjut makan lagi"
    hide dad_cas with dissolve
    hide mom with dissolve
    "Kami pun lanjut makan, Setelah itu aku pergi kembali tidur lagi"

    scene sky_malam with dissolve
    "Kami Melanjutkan Telpon, makin lama hubungan kami makin dekat"
    "Setelah Lulus kami mengambil Universitas yang sama bahkan jurusannya sama"
    "Tetap Melanjutkan hubungan ini"

    stop music fadeout 1.0

    jump credits

    return

label day5_Airin:

    play music pagi fadein 1.0
    window hide dissolve
    scene sky2 with dissolve
    show day5 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day5 with dissolve
    window show dissolve
    
    scene kamar with dissolve
    stop sound fadeout 1.0
    play sound burung_terbang fadein 1.0
    window hide dissolve
    pause 3.0
    window show dissolve
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Meoowww Meooww Meooww"
    mc "Hooamm.. Sudah bangun ternyata"
    mc "Loh ada [cat] Oiyaa,, kemarin pintu kamar kubuka"
    mc "Jam Berapa ini ?"
    cat "meooww meooww"
    mc "Hoo jam 5.45"
    cat "Meooww"
    mc "Mau Keluar ternyata hahahha.."
    mc "Kuy ke dapur"
    cat "Nyaaaa"
    hide cat with moveoutleft

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Makanannya belum siap"
    mc "Aku mau ngasih makan [cat] dulu setelah itu mandi"
    hide mom with dissolve
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Nyaaaa"
    mc "Makann yang banyakk [cat]"
    cat "Nyaaaa Nyaaa Nyaaa"
    hide cat with dissolve

    scene kamar mandi with dissolve
    "Aku lupa mau siapin buat sekolah, sudahlah nanti saja"

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
    mom "Dimana [dad] ?"
    mc "Katanya [dad] duluan saja"
    mc "Kalau gitu aku duluan makan aja bu soalnya mau masuk sekolah"
    show mom at center with dissolve:
        ypos 1.2
        xzoom -1
    show dad_cas at center with moveinright:
        xpos 0.675
        ypos 1.2
    dad "Ayo makan Hehhe maaf nungguin aku"
    mom "Dasar.. ayoo makan"
    hide mom with dissolve
    hide dad_cas with dissolve
    "Kami pun makan bersama tak lupa dengan [cat] juga"
    mc "Bu Aku sudah selesai.."
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    show mom at center with dissolve:
        ypos 1.2
        xzoom -1
    show dad_cas at center with dissolve:
        xpos 0.675
        ypos 1.2
    mom "Bentar Ibu siapkan bekalnya.."
    dad "Ini uang sangumu"
    $ money += 10000
    mc "Terima kasih Ayah dan Ibu"
    mom "Ini bekalmu"
    mc "Kalau gitu aku berangkat dulu Ayah dan Ibu"
    ai "Iyaa nak hati-hati dijalan"
    hide dad_cas with dissolve
    hide mom with dissolve

    stop music fadeout 1.0
    play music jalan_jalan fadein 1.0
    scene jalan with dissolve
    show airin_alma at center with moveinright:
        ypos 1.2
    mg3 "Dooor"
    mc "Ackkkhh Astaga"
    mg3 "Hahahahhah lucu banget kagetnya"
    mc "Dasar kau ini"
    mg3 "Maaf-maaf Hahahah"
    mc "...."
    mg3 "Heee... kamu marah ?"
    mc "Ga juga. Ngomong-ngomong kamu berangkatnya berjalan lagi ?"
    mg3 "Iyaa"
    mc "Tumben"
    mg3 "Seru juga sih berangkat dengan jalan kaki"
    mc "Benar kan"
    mg3 "Hehehehehe"
    hide airin_alma with moveoutleft

    scene gerbang_sekolah with dissolve
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Oee oeee"
    na "Barengan lagi nih berangkatnya"
    show nada_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Iyaa,, seru juga jalan kaki berhubung Sekolahnya deket juga dari arah rumah"
    na "Ha  hahahaha Berarti rumah kalian dekat"
    mc "Ga terlalu dekat agak jauh dikit"
    hide airin_alma with moveoutleft
    hide nada_alma with moveoutleft

    scene kelas with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat pagi anak-anak"
    sk "Pagi bu"
    sr "Hari ini kita mulai saja ya"
    sk "Iya bu"
    $ _skipping = False
    show bu_senda at center with moveinleft:
        xpos 0.7
        ypos 1.2
    "~Materi Klasifikasi Lanjutan~"
    sr "KINGDOM FUNGI" with dissolve
    sr "Kelompok jamur (fungi), merupakan kelompok makhluk hidup yang memperoleh makanan dengan cara menguraikan bahan organik makhluk hidup yang sudah mati" with dissolve
    sr "Jamur tidak berklorofil, berspora, tidak mempunyai akar, batang, dan daun" with dissolve
    sr "Jamur hidup di tempat yang lembap, bersifat saprofit (organisme yang hidup dan makan dari bahan organik yang sudah mati atau yang sudah busuk)" with dissolve
    sr "dan parasit (organisme yang hidup dan mengisap makanan dari organisme lain yang ditempelinya)." with dissolve
    sr "Sebelum dikenalkannya metode molekuler untuk analisis filogenetik, dulu fungi dimasukkan ke dalam kerajaan tumbuhan atau plantae karena fungi memiliki" with dissolve
    sr "beberapa kemiripan dengan tumbuhan yaitu tidak dapat berpindah tempat, juga struktur morfologi dan tempat hidupnya yang memiliki banyak kesamaan." with dissolve
    sr "Dalam perkembangannya, fungi dipisahkan dari kerajaan tumbuhan dan mempunyai kerajaan sendiri" with dissolve
    sr "Tubuh jamur terdiri atas benang-benang halus yang disebut hifa. Hifa saling bersambungan membentuk miselium" with dissolve
    sr "Berdasarkan bentuk hifa jamur dibedakan menjadi dua, yaitu:" with dissolve
    sr "Jamur Ganggang (Phycomycetes): Pada tempe terdapat benang-benang halus disebut miselium yaitu cabang hifa, apabila tempe membusuk maka permukaan tempe juga akan membusuk." with dissolve
    sr "Jamur Benar (Eumycetes) Jamur ini memiliki hifa yang bersekat-sekat." with dissolve
    sr "Contoh makhluk hidup yang termasuk kelompok jamur adalah jamur roti, ragi tapai, jamur tiram putih, dan jamur kayu. Fungi melakukan reproduksi secara aseksual dan seksual" with dissolve
    sr "Reproduksi secara aseksual terjadi dengan pembentukan kuncup atau tunas pada jamur uniselule serta pemutusan benang hifa (fragmentasi miselium)" with dissolve
    sr "dan pembentukan spora aseksual (spora vegetatif) pada fungi multiseluler" with dissolve
    sr "Reproduksi jamur secara seksual dilakukan oleh spora seksual. Spora seksual dihasilkan secara singami yang terdiri dari dua tahap, yaitu tahap plasmogami dan tahap kariogami" with dissolve
    sr "KINGDOM PLANTAE" with dissolve
    sr "Kelompok ini beranggotakan makhluk hidup bersel banyak yang mampu berfotosintesis" with dissolve
    sr "Kemampuan fotosintesis ini dikarenakan adanya klorofil di dalam kloroplas" with dissolve
    sr "Klorofil memanfaatkan energi cahaya matahari untuk membuat makanan. Perbedaan lain antara tumbuhan dengan makhluk hidup bersel banyak adalah dalam struktur selnya." with dissolve
    sr "Sel-sel tumbuhan mempunyai dinding sel yang terbuat dari bahan selulosa (sejenis karbohidrat)" with dissolve
    sr "Oleh karena itu, tumbuhan biasanya bersifat kaku dan tidak mudah patah" with dissolve
    sr "Kingdom Plantae dapat dikelompokkan menjadi 2 kelompok yaitu tumbuhan tidak berpembuluh (tidak mempunyai xilem dan floem) dan tumbuhan berpembuluh" with dissolve
    sr "Tumbuhan yang termasuk ke dalam kelompok tumbuhan tidak berpembuluh adalah tumbuhan lumut. Sedangkan, tumbuhan paku dan tumbuhan berbiji termasuk tumbuhan berpembuluh." with dissolve
    $ _skipping = True
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    stop music fadeout 1.0
    play music jalan_jalan2 fadein 1.0
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Waktunya sudah habis anak-anak kalian boleh istirahat"
    sk "Terima kasih bu Senda"
    sr "Kalau gitu Bu senda pergi dulu"
    hide bu_senda with moveoutright
    sk "Baik bu"
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Nanti main kerumahmu bro"
    mc "Hmmmm.. Okk"
    na "Bentar aku ajak yang lain juga"
    mc "Hah ? jangan rame-rame"
    na "Gapapa biar heboh"
    mc "Sigh..."
    na "[mg3_First] mau ikut kerumah [mcFirst] ?"
    show nada_alma at center with moveinright:
        xpos 0.3
        ypos 1.2
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Boleh ada siapa aja ?"
    na "Aku, kamu, [wkk], [kk], [bl] kayaknya ini"
    na "Aku ajak mereka dulu"
    mg3 "Okk"
    hide airin_alma with dissolve
    na "Bro Mau ikut main ga ke rumah [mcFirst] ?"
    wkk "Boleh-Boleh gasskan"
    na "Bro ajak [kk] juga.. Aku mau ajak [bl]"
    wkk "Okk Bro"
    na "[bl] Mau ikut kerumah [mcFirst] nanti ?"
    bl "Gapapa sih.. Okk dah"
    na "[wkk] Gimana si [kk] ?"
    wkk "Ga jadi ikut bro"
    na "Yaudah kalau gitu"
    na "Kuy Kantin"
    wkk "Gass.. [mcFirst] gmna ?"
    mc "Aku ga ikut sekarang bawa bekal \nEhh.. tapi titip aja ini uangnya \nTerserah mau dibelikan apa"
    $ money -= 10000
    na "Okk Bro"
    mc "[mg3_First] mungkin mau titip juga"
    na "Dia ke kantin kayaknya sudah ga ada orangnya"
    mc "ehh.. iya yaudah"
    na "aku duluan bro"
    hide nada_alma with moveoutright
    mc "Okk"
    "Sudahh sepi Huh.. Saatnya aku makan bekalku"
    mc "Fuuh.. Kenyangnya"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    "Sudah bel masuk ternyata"
    show nada_alma at center with moveinright:
        ypos 1.2
    na "Broo ini titipnya"
    mc "Makasih,, Kembaliannya ambil saja lur"
    na "Mantap Lucky"
    hide nada_alma with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Hayoo duduk duluu"
    sk "Heheheh Iya bu"
    sr "Selamat Siang anak-anak sudah kah siap untuk belajar lagi siang hari ini ?"
    sk "Tidak bu!!"
    sr "Kalau gitu tidur aja yaa "
    wkk "Ihh Bu Senda.. Kami Bercanda bu"
    sr "Sama Ibu juga Hahahaha"
    sr "Sebelumnya bikin kelompok dulu ya bebas. 1 kelompok terdiri 4 orang"
    hide bu_senda with dissolve
    show nada_alma at center with dissolve:
        ypos 1.2
    na "[mcFirst] gimana kalau kita sekolompokan dengan [wkk], [mg3_First], dan [bl] \n dah pas juga sih misal disuruh kerjakan dirumah kan sekalian hehe"
    mc "Boleh-boleh aja"
    na "[mg3_First] Skuy kelompokan.."
    mg3 "Iyaa"
    na "[wkk] Kuy kelompokan"
    wkk "Siapa aja ?"
    na "Yaa kayak tadi itu"
    wkk "Gasss"
    na "[bl] ayo kelompokan denganku"
    bl "Okk"
    hide nada_alma with dissolve
    "Setelah itu kelas ramai dengan memilih kelompok masing-masing"
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Apa sudah membuat kelompok semuanya ?"
    sk "Sudah bu"
    sr "Kalau gitu Bu Senda kasih soalnya.. \nkerjakan dirumah yaa karena ada rapat ntar lagi mungkin sebentar lagi akan pulang"
    sr "Dikumpulkan Besok semuanya harus sudah selesai.. sama bikin presentasi materi ya"
    sk "Baik buu"
    na "Tuhkan, aku instingku benar hahahha \nJadi,, nanti sekalian ngerjain di rumah [mcFirst]"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    sr "Sudah bel anak-anak kalian boleh pulang"
    hide bu_senda with moveoutright
    sk "Yeayy.. Baik bu.."
    wkk "Kita berangkat sekarang ini ?"
    bl "Ayo-ayo aja sih aku"
    mc "Nunggu sepi baru pulang"
    bl "Heee.. kok gitu"
    mc "gapapa"
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Sudah sudah.. \nkalau gitu ada yang beli camilan sisanya langsung ke rumah [mcFirst]"
    wkk "Aku aja kalau gitu"
    bl "Aku ikut juga dong"
    wkk "Okk dah kalau gitu"
    wkk "Aku sama [bl] duluan beli camilan dulu"
    na "Okk dah"
    show nada_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Ayo [mcFirst]"
    mc "Haii.. Haii.."
    hide nada_alma with dissolve
    hide airin_alma with dissolve

    scene jalan_siang with dissolve
    mc "Nanti jangan lupa kabarin mereka \nShareloc ke mereka"
    show nada_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Iyaa, kalau ga di shareloc nanti bisa tersesat hahaha"
    na "Nanti kalau sudah sampe rumahmu aku shareloc ke mereka"
    hide nada_alma with dissolve
    hide airin_alma with dissolve

    stop music fadeout 1.0
    play music pagi fadein 1.0
    scene depan_rumah_siang with dissolve
    mc "Aku Pulang!!"
    show nada_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    show airin_alma at center with dissolve:
        ypos 1.2
    $ nmg3 = "Nada dan [mg3_First]"
    nmg3 "Permisi"
    hide nada_alma with dissolve
    hide airin_alma with dissolve

    scene ruang_tamu_siang with dissolve
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Miiaauuuww"
    mc "Ahhh... [cat]"
    show nada_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    show airin_alma at center with dissolve:
        xpos 0.7
        ypos 1.2
    na "Kamu pnya kucing ? Astaga Lucu bro"
    mg3 "Aaaaa [cat].."
    cat "Miaauuww"
    hide cat with dissolve
    mg3 "Aaawww [cat]"
    na "Kucingnya akrab banget sama [mg3_First]"
    mc "Seperti biasa [cat] selalu manja kalau ada [mg3_First]"
    na "[mg3_First] pernah kesini ?"
    mc "Iyaa pernah"
    na "Hayolohh.. ngapain ?"
    mc "Cuma mampir saja"
    mg3 "Hehehhe.. Oiyaa,, mereka sudah dikirim shareloc ?"
    na "Ahh,, iya lupa langsung ku shareloc"
    mc "Sudah di shareloc da ?"
    na "Sudah"
    mc "Kuy.. Mari kerjakan di kamarku saja"
    hide nada_alma with dissolve
    hide airin_alma with dissolve

    scene ruang_keluarga_siang with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Loh,, sudah pulang ? ada teman-temanmu juga"
    show nada_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    show airin_alma at center with dissolve:
        xpos 0.7
        ypos 1.2
    na "Halo te"
    mc "Iya bu sekalian kerja kelompok"
    mom "Hohohoh.... \nehh.. ada [mg3_First] lagi"
    mg3 "Iya te hehheh berhubung sekelompok sama [mcFirst]"
    mc "Ayoo sini ke kamar"
    mom "Hohohoho"
    mc "Oiya,, bu nanti ada temanku lagi 2 mau datang kesini"
    mom "Okie Doki"
    mom "Kalau gitu Ibu siapkan cemilan dulu"
    hide mom with moveoutleft
    na "waduh ga usah repot-repot tante"
    mc "Halah gayamu"
    na "Hehehe"
    hide nada_alma with dissolve
    hide airin_alma with dissolve

    scene kamar_siang with dissolve
    show nada_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Baru kali ini aku masuk kamar cowo \n kamarmu rapi sekali ya"
    na "dah biasa cowo kamarnya rapilah kamarku ya juga rapi hahaha"
    mg3 "Kukira kamar cowo itu berantakan"
    mc "ga juga \n Semuanya itu tergantung orangnya juga"
    mg3 "Bener sih"
    "~[mcFirst]!!!!! ~[mcFirst]!!!!! ~[mcFirst]!!!!!"
    mc "Kayaknya mereka sudah datang"
    hide nada_alma with dissolve
    hide airin_alma with dissolve

    scene depan_rumah_siang with dissolve
    wkk "[mcFirst]!! [mcFirst]!! [mcFirst]!!"
    show mom at center with moveinright:
        ypos 1.15
    mom "OyaaOyaa... Temannya [mcFirst]"
    wkk "Iya te.. [mcFirst] ada ?"
    mom "Ada silahkan masuk.. "
    bl "Kalau gitu permisi tante"
    wkk "Permisi tante"
    wkk "[mcFirst] ada dimana te?"
    mom "Langsung aja ke kamarnya"
    bl "Kalau gitu permisi dulu tante"
    mom "Silahkan silahkan"
    hide mom with moveoutright

    scene kamar_siang with dissolve
    bl "Kami Boleh masuk ini ?"
    wkk "Hayoo.. Kalian lagi ngapain ?"
    mc "Masuk saja"
    bl "Wahh... Rapi banget.. \n bahkan kamarku ga serapi ini"
    mc "Biasa aja"
    show nada_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    na "Benar biasa aja cowo biasanya kamarnya selalu rapi"
    wkk "Hooh.. kamar cowo selalu rapi daripada cewe"
    $ mgb = "[mg3_First] dan [bl]"
    mgb "Halahh.."
    mgb "Lebih rapi kamarku lah"
    mgb "Nyesal aku puji kamar kalian rapi"
    mc "Pffffttt.. \n HAHAHAHAHA"
    mgb "Ihhh..... Malah ketawa"
    $ wkn = "[wkk] dan [na]"
    wkn "Hahahahahahaha"
    mgb "HAHhahahhaha"
    mc "aduh.. aduh.. perutku sakit"
    bl "Sudah ah.. ayo kerjakan"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Iyaa biar cepet selesai"
    show airin_alma at center with dissolve:
        xpos 0.7
        ypos 1.2
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Miaauuuuwww"
    mg3 "Lohh ada kamu dibelakangku"
    bl "Aaaaaa... Kucingnya comel"
    bl "Siapa namanya ?"
    mc "Namanya [cat]"
    bl "Artinya apa ?"
    mc "Bahagia"
    bl "heeee.. baguss.."
    hide cat with dissolve
    show mom at center with moveinright:
        ypos 1.15
    mom "Ini Cemilan sudah tante siapin"
    mom "Dimakan yaa"
    wkk "Ehh.. Tante ga usah repot-repot kami sudah beli cemilan"
    mom "Tak apa,, ini Homemade tante sendiri"
    wkk "Wahh.. kalau gitu terima kasih tante"
    mom "Oyaoya Tante baru tau banyak temen kesini tau gitu tante masak besar"
    mom "Yaudah,, kalau gitu selamat mengerjakan \nSini [cat].."
    show cat_angry at center with moveinbottom:
        ypos 0.775
    cat "Miauuuww hssss" with hpunch
    hide cat_angry with moveoutbottom
    mom "Ehh.. jadi ganas"
    $ all = "Semuanya"
    all "Hahahahha"
    mg3 "[cat] maunya sama aku te hahahah"
    mom "Huhuhuuhuhu... Sedih..."
    mom "Hehehhe silahkan menikmati waktunya"
    hide mom with moveoutright
    mc "Dah dah.. Mari Kerjakan.."
    na "Ayoo.. ada camilan juga ini bakal semangat"
    mg3 "Lets go!!"
    hide nada_alma with dissolve
    hide airin_alma with dissolve

    "~SOAL~" with dissolve
    #Initialize score
    $ quiz5_klasifikasi_score = 0

    label quiz5_klasifikasi:

        $ quick_menu = False

        "1. Di bawah ini yang temasuk dalam kelompok crustacea adalah …."
        menu:
            "A. udang dan belalang":
                $ quiz5_klasifikasi_score += 0
            "B. kepiting dan udang":
                $ quiz5_klasifikasi_score += 10
            "C. kutu dan kelabang":
                $ quiz5_klasifikasi_score += 0
            "D. belalang dan kelabang":
                $ quiz5_klasifikasi_score += 0

        "2. Hewan yang mendapatkan julukan mamalia berkantung adalah …."
        menu:
            "A. monyet":
                $ quiz5_klasifikasi_score += 0
            "B. tikus":
                $ quiz5_klasifikasi_score += 0
            "C. lumba-lumba":
                $ quiz5_klasifikasi_score += 0
            "D. kanguru":
                $ quiz5_klasifikasi_score += 10 

        "3. Tingkatan terendah dari klasifikasi tumbuhan dan hewan adalah …."
        menu:
            "A. Kingdom":
                $ quiz5_klasifikasi_score += 0
            "B. Spesies":
                $ quiz5_klasifikasi_score += 10
            "C. Filum":
                $ quiz5_klasifikasi_score += 0
            "D. Divisi":
                $ quiz5_klasifikasi_score += 0

        "4. Suku kata pertama pada tata cara pemberian nama ganda menunjukkan …."
        menu:
            "A. kelas":
                $ quiz5_klasifikasi_score += 0
            "B. ordo":
                $ quiz5_klasifikasi_score += 0
            "C. genus":
                $ quiz5_klasifikasi_score += 10
            "D. spesies":
                $ quiz5_klasifikasi_score += 0
            
        "5. Pisang, mangga, kelengkeng, dan durian dikelompokkan dalam tumbuhan buah-buahan. Pengklasifikasian ini tergolong dalam klasifikasi sistem …."
        menu:
            "A. natural":
                $ quiz5_klasifikasi_score += 0
            "B. artifisial":
                $ quiz5_klasifikasi_score += 0
            "C. praktis":
                $ quiz5_klasifikasi_score += 10
            "D. manfaat":
                $ quiz5_klasifikasi_score += 0

        "6. Filum dalam klasifikasi hewan yang disebut juga …."
        menu:
            "A. divisio":
                $ quiz5_klasifikasi_score += 10
            "B. genus":
                $ quiz5_klasifikasi_score += 0
            "C. marga":
                $ quiz5_klasifikasi_score += 0
            "D. ordo":
                $ quiz5_klasifikasi_score += 0

        "7. Daftar yang memuat sejumlah keterangan suatu makhluk hidup yang dapat digunakan untuk mengidentifikasi dan menentukan kelompok makhluk hidup berdasarkan ciri-ciri yang dimilikinya disebut …."
        menu:
            "A. kunci dikotomi":
                $ quiz5_klasifikasi_score += 0
            "B. kunci determinasi":
                $ quiz5_klasifikasi_score += 10
            "C. klasifikasi":
                $ quiz5_klasifikasi_score += 0
            "D. Pengelompokan":
                $ quiz5_klasifikasi_score += 0

        "8. Jenis makhluk hidup yang menyerupai tumbuhan dan hewan, tetapi bukan tumbuhan dan bukan hewan disebut …."
        menu:
            "A. Monera":
                $ quiz5_klasifikasi_score += 0
            "B. Fungi":
                $ quiz5_klasifikasi_score += 0
            "C. Protista":
                $ quiz5_klasifikasi_score += 10
            "D. Plantae":
                $ quiz5_klasifikasi_score += 0

        "9. Pasangan yang memiliki kekerabatan paling dekat adalah …."
        menu:
            "A. Rubah dan Serigala":
                $ quiz5_klasifikasi_score += 0
            "B. Rubah dan berang-berang":
                $ quiz5_klasifikasi_score += 0
            "C. Rubah dan anjing":
                $ quiz5_klasifikasi_score += 10
            "D. Serigala dan Anjing":
                $ quiz5_klasifikasi_score += 0

        "10. Difa adalah seorang ahli ekologi. Manfaat taksonomi bagi Difa adalah …."
        menu:
            "A. Menemukan adanya spesies baru":
                $ quiz5_klasifikasi_score += 0
            "B. Menemukan adanya senyawa antibodi berciri khusus pada suatu makhluk hidup":
                $ quiz5_klasifikasi_score += 0
            "C. Dapat memperkirakan tentang nenek moyang makhluk hidup tertentu":
                $ quiz5_klasifikasi_score += 10
            "D. Mempelajari deversitas makhluk hidup yang ada":
                $ quiz5_klasifikasi_score += 0

        "Jawaban : 
            \n
            1. B \ \ \ \ 3. B \ \ \ \ 5. C \ \ \ \ 7. B \ \ \ \ 9. C
            \n  
            2. D \ \ \ \ 4. C \ \ \ \ 6. A \ \ \ \ 8. C \ \ \ \ 10. C"

        "Nilaiku adalah [quiz5_klasifikasi_score]"

    # Check the quiz 1 score
    if quiz5_klasifikasi_score >= 75:
        # Win
        # Win
        $ quick_menu = True
        bl "Akhirnya sudah selesai.."
        wkk "Jajannya enak"
        show nada_alma at center with dissolve:
            xpos 0.3
            ypos 1.2
        show airin_alma at center with dissolve:
            ypos 1.2
        mg3 "Benerkan, jajannya enak disini"
        na "Sasuga Ibu [mcFirst] bikinannya enak"
        # Did he win? Yes.
        #$ quiz4_win = True
        #$ quiz4_lose = False   
    else:
        # Lose
        "Susahnya.. Kita biarin aja atau lanjut ?"
        menu:
            "Lanjut":
                $ quiz5_klasifikasi_score = 0
                jump quiz5_klasifikasi
            "Biarin":
                "Kalian gagal sebagai murid"
                "~END~"
                return
    
    wkk "Sisa camilannya masih banyak yang beli masih sisa"
    na "Kenyangnya.."
    bl "Iyaaa.."
    mg3 "Gimana kalau kita sambil main juga"
    mc "Boleh ini"
    na "Ada kartu ga brader"
    wkk "Main Kartu bisa ini"
    mc "Ada sih Kartu"
    bl "Gass Keun"
    hide nada_alma with dissolve
    hide airin_alma with dissolve
    "Kami pun bermain Kartu, dan lain lain hingga sore"

    stop music fadeout 1.0
    play music sore fadein 1.0
    scene kamar_sore with dissolve
    wkk "Wahh.. sudah jam segini.. Aku pulang dulu kalau gitu"
    bl "Ehh.. iya sudah jam segini.. kalau gitu aku pulang dulu"
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Aku juga"
    mc "Okayy.."
    hide nada_alma with dissolve
    
    scene ruang_keluarga_sore with dissolve
    mc "Bu, Temanku pulang"
    show mom at center with dissolve:
        ypos 1.15
    mom "Ehh.. kok cepet ? \n Ga sampai malam ?"
    wkk "hehehhe Ga tante"
    mom "Yaudah kalau gitu"
    bl "Maaf ngerepotin tante"
    mom "Gapapa, tante malah senang kalian datang"
    bl "Hehehe.. iya te"
    $ wbn = "[wkk], [bl], dan Nada"
    show nada_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    wbn "Kalau gitu kami pulang dulu tante dan [mcFirst]"
    mom "Iyaa Hati-hati"
    hide nada_alma with moveoutleft
    mom "Oyaoya... [mg3_First] ga pulang juga ?"
    show airin_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    mg3 "Sebentar lagi tante, Rumahku juga ga jauh dari sini kok te"
    mom "Pulang setelah makan malam ya"
    mg3 "Iyaa te.. mau main sama [cat] juga tapi sudah ketiduran gara-gara tadi main"
    mom "Yaudah kalau gitu.. bantuin tante nyiapin ya.."
    mg3 "Okie Tante"
    hide mom with moveoutright
    hide airin_alma with moveoutright
    mc "Yaudah kalau gitu aku tidur dulu"

    scene dapur_sore with dissolve
    show mom at center with dissolve:
        ypos 1.15
    show airin_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    mom "Kerjaanya jadi lebih cepat kalau ada kamu"
    mg3 "Ahh.. bisa saja Tante"
    "~Aku Pulang !!!"
    mom "Kayaknya, Om sudah pulang"
    show dad_uni at center with moveinright:
        xpos 0.7
        ypos 1.2
    dad "Loh Loh,, Calon Mantu ini bu ?"
    mom "Oyaoya.. Iyaa. ada Calon Mantu jadi cepat"
    mg3 "Hahahahha.. Tante sama Om ada ada saja nih"
    dad "Hahahahhaha"
    mom "Oiya,, bisa minta tolong bangunkan [mcFirst] ?"
    mg3 "Boleh te"
    hide dad_uni with dissolve
    hide mom with dissolve
    hide airin_alma with moveoutleft

    scene kamar_malam with dissolve
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "[mcFirst] Bangunn !!"
    mc "Hai.. Haii.. sudah bangun"
    mg3 "Kalau gitu kita makan kuy"
    mc "Iyaa aku mau raup dulu"
    hide airin_alma with moveoutright

    scene dapur_malam with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Gimana ?"
    show airin_alma at center with dissolve:
        xpos 0.3
        ypos 1.2
    mg3 "Katanya duluan masih cuci wajah"
    mc "Ayo makan"
    show dad_cas at center with dissolve:
        xpos 0.7
        ypos 1.2
    dad "Nah,, ini sudah datang"
    hide mom with dissolve
    hide dad_cas with dissolve
    hide airin_alma with dissolve
    "~Akhirnya Kami semua makan bersama meskipun lebih ramai tapi aku suka setelah itu aku mengantarkan [mg3_First] pulang kerumahnya~"

    scene jalan_malam with dissolve
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Oiya,, ceritain masalahmu ketika dulu lah sepertinya ada hal yang ga begitu baik"
    mc "Kamu sendiri ga mau ceritain"
    mg3 "yaudah gimana kalau besok kita saling bercerita"
    mc "Boleh kalau gitu"
    hide airin_alma with dissolve

    scene depan_rumah_airin_malam with dissolve
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Sudah sampai.. \nTerima kasih atas semuanya"
    mc "Aku juga Kalau gitu aku pulang dulu ya"
    mg3 "Iya hati-hati dijalan"
    hide airin_alma with dissolve

    stop music fadeout 1.0

    jump day6_Airin

    return
