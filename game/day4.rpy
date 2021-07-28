label day4_Kirana:

    play music pagi fadein 1.0
    window hide dissolve
    scene sky2 with dissolve
    show day4 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day4 with dissolve
    window show dissolve

    scene kamar with dissolve
    "Ugghh.. pusing sekali dan lapar juga mungkin ini gara-gara aku langsung tidur"
    stop sound fadeout 1.0
    play sound burung_terbang fadein 1.0
    window hide dissolve
    pause 3.0
    window show dissolve
    "Kipasnya menghadap persis di aku lagi, malam ga makan sama sekali bisa jadi ini masuk angin"
    "Pasti [cat] sudah keluar kamar duluan dan makan"
    "Lebih Baik aku cuci muka dulu"

    scene kamar_mandi with dissolve
    play sound mandi fadein 1.0
    "Ughhh.. aku mandi pakai air panas aja kalau gitu"
    stop sound fadeout 1.0

    scene kamar with dissolve
    "Masih tetap pusing.. Ughhh..."
    "Aku pakai seragam aja dulu nanti tinggal makan saja"

    scene dapur with dissolve
    mc "[cat] Ternyata dah disini aja kamu hahahha"
    mc "Dasarr haha"
    show cat at center with moveinbottom:
        ypos 0.75
    cat "Nyaaa Nya Nyaa"
    hide cat
    mc "Bu,, aku kenapa ya kok lapar banget ?"
    show mom at center with dissolve:
        ypos 1.15
    mom "kamu kan tadi malam ga makan sama sekali"
    mom "langsung tidur kan jadi wajar paginya lapar"
    mom "Ini Makanannya sudah siap juga, bekalnya ada di meja makan juga nanti bawa"
    mc "Iyaa bu. Kalau gitu aku makan dulu bu"
    show mom at center with moveinright:
        xpos 0.3
        ypos 1.15
    show dad_cas at center with moveinleft:
        ypos 1.2
    dad "Loh [mcFirst] sudah bangun langsung makan nih haha"
    mc "Sini Yah sudah jadi makanan ibu"
    dad "Ayah mau cuci muka dulu"
    mc "Aku sudah selesai bu makannya"
    hide dad_cas with moveoutright
    hide mom with dissolve
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    mc "Bu, ada obat pusing ga ?"
    show mom at center with dissolve:
        ypos 1.15
    mom "Loh, Kamu sakit ?"
    mc "Agak Pusing saja Heheheh.."
    mc "Mungkin gara-gara masuk angin"
    mom "Kalau gitu mending ijin sekolah saja. Biar istirahat dirumah"
    mc "Ga Masalah bu, aku bawa Obat aja ke sekolah"
    mc "Sekarang Minum Obat dulu biar lebih enakan"
    mom "Yaudah kalau kamu memang mau sekolah"
    mom "Nanti kalau sudah parah langsung ke UKS saja"
    mc "Ahh.. Okk"
    mc "Kalau gitu aku berangkat dulu bu"
    show mom at center with moveinleft:
        xpos 0.65
        ypos 1.15
        xzoom -1
    show dad_cas at center with moveinright:
        ypos 1.2
    dad "Loh sudah mau berangkat aja"
    mc "Iya yah"
    show mom at center with moveinright:
        xpos 0.35
        ypos 1.15
    ai "Kalau gitu hati-hati dijalan nak"
    mc "Iyaa"
    hide mom with dissolve
    hide dad_cas with dissolve

    stop music fadeout 1.0
    play music jalan_jalan fadein 1.0

    scene jalan with dissolve
    "Siall,, aku masih pusing. seharusnya aku tidak usah sekolah dulu"
    "Tapi sudah sampai separuh jalan masa aku pulang"
    "Jika sudah agak parah mungkin aku akan langsung ke UKS"

    scene gerbang_sekolah with dissolve
    "~Puk~" with vpunch
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Kok kamu keliatan lesu bro ? agak pucat juga"
    mc "Kayaknya aku masuk angin agak pusing"
    na "Kalau gitu kan ga usah sekolah lur"
    na "Lagian, lebih enak diam dirumah"
    mc "Iya juga ya ahhaha"
    na "Nanti taruh tas aja lur di kelas setelah itu langsung ke UKS"
    mc "Oh Ok"
    hide nada_alma with moveoutleft

    scene kelas with dissolve
    mc "Capeknya hufft.."
    show ardana_alma at center with dissolve:
        ypos 1.2
    mg2 "Lahh,, kamu kok pucat sekali ?"
    mc "Agak ga enak badan aku"
    hide ardana_alma
    show ardana_alma_emosi at center:
        ypos 1.2
    mg2 "Lah kok masuk sekolah mending gitu ga usah sekolah"
    mc "Nah itu tadi sudah separuh jalan sampai sekolah berhubung naggung jadi ya yaudah sekolah aja"
    hide ardana_alma_emosi
    show ardana_alma_cuek at center:
        ypos 1.2
    mg2 "Astaga,, hmm.."
    hide ardana_alma_cuek with dissolve
    mc "Kalau gitu aku ke UKS aja sekalian titip tasku ya sama ijinkan ke Bu Senda"
    show ardana_alma at center with dissolve:
        ypos 1.2
    mg2 "Okay.. Tenang aja nanti ku ijinin ke Bu Senda"
    mc "Makasih, kalau gitu aku ke UKS dulu"
    hide ardana_alma with dissolve
    wkk "Mau kemana bro ? eh,, mukamu pucat banget bro"
    mc "ke UKS, dah ga kuat aku. Titip ijinin ke Bu Senda ya"
    wkk "Okk dah"

    scene lorong with dissolve
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    "Harus ke UKS ini sudah ga kuat. Astaga, ternyata sudah masuk"
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Loh, [mcFirst] eh mau kemana ? bentar lagi kelas"
    mc "Saya ijin ke UKS dulu bu"
    sr "Ehhh.. Mukamu pucat, Sana ke UKS istirahat dulu"
    mc "Iya bu"
    hide bu_senda with dissolve

    scene kelas with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat pagi anak-anak. Masih semangat semua kan ?"
    sk "Baik semua bu, masih dong"
    wkk "Oiya bu, [mcFirst] ijin ke UKS soalnya sakit"
    sr "Iyaa, tadi bu Senda ketemu sama [mcFirst] sudah ijin juga"
    sr "Kalau gitu mari kita mulai kelasnya"
    $ _skipping = False
    "~Materi Virus Lanjutan~"
    sr "Jenis Virus itu dibagi 2: \nPertama, Virus Golongan RNA \nKedua, Virus Golongan DNA" with dissolve
    sr "Virus RNA:" with dissolve
    sr "Virus RNA adalah virus yang materi genetiknya berupa asam nukleat yang berbentuk rantai tunggal atau ganda tidak berpilin." with dissolve
    sr "Di dalam sel inangnya, RNA pada virus akan mengalami transkripsi balik menjadi Hibrid RNA-DNA dan akhirnya membentuk DNA" with dissolve
    sr "Selanjutnya DNA virus akan masuk ke inti sel inangnya, menyisip ke dalam DNA inangnya. DNA virus akan merusak DNA inangnya dan membentuk mRNA" with dissolve
    sr "mRNA akan mengalami translasi untuk menghasilkan protein selubung virus untuk menbentuk virus – virus baru" with dissolve
    sr "Contoh Virus RNA:" with dissolve
    sr "HIV AIDS, Influenza, Virus Hepatitis E, Poliovirus, Paramyxovirus Paramyxovirus, Virus enterik, Virus rubella, Virus demam kuning, dll" with dissolve
    sr "Virus DNA:" with dissolve
    sr "Virus DNA adalah virus yang materi genetiknya berupa asam nukleat yang berbentuk rantai ganda berpilin" with dissolve
    sr "Di dalam sel inangnya, DNA pada virus akan mengalami replikasi menjadi beberapa DNA dan juga akan mengalami transkripsi menjadi mRNA" with dissolve
    sr "mRNA akan mengalami translasi untuk menghasilkan protein selubung virus" with dissolve
    sr "Masih di dalam sel inang, DNA dan protein virus mengkonstruksikan diri menjadi virus – virus baru" with dissolve
    sr "mRNA juga akan membentuk enzim penghancur (Lisozim) sehingga sel inang lisis (hancur) dan virus – virus keluar untuk menginfeksi sel inang lainnya" with dissolve
    sr "Contoh Virus DNA:" with dissolve
    sr "Papiloma, Poliloma, Parvovirus B19, Adenovirus, Herpes simpleks I (luka di sekeliling mulut), Herpes simpleks II (perlukaan genital), dll" with dissolve
    hide bu_senda with dissolve
    $ _skipping = True

    stop music fadeout 1.0
    play music kesepian fadein 1.0

    scene uks with dissolve
    $ iguk = "Ibu Guru UKS"
    mc "Permisi, saya ingin beristirahat dan minta obat"
    iguk "Kamu sakit apa ?"
    mc "Saya sedikit pusing bu dan agak demam"
    iguk "Mukamu Pucat, yaudah tidur sini"
    iguk "Bentar ibu ambilkan obat"
    iguk "Mau Teh Hangat juga ?"
    mc "Ga usah repot - repot bu"
    mc "Saya cuma ingin istirahat dan minta obat"
    iguk "gapapa, bentar ibu siapkan obat sama minumnya"
    mc "Iyaa bu" 
    iguk "Ini Obatnya setelah itu langsung tidur ya"
    mc 'Baik bu'
    iguk "Kalau sudah mendingan kabarin ya"
    "Mungkin aku bisa tidur sementara disini"
    "~4 Jam Kemudian Bel Berbunyi~"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    "Sudah enakan kalau gini aku bisa kembali ke kelas"
    mc "Bu saya rasa sudah mendingan ga pusing bu"
    iguk "Yaudah kalau gitu, obatnya bawa juga ya sekalian jaga-jaga"
    iguk "Terus Tehnya dihabisin sudah Ibu sediain juga"
    mc "Terima Kasih Bu Guru"

    stop music fadeout 1.0
    play music jalan_jalan2 fadein 1.0

    scene lorong_siang with dissolve
    nd "Loh,, [mcFirst] gimana sudah enakan ?"
    mc "Sudah mendingan sih. yaudah aku ke bangkuku dulu ya"

    scene kelas with dissolve
    "Nada sama [mg2_Last] pasti lagi ke kantin"
    "Kalau gitu aku tidur dulu aja lah sembari menunggu bell"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Bangun Bre, sudah masukk"
    mc "...."
    na "Sudah enakan ?"
    mc "Sudah sih"
    show ardana_alma at center with dissolve:
        xpos 0.4
        ypos 1.2
    show nada_alma at center with dissolve:
        xpos 0.6
        ypos 1.2
    mg2 "Kalau masih sakit mending langsung pulang aja deh"
    mc "Aman,, Masih kuat"
    hide nada_alma with moveoutleft
    hide ardana_alma with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Siang anak-anak. Loh [mcFirst] sudah enakan ?"
    mc "Sudah Bu Senda"
    sr "Tapi jangan dipaksaain ya misal mulai sakit langsung pulang aja"
    mc "Iya buu"
    sr "Kalau gitu ibu mulai,, dibagi kelompoknya ada 8 kelompok 1 kelompok 4 orang sisanya menyesuaikan ya"
    sr "Bikin pakai nomor acak yaa"
    hide bu_senda with dissolve
    "Semoga aku sekelompok dengan orang yang ga merepotkan"
    "~Pemilihan Kelompok~"
    $ st = "Shinta"
    $ bl = "Bella"
    st "Siapa kelompok 4 ?"
    mc "Aku"
    bl "Aku Kelompok 4"
    ad "Aku juga"
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Kalau sudah silahkan duduk bersama dengan kelompoknya. Tugasnya ibu kasih ini dikumpulkan besok sekalian presentasi materi yang dipelajari ya"
    sr "Sekarang silahkan berdiskusi mau dikerjakan disini gapapa"
    sr "Bu Senda tinggal dulu ya"
    hide bu_senda with moveoutright
    sk "Baik buu"
    st "Mau Kerkel dimana nih ?"
    ad "Di cafe boleh sih"
    bl "Aku dengar ada cafe baru didekat mall"
    bl "Nama Cafenya D'Teras"
    st "Boleh tuh kesana aja kalau gitu"
    mc "Aku ngikut aja"
    ad "Okk dah kalau gitu nanti malam kerkel di cafe D'Teras"
    ad "Jam 7 Malam ya jangan telat"
    mc "Okk"
    st "Kalau gitu santai - santai aja dulu hahah"
    mc "Aku kembali ke bangkuku dulu"
    bl "Iyaa"
    "Yaudahlah tidur aja kalau gitu"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show ardana_alma at center with dissolve:
        ypos 1.2
    mg2 "Bangun.. Sudah Bell Pulang ini"
    mc "Ahh.. sudah pulang ya ?"
    mg2 "Iyaa Ayo Pulangg"
    hide ardana_alma
    show ardana_alma_emosi at center:
        ypos 1.2
    mg2 "Akhh aku mau mampir kerumahmu tapi aku ada kerkel nanti"
    mc "Hahhaa Next time mungkin"
    hide ardana_alma_emosi
    show ardana_alma at center:
        ypos 1.2
    mg2 "Yaudah kuy pulang, tungguin di gerbang sekolah ya"
    mc "Okie"
    hide ardana_alma with moveoutright

    scene gerbang_sekolah_sore with dissolve
    show ardana_alma at center with dissolve:
        ypos 1.2
    mg2 "Skuy berangkat"
    mc "Okk"
    hide ardana_alma with moveoutleft

    scene jalan_sore with dissolve
    show ardana_alma at center with dissolve:
        ypos 1.2
    mg2 "Kamu kerja kelompok kapan ?"
    mc "Aku Nanti malam sih, mau ikut ?"
    mg2 "Ngaaak,, cuma tanya aja"
    mc "Okk"
    hide ardana_alma with dissolve

    stop music fadeout 1.0
    play music sore fadein 1.0

    scene depan_rumah_sore with dissolve
    show ardana_alma at center with dissolve:
        ypos 1.2
    mg2 "Sudah ah aku langsung pulang aja"
    mc "Iyaa makasih yaa hati-hati di jalan"
    mg2 "Titip salam ke tante ya"
    mc "Okk dah"
    hide ardana_alma with moveoutleft

    scene ruang_tamu_sore with dissolve
    mc "Aku Pulang"
    
    scene ruang_keluarga_sore with dissolve
    show mom at center with dissolve:
        ypos 1.2
    mom "Gimana tadi ?"
    mc "Tadi sempat ke UKS sih bu"
    mc "Sekarang sudah mendingan"
    mom "Syukurlah, kapan - kapan kalau sakit mending ijin aja jangan dipaksakan"
    mc "Iya,, bu "
    mc "Kalau gitu aku langsung tidur aja bu soalnya nanti malam mau kerkel"
    mc "Biar ga tambah parah sakitnya"
    mom "Yaudah Kalau gitu"
    hide mom with dissolve

    scene kamar_sore with dissolve
    "Capeknyaa, masih pusing dikit tapi mungkin dibuat tidur jadi sembuh total"

    scene kamar_malam with dissolve
    "Hoaam.. sudah malam ternyata lebih baik bersiap dulu buat kerkel"
    
    scene ruang_keluarga_malam with dissolve
    mc "Bu, aku langsung berangkat"
    show mom at center with dissolve:
        ypos 1.15
    mom "loh,, loh Ga makan dulu ?"
    mom "Nanti sakit lagi"
    mc "Sudah sembuh bu. Nanti langsung makan di cafe aja bu pas kerkel"
    mom "Yaudah kalau gitu, ini ibu kasih uang sangu"
    mom "Buat makan di cafe"
    mc "Iya bu makasih"
    mc "Aku berangkat dulu"
    mom "Iya nak Hati-hati"
    mc "Bu aku pinjam motornya"
    mom "Iya nak hati-hati"
    hide mom with dissolve

    scene parkir_malam
    scene cafe_malam with dissolve
    bl "[mcFirst]!!! [mcFirst]!!! [mcFirst]!!! \nSini.. Sinii"
    mc "Ahh itu dia.. \nGimana anak-anak ?"
    bl "Bentar aku Telpon dulu"
    "~Telpon~"
    stop music fadeout 1.0
    play music bertengkar fadein 1.0
    st "Bel maaf ya aku sama ardi gabisa ikut kerja kelompok karna kita udah ada janji pergi sama temen ke mall"
    st "Kalian kerjain aja berdua ya nanti masalah urunan kabarin aja"
    st "Aku yang bayar"
    bl "Tapi Shin, nanti kalian engga ngerti materinya"
    st "Nanti kan yang presentasi bisa kamu sama si [mcFirst] itu, gausah ribet kan ini Cuma pelajaran biologi"
    bl "Tapi kan Sin, loh malah dimatikan telponnya nih"
    "~Tutup Telpon~"
    bl "Astagaaa"
    mc "Bentar aku nelpon [ad]"
    bl "Gimana ?"
    mc "Ga diangkat"
    bl "Astagaa, ada apa dengan mereka ini sih"
    bl "Gimana, nih kita harus ngerjain berdua kayanya ?"
    mc "Yaudah mau gimana lagi bel, daripada kita dapet nilai jelek juga karena ga ngerjain"
    stop music fadeout 1.0
    play music sore fadein 1.0
    bl "Iya dah kalau gitu. Btw Pesan dulu saja"
    mc "Bawa menunya aja sama kertasnya tulis"
    bl "Okie, kamu nyari tempat duduknya ya"
    mc "Ok"
    "Disini muungkin enak tempat duduknya"
    bl "ini menunya, umm aku bingung mau pesan apa ?"
    mc "Kalau gitu aku dulu yang liat menunya"
    mc "Mungkin aku pesan Jus Strawberry sama Nasi Goreng Jawa"
    bl "umm.. mungkin aku ini saja."
    bl "Yang ngasih ke kasirnya aku apa kamu ?"
    mc "Kamu aja"
    bl "Iyaa dah"
    mc "Aku mau ngeluarin tugasnya dulu"
    "~Sementara [bl] Pesan makanan dan minuman~"
    bl "Sudah aku pesanin"
    bl "Kuy Kerjain sembari nunggu pesenan datang"

    "~Soal Hari ke-4~" with dissolve
    #Initialize score
    $ quiz4_score = 0

    label quiz4:
        $ quick_menu = False

        "1. Flu burung merupakan jenis penyakit menular yang akibatkan oleh virus yang menjangkit unggas. Penyebab penyakit tersebut masuk dalam golongan virus influenza tipe ….."
        menu:
            "A. B":
                $ quiz4_score += 0
            "B. C":
                $ quiz4_score += 0
            "C. A":
                $ quiz4_score += 8
            "D. Jawaban A dan B benar":
                $ quiz4_score += 0

        "2. H5NI (Avian Influenza A) merupakan penyebab penyakit ……"
        menu:
            "A. tumor pada hewan":
                $ quiz4_score += 0
            "B. flu burung":
                $ quiz4_score += 8
            "C. rabies":
                $ quiz4_score += 0
            "D. polio":
                $ quiz4_score += 0 

        "3. Penyakit AIDS dapat ditularkan melalui ...."
        menu:
            "A. Garuk garuk kepala":
                $ quiz4_score += 0
            "B. Menatap Muka":
                $ quiz4_score += 0
            "C. Gigitan nyamuk":
                $ quiz4_score += 0
            "D. Hubungan seksual":
                $ quiz4_score += 8
        
        "4. HIV yang ada pada penderita AIDS mengakibatkan penderita mengalami ……"
        menu:
            "A. Rapuhnya sistem kekebalan":
                $ quiz4_score += 8
            "B. Penurunan kadar trombosit":
                $ quiz4_score += 0
            "C. Kerusakan hati":
                $ quiz4_score += 0
            "D. Peningkatan kadar trombosit":
                $ quiz4_score += 0
        
        show virusd4_1 at truecenter with dissolve
        "5. Perhatikan gambar di diatas!  Nomor 1,2, dan 3 merupakan ..."
        menu:
            "A. DNA, kapsid, ekor":
                $ quiz4_score += 8
            "B. kapsid, DNA, ekor":
                $ quiz4_score += 0
            "C. DNA, ekor, kapsid":
                $ quiz4_score += 0
            "D. kapsid, RNA, ekor":
                $ quiz4_score += 0
        hide virusd4_1 with dissolve

        "6. Selubung protein penyusun virus dinamakan…."
        menu:
            "A. dinding sel":
                $ quiz4_score += 0
            "B. Virion":
                $ quiz4_score += 0
            "C. Kapsid":
                $ quiz4_score += 8
            "D. membran":
                $ quiz4_score += 0

        show virusd4_2 at center with dissolve:
            ypos 0.725
        "7. Perhatikan gambar di atas ini. Berdasarkan daur hidup, secara berurutan virus x, y, dan z secara berurutan adalah…."
        menu:
            "A. absorbsi, sintesis, lisis":
                $ quiz4_score += 0
            "B. absorbsi, penetrasi, sintesis":
                $ quiz4_score += 0
            "C. penetrasi, perakitan, lisis":
                $ quiz4_score += 8
            "D. penetrsi, absorbsi, sintesis":
                $ quiz4_score += 0
        hide virusd4_2 with dissolve

        "8. Berdasarkan sistem klasifikasi, organisme yang menyebabkan AIDS dimasukkan ke kelompok ….."
        menu:
            "A. protista":
                $ quiz4_score += 0
            "B. Monera":
                $ quiz4_score += 0
            "C. animalia":
                $ quiz4_score += 0
            "D. virus":
                $ quiz4_score += 8

        "9. Di bawah ini yang merupakn pernyataan yang benar tentang virus yaitu ….."
        menu:
            "A. Partikel virus memiliki DNA dan RNA":
                $ quiz4_score += 8
            "B. Perakitan kapsid virus dari protein memerlukan sel inang":
                $ quiz4_score += 0
            "C. Pertumbuhan partikel virus setelah perakitan kapsid, berlanjut sampai pada pelepasan partikel-partikel virus baru":
                $ quiz4_score += 0
            "D. Partikel virus bisa dilihat dengan menggunakan mikroskop cahaya":
                $ quiz4_score += 0

        "Berdasarkan pernyataan di atas bentuk dari virus terdapat pada nomor" (multiple=2)
        "10. Perhatikanlah macam-macam virus di bawah ini !
                \n
                1) Simplexvirus
                \n
                2) Bakteriofag
                \n
                3) Lyssavirus
                \n
                4) Enterovirus
                \n
                5) Ortohepadnavirus" (multiple=2)
        menu:
            "A. Semuanya benar":
                $ quiz4_score += 0
            "B. 3,4, dan 5":
                $ quiz4_score += 8
            "C. 2,3, dan 5":
                $ quiz4_score += 0
            "D. 4 dan 5":
                $ quiz4_score += 0

        "11. Virus HIV sangat berbahaya karena menyerang ….."
        menu:
            "A. Otak":
                $ quiz4_score += 0
            "B. Otot":
                $ quiz4_score += 0
            "C. Hati":
                $ quiz4_score += 0
            "D. Sel darah":
                $ quiz4_score += 8

        "12. Virus flu burung banyak sekali tipenya, tetapa yang paling berbahaya adalah tipe …."
        menu:
            "A. H4N5":
                $ quiz4_score += 0
            "B. H1N1":
                $ quiz4_score += 0
            "C. H1N5":
                $ quiz4_score += 0
            "D. H5N1":
                $ quiz4_score += 8

        "13. Berikut ini yang bukan merupakan sifat-sifat dari virus adalah ….."
        menu:
            "A. Untuk reproduksinya hanya membutuhkan bahan anorganik saja":
                $ quiz4_score += 8
            "B. Virus bukan sel, jadi tidak memiliki protoplasma":
                $ quiz4_score += 0
            "C. Bentuk dan ukuran virus bervariasi":
                $ quiz4_score += 0
            "D. Virus mempunyai selubung dari protein dan materi genetik DNA/RNA":
                $ quiz4_score += 0

        "14. Virus yang menyebabkan pecahnya sel inang disebut ….."
        menu:
            "A. Bakteriofag":
                $ quiz4_score += 0
            "B. Profag":
                $ quiz4_score += 8
            "C. Virus heliks":
                $ quiz4_score += 0
            "D. Virus virulen":
                $ quiz4_score += 0

        "15. Enzim yang di hasilkan oleh virus yang dapat memecahkan dinding sel bakteri disebut ….."
        menu:
            "A. Neuraminidase":
                $ quiz4_score += 0
            "B. Lisozim":
                $ quiz4_score += 8
            "C. Lisogenik":
                $ quiz4_score += 0
            "D. Litik":
                $ quiz4_score += 0

        "Jawaban : 
            \n
            1. C \ \ \ \ 3. D \ \ \ \ 5. A \ \ \ \ 7. C \ \ \ \ 9. A \ \ \ \ 11. D \ \ \ \ 13. A \ \ \ \ 15. B
            \n
            2. B \ \ \ \ 4. A \ \ \ \ 6. C \ \ \ \ 8. D \ \ \ \ 10. B \ \ \ \ 12. D \ \ \ \ 14. B"

        $ quiz4_score_total = quiz4_score - 20

        "Nilaiku adalah [quiz4_score_total]"

    # Check the quiz 1 score
    if quiz4_score_total >= 75:
        # Win
        $ quick_menu = True
        mc "Yang rangkum buat presentasi siapa ?"
        bl "Kita selesaikan juga hari ini semuanya"
        mc "Okie"
        # Did he win? Yes.
        #$ quiz4_win = True
        #$ quiz4_lose = False   
    else:
        # Lose
        bl "Biar dah ga usah di kerjakan, capek aku"
        bl "Mereka berdua ga ada lagi"
        menu:
            "Semangat":
                bl "Coba dulu lagi"
                $ quiz4_score = 0
                jump quiz4
            "Pulang saja!":
                "Anda gagal sebagai murid"
                "~END~"
                return

    $ psc = "Pelayan Cafe"
    psc "Ini Pesanannya, selamat dinikmati kalau gitu permisi dulu"
    mc "Iya mas, terima kasih"
    bl "Terima Kasih mas"
    "~Beberapa jam mengerjakan tugas dan menikmati camilan~"
    bl "Fuuuhh.. Capeknyaa, mereka berdua ga datang juga salah"
    bl "Coba kalau datang pasti cepat selesai"
    mc "Hahaha iyaaa benar"
    bl "Bisa-bisanya meraka ga datang \nHadeh..."
    mc "Mungkin ada urusan penting {p}Oiya.. Kalau gitu aku pulang dulu ya"
    bl "ehh,, tungguin aku juga mau pulang"
    mc "okk dah"
    
    scene parkiran_mall_malam with dissolve
    mc "[bl] duluan"
    bl "Iyaa hati hati"

    scene depan_rumah_malam with dissolve
    mc "Aku Pulang"

    scene ruang_keluarga_malam with dissolve
    show dad_cas at center with dissolve:
        ypos 1.2
    dad "Oii Nak"
    mc "Loh Ayah sudah pulang ga lembur lagi ?"
    dad "Sudah dong, ga ada job lagi tapi ada sih cuma pengen agak santai juga hari ini"
    mc "Ealah,, okk yah"
    mc "Ibu dimana ?"
    dad "Ibu tidur"
    mc "Yaudah kalau gitu aku langsung tidur aja"
    dad "Iyaa nak, kalau ga salah [cat] Feliz ada di kamarmu"
    mc "okie yah"
    hide dad_cas with dissolve

    scene kamar_malam with dissolve
    "Fuuh Capeknyaa, aku mau tidur dulu lah"
    "[cat] Nungguin aku sampai tertidur juga hahahah"
    "Oke saatnya tidur"

    stop music fadeout 1.0

    jump day5_Kirana

    return

