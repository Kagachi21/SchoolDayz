label day1_Miselia:

    hide screen gotoMiselia
    hide screen gotoKirana
    hide screen gotoAirin

    scene jalan with dissolve
    "Ah... Jalan ini selalu tenang kalau pagi"

    stop music fadeout 1.0
    play music bertengkar fadein 1.0
    scene gerbang_sekolah with dissolve
    "Akhh.. Aku Menabrak sesuatu" with hpunch
    mc "ahh.. Maaf Kak, aku tidak sengaja"
    $ kk = "Kakak Kelas"
    kk "kamu anak kelas brapa ? kalo jalan tuh pakai mata dong !!"
    mc "iiya kak,, aku kelas 10, sekali lagi aku minta maaf ya"
    "Mungkin aku harus lari saja agar terhindar dari masalah"
    kk "loh eh eh mau kemana kamu ?"
    kk "Anak Baru Banyak belagu sekarang ya !!"

    play sound laridilorong fadein 1.0
    scene lorong with dissolve
    stop music fadeout 1.0
    play music jalan_jalan fadein 1.0
    stop sound fadeout 1.0
    "Huft.. Huftt.. Hufft.."
    "Sudah aman kah ? sepertinya sudah aman"

    scene kelas with dissolve
    "Seperti biasa suasananya sangat ramai.. Sigh.."
    "Lebih baik aku duduk dulu dan menggambar sembari nunggu bel masuk"
    "~Tuingg" with vpunch
    "Hmm apa Botol ? Siapa yang melempar ? Biar dah"
    skce2 "Ehhh... Maaf Maaf aku ga sengaja, ngelempar kena kamu"
    mc "hmm.. iyaa gapapa"
    "Aku Melihat ada cewe menghampiriku"
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Kamu gapapa ?"
    mg1 "Pusing tidak ?"
    mg1 "Ikut aku ke UKS ya"
    show miselia_uni at right with moveinleft:
        xpos 0.8
        ypos 1.2 
    mc "gapapa, aman"
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "oh okey baiklah kalo kamu ga kenapa-napa. aku duduk sini ya sebelahmu oke ?"
    show miselia_uni at right with moveinleft:
        xpos 0.8
        ypos 1.2
    mc "haa ?"
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Emang Kenapa ?"
    show miselia_uni at right with moveinleft:
        xpos 0.8
        ypos 1.2
    mc "Hmm.. Ok"
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Makasih"
    show miselia_uni at center with moveinleft:
        xpos 0.3
        ypos 1.2
    show nada_uni at right with moveinright:
        xpos 0.7
        ypos 1.2
    na "Cie cie ada apa ini ? kok Duduknya sebelahan"
    mc "Diam Kau"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    hide miselia_uni with moveoutleft
    hide nada_uni with moveoutleft
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "selamat pagi anak anak semuanya"
    sk "Pagii buu.."
    sr "bagaimana kabar pagi ini? apa kalian sehat dan bahagia? ibu harap kalian begitu ya"
    mg1 "alhamdulillah bu sehat dan selalu bahagia"
    sr "okelah, nahh untuk materi hari ini , eiitss tunggu tunggu, kalian apa uda siap buat menerima materi di pagi hari ini ?"
    $ wkk = "Wakil Ketua Kelas"
    wkk "sudah dong bu.. siap banget malah"
    sr "oke baiklah , ibu mulai ya.... nahhh untuk awal materi, ibu mau kalian baca dulu ya "
    sr "nanti baru ibu akan jelaskan yaaa! paham semuanya ??"
    sk "Paham Buu..."
    show bu_senda at right with moveinleft:
        xpos 0.9
        ypos 1.2
    #Materi Fungi
    $ _skipping = False
    sr "Kata jamur berasal dari kata latin yakni fungi. Jamur (fungi) bereproduksi secara aseksual yang menghasilkan spora, kuncup, dan fragmentasi" with dissolve
    sr "Ada lebih dari 50.000 spesies fungi yang ada di dunia ini. Karena jumlah spesiesnya sangat banyak," with dissolve
    sr "ada ilmu khusus untuk mempelajari tentang fungi atau jamur yang disebut Mikologi. Istilah Mikologi berasal dari bahasa Yunani “mykos”, yang berarti cendawan atau jenis jamur berbentuk payung." with dissolve
    sr "Sedangkan dengan cara seksual pada zigospora, askospora, dan basidiospora. Jamur (fungi) hidup di tempat-tempat yang lembap, air laut, air tawar," with dissolve
    sr " tempat yang asam dan bersimbosis dengan ganggang hingga kemudian membentuk lumut (lichenes)" with dissolve
    sr "Menurut Gandjar (2006) jamur atau fungi adalah sel eukariotik yang tidak memiliki klorofil, tumbuh sebagai hifa, memiliki dinding sel yang mengandung kitin" with dissolve
    sr "bersifat heterotrof, menyerap nutrien melalui dinding selnya, mengekskresikan enzim ekstraselular ke lingkungan melalui spora, dan melakukan reproduksi secara seksual dan aseksual" with dissolve
    sr "Sementara menurut Campbell (2003) Fungi adalah eukariota, dan sebagian besarnya merupakan eukariota multiseluler" with dissolve
    sr "Meskipun fungi pernah dikelompokkan ke dalam kingdom tumbuhan, fungi adalah organisme unik yang umumnya berbeda dari eukariota lainnya ditinjau dari caranya memperoleh makanan, organisasi struktural, pertumbuhan dan cara bereproduksi" with dissolve
    sr "Ciri-ciri Fungi (Jamur)" with dissolve
    sr "Secara umum, fungi atau jamur memiliki ciri-ciri sebagai berikut:" with dissolve
    sr "1. Memiliki benang halus atau yang biasa disebut hifa, dan kumpulan dari hifa disebut miselium. Hifa tersusun dari sel-sel yang terbentuk akibat pertumbuhan spora, dan hifa tersebut bisa berupa hifa tunggal atau hifa bercabang" with dissolve
    sr "2. Memiliki dan memproduksi spora" with dissolve
    sr "3. Berkembang biak baik secara seksual (generatif) dan aseksual (vegetatif)." with dissolve
    sr "4. Mengandung zat kitin, glukan, selulosa, dan mannan pada struktur tubuh jamur yang berfilamen dan dinding selnya." with dissolve
    $ _skipping = True
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Bel sudah berbunyi kalau gitu ibu akhiri \nSilahkan istirahat"
    hide bu_senda with moveoutright
    show nada_uni at center with moveinright:
        ypos 1.2
    na "[mcFirst] ikut ke kantin ?"
    mc "Ga ikut \n Aku malas sekali mau pergi ke kantin"
    na "Titip Lur ?"
    mc "Ga usah"
    na "Kalau gitu aku ke kantin dulu bro"
    hide nada_uni with moveoutright
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Kamu ga mau ikut nada ke kantin ?"
    mc "Ga"
    mg1 "Lahh Kenapa ?"
    mc "Mager, terlalu banyak orang orang"
    mg1 "Beneran ga ikut ? Soalnya, aku dengar dengar ada pentol enak di kantin"
    mg1 "ayoo , ikut ke kantin, beli pentol enduls"
    mc "Ga mau"
    mg1 "kamu harus ikut lah"
    mc "aku titip aja ya mei, gappa kan ? Aku capek soalnya."
    hide miselia_uni
    show miselia_uni_emosi at center:
        ypos 1.2
    mg1 "nggakk, kamu harus ikuutt!!" with hpunch
    "Merepotkan.."
    hide miselia_uni_emosi with moveoutright

    scene kantin with dissolve
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Sana cari tempat tunggu sana biar aku yang pesenin"
    mc "...."
    "Terlalu Ramai disini Hmm.. "
    "Aku Menyesal ikut kesini, kalau gitu aku ke [mg1_First] aja"
    mg1 "eehhhh,, ngapainn kesini? katanya males, disuruh tunggu sana , malah milih kesini hm. ini loh udah selesai"
    mc "Kurang enak suasanya ramai"
    mg1 "nanti malah ga ketemu tempat duduk"
    kt "Ini mbak Pentol Pedesnya"
    mg1 "makasih bu "
    hide miselia_uni
    show miselia_uni_emosi at center:
        ypos 1.2
    mg1 "Mana ya tempat duduk ?"
    mg1 "Tuhkan ga ada "
    mc "M-maaf"
    hide miselia_uni_emosi
    show miselia_uni_cuek at center:
        ypos 1.2
    mg1 "dah lah ayok balik ke kelas aja"
    hide miselia_uni_cuek with moveoutleft

    scene kelas with dissolve
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Oiyaa, Kamuu itu murid yang dibully parah waktu smp dulu kan ?"
    mc "...."
    mc "Siapa itu ?"
    mc "Sudah sudah, nanti pentolnya jadi ga enak karena dingin Mending kita makan"
    hide miselia_uni
    show miselia_uni_emosi at center:
        ypos 1.2
    mg1 "hmm... Iyaa"
    hide miselia_uni_emosi with dissolve
    "Ternyata rasanya enak, ga begitu buruk juga"
    "Aku pikir rasanya biasa biasa aja"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    stop music fadeout 1.0
    play music jalan_jalan2 fadein 1.0
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat siang anak - anak"
    sk 'Siangg Bu~'
    sr "Kok kelihatan letih semua"
    skco1 "Capek bu mau cepat cepat pulang"
    sr "Ayo semangat semangat"
    skce2 "Baikk Buu!"
    sr "Ini ibu akan melanjutkan meteri yang tadi"
    sr "Ini Ibu Kasih soalnya dikerjakan ya"
    skco2 "Sekarang bu ?"
    sr "Iyaa sekarangg"
    skco2 "Saya kira Minggu depan bu Hehehehe"
    sr "isshh.. Kamu ini. Oiya, Kalau sudah selesai nanti kita koreksi bersama ya"
    sr "Setelah itu kalian bebas mau ngapain aja sampai jam pelajaran habis"
    sk "Yuuuhuuu~ Siapp Bu"
    sr "Ini Soalnya bagikan ke belakang"
    sr "kalau sudah selamat mengerjakan"
    hide bu_senda with moveoutright

    "~SOAL~"
    #Initialize score
    $ quiz_fungi1_score = 0

    label quiz_fungi1:
        $ quick_menu = False

        "1. Jamur yang berperan dalam pembuatan tempe adalah ..."
        menu:
            "A. Aspergilus sp":
                $ quiz_fungi1_score += 0
            "B. Rhizopus sp":
                $ quiz_fungi1_score += 10
            "C. Therospora sp ":
                $ quiz_fungi1_score += 0
            "D. Mucor sp":
                $ quiz_fungi1_score += 0

        show fungid1 at truecenter with dissolve
        "2. Perhatikan dan amati gambar di atas! Bagian sporangiosfor terdapat pada nomor ..."
        menu:
            "A. 1":
                $ quiz_fungi1_score += 0
            "B. 4":
                $ quiz_fungi1_score += 0
            "C. 2":
                $ quiz_fungi1_score += 10
            "D. 3":
                $ quiz_fungi1_score += 0
        hide fungid1 with dissolve

        "3. Klasifikasi jamur dikelompokkan berdasarkan ...."
        menu:
            "A. habitatnya":
                $ quiz_fungi1_score += 0
            "B. ciri morfologi":
                $ quiz_fungi1_score += 0
            "C. ciri reproduksi":
                $ quiz_fungi1_score += 10
            "D. ciri biokimia":
                $ quiz_fungi1_score += 0

        "4. Jamur tidak dapat digolongkan ke dalam dunia tumbuhan 
        karena...."
        menu:
            "A. bersifat autrotof":
                $ quiz_fungi1_score += 0
            "B. tidak mempunyai klorofil":
                $ quiz_fungi1_score += 10
            "C. mempunyai spora":
                $ quiz_fungi1_score += 0
            "D. mempunyai floem":
                $ quiz_fungi1_score += 0
            
        "5. Kumpulan benang­ - benang halus yang terdapat pada jamur disebut ...."
        menu:
            "A. miselium":
                $ quiz_fungi1_score += 10
            "B. askospora":
                $ quiz_fungi1_score += 0
            "C. spora":
                $ quiz_fungi1_score += 0
            "D. basidiospora":
                $ quiz_fungi1_score += 0

        "6. Sekat yang menonjol dalam sprangium pada Mucor mocedo disebut ..."
        menu:
            "A. sporangium":
                $ quiz_fungi1_score += 0
            "B. basidium":
                $ quiz_fungi1_score += 0
            "C. konidium":
                $ quiz_fungi1_score += 0
            "D. kulomela":
                $ quiz_fungi1_score += 10

        "7. Jamur tidak memiliki kormus, tetapi hanya memiliki …."
        menu:
            "A. daun":
                $ quiz_fungi1_score += 0
            "B. talus":
                $ quiz_fungi1_score += 10
            "C. cabang":
                $ quiz_fungi1_score += 0
            "D. batang":
                $ quiz_fungi1_score += 0

        "8. Salah satu contoh jamur Zygomycota adalah …."
        menu:
            "A. jamur ragi":
                $ quiz_fungi1_score += 0
            "B. jamur merang":
                $ quiz_fungi1_score += 0
            "C. jamur tempe":
                $ quiz_fungi1_score += 10
            "D. jamur kuping":
                $ quiz_fungi1_score += 0

        "9. Di bawah ini yang merupakan pernyataan yang benar adalah …."
        menu:
            "A. anteridium mengandung dua inti":
                $ quiz_fungi1_score += 0
            "B. askogonium mengandung dua inti":
                $ quiz_fungi1_score += 0
            "C. inti askogonium berpindah tempat ke anteridium":
                $ quiz_fungi1_score += 0
            "D. anteridium mengandung inti yang haploid":
                $ quiz_fungi1_score += 10

        "10. Dinding sel pada jamur Zygomycota mengandung zat …."
        menu:
            "A. Kitin":
                $ quiz_fungi1_score += 10
            "B. tanduk":
                $ quiz_fungi1_score += 0
            "C. selulosa":
                $ quiz_fungi1_score += 0
            "D. Fiositin":
                $ quiz_fungi1_score += 0

        "Jawaban : 
            \n
            1. B \ \ \ \ 3. C \ \ \ \ 5. A \ \ \ \ 7. B \ \ \ \ 9. D
            \n  
            2. C \ \ \ \ 4. B \ \ \ \ 6. D \ \ \ \ 8. C \ \ \ \ 10. A"

        "Nilaiku adalah [quiz_fungi1_score]"

    # Check the quiz 1 score
    if quiz_fungi1_score >= 75:
        # Win
        $ quick_menu = True
        show bu_senda at center with dissolve:
            ypos 1.2
        sr "Selamat Bagi yang Nilainya Bagus"
        sr "Kalian bebas melakukan apa saja sampai waktu pelajaran habis"
        # Did he win? Yes.
        #$ quiz_fungi1_win = True
        #$ quiz_fungi1_lose = False   
    else:
        # Lose
        sr "Bagi yang Nilainya jelek bisa mengulang lagi"
        menu:
            "Mengulang Lagi":
                $ quiz_fungi1_score = 0
                jump quiz_fungi1
            "Tidak Ingin Mengulang":
                "Anda gagal sebagai murid"
                "~END~"
                return
        # Did he win? No.
        #$ quiz1_win = False
        #$ quiz1_lose = True

    #if quiz1_win:
        #jump happylove
        
    #if quiz1_lose:
        #jump breakup

    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    sk "Yeay Sudah Pulang"
    sr "Baik Anak - Anak sekian dari Ibu"
    sr "Kalian sudah boleh pulang"
    hide bu_senda with moveoutright
    show miselia_uni at center with moveinleft:
        ypos 1.2
    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    mg1 "Pulangg yuuk [mcFirst]"
    mg1 "Aku bawa Sepeda Motor, biar makin cepet gitu"
    mc "Ga usah, Rumahku ga begitu jauh juga"
    mg1 "Aku sekalian biar tau rumahmu Hehehe"
    mc "...."
    mc "ga usah repot repot, Terima kasih atas tawarannya aku jalan saja"
    hide miselia_uni with moveoutright

    scene jalan_sore with dissolve
    mc "Ngapain ikutin aku segala ?"
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Aku pengen tau rumahmu juga"
    mc "...."
    mc "Yaudah, sini sini aku yang nyetir"
    mg1 "Yeayyy"
    hide miselia_uni with moveoutleft

    stop music fadeout 1.0
    play music sore fadein 1.0

    scene depan_rumah_sore with dissolve
    mc "Makasih ya.. sudah sana pulang"
    show miselia_uni_emosi at center with moveinright:
        ypos 1.2
    mg1 "Hai.. Haii.."
    show miselia_uni_emosi at left with moveinright:
        xpos 0.1
        ypos 1.2
    show mom at center with moveinright:
        ypos 1.15
    mom "Lohh,, [mcFirst] temannya ga disuruh mampir dulu ?"
    mc "ehh, gak gak gak, gausa bu, biarin meiris pulang "
    mc "Dia terburu - terburu"
    hide miselia_uni_emosi
    show miselia_uni_cuek at center with moveoutleft:
        ypos 1.2
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    mg1 "heh, apa an si kamu ? iyaa te meiris mampir dulu"
    hide miselia_uni_cuek
    show miselia_uni at center:
        ypos 1.2
    mg1 "meiris parkir motor dulu ya "
    show miselia_uni at left with moveinright:
        xpos 0.25
        ypos 1.2
    show mom at center with moveinright:
        ypos 1.15
    mom "Iyaa Parkir disana ya "
    hide miselia_uni with moveoutleft
    mom "Siapa Namamu ?"
    show miselia_uni at left with moveinleft:
        xpos 0.25
        ypos 1.2
    mg1 "Nama Saya [mg1] te"
    mom "Tante baru tau kalau [mcFirst] ternyata sudah punya teman"
    mg1 "Hehehe.. Iya te"
    mc "...."
    mom "Marii Masuk Tante siapkan Makanan dulu. Pasti kalian lapar kan ?"
    mg1 "Yeayy, Iya te hehhe"
    hide mom with moveoutright
    hide miselia_uni with moveoutright
    mc "...."
    mc "Aku mau ganti baju dulu"

    scene ruang_tamu_sore with dissolve
    show miselia_uni at left with moveinleft:
        xpos 0.25
        ypos 1.2
    show mom at center with moveinleft:
        ypos 1.15
    mom "Nak Meiris tunggu sini ya"
    mg1 "Iyaa te hehe"
    mom "[mcFirst] Kalau sudah ganti baju temani dulu si [mg1_Last] !!"
    mc "Iya !!!"
    mg1 "Kalau gitu aku lihat lihat hal sekitar ya te"
    mom "Iyaa nak"
    hide mom with moveoutright
    hide miselia_uni with dissolve

    scene dapur_sore with dissolve
    show miselia_uni at right with moveinright:
        xpos 0.75
        ypos 1.2
    mg1 "Tante Tante ini foto siapa ? "
    show mom at center with dissolve:
        ypos 1.15
    mom "Itu Fotonya [mcFirst]"
    mg1 "Hahahahah Lucu Banget te" with vpunch
    mom "Bener kan"
    "Ada apa ini ramai ramai di dapur ?"
    mg1 "Ahhh Orangnya sudah ada disini"
    mg1 "Lihat - Lihat fotomu masih kecil lucu sekali"
    mg1 "Hahahaha" with vpunch
    mc "...."
    mc "kan resek banget sih jadi cewe"
    mc "Mana Fotonya ?"
    mg1 "Maaf maaf.. Habisnya lucu banget"
    mg1 "ini Fotonya"
    mc "kalau gitu aku taruh ini dulu"
    hide miselia_uni with dissolve
    hide mom with dissolve

    scene ruang_tamu_sore with dissolve
    mc "Bisa bisanya dia lihat fotoku"
    mc "Merepotkan"
    mom "Makanannya sudah siap!!!"
    
    scene dapur_sore with dissolve
    mc "Mantap sudah jadi"
    show miselia_uni at center with dissolve:
        ypos 1.2
    mg1 "Okay te Makasih banyak tante"
    mg1 "Wah,, terlihat enak tante"
    show mom at center with dissolve:
        xpos 0.7
        ypos 1.15
    mom "Iyaa silahkan dimakan"
    mc "Kalau sudah selesai segera pulang ya"
    mc "Biar ga kemalaman"
    mg1 "ahahaha Iyaa"
    mom "Gimana [mg1_Last] makanannya ?"
    mg1 "Wuiihh Enakk Tante masakannya tante"
    mg1 "Top Markotop !!"
    mom "Bisa aja kamu ini"
    hide mom with dissolve
    hide miselia_uni with dissolve
    "Kami pun makan dengan lahap. Lalu [mom] bermain bersama [cat]"
    show miselia_uni at center with dissolve:
        ypos 1.2
    mg1 "Kenyangnyaa~"
    mg1 "Saatnya cuci Piring"
    show mom at center with dissolve:
        xpos 0.7
        ypos 1.15
    mom "Ga usah nak meiris biar tante aja yang cuci piringnya"
    mg1 "Gapapa te soalnya Meiris sudah ngerepotin Tante dan [mcFirst] juga"
    mg1 "[mcFirst] ayoo temenin aku cuci piring"
    mc "Iya"
    hide mom with dissolve
    hide miselia_uni with moveoutleft
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    show miselia_uni at center with dissolve:
        ypos 1.2
    mg1 "Fuuhh Sudah selesai Cuci Piringnya "
    mg1 "Kalau gitu aku pulang dulu"
    mg1 "Aku mau pamit sama Tante dulu"
    mc "Mungkin ada di Ruang Keluarga"
    hide miselia_uni with moveoutleft

    scene ruang_keluarga_sore with dissolve
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Tante Tante"
    mg1 "Meiris Pulang dulu ya takut kemalaman terus ganggu tante sama [mcFirst]"
    show mom at center with dissolve:
        xpos 0.7
        ypos 1.15
    mom "Gapapa kok ga ngerepotin malah tante senang"
    mg1 "Iyaa te meiris sampai kenyang padahal pertama kali meiris kesini loh te"
    mg1 "Tapi sama tante sudah disuguhi banyak makanan"
    mom "Hahaha Iyaa gapapa"
    mg1 "Heheheh Kalau gitu Meiris pulang dulu ya te "
    mom "Iyaa hati - hati dijalan"
    mom "makasih juga udah mau nganterin,, anak ibu yang ganteng ini sampai rumah "
    hide mom with dissolve
    mg1 "Iya te Heheh"
    hide miselia_uni with moveoutleft

    scene depan_rumah_sore with dissolve
    mc "Terima Kasih [mg1_Last]"
    show miselia_uni at center with dissolve:
        ypos 1.2
    mg1 "Iyaa sama-sama"
    mc "Hati - Hati dijalan"
    "~Bruumm Brumm~"
    hide miselia_uni with moveoutleft

    "Lelahnya lebih baik aku tidur saja"

    stop music fadeout 1.0

    jump day2_Miselia

    return

label day1_Kirana:

    hide screen gotoMiselia
    hide screen gotoKirana
    hide screen gotoAirin

    scene jalan with dissolve
    "Ah... Jalan ini selalu tenang kalau pagi"

    stop music fadeout 1.0
    play music bertengkar fadein 1.0
    scene gerbang_sekolah with dissolve
    "Akhh.. Aku Menabrak sesuatu" with hpunch
    mc "ahh.. Maaf Kak, aku tidak sengaja"
    $ kk = "Kakak Kelas"
    kk "kamu anak kelas brapa ? kalo jalan tuh pakai mata dong !!"
    mc "iiya kak,, aku kelas 10, sekali lagi aku minta maaf ya"
    "Mungkin aku harus lari saja agar terhindar dari masalah"
    kk "loh eh eh mau kemana kamu ?"
    kk "Anak Baru Banyak belagu sekarang ya !!"
    play sound laridilorong fadein 1.0
    
    scene lorong with dissolve
    stop music fadeout 1.0
    play music jalan_jalan fadein 1.0
    stop sound fadeout 1.0
    "Huft.. Huftt.. Hufft.."
    "Sudah aman kah ? sepertinya sudah aman"

    scene kelas with dissolve
    "Seperti biasa suasananya sangat ramai.. Sigh.."
    "Lebih baik aku duduk dulu dan menggambar sembari nunggu bel masuk"
    "~Tuingg" with vpunch
    "Hmm apa Botol ? Siapa yang melempar ? Biar dah"
    skce2 "Ehhh... Maaf Maaf aku ga sengaja, ngelempar kena kamu"
    mc "hmm.. iyaa gapapa"
    "Aku Melihat ada cewe menghampiriku"
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Kamu gapapa ?"
    mg2 "Pusing tidak ?"
    mg2 "Ikut aku ke UKS ya"
    show ardana_uni at right with moveinleft:
        xpos 0.8
        ypos 1.2 
    mc "gapapa, aman"
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "oh okey baiklah kalo kamu ga kenapa-napa. aku duduk sini ya sebelahmu oke ?"
    show ardana_uni at right with moveinleft:
        xpos 0.8
        ypos 1.2
    mc "haa ?"
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Emang Kenapa ?"
    show ardana_uni at right with moveinleft:
        xpos 0.8
        ypos 1.2
    mc "Hmm.. Ok"
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Makasih"
    show ardana_uni at center with moveinleft:
        xpos 0.3
        ypos 1.2
    show nada_uni at right with moveinright:
        xpos 0.7
        ypos 1.2
    na "Cie cie ada apa ini ? kok Duduknya sebelahan"
    mc "Diam Kau"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    hide ardana_uni with moveoutleft
    hide nada_uni with moveoutleft
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "selamat pagi anak anak semuanya"
    sk "Pagii buu.."
    sr "bagaimana kabar pagi ini? apa kalian sehat dan bahagia? ibu harap kalian begitu ya"
    mg2 "alhamdulillah bu sehat dan selalu bahagia"
    sr "okelah, nahh untuk materi hari ini , eiitss tunggu tunggu, kalian apa uda siap buat menerima materi di pagi hari ini ?"
    $ wkk = "Wakil Ketua Kelas"
    wkk "sudah dong bu.. siap banget malah"
    sr "oke baiklah , ibu mulai ya.... nahhh untuk awal materi, ibu mau kalian baca dulu ya "
    sr "nanti baru ibu akan jelaskan yaaa! paham semuanya ??"
    sk "Paham Buu..."
    show bu_senda at right with moveinleft:
        xpos 0.9
        ypos 1.2
    #Materi Fungi
    $ _skipping = False
    sr "Virus berasal dari Bahasa Latin venom yang berarti cairan beracun. Berdasarkan sifatnya, virus digolongkan ke dalam kingdom tersendiri. Virus juga tidak termasuk ke dalam sel, karena tidak memiliki sitoplasma dan nukelus" with dissolve
    sr "Virus termasuk bagian dari mikroorganisme. Dinamakan bagian dari mikroorganisme karena merupakan makhluk hidup dengan ukuran hanya beberapa mikro atau mungkin lebih kecil dari itu, karena 1 mikron sama dengan 0,001 mm" with dissolve
    sr "Berdasarkan letaknya, virus bisa terdapat diluar maupun di dalam sel." with dissolve
    sr "Diluar sel, virus tidak bisa melakukan aktivitas hidupnya, sehingga hanya berupa partikel submikroskopis yang mengandung asam nukleat dan dibungkus oleh protein dan makromolekul lain." with dissolve
    sr "Di dalam sel, virus dapat melakukan aktivitas hidup dan memperbanyak diri, kemudian bisa menginfeksi sel hidup sehingga sel tersebut dapat mengalami gangguan bahkan kematian pada makhluk hidup yang diinfeksi." with dissolve
    sr "Para penemu virus antara lain D. Iwanoski (1892) pada tanaman tembakau, dilanjutkan M. Beijerinck (1898), Loffern dan Frooch (1897) menemukan dan memisahkan virus penyebab penyakit mulut dan kaki (food and mouth diseases)" with dissolve
    sr "Reed (1900) berhasil menemukan virus penyebab kuning (yellow fever), Twort dan Herelle (1917) penemu Bakteriofage, Wendell M. Stanley (1935) berhasil mengkristalkan virus mosaik pada tembakau" with dissolve
    sr "Pengetahuan tentang virus terus berkembang sampai lahir ilmu cabang biologi yang mempelajari virus disebut virology." with dissolve
    $ _skipping = True
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Bel sudah berbunyi kalau gitu ibu akhiri \nSilahkan istirahat"
    hide bu_senda with moveoutright
    show nada_uni at center with moveinright:
        ypos 1.2
    na "[mcFirst] ikut ke kantin ?"
    mc "Ga ikut \n Aku malas sekali mau pergi ke kantin"
    na "Titip Lur ?"
    mc "Ga usah"
    na "Kalau gitu aku ke kantin dulu bro"
    hide nada_uni with moveoutright
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Kamu ga mau ikut nada ke kantin ?"
    mc "Ga"
    mg2 "Lahh Kenapa ?"
    mc "Mager, terlalu banyak orang orang"
    mg2 "Beneran ga ikut ? Soalnya, aku dengar dengar ada pentol enak di kantin"
    mg2 "ayoo , ikut ke kantin, beli pentol enduls"
    mc "Ga mau"
    mg2 "kamu harus ikut lah"
    mc "aku titip aja ya na, gappa kan ? Aku capek soalnya."
    hide ardana_uni
    show ardana_uni_emosi at center:
        ypos 1.2
    mg2 "nggakk, kamu harus ikuutt!!" with hpunch
    "Merepotkan.."
    hide ardana_uni_emosi with moveoutright

    scene kantin with dissolve
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Sana cari tempat tunggu sana biar aku yang pesenin"
    mc "...."
    "Terlalu Ramai disini Hmm.. "
    "Aku Menyesal ikut kesini, kalau gitu aku ke [mg2_First] aja"
    mg2 "eehhhh,, ngapainn kesini? katanya males, disuruh tunggu sana , malah milih kesini hm. ini loh udah selesai"
    mc "Kurang enak suasanya ramai"
    mg2 "nanti malah ga ketemu tempat duduk"
    kt "Ini mbak Pentol Pedesnya"
    mg2 "makasih bu "
    hide ardana_uni
    show ardana_uni_emosi at center:
        ypos 1.2
    mg2 "Mana ya tempat duduk ?"
    mg2 "Tuhkan ga ada "
    mc "M-maaf"
    hide ardana_uni_emosi
    show ardana_uni_cuek at center:
        ypos 1.2
    mg2 "dah lah ayok balik ke kelas aja"
    hide ardana_uni_cuek with moveoutleft

    scene kelas with dissolve
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Oiyaa, Kamuu itu murid yang dibully parah waktu smp dulu kan ?"
    mc "...."
    mc "Siapa itu ?"
    mc "Sudah sudah, nanti pentolnya jadi ga enak karena dingin Mending kita makan"
    hide ardana_uni
    show ardana_uni_emosi at center:
        ypos 1.2
    mg2 "hmm... Iyaa"
    hide ardana_uni_emosi with dissolve
    "Ternyata rasanya enak, ga begitu buruk juga"
    "Aku pikir rasanya biasa biasa aja"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    stop music fadeout 1.0
    play music jalan_jalan2 fadein 1.0
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat siang anak - anak"
    sk 'Siangg Bu~'
    sr "Kok kelihatan letih semua"
    skco1 "Capek bu mau cepat cepat pulang"
    sr "Ayo semangat semangat"
    skce2 "Baikk Buu!"
    sr "Ini ibu akan melanjutkan meteri yang tadi"
    sr "Ini Ibu Kasih soalnya dikerjakan ya"
    skco2 "Sekarang bu ?"
    sr "Iyaa sekarangg"
    skco2 "Saya kira Minggu depan bu Hehehehe"
    sr "isshh.. Kamu ini. Oiya, Kalau sudah selesai nanti kita koreksi bersama ya"
    sr "Setelah itu kalian bebas mau ngapain aja sampai jam pelajaran habis"
    sk "Yuuuhuuu~ Siapp Bu"
    sr "Ini Soalnya bagikan ke belakang"
    sr "kalau sudah selamat mengerjakan"
    hide bu_senda with moveoutright

    "~SOAL~" with dissolve
    #Initialize score
    $ quiz1_score = 0

    label quiz1:
        $ quick_menu = False

        "1. Pengertian Virus"
        menu:
            "A. Merupakan organisme parasit, yang memiliki Bahasa Latin venom yang berarti cairan beracun":
                $ quiz1_score += 10
            "B. Merupakan kelompok makhluk hidup yang terdiri atas makhluk hidup bersel satu (tunggal) atau uniseluler":
                $ quiz1_score += 0
            "C. Salah Satu Sel yang membantu pencernaan pada tubuh manusia":
                $ quiz1_score += 0
            "D. Prokariot atau prokariotik merupakan salah satu klasifikasi makhluk hidup berdasarkan ada tidaknya membran yang membungkus inti sel":
                $ quiz1_score += 0

        "2. Sejarah Virus Dimitri ivanovsky"
        menu:
            "A. Berhasil meneliti penyakit pada tembakau yang menyebabkan daun memiliki bercak kekuningan":
                $ quiz1_score += 0
            "B. Berhasil mengristalkan makhluk penyebab penyakit pada tembakau pada tahun 1935. Kemudian, penyakit tersebut diberi nama Tobacco Mosaic Virus (TMV)":
                $ quiz1_score += 0
            "C. Menonaktifkan makhluk penyebab penyakit tersebut menggunakan alkohol. Hasilnya alkohol tidak bisa menonaktifkan makhluk tersebut":
                $ quiz1_score += 10
            "D. Disusun berdasarkan struktur organisasi internal sel, struktur organisasi sel, dan tipe nutrisi sel":
                $ quiz1_score += 0 

        "Berdasarkan pernyataan di atas ciri-ciri dari virus terdapat pada nomor" (multiple=2)
        "3. Perhatikanlah ciri-ciri struktur organisme di bawah ini !
                \n
                1. Ultramikroskopis
                \n
                2. Berkembang biak pada sel hidup
                \n
                3. Sel bersifat prokariotik
                \n
                4. Memiliki materi gen RNA atau DNA
                \n
                5. Memiliki sitoplasma" (multiple=2)
        menu:
            "A. 2, 3, dan 5":
                $ quiz1_score += 0
            "B. Semuanya benar":
                $ quiz1_score += 0
            "C. 1, 2, dan 4":
                $ quiz1_score += 10
            "D. 3, 4, dan 5":
                $ quiz1_score += 0

        "4. Sejarah Virus Martinus Beijerinck"
        menu:
            "A. Disusun berdasarkan struktur organisasi internal sel, struktur organisasi sel, dan tipe nutrisi sel":
                $ quiz1_score += 0
            "B. Menonaktifkan makhluk penyebab penyakit tersebut menggunakan alkohol. Hasilnya alkohol tidak bisa menonaktifkan makhluk tersebut":
                $ quiz1_score += 10
            "C. Berhasil mengristalkan makhluk penyebab penyakit pada tembakau pada tahun 1935. Kemudian, penyakit tersebut diberi nama Tobacco Mosaic Virus (TMV)":
                $ quiz1_score += 0
            "D. Berhasil meneliti penyakit pada tembakau yang menyebabkan daun memiliki bercak kekuningan":
                $ quiz1_score += 0
            
        "Berdasarkan pernyataan di atas yang bukam ciri-ciri dari virus terdapat pada nomor" (multiple=2)
        "5. Perhatikanlah ciri-ciri struktur organisme di bawah ini !
            \n
            1. Ultramikroskopis
            \n
            2. Sel bersifat prokariotik
            \n
            3. Memiliki sitoplasma
            \n
            4. Berkembang biak pada sel hidup
            \n
            5. Tersusun atas mukopolisakarida dan peptidoglikan"(multiple=2)
        menu:
            "A. 2, 3, dan 5":
                $ quiz1_score += 10
            "B. 1, 3, dan 4":
                $ quiz1_score += 0
            "C. Semuanya benar":
                $ quiz1_score += 0
            "D. 1 dan 4":
                $ quiz1_score += 0

        "6. Sejarah Virus Wendell Meredith Stanley"
        menu:
            "A. Berhasil meneliti penyakit pada tembakau yang menyebabkan daun memiliki bercak kekuningan":
                $ quiz1_score += 0
            "B. Disusun berdasarkan struktur organisasi internal sel, struktur organisasi sel, dan tipe nutrisi sel":
                $ quiz1_score += 0
            "C. Menonaktifkan makhluk penyebab penyakit tersebut menggunakan alkohol. Hasilnya alkohol tidak bisa menonaktifkan makhluk tersebut":
                $ quiz1_score += 0
            "D. Berhasil mengristalkan makhluk penyebab penyakit pada tembakau pada tahun 1935. Kemudian, penyakit tersebut diberi nama Tobacco Mosaic Virus (TMV)":
                $ quiz1_score += 10

        "7. Virus dikategorikan bukan sebagai sel karena tidak memiliki bagian dari"
        menu:
            "A. Asam nukleat":
                $ quiz1_score += 0
            "B. Protoplasma":
                $ quiz1_score += 10
            "C. Protein":
                $ quiz1_score += 0
            "D. Organel":
                $ quiz1_score += 0

        "8. Cabang ilmu Biologi yang mengkaji mengenai virus yatu"
        menu:
            "A. Serologi":
                $ quiz1_score += 0
            "B. Struktur hewan":
                $ quiz1_score += 0
            "C. Virology":
                $ quiz1_score += 10
            "D. Anatomi virus":
                $ quiz1_score += 0

        "9. Salah satu sifat virus yang sama dengan makhluk hidup lainnya adalah"
        menu:
            "A. Tidak pernah bisa dihambat dengan antiboitik":
                $ quiz1_score += 0
            "B. Bisa mengalami perubahan wujud":
                $ quiz1_score += 0
            "C. Meiliki ukuran yang ultramikroskopis":
                $ quiz1_score += 0
            "D. Mampu bereproduksi":
                $ quiz1_score += 10

        "10. Virus tidak dapat hidup di alam bebas, melainkan harus hidup secara parasit. Oleh karena itu, untuk memelihara virus digunakan"
        menu:
            "A. Embrio Ayam":
                $ quiz1_score += 10
            "B. Medium kentang dan agar–agar":
                $ quiz1_score += 0
            "C. Medium agar–agar":
                $ quiz1_score += 0
            "D. Medium air kelapa":
                $ quiz1_score += 0

        "Jawaban : 
            \n
            1. A \ \ \ \ 3. C \ \ \ \ 5. A \ \ \ \ 7. B \ \ \ \ 9. D
            \n
            2. C \ \ \ \ 4. B \ \ \ \ 6. D \ \ \ \ 8. C \ \ \ \ 10. A"

        "Nilaiku adalah [quiz1_score]"

    # Check the quiz 1 score
    if quiz1_score >= 75:
        # Win
        $ quick_menu = True
        show bu_senda at center with moveinright:
            ypos 1.2
        sr "Selamat Bagi yang Nilainya Bagus"
        sr "Kalian bebas melakukan apa saja sampai waktu pelajaran habis"
        # Did he win? Yes.
        #$ quiz1_win = True
        #$ quiz1_lose = False   
    else:
        # Lose
        show bu_senda at center with moveinright:
            ypos 1.2
        sr "Bagi yang Nilainya jelek bisa mengulang lagi"
        hide bu_senda with dissolve
        menu:
            "Mengulang Lagi":
                $ quiz1_score = 0
                jump quiz1
            "Tidak Ingin Mengulang":
                "Anda gagal sebagai murid"
                "~END~"
                return
        # Did he win? No.
        #$ quiz1_win = False
        #$ quiz1_lose = True

    #if quiz1_win:
        #jump happylove
        
    #if quiz1_lose:
        #jump breakup

    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    sk "Yeay Sudah Pulang"
    sr "Baik Anak - Anak sekian dari Ibu"
    sr "Kalian sudah boleh pulang"
    hide bu_senda with moveoutright
    show ardana_uni at center with moveinleft:
        ypos 1.2
    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    mg2 "Pulangg yuuk [mcFirst]"
    mg2 "Aku bawa Sepeda Motor, biar makin cepet gitu"
    mc "Ga usah, Rumahku ga begitu jauh juga"
    mg2 "Aku sekalian biar tau rumahmu Hehehe"
    mc "...."
    mc "ga usah repot repot, Terima kasih atas tawarannya aku jalan saja"
    hide ardana_uni with moveoutright

    scene jalan_sore with dissolve
    mc "Ngapain ikutin aku segala ?"
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Aku pengen tau rumahmu juga"
    mc "...."
    mc "Yaudah, sini sini aku yang nyetir"
    mg2 "Yeayyy"
    hide ardana_uni with moveoutleft

    stop music fadeout 1.0
    play music sore fadein 1.0

    scene depan_rumah_sore with dissolve
    mc "Makasih ya.. sudah sana pulang"
    show ardana_uni_emosi at center with moveinright:
        ypos 1.2
    mg2 "Hai.. Haii.."
    show ardana_uni_emosi at left with moveinright:
        xpos 0.1
        ypos 1.2
    show mom at center with moveinright:
        ypos 1.15
    mom "Lohh,, [mcFirst] temannya ga disuruh mampir dulu ?"
    mc "ehh, gak gak gak, gausa bu, biarin arda pulang "
    mc "Dia terburu - terburu"
    hide ardana_uni_emosi
    show ardana_uni_cuek at center with moveoutleft:
        ypos 1.2
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    mg2 "heh, apa an si kamu ? iyaa te arda mampir dulu"
    hide ardana_uni_cuek
    show ardana_uni at center:
        ypos 1.2
    mg2 "arda parkir motor dulu ya "
    show ardana_uni at left with moveinright:
        xpos 0.25
        ypos 1.2
    show mom at center with moveinright:
        ypos 1.15
    mom "Iyaa Parkir disana ya "
    hide ardana_uni with moveoutleft
    mom "Siapa Namamu ?"
    show ardana_uni at left with moveinleft:
        xpos 0.25
        ypos 1.2
    mg2 "Nama Saya [mg2] te"
    mom "Tante baru tau kalau [mcFirst] ternyata sudah punya teman"
    mg2 "Hehehe.. Iya te"
    mc "...."
    mom "Marii Masuk Tante siapkan Makanan dulu. Pasti kalian lapar kan ?"
    mg2 "Yeayy, Iya te hehhe"
    hide mom with moveoutright
    hide ardana_uni with moveoutright
    mc "...."
    mc "Aku mau ganti baju dulu"

    scene ruang_tamu_sore with dissolve
    show ardana_uni at left with moveinleft:
        xpos 0.25
        ypos 1.2
    show mom at center with moveinleft:
        ypos 1.15
    mom "Nak Arda tunggu sini ya"
    mg2 "Iyaa te hehe"
    mom "[mcFirst] Kalau sudah ganti baju temani dulu si [mg2_Last] !!"
    mc "Iya !!!"
    mg2 "Kalau gitu aku lihat lihat hal sekitar ya te"
    mom "Iyaa nak"
    hide mom with moveoutright
    hide ardana_uni with dissolve

    scene dapur_sore with dissolve
    show ardana_uni at right with moveinright:
        xpos 0.75
        ypos 1.2
    mg2 "Tante Tante ini foto siapa ? "
    show mom at center with dissolve:
        ypos 1.15
    mom "Itu Fotonya [mcFirst]"
    mg2 "Hahahahah Lucu Banget te" with vpunch
    mom "Bener kan"
    "Ada apa ini ramai ramai di dapur ?"
    mg2 "Ahhh Orangnya sudah ada disini"
    mg2 "Lihat - Lihat fotomu masih kecil lucu sekali"
    mg2 "Hahahaha" with vpunch
    mc "...."
    mc "kan resek banget sih jadi cewe"
    mc "Mana Fotonya ?"
    mg2 "Maaf maaf.. Habisnya lucu banget"
    mg2 "ini Fotonya"
    mc "kalau gitu aku taruh ini dulu"
    hide ardana_uni with dissolve
    hide mom with dissolve

    scene ruang_tamu_sore with dissolve
    mc "Bisa bisanya dia lihat fotoku"
    mc "Merepotkan"
    mom "Makanannya sudah siap!!!"
    
    scene dapur_sore with dissolve
    mc "Mantap sudah jadi"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Okay te Makasih banyak tante"
    mg2 "Wah,, terlihat enak tante"
    show mom at center with dissolve:
        xpos 0.7
        ypos 1.15
    mom "Iyaa silahkan dimakan"
    mc "Kalau sudah selesai segera pulang ya"
    mc "Biar ga kemalaman"
    mg2 "ahahaha Iyaa"
    mom "Gimana [mg2_Last] makanannya ?"
    mg2 "Wuiihh Enakk Tante masakannya tante"
    mg2 "Top Markotop !!"
    mom "Bisa aja kamu ini"
    hide mom with dissolve
    hide ardana_uni with dissolve
    "Kami pun makan dengan lahap. Lalu [mom] bermain bersama [cat]"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Kenyangnyaa~"
    mg2 "Saatnya cuci Piring"
    show mom at center with dissolve:
        xpos 0.7
        ypos 1.15
    mom "Ga usah nak arda biar tante aja yang cuci piringnya"
    mg2 "Gapapa te soalnya Arda sudah ngerepotin Tante dan [mcFirst] juga"
    mg2 "[mcFirst] ayoo temenin aku cuci piring"
    mc "Iya"
    hide mom with dissolve
    hide ardana_uni with moveoutleft
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Fuuhh Sudah selesai Cuci Piringnya "
    mg2 "Kalau gitu aku pulang dulu"
    mg2 "Aku mau pamit sama Tante dulu"
    mc "Mungkin ada di Ruang Keluarga"
    hide ardana_uni with moveoutleft

    scene ruang_keluarga_sore with dissolve
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Tante Tante"
    mg2 "Arda Pulang dulu ya takut kemalaman terus ganggu tante sama [mcFirst]"
    show mom at center with dissolve:
        xpos 0.7
        ypos 1.15
    mom "Gapapa kok ga ngerepotin malah tante senang"
    mg2 "Iyaa te arda sampai kenyang padahal pertama kali arda kesini loh te"
    mg2 "Tapi sama tante sudah disuguhi banyak makanan"
    mom "Hahaha Iyaa gapapa"
    mg2 "Heheheh Kalau gitu Arda pulang dulu ya te "
    mom "Iyaa hati - hati dijalan"
    mom "makasih juga udah mau nganterin,, anak ibu yang ganteng ini sampai rumah "
    hide mom with dissolve
    mg2 "Iya te Heheh"
    hide ardana_uni with moveoutleft

    scene depan_rumah_sore with dissolve
    mc "Terima Kasih [mg2_Last]"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Iyaa sama-sama"
    mc "Hati - Hati dijalan"
    "~Bruumm Brumm~"
    hide ardana_uni with moveoutleft

    "Lelahnya lebih baik aku tidur saja"

    stop music fadeout 1.0
    jump day2_Kirana
    return