label day4_Miselia:

    play music pagi fadein 1.0
    window hide dissolve
    scene sky2 with dissolve
    show day4 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day4 with dissolve
    window hide dissolve

    scene kamar with dissolve
    "Ugghh.. pusing sekali dan lapar juga mungkin ini gara-gara aku langsung tidur"
    stop sound fadeout 1.0
    play sound burung_terbang fadein 1.0
    window hide dissolve
    pause 3.0
    window show dissolve
    "Kipasnya menghadap persis di aku lagi, malam ga makan sama sekali bisa jadi ini masuk angin"
    "Pasti [cat] sudah keluar kamar duluan dan makan"
    "Lebih Baik aku cuci muka dulu"

    scene kamar_mandi with dissolve
    play sound mandi fadein 1.0
    "Ughhh.. aku mandi pakai air panas aja kalau gitu"
    stop sound fadeout 1.0

    scene kamar with dissolve
    "Masih tetap pusing.. Ughhh..."
    "Aku pakai seragam aja dulu nanti tinggal makan saja"

    scene dapur with dissolve
    mc "[cat] Ternyata dah disini aja kamu hahahha"
    mc "Dasarr haha"
    show cat at center with moveinbottom:
        ypos 0.75
    cat "Nyaaa Nya Nyaa"
    hide cat
    mc "Bu,, aku kenapa ya kok lapar banget ?"
    show mom at center with dissolve:
        ypos 1.15
    mom "kamu kan tadi malam ga makan sama sekali"
    mom "langsung tidur kan jadi wajar paginya lapar"
    mom "Ini Makanannya sudah siap juga, bekalnya ada di meja makan juga nanti bawa"
    mc "Iyaa bu. Kalau gitu aku makan dulu bu"
    show mom at center with moveinright:
        xpos 0.3
        ypos 1.15
    show dad_cas at center with moveinleft:
        ypos 1.2
    dad "Loh [mcFirst] sudah bangun langsung makan nih haha"
    mc "Sini Yah sudah jadi makanan ibu"
    dad "Ayah mau cuci muka dulu"
    mc "Aku sudah selesai bu makannya"
    hide dad_cas with moveoutright
    hide mom with dissolve
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    mc "Bu, ada obat pusing ga ?"
    show mom at center with dissolve:
        ypos 1.15
    mom "Loh, Kamu sakit ?"
    mc "Agak Pusing saja Heheheh.."
    mc "Mungkin gara-gara masuk angin"
    mom "Kalau gitu mending ijin sekolah saja. Biar istirahat dirumah"
    mc "Ga Masalah bu, aku bawa Obat aja ke sekolah"
    mc "Sekarang Minum Obat dulu biar lebih enakan"
    mom "Yaudah kalau kamu memang mau sekolah"
    mom "Nanti kalau sudah parah langsung ke UKS saja"
    mc "Ahh.. Okk"
    mc "Kalau gitu aku berangkat dulu bu"
    show mom at center with moveinleft:
        xpos 0.65
        ypos 1.15
        xzoom -1
    show dad_cas at center with moveinright:
        ypos 1.2
    dad "Loh sudah mau berangkat aja"
    mc "Iya yah"
    show mom at center with moveinright:
        xpos 0.35
        ypos 1.15
    ai "Kalau gitu hati-hati dijalan nak"
    mc "Iyaa"
    hide mom with dissolve
    hide dad_cas with dissolve

    stop music fadeout 1.0
    play music jalan_jalan fadein 1.0

    scene jalan with dissolve
    "Siall,, aku masih pusing. seharusnya aku tidak usah sekolah dulu"
    "Tapi sudah sampai separuh jalan masa aku pulang"
    "Jika sudah agak parah mungkin aku akan langsung ke UKS"

    scene gerbang_sekolah with dissolve
    "~Puk~" with vpunch
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Kok kamu keliatan lesu bro ? agak pucat juga"
    mc "Kayaknya aku masuk angin agak pusing"
    na "Kalau gitu kan ga usah sekolah lur"
    na "Lagian, lebih enak diam dirumah"
    mc "Iya juga ya ahhaha"
    na "Nanti taruh tas aja lur di kelas setelah itu langsung ke UKS"
    mc "Oh Ok"
    hide nada_alma with moveoutleft

    scene kelas with dissolve
    mc "Capeknya hufft.."
    show miselia_alma at center with dissolve:
        ypos 1.2
    mg1 "Lahh,, kamu kok pucat sekali ?"
    mc "Agak ga enak badan aku"
    hide miselia_alma
    show miselia_alma_emosi at center:
        ypos 1.2
    mg1 "Lah kok masuk sekolah mending gitu ga usah sekolah"
    mc "Nah itu tadi sudah separuh jalan sampai sekolah berhubung naggung jadi ya yaudah sekolah aja"
    hide miselia_alma_emosi
    show miselia_alma_cuek at center:
        ypos 1.2
    mg1 "Astaga,, hmm.."
    hide miselia_alma_cuek with dissolve
    mc "Kalau gitu aku ke UKS aja sekalian titip tasku ya sama ijinkan ke Bu Senda"
    show miselia_alma at center with dissolve:
        ypos 1.2
    mg1 "Okay.. Tenang aja nanti ku ijinin ke Bu Senda"
    mc "Makasih, kalau gitu aku ke UKS dulu"
    hide miselia_alma with dissolve
    wkk "Mau kemana bro ? eh,, mukamu pucat banget bro"
    mc "ke UKS, dah ga kuat aku. Titip ijinin ke Bu Senda ya"
    wkk "Okk dah"

    scene lorong with dissolve
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    "Harus ke UKS ini sudah ga kuat. Astaga, ternyata sudah masuk"
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Loh, [mcFirst] eh mau kemana ? bentar lagi kelas"
    mc "Saya ijin ke UKS dulu bu"
    sr "Ehhh.. Mukamu pucat, Sana ke UKS istirahat dulu"
    mc "Iya bu"
    hide bu_senda with dissolve

    scene kelas with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat pagi anak-anak. Masih semangat semua kan ?"
    sk "Baik semua bu, masih dong"
    wkk "Oiya bu, [mcFirst] ijin ke UKS soalnya sakit"
    sr "Iyaa, tadi bu Senda ketemu sama [mcFirst] sudah ijin juga"
    sr "Kalau gitu mari kita mulai kelasnya"
    $ _skipping = False
    "~Materi Fungi Lanjutan~"
    sr "REPRODUKSI JAMUR" with dissolve
    sr "Reproduksi pada jamur terdiri atas dua yaitu reproduksi secara generative (seksual) dan vegetative (aseksual)." with dissolve
    sr "REPRODUKSI GENERATIF (SEKSUAL)" with dissolve
    sr "Biasanya jamur bereproduksi secara generative karena kondisi lingkungan yang berubah atau pada kondisi darurat lainnya." with dissolve
    sr "Keturunan yang dihasilkan sendiri memiliki genetik yang beragam dan lebih adaptif terhadap perubahan lingkungan" with dissolve
    sr "Reproduksi secara generative didahului dengan pembentukan spora seksual yang memiliki jenis hifa berbeda" with dissolve
    sr "Hifa (+) dan hifa (-) yang berkromosom haploid mendekat dan membentuk gametangium (organ yang menghasilkan gamet)" with dissolve
    sr "Gametangium berplasmogami yaitu peleburan sitoplasma dan kemudian membentuk zigosporangium dikariotik (heterokarotik) dengan pasangan nucleus haploid yang belum bersatu" with dissolve
    sr "Zigosporangium ini memiliki dinding sel yang tebal dan kasar yang memungkinkan untuk bertahan pada kondisi lingkungan yang buruk dan kering" with dissolve
    sr "Bila kondisi lingkungannya membaik, zigosporangium akan menjadi kariogami (peleburan inti) sehingga zigosporangium memiliki inti yang berkromosom diploid (2n)" with dissolve
    sr "Zigosporangium yang berinti haploid (2n) akan mengalami pembelahan secara mitosis yang menghasilkan zigospora haploid didalam zigosporangium." with dissolve
    sr "Zigospora haploid akan berkecambah membentuk sporangium bertangkai pendek dengan kromosom haploid" with dissolve
    sr "Sporangium haploid akan menghasilkan spora-spora yang haploid yang memiliki keanekaragaman genetik" with dissolve
    sr "Bila spora-spora haploid jatuh di tempat yang sesuai, spora akan berkecambah (germinasi) menjadi hifa jamur yang haploid." with dissolve
    sr "Hifa akan tumbuh membentuk jaringan miselium yang semuanya haploid." with dissolve
    sr "REPRODUKSI VEGETATIF (ASEKSUAL)" with dissolve
    sr "Pada jamur yang uniseluler reproduksi vegetative dilakukan dengan pembentukan tunas yang akan tumbuh menjadi individu baru" with dissolve
    sr "Pada jamur yang multiseluler dilakukan dengan cara fragmentasi hifa dan pembentukan spora vegetative" with dissolve
    sr "Fragmentasi hifa (pemutusan hifa), potongan hifa yang putus tumbuh menjadi individu baru." with dissolve
    sr "Pembentukan spora vegetative yang berupa sporangiospora dan konidiospora" with dissolve
    sr "Jamur yang telah dewasa menghasilkan spongiofor (tangkai kotak spora). Pada ujung sporangiofor terdapat sporangium (kotak spora)" with dissolve
    sr "Di dalam kotak spora pembelahan sel dilakukan secara  mitosis dan menghasilkan banyak sporangiospora dengan kromosom yang haploid (n)" with dissolve
    sr "Adapun jamur jenis lain menghasilkan konidiofor (tangkai konidia). Pada ujung konidiofor terdapat konidium (kotak konidiospora)" with dissolve
    sr "Di dalam konidium terjadi pembelahan sel secara mitosis yang menghasilkan banyak konidiospora dengan kromosom yang haploid (n)" with dissolve
    sr "Baik sporangiospora maupun konidiospora, bila jatuh di tempat yang sesuai akan tumbuh menjadi hifa baru yang haploid (n)." with dissolve
    hide bu_senda with dissolve
    $ _skipping = True

    stop music fadeout 1.0
    play music kesepian fadein 1.0

    scene uks with dissolve
    $ iguk = "Ibu Guru UKS"
    mc "Permisi, saya ingin beristirahat dan minta obat"
    iguk "Kamu sakit apa ?"
    mc "Saya sedikit pusing bu dan agak demam"
    iguk "Mukamu Pucat, yaudah tidur sini"
    iguk "Bentar ibu ambilkan obat"
    iguk "Mau Teh Hangat juga ?"
    mc "Ga usah repot - repot bu"
    mc "Saya cuma ingin istirahat dan minta obat"
    iguk "gapapa, bentar ibu siapkan obat sama minumnya"
    mc "Iyaa bu" 
    iguk "Ini Obatnya setelah itu langsung tidur ya"
    mc 'Baik bu'
    iguk "Kalau sudah mendingan kabarin ya"
    "Mungkin aku bisa tidur sementara disini"
    "~4 Jam Kemudian Bel Berbunyi~"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    "Sudah enakan kalau gini aku bisa kembali ke kelas"
    mc "Bu saya rasa sudah mendingan ga pusing bu"
    iguk "Yaudah kalau gitu, obatnya bawa juga ya sekalian jaga-jaga"
    iguk "Terus Tehnya dihabisin sudah Ibu sediain juga"
    mc "Terima Kasih Bu Guru"

    stop music fadeout 1.0
    play music jalan_jalan2 fadein 1.0

    scene lorong_siang with dissolve
    nd "Loh,, [mcFirst] gimana sudah enakan ?"
    mc "Sudah mendingan sih. yaudah aku ke bangkuku dulu ya"

    scene kelas with dissolve
    "Nada sama [mg2_Last] pasti lagi ke kantin"
    "Kalau gitu aku tidur dulu aja lah sembari menunggu bell"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Bangun Bre, sudah masukk"
    mc "...."
    na "Sudah enakan ?"
    mc "Sudah sih"
    show miselia_alma at center with dissolve:
        xpos 0.4
        ypos 1.2
    show nada_alma at center with dissolve:
        xpos 0.6
        ypos 1.2
    mg1 "Kalau masih sakit mending langsung pulang aja deh"
    mc "Aman,, Masih kuat"
    hide nada_alma with moveoutleft
    hide miselia_alma with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Siang anak-anak. Loh [mcFirst] sudah enakan ?"
    mc "Sudah Bu Senda"
    sr "Tapi jangan dipaksaain ya misal mulai sakit langsung pulang aja"
    mc "Iya buu"
    sr "Kalau gitu ibu mulai,, dibagi kelompoknya ada 8 kelompok 1 kelompok 4 orang sisanya menyesuaikan ya"
    sr "Bikin pakai nomor acak yaa"
    hide bu_senda with dissolve
    "Semoga aku sekelompok dengan orang yang ga merepotkan"
    "~Pemilihan Kelompok~"
    $ st = "Shinta"
    $ bl = "Bella"
    st "Siapa kelompok 4 ?"
    mc "Aku"
    bl "Aku Kelompok 4"
    ad "Aku juga"
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Kalau sudah silahkan duduk bersama dengan kelompoknya. Tugasnya ibu kasih ini dikumpulkan besok sekalian presentasi materi yang dipelajari ya"
    sr "Sekarang silahkan berdiskusi mau dikerjakan disini gapapa"
    sr "Bu Senda tinggal dulu ya"
    hide bu_senda with moveoutright
    sk "Baik buu"
    st "Mau Kerkel dimana nih ?"
    ad "Di cafe boleh sih"
    bl "Aku dengar ada cafe baru didekat mall"
    bl "Nama Cafenya D'Teras"
    st "Boleh tuh kesana aja kalau gitu"
    mc "Aku ngikut aja"
    ad "Okk dah kalau gitu nanti malam kerkel di cafe D'Teras"
    ad "Jam 7 Malam ya jangan telat"
    mc "Okk"
    st "Kalau gitu santai - santai aja dulu hahah"
    mc "Aku kembali ke bangkuku dulu"
    bl "Iyaa"
    "Yaudahlah tidur aja kalau gitu"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show miselia_alma at center with dissolve:
        ypos 1.2
    mg1 "Bangun.. Sudah Bell Pulang ini"
    mc "Ahh.. sudah pulang ya ?"
    mg1 "Iyaa Ayo Pulangg"
    hide miselia_alma
    show miselia_alma_emosi at center:
        ypos 1.2
    mg1 "Akhh aku mau mampir kerumahmu tapi aku ada kerkel nanti"
    mc "Hahhaa Next time mungkin"
    hide miselia_alma_emosi
    show miselia_alma at center:
        ypos 1.2
    mg1 "Yaudah kuy pulang, tungguin di gerbang sekolah ya"
    mc "Okie"
    hide miselia_alma with moveoutright

    scene gerbang_sekolah_sore with dissolve
    show miselia_alma at center with dissolve:
        ypos 1.2
    mg1 "Skuy berangkat"
    mc "Okk"
    hide miselia_alma with moveoutleft

    scene jalan_sore with dissolve
    show miselia_alma at center with dissolve:
        ypos 1.2
    mg1 "Kamu kerja kelompok kapan ?"
    mc "Aku Nanti malam sih, mau ikut ?"
    mg1 "Ngaaak,, cuma tanya aja"
    mc "Okk"
    hide miselia_alma with dissolve

    stop music fadeout 1.0
    play music sore fadein 1.0

    scene depan_rumah_sore with dissolve
    show miselia_alma at center with dissolve:
        ypos 1.2
    mg1 "Sudah ah aku langsung pulang aja"
    mc "Iyaa makasih yaa hati-hati di jalan"
    mg1 "Titip salam ke tante ya"
    mc "Okk dah"
    hide miselia_alma with moveoutleft

    scene ruang_tamu_sore with dissolve
    mc "Aku Pulang"
    
    scene ruang_keluarga_sore with dissolve
    show mom at center with dissolve:
        ypos 1.2
    mom "Gimana tadi ?"
    mc "Tadi sempat ke UKS sih bu"
    mc "Sekarang sudah mendingan"
    mom "Syukurlah, kapan - kapan kalau sakit mending ijin aja jangan dipaksakan"
    mc "Iya,, bu "
    mc "Kalau gitu aku langsung tidur aja bu soalnya nanti malam mau kerkel"
    mc "Biar ga tambah parah sakitnya"
    mom "Yaudah Kalau gitu"
    hide mom with dissolve

    scene kamar_sore with dissolve
    "Capeknyaa, masih pusing dikit tapi mungkin dibuat tidur jadi sembuh total"

    scene kamar_malam with dissolve
    "Hoaam.. sudah malam ternyata lebih baik bersiap dulu buat kerkel"
    
    scene ruang_keluarga_malam with dissolve
    mc "Bu, aku langsung berangkat"
    show mom at center with dissolve:
        ypos 1.15
    mom "loh,, loh Ga makan dulu ?"
    mom "Nanti sakit lagi"
    mc "Sudah sembuh bu. Nanti langsung makan di cafe aja bu pas kerkel"
    mom "Yaudah kalau gitu, ini ibu kasih uang sangu"
    mom "Buat makan di cafe"
    mc "Iya bu makasih"
    mc "Aku berangkat dulu"
    mom "Iya nak Hati-hati"
    mc "Bu aku pinjam motornya"
    mom "Iya nak hati-hati"
    hide mom with dissolve

    scene parkir_malam
    scene cafe_malam with dissolve
    bl "[mcFirst]!!! [mcFirst]!!! [mcFirst]!!! \nSini.. Sinii"
    mc "Ahh itu dia.. \nGimana anak-anak ?"
    bl "Bentar aku Telpon dulu"
    "~Telpon~"
    stop music fadeout 1.0
    play music bertengkar fadein 1.0
    st "Bel maaf ya aku sama ardi gabisa ikut kerja kelompok karna kita udah ada janji pergi sama temen ke mall"
    st "Kalian kerjain aja berdua ya nanti masalah urunan kabarin aja"
    st "Aku yang bayar"
    bl "Tapi Shin, nanti kalian engga ngerti materinya"
    st "Nanti kan yang presentasi bisa kamu sama si [mcFirst] itu, gausah ribet kan ini Cuma pelajaran biologi"
    bl "Tapi kan Sin, loh malah dimatikan telponnya nih"
    "~Tutup Telpon~"
    bl "Astagaaa"
    mc "Bentar aku nelpon [ad]"
    bl "Gimana ?"
    mc "Ga diangkat"
    bl "Astagaa, ada apa dengan mereka ini sih"
    bl "Gimana, nih kita harus ngerjain berdua kayanya ?"
    mc "Yaudah mau gimana lagi bel, daripada kita dapet nilai jelek juga karena ga ngerjain"
    stop music fadeout 1.0
    play music sore fadein 1.0
    bl "Iya dah kalau gitu. Btw Pesan dulu saja"
    mc "Bawa menunya aja sama kertasnya tulis"
    bl "Okie, kamu nyari tempat duduknya ya"
    mc "Ok"
    "Disini muungkin enak tempat duduknya"
    bl "ini menunya, umm aku bingung mau pesan apa ?"
    mc "Kalau gitu aku dulu yang liat menunya"
    mc "Mungkin aku pesan Jus Strawberry sama Nasi Goreng Jawa"
    bl "umm.. mungkin aku ini saja."
    bl "Yang ngasih ke kasirnya aku apa kamu ?"
    mc "Kamu aja"
    bl "Iyaa dah"
    mc "Aku mau ngeluarin tugasnya dulu"
    "~Sementara [bl] Pesan makanan dan minuman~"
    bl "Sudah aku pesanin"
    bl "Kuy Kerjain sembari nunggu pesenan datang"

    "~SOAL~"
    #Initialize score
    $ quiz_fungi4_score = 0

    label quiz_fungi4:
        $ quick_menu = False

        "1. Jamur mampu berkembang biak dengan cara tak kawin / vegetatif dengan membentuk … "
        menu:
            "A. Konidium":
                $ quiz_fungi4_score += 10
            "B. Sporangium":
                $ quiz_fungi4_score += 0
            "C. Sorus":
                $ quiz_fungi4_score += 0
            "D. Gemma":
                $ quiz_fungi4_score += 0

        "2. Pohon pinus akan mendapatkan … dengan adanya mikroza yang terdapat pada akarnya. Jawaban yang tepat untuk mengisi ruang rumpang pada kalimat di atas ialah …"
        menu:
            "A. air dan bahan organik":
                $ quiz_fungi4_score += 10
            "B. toksin untuk mengusir hama":
                $ quiz_fungi4_score += 0
            "C. enzim pencernaan makanan":
                $ quiz_fungi4_score += 0
            "D. toksin untuk mengusir hama":
                $ quiz_fungi4_score += 0

        "3. Spora yang dapat bergerak dengan menggunakan flagel disebut dengan … "
        menu:
            "A. oospora":
                $ quiz_fungi4_score += 0
            "B. sporofit":
                $ quiz_fungi4_score += 0
            "C. gemma":
                $ quiz_fungi4_score += 10
            "D. zoospore":
                $ quiz_fungi4_score += 0

        "4. Dibawah ini bukanlah contoh dari perkembangbiakan jamur secara aseksual, ialah … "
        menu:
            "A. Pertunasan":
                $ quiz_fungi4_score += 0
            "B. Fragmentasi":
                $ quiz_fungi4_score += 10
            "C. Pembentukan spora":
                $ quiz_fungi4_score += 0
            "D. Pembentukan konida":
                $ quiz_fungi4_score += 0
            
        "5. Ganggang tetap mampu hidup meskipun tidak bersimbiosis dengan lumut. Hal tersebut dapat terjadi karena ganggan mampu … "
        menu:
            "A. Dapat berkembang biak dengan membelah diri":
                $ quiz_fungi4_score += 0
            "B. Hidup secara fotoautotrof":
                $ quiz_fungi4_score += 0
            "C. Hidup secara heterotrof":
                $ quiz_fungi4_score += 0
            "D. Hidup secara saprofit":
                $ quiz_fungi4_score += 10

        "6. Berikut ini yang merupakan perbedaan antara zygomycota dan oomycota secara spesifik ialah … "
        menu:
            "A. struktur hifanya":
                $ quiz_fungi4_score += 0
            "B. pencernaan makananannya":
                $ quiz_fungi4_score += 0
            "C. reproduksi aseksualnya":
                $ quiz_fungi4_score += 0
            "D. reproduksi seksualnya":
                $ quiz_fungi4_score += 10

        "7. Aspergillus dapat hidup secara … "
        menu:
            "A. Mandiri":
                $ quiz_fungi4_score += 0
            "B. Parasit":
                $ quiz_fungi4_score += 0
            "C. Autotrof":
                $ quiz_fungi4_score += 0
            "D. Saprofit":
                $ quiz_fungi4_score += 10

        "8. Jamur makroskopik tergolong ke dalam jenis kelompok … "
        menu:
            "A. Ascomycota":
                $ quiz_fungi4_score += 0
            "B. Zygomycota":
                $ quiz_fungi4_score += 10
            "C. Basidiomycota":
                $ quiz_fungi4_score += 0
            "D. Deuteromycota":
                $ quiz_fungi4_score += 0

        "9. Dibawah ini yang tidak tergolong ke dalam kelompok jamur divisi basidiomycota ialah … "
        menu:
            "A. Jamur beracun":
                $ quiz_fungi4_score += 0
            "B. Jamur Pinicilin":
                $ quiz_fungi4_score += 0
            "C. Jamur Tempe":
                $ quiz_fungi4_score += 10
            "D. Jamur kuping":
                $ quiz_fungi4_score += 0

        "10. Jamur yang menyebabkan penyakit kaki pada atlet berasal dari divisi jamur … "
        menu:
            "A. Deteromycota":
                $ quiz_fungi4_score += 10
            "B. Zygomycota":
                $ quiz_fungi4_score += 0
            "C. Basidiomycota":
                $ quiz_fungi4_score += 0
            "D. Phicomycota":
                $ quiz_fungi4_score += 0

        "Jawaban : 
            \n
            1. A \ \ \ \ 3. C \ \ \ \ 5. D \ \ \ \ 7. D \ \ \ \ 9. C
            \n
            2. A \ \ \ \ 4. B \ \ \ \ 6. D \ \ \ \ 8. B \ \ \ \ 10. A"

        "Nilaiku adalah [quiz_fungi4_score]"

    # Check the quiz 1 score
    if quiz_fungi4_score >= 75:
        # Win
        $ quick_menu = True
        mc "Yang rangkum buat presentasi siapa ?"
        bl "Kita selesaikan juga hari ini semuanya"
        mc "Okie"
        # Did he win? Yes.
        #$ quiz_fungi4_win = True
        #$ quiz_fungi4_lose = False   
    else:
        # Lose
        bl "Biar dah ga usah di kerjakan, capek aku"
        bl "Mereka berdua ga ada lagi"
        menu:
            "Semangat":
                bl "Coba dulu lagi"
                $ quiz_fungi4_score = 0
                jump quiz_fungi4
            "Pulang saja!":
                "Anda gagal sebagai murid"
                "~END~"
                return

    $ psc = "Pelayan Cafe"
    psc "Ini Pesanannya, selamat dinikmati kalau gitu permisi dulu"
    mc "Iya mas, terima kasih"
    bl "Terima Kasih mas"
    "~Beberapa jam mengerjakan tugas dan menikmati camilan~"
    bl "Fuuuhh.. Capeknyaa, mereka berdua ga datang juga salah"
    bl "Coba kalau datang pasti cepat selesai"
    mc "Hahaha iyaaa benar"
    bl "Bisa-bisanya meraka ga datang \nHadeh..."
    mc "Mungkin ada urusan penting {p}Oiya.. Kalau gitu aku pulang dulu ya"
    bl "ehh,, tungguin aku juga mau pulang"
    mc "okk dah"
    
    scene parkiran_mall_malam with dissolve
    mc "[bl] duluan"
    bl "Iyaa hati hati"

    scene depan_rumah_malam with dissolve
    mc "Aku Pulang"

    scene ruang_keluarga_malam with dissolve
    show dad_cas at center with dissolve:
        ypos 1.2
    dad "Oii Nak"
    mc "Loh Ayah sudah pulang ga lembur lagi ?"
    dad "Sudah dong, ga ada job lagi tapi ada sih cuma pengen agak santai juga hari ini"
    mc "Ealah,, okk yah"
    mc "Ibu dimana ?"
    dad "Ibu tidur"
    mc "Yaudah kalau gitu aku langsung tidur aja"
    dad "Iyaa nak, kalau ga salah [cat] Feliz ada di kamarmu"
    mc "okie yah"
    hide dad_cas with dissolve

    scene kamar_malam with dissolve
    "Fuuh Capeknyaa, aku mau tidur dulu lah"
    "[cat] Nungguin aku sampai tertidur juga hahahah"
    "Oke saatnya tidur"

    stop music fadeout 1.0

    jump day5_Miselia

    return