label day1_Airin:
    
    hide screen gotoMiselia
    hide screen gotoKirana
    hide screen gotoAirin

    scene jalan with dissolve
    "Sudah mulai ramai ternyata disini"

    scene gerbang_sekolah with dissolve
    show nada_uni at center with dissolve:
        ypos 1.2
    na "oeee [mcFirst] Tunggu akuu!!"
    mc "...."
    na "Akhirnya sampai juga, dihh ga di tungguin lur"
    mc "Sudah, tadi jalan pelan klo dah ga ditungguin bakal lari aku"
    na "Iya juga ya hahahha"
    na "Di kantin ada pentol enak bro"
    mc "Berapaan itu ?"
    na "1 Pentol 500 an ada yang pedes ada yang biasa"
    na "yang pedes enak pentolnya, nanti ke kantin bareng-bareng temen aja"
    mc "oh ok"
    hide nada_uni with dissolve

    scene lorong with dissolve
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Ada apa bro mulai tadi lihat [mg3_First] suka ya ?"
    mc "Hah ? Ga"
    na "Halah palingan suka. Namanya dia [mg3]{p}dia sekelas sama kita{p}wait wait kemarin kemana aja kamu ? kayaknya ada di kelas"
    mc "Ohh.. sekelas ya. kemarin aku ga merhatikan waktu perkenalan"
    na "Pantas aja kamu ga tau tapi kok tiba-tiba lihat dia mulu"
    na "Apa ada sesuatu ?"
    mc "Ga ada"
    hide nada_uni with dissolve

    scene kelas with dissolve
    "Ternyata dia pendiam juga di kelas sama sepertiku ga terlalu suka bersosial"
    skce2 "Kamu mau ikut keluar ?"
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Umm.. ga, aku diam di kelas aja"
    hide airin_uni with dissolve
    skce2 "Ahh.. okk"
    "Ahhh dia lihat balik aku.."
    "Kenapa aku bisa melihat dia terus-terusan ? Dahlah"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "selamat pagi anak anak semuanya"
    sk "Pagii buu.."
    sr "bagaimana kabar pagi ini? apa kalian sehat dan bahagia? ibu harap kalian begitu ya"
    sk "alhamdulillah bu sehat dan selalu bahagia"
    sr "okelah, nahh untuk materi hari ini , eiitss tunggu tunggu, kalian apa uda siap buat menerima materi di pagi hari ini ?"
    $ wkk = "Wakil Ketua Kelas"
    wkk "sudah dong bu.. siap banget malah"
    sr "oke baiklah , ibu mulai ya.... nahhh untuk awal materi, dengarkan penjelasan Bu Senda ya"
    sr "nanti baru ibu akan berikan soalnya! paham semuanya ??"
    sk "Paham Buu.."
    show bu_senda at right with moveinleft:
        xpos 0.9
        ypos 1.2
    $ _skipping = False
    "~Materi Klasifikasi~"
    window hide dissolve
    stop music fadeout 1.0
    #Video Klasifikasi
    show pengertian_klasi behind sr at center with dissolve:
        xpos 0.3
        ypos 0.6
        zoom 0.5
    $ renpy.pause(23.5, hard=True)
    hide pengertian_klasi with dissolve
    window show dissolve
    $ _skipping = True
    play music jalan_jalan2 fadein 1.0
    sr "Sudah baca kah semuanya ?"
    sk "Sudah bu.."
    sr "Kalau gitu ini soalnya dibagi ya"
    sk "Okie bu"
    hide bu_senda with dissolve

    "~SOAL~" with dissolve
    #Initialize score
    $ quiz1_klasifikasi_score = 0

    label quiz1_klasifikasi:
        $ quick_menu = False

        "1. Suatu sistem yang dapat memudahkan kita mempelajari dan mengenal makhluk hidup adalah…… "
        menu:
            "A. Sistem klasifikasi":
                $ quiz1_klasifikasi_score += 10
            "B. Proses klasifikasi":
                $ quiz1_klasifikasi_score += 0
            "C. Klasifikasi sistem alami":
                $ quiz1_klasifikasi_score += 0
            "D. Klasifikasi sistem buatan":
                $ quiz1_klasifikasi_score += 0

        "2. Cara pengelompokan berdasarkan ciri morfologi, anatomi, dan fisiologi disebut……"
        menu:
            "A. klasifikasi sistem buatan":
                $ quiz1_klasifikasi_score += 0
            "B. klasifikasi sistem alami":
                $ quiz1_klasifikasi_score += 10
            "C. proses Klasifikasi":
                $ quiz1_klasifikasi_score += 0
            "D. taksonomi":
                $ quiz1_klasifikasi_score += 0 

        "3. cara pengelompokan sejarah evolusi suatu makhluk hidup disebut……"
        menu:
            "A. klasifikasi sistem buatan":
                $ quiz1_klasifikasi_score += 0
            "B. klasifikasi sistem alami":
                $ quiz1_klasifikasi_score += 0
            "C. klasifikasi sistem filogeni":
                $ quiz1_klasifikasi_score += 10
            "D. taksonomi":
                $ quiz1_klasifikasi_score += 0

        "4. Cabang ilmu biologi yang mengkaji pengelompokan makhluk hidup disebut……"
        menu:
            "A. klasifikasi sistem buatan":
                $ quiz1_klasifikasi_score += 0
            "B. proses klasifikasi":
                $ quiz1_klasifikasi_score += 0
            "C. klasifikasi sistem filogeni":
                $ quiz1_klasifikasi_score += 0
            "D. taksonomi":
                $ quiz1_klasifikasi_score += 10
            
        "5. Sistem klasifikasi makhluk hidup pertama kali dipelopori oleh……"
        menu:
            "A. Carolus Linnaeus":
                $ quiz1_klasifikasi_score += 10
            "B. A. mayer":
                $ quiz1_klasifikasi_score += 0
            "C. Thomas alfa A":
                $ quiz1_klasifikasi_score += 0
            "D. Anthony Van Leuwenhoek":
                $ quiz1_klasifikasi_score += 0

        "6. Urutan tingkat takson dari yang tertinggi sampai terendah adalah……"
        menu:
            "A. Kingdom-filum/divisi-kelas-ordo-famili-genus-spesies":
                $ quiz1_klasifikasi_score += 10
            "B. Kingdom-filum/divisi-ordo-kelas-famili-genus-spesies":
                $ quiz1_klasifikasi_score += 0
            "C. Kingdom-filum/divisi-ordo-kelas-genus-famili-spesies":
                $ quiz1_klasifikasi_score += 0
            "D. Kingdom-filum/divisi-kels-ordo-genus-famili-spesies":
                $ quiz1_klasifikasi_score += 0

        "7. Berikut ini yang memiliki kesamaan ciri lebih banyak adalah orgamisme dalam satu……"
        menu:
            "A. Spesies":
                $ quiz1_klasifikasi_score += 0
            "B. Kelas":
                $ quiz1_klasifikasi_score += 0
            "C. Ordo":
                $ quiz1_klasifikasi_score += 0
            "D. Genus":
                $ quiz1_klasifikasi_score += 10

        "8. Sistem klasifikasi yang dikembangkan pertama kali oleh ilmuan adalah……"
        menu:
            "A. Sistem enam kingdom":
                $ quiz1_klasifikasi_score += 0
            "B. Sistem lima kingdom":
                $ quiz1_klasifikasi_score += 0
            "C. Sistem dua kingdom":
                $ quiz1_klasifikasi_score += 10
            "D. Sistem tiga kingdom":
                $ quiz1_klasifikasi_score += 0

        "9. Sistem dua kingdom ini makhluk hidup dikelompokan dalam dua kelompok besar yaitu……"
        menu:
            "A. Kelompok tumbuhan (kingdom fungi) dan kelompok hewan (kingdom plantae)":
                $ quiz1_klasifikasi_score += 0
            "B. Kelompok tumbuhan (kingdom plantae) dan kelompok hewan (kingdom animalia)":
                $ quiz1_klasifikasi_score += 10
            "C. Kelompok tumbuhan (kingdom monera) dan kelompok hewan (kingdom animalia)":
                $ quiz1_klasifikasi_score += 0
            "D. Kelompok tumbuhan (kingdom protista) dan kelompok hewan (kingdom monera)":
                $ quiz1_klasifikasi_score += 0

        "10. Sistem tiga kingdom muncul setelah adanya……"
        menu:
            "A. Mikroskop":
                $ quiz1_klasifikasi_score += 10
            "B. Teropong":
                $ quiz1_klasifikasi_score += 0
            "C. Kamera":
                $ quiz1_klasifikasi_score += 0
            "D. Teleskop":
                $ quiz1_klasifikasi_score += 0

        "Jawaban :
            \n
            1. A \ \ \ \ 3. C \ \ \ \ 5. A \ \ \ \ 7. D \ \ \ \ 9. B
            \n  
            2. B \ \ \ \ 4. D \ \ \ \ 6. A \ \ \ \ 8. C \ \ \ \ 10. A"

        "Nilaiku adalah [quiz1_klasifikasi_score]"

    # Check the quiz 1 score
    if quiz1_klasifikasi_score >= 75:
        # Win
        $ quick_menu = True
        show bu_senda at center with dissolve:
            ypos 1.2
        sr "Selamat Bagi yang Nilainya Bagus"
        sr "Kalian bebas melakukan apa saja sampai waktu pelajaran habis"
        # Did he win? Yes.
        #$ quiz1_klasifikasi_win = True
        #$ quiz1_klasifikasi_lose = False   
    else:
        # Lose
        sr "Bagi yang Nilainya jelek bisa mengulang lagi"
        menu:
            "Mengulang Lagi":
                $ quiz1_klasifikasi_score = 0
                jump quiz1_klasifikasi
            "Tidak Ingin Mengulang":
                "Anda gagal sebagai murid"
                "~END~"
                return
        # Did he win? No.
        #$ quiz1_klasifikasi_win = False
        #$ quiz1_klasifikasi_lose = True

    #if quiz1_klasifikasi_win:
        #jump happylove
        
    #if quiz1_klasifikasi_lose:
        #jump breakup

    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    sr "Waktunya sudah habis anak-anak, Bu Senda akhiri sekarang, semuanya sudah boleh pulang"
    sk "Yeay,, Pulang"
    sr "Kalau gitu ibu keluar dulu"
    hide bu_senda with moveoutright
    sk "Baik bu.."
    "Haaa.. Masih ramai kutunggu lainnya keluar dulu aja dah"
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Lur, Ga pulang ?"
    mc "Nanti saja duluan gapapa"
    na "Kemarin juga gitu.. Okk dah kalau gitu aku duluan"
    hide nada_uni with moveoutright
    mc "Ada sesuatu soalnya hahah.. Okk Hati-hati lur"
    "Sudah sepi ternyata saatnya pulang"
    
    stop music fadeout 1.0
    play music nyanyi fadein 1.0

    scene lorong_sore with dissolve
    "Hmm.. Terdengar lagi nyanyiannya, aku penasaran apakah yang cewe yang kemarin ya ?"

    scene atap_sore with dissolve
    "Wahh.... Apa dia setiap hari latihan disini ? Mungkin dia dari ekskul padsu atau sejenisnya"
    "Suaranya enak apa aku harus diam dulu disini sampai dia selesai ?"
    "Sudah selesai ? Mungkin aku intip saja"
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Hmm.. ??"
    hide airin_uni
    show airin_jalan_uni at center:
        ypos 0.95
    "Dia telah melihatku, sepertinya dia mau kesini kalau gitu aku langsung pulang saja lah"
    hide airin_jalan_uni
    show airin_uni at center:
        ypos 1.2
    mg3 "Lohh.. ga ada siapa-siapa ? apa aku salah lihat ya"
    mg3 "Aneh padahal tadi kayak ada seseorang yang merhatiin"
    mg3 "Sudah lah..."
    hide airin_uni with dissolve

    scene lorong_sore with dissolve
    "Hoshh.. Hoshh.. Hosshh Syukurlah ga ketemu hahahaha"
    "Sudah lah aku pulang saja"

    scene gerbang_sekolah_sore with dissolve
    "Ternyata dia masih mau latihan nyanyi lagi"

    stop music fadeout 1.0
    play music jalan_jalan2 fadein 1.0

    scene atap_sore with dissolve
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Ternyata laki yang kemarin baru saja pulang"
    mg3 "Hmmm.. apa dia yaa yang ngeliatin aku tadi ya?"
    hide airin_uni with dissolve

    stop music fadeout 1.0
    play music sore fadein 1.0

    scene depan_rumah_sore with dissolve
    mc "Aku Pulangg !!"

    scene ruang_tamu_sore with dissolve
    mc "Lohh,, ada [cat] Hee.. kamu lapar ?"
    show cat_happy at center with moveoutbottom:
        ypos 0.775
    cat "Meooww ///"
    mc "Kuy ikut aku di dapur"
    hide cat_happy with dissolve

    scene dapur_sore with dissolve
    mc "Ini makanannya. Btw, kok sepi ya"
    mc "Semuanya pada kemana [cat] kok sepi ? Kalau ayah pasti masih kerja"
    show cat at center with dissolve:
        ypos 0.775
    cat "Meooowww ??"
    mc "Kalau gitu aku langsung tidur aja [cat] selamat menikmati makanannya"
    cat "Meooowww"
    hide cat with dissolve

    scene kamar_sore with dissolve
    "Haaa.. capeknyaa... \n ganti baju dulu lalu tidur"

    scene kamar_malam with dissolve
    "Hoaamm... Sudah malam ternyata"

    scene ruang_keluarga_malam with dissolve
    mc "Hooo [dad] sudah pulang"
    show dad_cas at center with dissolve:
        ypos 1.2
    dad "Iyaa dong ahhaa.."
    dad "Ini ada [cat] juga disebelah tidur setelah main sama [dad]"
    mc "Ibu dimana ? tadi ga ada soalnya"
    dad "Ayah juga gatau soalnya ayah datang [mom] sudah ada dirumah \n sekarang ada di dapur lagi masak buat makan malam"
    mc "ohh.. okk si [cat] tenang sekali"
    dad "Nahh,, iyaa kyaknya nyaman sama [dad] hahahha"
    hide dad_cas with dissolve

    scene dapur_malam with dissolve
    mc "Bu, tadi kemana ?"
    show mom at center with dissolve:
        ypos 1.15
    mom "Umm... Tadi [mom] belanja di pasar"
    mom "Bentar lagi [mom] selesai masaknya, Tolong, [dad] dan [cat] panggilkan"
    mc "Okk bu"
    hide mom with dissolve

    scene ruang_keluarga_malam with dissolve
    mc "[dad] dan [cat] Makanan sudah siap"
    show dad_cas at center with dissolve:
        xpos 0.65
        ypos 1.2
    show cat at center with moveoutbottom:
        ypos 0.775
    dad "Hoo.. sudah siapp.. Ayo [cat] makan"
    cat "Meoooowww"
    hide cat with dissolve
    hide dad_cas with dissolve
    
    scene dapur_malam with dissolve
    mc "Ini kutuangkan untukmu [cat]"
    show cat at center with dissolve:
        ypos 0.775
    cat "Meoooww"
    hide cat with dissolve
    show dad_cas at center with dissolve:
        ypos 1.2
    dad "Enaknyaa,, sampe lapar hahaha"
    show mom at center with dissolve:
        ypos 1.15
    show dad_cas at center with dissolve:
        xpos 0.65
        ypos 1.2
    mom "ihhh.. ahhaha ayooo di makan"
    mom "Oiya,, gimana sekolahmu ? apa ada masalah ?"
    mc "Ga ada bu, aman cuma ada yang merepotkan"
    mom "apa itu ?"
    mc "tapi gapapa kok bu"
    mom "Baiklah, kalau gitu misal ada apa-apa bilang sama [dad] dan [mom] ya"
    mc "Iya bu"
    hide dad_cas with dissolve
    hide mom with dissolve

    scene kamar_malam with dissolve
    "Kenyangnya.. Fuuhh~~"
    "Masalah kah ? semoga kedepannya ga ada masalah sama sekali kejadian dulu tak terulang"

    stop music fadeout 1.0

    jump day2_Airin
    return