label day4_Airin:

    play music pagi fadein 1.0
    window show dissolve
    scene sky2 with dissolve
    show day4 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day4 with dissolve
    window hide dissolve

    scene kamar with dissolve
    play sound lapar fadein 1.0
    "Ugghh.. Bangun-bangun sudah sakit perut saja mungkin karena kemarin aku makannya kebanyakan"
    stop sound fadeout 1.0
    play sound burung_terbang fadein 1.0
    window hide dissolve
    pause 3.0
    window show dissolve

    scene kamar_mandi with dissolve
    play sound mandi fadein 1.0
    "syukurlah ga ada orang di kamar mandi"
    stop sound fadeout 1.0

    scene ruang_keluarga with dissolve
    "Leganyaa setelah BAB"
    show mom at center with dissolve:
        ypos 1.15
    mom "Loh,, [mcFirst] sudah bangun"
    mc "Iya bu.. "
    mom "[mom] baru selesai belanja buat sarapan.."
    mc "Bareng [dad] bu ?"
    mom "Iyaa itu ada di depan main sama [cat]"
    mc "hoo.. kalau gitu aku mau mandi ama siap-siap berangkat ke sekolah"
    mom "Iyaa.. [mom] siapkan sarapannya"
    hide mom with dissolve

    scene kamar with dissolve
    "Sudah siap semuanya kalau gitu tinggal sarapan"

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "[mcFirst] bisa panggilin [dad] sama [cat] Soalnya sarapannya sudah siap"
    mc "Ohh.. Okk [mom]"
    hide mom with dissolve

    scene depan_rumah
    mc "[dad] dan [cat] Makanan sudah siap"
    show dad_cas at center with dissolve:
        xpos 0.7
        ypos 1.2
    show cat_happy at center with dissolve:
        ypos 0.775
    dad "Lets go!! ayo [cat]"
    cat "Nyaa Nyaa"
    mc "Lah,, aku malah ditinggal"
    hide dad_cas with moveoutright
    hide cat_happy with moveoutright

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Sini sini makanan sudah siap"
    mom "Makananmu juga sudah siap [cat]"
    show mom at center with moveinright:
        xpos 0.3
        ypos 1.15
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Nyaa nyaa"
    hide cat with dissolve
    show mom at center with moveinleft: 
        ypos 1.15
    show dad_cas at center with dissolve:
        xpos 0.675
        ypos 1.2
    dad "Hari ini kamu terlihat lebih cerah"
    mc "Ahh.. Aku yah ?"
    dad "Iyaa kamu"
    mc "Ga ada apa-apa"
    mom "Iyaa lebih seperti ada semangat pagi gitu"
    mc "Hahah Ibu bisa saja"
    mc "Sudah sudah mari kita makan"
    "Kami pun sarapan dan bercanda.."
    "Andaikan setiap hari seperti ini tenang dan tentram"
    mom "Ga usah, Ibu aja yang cuci piringnya. Kamu berangkat aja"
    mc "Gapapa bu.. aku saja"
    hide mom with dissolve
    hide dad_cas with dissolve
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    mc "aku berangkat dulu"
    show mom at center with dissolve:
        ypos 1.15
    mom "Ini Uang sangumu dan bekalmu"
    $ money += 10000
    mc "Terima Kasih Bu"
    show mom at center with moveinright:
        ypos 1.15
    show dad_cas at center with dissolve:
        xpos 0.675
        ypos 1.2
    ai "Hati-hati dijalan"
    show mom at center with moveinright:
        xpos 0.3
        ypos 1.15
    show dad_cas at center with dissolve:
        xpos 0.675
        ypos 1.2
    show cat at center with moveoutbottom:
        ypos 0.775
    cat "Nyaaaa"
    hide cat with dissolve
    dad "Eh,, iyaa aku sebentar lagi masuk jam kerja aku harus bergegas"
    show cat_angry at center with moveoutbottom:
        ypos 0.775
    cat "Nyaa hssss"
    dad "Ahh.. maap maap ekormu kena injak"
    hide cat_angry with dissolve
    hide dad_cas with moveoutleft
    mom "hahahah.. "
    hide mom with dissolve

    stop music fadeout 1.0
    play music jalan_jalan fadein 1.0

    scene jalan with dissolve
    show airin_alma at center with moveinright:
        ypos 1.2
    mg3 "[mcFirst]!!! [mcFirst]!!!"
    "Sepertinya ada yang memanggilku"
    mg3 "[mcFirst]!!! [mcFirst]!!! Lahh,, dicuekkin"
    hide airin_alma with dissolve
    "Ack.. Ternyata [mg3_First]"
    mc "Aku sempat kaget kukira siapa"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "hehehehe"
    mc "Tumben kamu jalan"
    mg3 "Rumahku kan deket juga jadi pengen coba rasanya jalan dari rumah ke sekolah sesekali"
    mc "Ahh.. jadi gituu hahahahaha"
    mg3 "Ihh.. malah ketawa"
    mc "Oiyaa,, gimana latihan nyanyimu ?"
    mg3 "Hmm.. seperti biasa"
    hide airin_alma with dissolve

    scene gerbang_sekolah with dissolve
    show airin_alma at center with moveinright:
        xpos 0.7
        ypos 1.2
    show nada_alma at center with moveinleft:
        ypos 1.2
    na "Ciee ciee berangkatnya barengan"
    hide airin_alma
    show airin_alma at center with moveinright:
        xpos 0.675
        ypos 1.2
    mc "Lahh,, ada kamu juga toh"
    na "Hahahhaha"
    mg3 "Soalnya, rumahku agak dekat sama rumah [mcFirst]"
    mc "Jadi ga ada aneh-aneh"
    na "Canda-canda kalian terlalu serius"
    mc "...."
    mg3 "Sudah sudah skuy masuk kelas"
    na "Hahahahha iyaa skuy"
    hide airin_alma with moveoutright
    hide nada_alma with moveoutright

    scene kelas with dissolve
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Kalau gitu aku duduk dulu di bangkuku"
    hide airin_alma with dissolve
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Iya aku juga"
    hide nada_alma with dissolve
    "Tinggal menunggu bel sekolah saja"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat Pagi anak-anak sudah kah siap untuk belajar hari ini ?"
    sk "Tidak bu!!"
    sr "Kalau gitu tidur aja yaa "
    wkk "Ihh Bu Senda.. Kami Bercanda bu"
    sr "Sama Ibu juga Hahahaha"
    sk "Astaga..."
    sr "yaudah kita mulai saja biar cepat selesai setelah itu biar santai-santai sambil nunggu bel istirahat"
    sk "Baiik bu!"
    $ _skipping = False
    show bu_senda at center with moveinleft:
        xpos 0.7
        ypos 1.2 
    "~Materi Klasifikasi lanjutan~" with dissolve
    sr "SISTEM KLASFIKASI MAHLUK HIDUP"
    sr "Klasifikasi makhluk hidup 5 kingdom yang sering digunakan merupakan cara pengelompokan yang dikemukakan oleh Robert H. Whittaker pada tahun 1969" with dissolve
    sr "Dia membagi makhluk hidup menjadi 5 kelompok besar yaitu monera, protista, jamur, tumbuhan, dan hewan" with dissolve
    sr "KINGDOM MONERA" with dissolve
    sr "Monera adalah kelompok organisme yang inti selnya masih belum memiliki membran inti atau disebut juga organisme prokariotik" with dissolve
    sr "Meskipun tidak memiliki membran inti, organisme ini memiliki bahan inti berupa asam inti atau DNA (deoxy ribonucleic acid atau asam deoksiribonukleat)" with dissolve
    sr "Organisme yang termasuk ke dalam Kingdom Monera adalah organisme dengan ciri-ciri sebagai berikut:" with dissolve
    sr "Bersel satu Tidak memiliki selaput inti atau prokariot, dapat membuat makanan sendiri atau autotroph, juga bergerak atau berpindah tempat" with dissolve
    sr "Monera dapat dibagi lagi menjadi dua, yaitu bakteri dan alga biru:" with dissolve
    sr "BAKTERI" with dissolve
    sr "kelompok organisme yang tidak memiliki membran inti sel. Organisme ini termasuk ke dalam domain prokariota dan berukuran sangat kecil (mikroskopik), serta memiliki peran besar dalam kehidupan di bumi" with dissolve
    sr "Bakteri berkembang biak dengan cara membelah diri" with dissolve
    sr "Beberapa bakteri ada yang berklorofil dan mampu melakukan fotosintesis" with dissolve
    sr "Misalnya, bakteri hijau. Beberapa jenis bakteri menguntungkan namun ada pula yang merugikan bagi kehidupan manusia" with dissolve
    sr "Berikut ini beberapa contohnya:" with dissolve
    sr "Salmonella typhi penyebab penyakit tifus \nMikrobakterium tuberculosis penyebab penyakit TBC" with dissolve
    sr "Escherichia coli hidup di usus besar manusia dan membantu pembusukan sisa makanan" with dissolve
    sr "Rhizobium radicicola hidup bersimbiosis dengan tanaman kacang-kacangan yang membantu menambat nitrogen dari udara dengan membentuk bintil-bintil akar." with dissolve
    sr "Bacillus anthracis penyebab penyakit anthrax pada ternak." with dissolve
    sr "Tubuh bakteri terdiri dari satu sel, sebagian besar bakteri hidup secara sporofit atau parasite, dan berkembangbiak dengan membelah diri atau konjugasi." with dissolve
    sr "ALGA BIRU"
    sr "ganggang yang tergolong dalam kingdom monera Divisio Cyanophyta, ganggang bersel tunggal atau berbentuk benang dengan struktur tubuh yang masih sederhana dimana intinya masih prokaryotik" with dissolve
    sr "Alga biru berkembang biak dengan membelah diri dan bersifat autotrof (mampu membuat makanan sendiri melalui proses fotosintesis)" with dissolve
    sr "Manfaat ganggang biru antara lain: Annabaena azollae yang digunakan sebagai pupuk, dan spiruLina sebagai bahan makanan yang mengandung protein dan lain-lain" with dissolve
    sr "KINGDOM PROTISTA" with dissolve
    sr "makhluk hidup bersel satu atau bersel banyak dan telah memiliki membran inti (selnya bersifat eukariot)" with dissolve
    sr "Protista bukan merupakan hewan ataupun tumbuhan, hanya mempunyai sifat yang menyerupai hewan, tumbuhan, dan jamur" with dissolve
    sr "Semua makhluk hidup eukariotik yang bukan merupakan hewan dan tumbuhan masuk dalam kelompok Protista" with dissolve
    sr "Kelompok Protista yang menyerupai tumbuhan adalah ganggang (Algae), kelompok Protista yang menyerupai hewan adalah Protozoa, sedangkan kelompok Protista yang menyerupai jamur adalah jamur lendir dan jamur air" with dissolve
    sr "Protista biasanya ditemukan di dalam air, dapat berupa plankton yang melayang-layang di dalam air atau melekat di dasar sungai, laut, atau danau." with dissolve
    sr "Protista dapat pula hidup di dalam tanah dan tempat-tempat yang lembap, baik sebagai parasit maupun sebagai saprofit, serta dapat pula hidup bersimbiosis dengan organisme lainnya" with dissolve
    sr "Umumnya, Protista bersifat aerobik dan menggunakan mitokondria untuk respirasi" with dissolve
    sr "Protista memiliki flagela atau cilia sehingga mampu berkembang secara aseksual atau seksual" with dissolve
    sr "Pada kondisi yang kurang menguntungkan, Protista dapat membentuk kistae. Secara taksonomis Protista dapat diklasifikasikan menjadi tiga kelompok, yaitu:" with dissolve
    sr "A. Protista Mirip Tumbuhan: Protista dikatakan mirip tumbuhan karena ia bersifat autotrof, memiliki klorofil, dan dengan bantuan cahaya matahari mampu melakukan fotosintesis" with dissolve
    sr "B. Protista Mirip Hewan: Dikatakan mirip hewan karena Protista ini bersifat heterotrof. Protista ini dapat memasukkan makanan dengan cara menelan melalui mulut pada membran selnya" with dissolve
    sr "Protista ini tidak dapat membuat makanan sendiri karena tidak mengandung klorofil" with dissolve
    sr "C. Protista Mirip Jamur: Protista ini melakukan pencernaan makanan di luar sel, kemudian terjadi penyerapan sari-sari makanan hasil pencernaan makanan oleh tubuh" with dissolve
    $ _skipping = True
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    stop music fadeout 1.0
    play music jalan_jalan2 fadein 1.0
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Sudah bel Anak - anak kalau gitu selamat istirahat"
    hide bu_senda with moveoutright
    sk "Yeay sudah istirahat"
    wkk "[mcFirst] ga mau ke kantin ?"
    show nada_alma at center with dissolve:
        ypos 1.2
    na "Kuy ke Kantin"
    mc "Aku skip dulu aku bawa bekal soalnya"
    wkk "Ohh.. Iya dah kalau gitu kami duluan"
    hide nada_alma with moveoutright
    show airin_alma at center with moveinright:
        ypos 1.2
    mg3 "Mau makan bekal bersama ?"
    skce1 "Aku mau ikutan dong"
    mc "...."
    mg3 "Silahkan.."
    mc "Eii.. Seharusnya aku itu"
    mg3 "Hahahahaha"
    skce1 "Makanan kalian enak-enak semua kelihatannya"
    mg3 "hahahah bisa saja.. Semuanya enak kok.. \npokok bisa dimakan"
    skce1 "Iyaa juga sih hahaha"
    skce1 "[mcFirst] Aku boleh cobain ga ?"
    mc "Silahkan.."
    skce1 "EENAKKK SEKALII!!"
    skce1 "Ini kamu masak sendiri ?"
    mc "Bukan itu masakan ibuku"
    mg3 "Aku mau coba juga"
    mg3 "Ehh.. Beneran Enak.. kamu boleh coba di bekalku kok"
    skce1 "Aku jugaa ahha"
    mc "Okk Kalau gitu aku coba juga punya kalian"
    mc "Enak,, Kalian masak sendiri ?"
    skce1 "hehehe.. aku masak sendiri"
    mg3 "Aku juga masak sendiri"
    hide airin_alma with dissolve
    "Kami pun menghabiskan bekal kami sambil berdiskusi dan bercanda"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    skce1 "ternyata sudah Bel.. Kalau gitu aku kembali ke bangku ku dulu"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "sama aku juga.. Oiyaa,, nanti kamu free ?"
    mc "Hmm.. iya"
    mg3 "Temenin aku latihan lagi ya"
    hide airin_alma with moveoutright
    mc "Ohh.. Okk"
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat siang anak-anak"
    sk "Siang buu!!"
    sr "Hoo.. masih semangat.. kalau gitu Ibu kasih soal tolong dikerjakan ya"
    sk "Baik bu!!"
    sr "Bu Senda mau keruang guru ada rapat"
    sr "Oiya,, lupa ini soalnya dibagi ya"
    sk "Baik bu!!"
    hide bu_senda with moveoutright

    "~SOAL~" with dissolve
    #Initialize score
    $ quiz4_klasifikasi_score = 0

    label quiz4_klasifikasi:
        $ quick_menu = False

        "1. Berikut ini termasuk kelompok tumbuhan tidak berpembuluh, kecuali …."
        menu:
            "A. ganggang":
                $ quiz4_klasifikasi_score += 0
            "B. tumbuhan paku":
                $ quiz4_klasifikasi_score += 10
            "C. lumut":
                $ quiz4_klasifikasi_score += 0
            "D. jamur":
                $ quiz4_klasifikasi_score += 0

        "2. Benang-benang halus berwarna putih yang tedapat pada jamur disebut …."
        menu:
            "A. spora":
                $ quiz4_klasifikasi_score += 0
            "B. rizoid":
                $ quiz4_klasifikasi_score += 0
            "C. sporangium":
                $ quiz4_klasifikasi_score += 0
            "D. hifa":
                $ quiz4_klasifikasi_score += 10 

        "3. Berikut ini yang termasuk dalam kelompok tumbuhan berbiji terbuka adalah …. "
        menu:
            "A. kacang hijau, jagung, jambu mete ":
                $ quiz4_klasifikasi_score += 0
            "B. pakis haji, melinjo, pinus":
                $ quiz4_klasifikasi_score += 10
            "C. kacang tanah, melinjo, pinus":
                $ quiz4_klasifikasi_score += 0
            "D. pakis haji, jambu mete, jagung":
                $ quiz4_klasifikasi_score += 0

        "4. Tumbuhan berbiji terbuka yang dapat dijadikan sebagai tanaman hias adalah …. "
        menu:
            "A. pakis haji":
                $ quiz4_klasifikasi_score += 10
            "B. tusam":
                $ quiz4_klasifikasi_score += 0
            "C. melinjo":
                $ quiz4_klasifikasi_score += 0
            "D. damar  j":
                $ quiz4_klasifikasi_score += 0
            
        "5. Kerangka hewan berpori dapat dimanfaatkan sebagai …. "
        menu:
            "A. penggosok pakaian":
                $ quiz4_klasifikasi_score += 0
            "B. penggosok kulit":
                $ quiz4_klasifikasi_score += 0
            "C. spons mandi":
                $ quiz4_klasifikasi_score += 10
            "D. vas bunga":
                $ quiz4_klasifikasi_score += 0

        "6. Burung termasuk dalam kelompok hewan berdarah panas, yang artinya …. "
        menu:
            "A. suhu tubuhnya mengikuti suhu lingkungan":
                $ quiz4_klasifikasi_score += 0
            "B. suhu tubuhnya lebih tinggi dari suhu lingkungan":
                $ quiz4_klasifikasi_score += 0
            "C. suhu tubuhnya tetap, meskipun suhu lingkungan berubah":
                $ quiz4_klasifikasi_score += 10
            "D. memiiki kemampuan adaptasi dengan lingkungan":
                $ quiz4_klasifikasi_score += 0

        "7. Berikut ini hewan yang memiliki rangka dalam adalah …. "
        menu:
            "A. belalang dan kupu-kupu":
                $ quiz4_klasifikasi_score += 0
            "B. lebah dan laba-laba ":
                $ quiz4_klasifikasi_score += 0
            "C. katak dan kadal ":
                $ quiz4_klasifikasi_score += 10
            "D. kumbang dan kalajengking":
                $ quiz4_klasifikasi_score += 0

        "8. Burung pada waktu terbang akan lebih efektif dalam bernapas jika menggunakan …. "
        menu:
            "A. paru-paru buku":
                $ quiz4_klasifikasi_score += 0
            "B. insang dan paru-paru":
                $ quiz4_klasifikasi_score += 0
            "C. pundi-pundi udara":
                $ quiz4_klasifikasi_score += 10
            "D. paru-paru dan pundi-pundi hawa":
                $ quiz4_klasifikasi_score += 0

        "9. Rhizopoda adalah hewan bersel satu yang bergerak dengan menggunakan …."
        menu:
            "A. kaki semu":
                $ quiz4_klasifikasi_score += 10
            "B. kaki tabung":
                $ quiz4_klasifikasi_score += 0
            "C. bulu getar":
                $ quiz4_klasifikasi_score += 0
            "D. bulu cambuk":
                $ quiz4_klasifikasi_score += 0

        "10. Berikut ini yang bukan termasuk ciri tumbuhan dikotil adalah …."
        menu:
            "A. akarnya tunggang":
                $ quiz4_klasifikasi_score += 0
            "B. batang bercabang":
                $ quiz4_klasifikasi_score += 0
            "C. daunnya menjari":
                $ quiz4_klasifikasi_score += 10
            "D. berkeping dua":
                $ quiz4_klasifikasi_score += 0

        "Jawaban : 
            \n
            1. B \ \ \ \ 3. B \ \ \ \ 5. C \ \ \ \ 7. C \ \ \ \ 9. A
            \n  
            2. D \ \ \ \ 4. A \ \ \ \ 6. C \ \ \ \ 8. C \ \ \ \ 10. C"

        "Nilaiku adalah [quiz4_klasifikasi_score]"

    # Check the quiz 1 score
    if quiz4_klasifikasi_score >= 75:
        # Win
        $ quick_menu = True
        mc "Akhirnya sudah selesai.."
        show nada_alma at center with dissolve:
            ypos 1.2
        na "Hahaha mau main kartu lur ?"
        mc "Rasanya mau tidur saja"
        mc "Oiyaa,, titip nanti kalau sudah mau dikumpulkan"
        hide nada_alma with dissolve
        # Did he win? Yes.
        #$ quiz4_win = True
        #$ quiz4_lose = False   
    else:
        # Lose
        "Susahnya,, Aku biarin atau aku tanya ke teman-teman ya ?"
        menu:
            "Bertanya ke teman-teman":
                $ quiz4_klasifikasi_score = 0
                jump quiz4_klasifikasi
            "Biarin":
                "Anda gagal sebagai murid"
                "~END~"
                return

    sk "Mantapp sudah selesai.."
    $ ad = "Ardi"
    ad "gass.. main-main skuy"
    kk "heee.. Jangan ramai-ramai \nMainnya santuy-santuy saja"
    sk "Baik Leader Hahahha"
    kk "Dasar kalian ini"
    "~Semuanya yang di kelasku pun bermain kartu ada yang makan camilan, ada yang curhat-curhat~"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    sk "Yeaayy.. Mantapp sudah pulangg"
    kk "Tugasnya jangan lupa dikumpulkan"
    kk "[wkk] jangan pulang duluan temani aku anterin tugasnya"
    wkk "heheheh ketahuan"
    sk "ahhahahah dasar pak Wakil"
    kk "Tugasnya sudah terkumpul semua kan ?"
    kk "Kalau gitu pulang gaes"
    $ fh = "Farhan"
    fh "gas Pulang"
    show nada_alma at center with dissolve:
        ypos 1.2
    na "[mcFirst] oee bangun !! oee bangun !! oee bangun !! lurr bangun!!"
    na "Sigh.. sudah nyenyak tidurnya.. Kalau gitu aku pulang duluan brader"
    na "[mg3_First] titip [mcFirst] ya.. Siapa tau kalau kamu yang bangunin ? jadi bangun beneran hahaha"
    show nada_alma at center with moveinright:
        xpos 0.3
        ypos 1.2
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "ehh.. Iyaa.. Iyaa.."
    na "Kalau gitu aku duluan"
    hide nada_alma with moveoutright

    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    
    mg3 "Okk"
    mg3 "[mcFirst] Bangun!! katanya mau temani latihan"
    mg3 "Kalau gitu aku tunggu dah. Btw, kok ngantuk juga ya"
    mg3 "Yaudah lah tidur sebentar juga.."
    hide airin_alma with dissolve
    "~15 Menit Kemudian~"
    mc "Hoamm.. Hmmm.. sudah sepi ?!"
    mc "Loh kok [mg3_First] disini juga ?"
    mc "Oiyaa,, katanya mau temani di atap sekolah tapi kok jadi tidur ?!"
    mc "Bangunn [mg3_First] ayo ktanya mau temani kamu latihan"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Umm... Hoamm... Ehh.. iyaa yaa.."
    mc "Ayooo ke atap"
    mg3 "Umm... Tapi aku masih ngantuk"
    mc "Raup dulu sana.. \nAku juga mau raup"
    mg3 "Iyaa iyaa"
    hide airin_alma with moveoutright

    scene toilet_sore with dissolve
    "Segarnyaa,, jadi ga ngantuk lagi \nAku sudah selesai mungkin aku tunggu di luar toilet saja"

    scene depan_toilet_sore with dissolve
    mc "Loh kamu sudah selesai ?"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Sudah dongg \nKuy ke Atap"
    mc "Haii.."
    hide airin_alma with moveoutleft

    scene atap_sore with dissolve
    mc "Aku jadi terbiasa sering pergi kesini karenamu Hahhaa"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "///// Ehh.. Eh.. Hahahhaha"
    mg3 "Kalau gitu aku mulaii yaa"
    mc "Iyaaa"
    hide airin_alma with dissolve
    stop music fadeout 1.0
    $ _skipping = False
    play music nyanyi fadein 1.0
    "~Mendengarkan Nyanyian~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    window show dissolve
    $ _skipping = True
    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Fuhh.. gimana ?"
    mc "Bagus seperti biasanya ada perkembangan sedikit meskipun aku bukan anak padsu atau sebagainya tapi aku ngerasain lebih bagus sekarang"
    mg3 "Terima kasih hehhe"
    mc "Oiyaa,, ngomong-ngomong kenapa kamu selalu bernyanyi ?"
    mg3 "deg... Deg.. Sigh.. itu ada alasannya"
    mc "Gapapa, kalau kamu ga mau nyeritain aku akan berhenti bertanya"
    mg3 "Eh.. gapapa kok.. \nAku ceritain Besok gimana ?"
    mc "Boleh.."
    mg3 "Oiyaa, sudah mau sore nih ayoo pulangg!!"
    mc "Iyaa ayoo pulang"
    hide airin_alma with moveoutleft

    scene jalan_sore with dissolve
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Ternyata enak ya pulang jalan kaki lebih sehat rasanya hahah meskipun agak kecapekan"
    mc "Soalnya kamu belum terbiasa pulang jalan kaki"
    mg3 "hehehhe.. iyaa benar"
    hide airin_alma with dissolve

    stop music fadeout 1.0
    play music sore fadein 1.0

    scene depan_rumah_sore with dissolve
    mc "Mau mampir kerumahku dulu ?"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Hmmm.. Okk kalau gitu aku mampir dulu.. sesekali mampir hahaha"
    mc "Hmm... Okk dah"

    scene ruang_tamu_sore with dissolve
    mc "Aku pulang !!!"
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Meoowww !!!"
    mc "Haii.. [cat] Aku kelitiki kau"
    cat "Nyaa Nyaa Nyaa Nyaa"
    mc "hahahahah Geli kan"
    show airin_alma at center with dissolve:
        xpos 0.7 
        ypos 1.2
    mg3 "Kamu melihara kucing ?"
    mc "Iyaa kutemukan di jalan sewaktu berangkat sekolah"
    mg3 "Ohh.. Lucu juga ya kucingnya.."
    mc "Tunggu sini yaa"
    mg3 "okk deh"
    hide cat with dissolve
    hide airin_alma with dissolve

    scene ruang_keluarga_sore with dissolve
    mc "[mom] ada temanku mampir kerumah kita"
    show mom at center with dissolve:
        ypos 1.15
    mom "Selamat datang!! \nEhh.. ada tamu tohh.. dimana sekarang temanmu?"
    mc "Diruang tamu.. \n kalau gitu aku ganti baju dulu ya bu"
    mom "Iyaa nak"
    hide mom with dissolve

    scene ruang_tamu_sore with dissolve
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Gulu Gulu Gulu"
    show airin_alma at center with dissolve:
        xpos 0.7
        ypos 1.2
    show cat at center with moveinbottom:
        ypos 0.775
    cat "Nyaa nya nyaa"
    show mom at center with moveinleft:
        xpos 0.3
        ypos 1.15
    mom "Oya Oyaa.. jadi ini temennya [mcFirst]"
    mg3 "Ahh.. Permisi tante"
    mom "Iyaa silahkan.. \n[mcFirst] lagi ganti baju"
    mg3 "Iyaa tante"
    mom "Kalau gitu tante kedalam dulu ya"
    hide mom with moveoutleft
    hide airin_alma with dissolve
    hide cat with dissolve

    scene kamar_sore with dissolve
    mc "Semogaa ga terjadi yang heboh.."

    scene dapur_sore with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "kalau gitu bikin Cheese Cake sama Milkshake saja"
    hide mom with dissolve

    scene ruang_tamu_sore with dissolve
    mc "[mom]ku kemana ?"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Tadi masuk kedalam"
    mc "[cat] tenang sekali sama kamu"
    mg3 "Ga tau juga mungkin aku punya pesona kucing hahahah"
    mc "Ada ada saja Hahaha"
    mg3 "Ngomong-ngomong ibumu ramah ya"
    mc "Hehehe Iyaa.. kadang heboh juga sih"
    mg3 "Andaikan ibuku seperti itu"
    mc "...."
    mg3 "Ahh.. lupakan-lupakan"
    mc "Iyaa"
    show airin_alma at center with moveinright:
        xpos 0.3
        ypos 1.2
    show mom at center with moveinright:
        ypos 1.15
    mom "Camilan sudah siap"
    mom "Baru kali ini loh [mcFirst] mengajak seseorang kerumah"
    mg3 "Memangnya dulu-dulu ada apa tante ?"
    mom "Canda Tehee~~"
    mg3 "Astaga tante Hahahah"
    mc "Dah dah dimakan itu.. \nenak ituu"
    mom "kalau gitu [mom] kedalam dulu"
    hide mom with moveoutleft
    show airin_alma at center with moveinleft:
        xpos 0.4
        ypos 1.2
    mc "Iya buu"
    mg3 "Heee.. Enak,, yang kemarin pun enak juga masakan [mom]mu"
    mc "Jelas dong hehehhe"
    hide airin_alma with dissolve
    "Kami pun berdiskusi, bercanda ria, dan main-main. Tak terasa sudah malam saja"
    
    scene ruang_tamu_malam with dissolve
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "Dimana orang tuamu ?"
    mc "Mungkin di ruang keluarga \nSini dah"
    mg3 "Permisi~"
    hide airin_alma with moveoutleft

    scene ruang_keluarga_malam with dissolve
    show airin_alma at center with moveinright:
        ypos 1.2
    mg3 "Om dan Tante aku pulang dulu ya"
    show airin_alma at center with moveinright:
        xpos 0.3
        ypos 1.2
    show dad_cas at center with dissolve:
        xpos 0.7
        ypos 1.2
    dad "Ga mau ditemeni ?"
    mg3 "gausah om nanti ngerepotin"
    show mom at center with dissolve:
        ypos 1.15
    mom "Gapapa biar [mcFirst] nanti yang anterin"
    mg3 "Ga usah tante saya bisa sendiri"
    mc "Sigh.. Mari aku temenin sampe rumahmu sekalian aku tau rumahmu"
    mg3 "umm... Iyaa dahh.."
    mg3 "Kalau gitu aku pamit dulu Om dan Tante"
    ai "Iya hari-hari dijalan"
    hide airin_alma with moveoutleft
    hide dad_cas with dissolve
    hide mom with dissolve

    scene jalan_malam with dissolve
    mc "Rumahmu masih agak jauh ?"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "ga kok bentar lagi sampe"
    mg3 "ngomong-ngomong kamu dulu kenapa ?"
    mc "Ahh.. ga ada apa- apa"
    mc "Tapi kalau penasaran besok aku ceritain juga jadi kamu juga cerita masalahmu yang dulu"
    mg3 "Hai hai.."
    hide airin_alma with dissolve

    scene depan_rumah_airin_malam with dissolve
    mc "Rumahmu besar juga ya"
    show airin_alma at center with dissolve:
        ypos 1.2
    mg3 "hahah ga juga.. Yaudah kalau gitu aku masuk dulu"
    mc "Iyaa aku pulang dulu"
    mg3 "Hati-hati dijalan"
    hide airin_alma with dissolve

    scene ruang_keluarga_malam with dissolve
    show dad_cas at center with dissolve:
        xpos 0.7
        ypos 1.2
    show mom at center with dissolve:
        ypos 1.15 
        xzoom -1
    dad "Sudah diantarin kerumahnya ?"
    mc "Sudah.. rumahnya ga begitu jauh dari sini"
    mc "Ayah,, Ibu,, Kalau gitu aku mau tidur duluan ya"
    ai "Iya Nak Sleep Well Have a Nice Dream"
    mc "hahah Iya"
    hide dad_cas with dissolve
    hide mom with dissolve

    scene kamar_malam with dissolve
    "Aku Harus tidur.. mataku sisa 5 watt hahaha"

    stop music fadeout 1.0

    jump day5_Airin

    return