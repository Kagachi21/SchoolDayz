label day2_Kirana:

    play music pagi fadein 1.0 
    window hide dissolve
    scene sky2 with dissolve
    show day2 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day2 with dissolve
    window show dissolve

    scene kamar with dissolve
    "Sepertinya aku sudah mulai terbiasa dengan pagi hari ini"
    stop sound fadeout 1.0
    play sound burung_terbang fadein 1.0
    window hide dissolve
    pause 3.0
    window show dissolve
    play sound kentut fadein 1.0
    "~Suara Kentut~"
    stop sound fadeout 1.0
    play sound lapar fadein 1.0
    "Aakkhh.. perutku sakit seperti gara-gara kemarin makan terlalu banyak"
    stop sound fadeout 1.0

    scene ruang_keluarga with dissolve
    "Haa.. Leganyaa!!"
    "Hmm.. ada yang bersihin motor"

    scene depan_rumah with dissolve
    mc "Ayah pagi-pagi udah rajin aja nih hehhe"
    show dad_cas at center with dissolve:
        ypos 1.2
    dad "loh, nakkk sudah bangun, kok tumben kamu ga bangkong"
    mc "kan tiap pagi emang bangun pagi kan hhaha"
    mc "kalau gitu aku mandi terus siap siap dulu buat berangkat sekolah"
    dad "Iyaa nak"
    hide dad_cas with dissolve

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Makanan Sudah Siap !!!"
    hide mom with dissolve

    scene depan_rumah with dissolve
    show dad_cas at center with dissolve:
        ypos 1.2
    dad "Iyaa Bu..!!"
    hide dad_cas with dissolve
    
    scene kamar_mandi with dissolve
    play sound mandi fadein 1.0
    mc "Iyaa !!"
    stop sound fadeout 1.0
    "Aku harus bergegas memakai baju"

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Sudah selesai siapin untuk ke sekolah ?"
    mc "Sudah bu"
    show dad_cas at center with dissolve:
        xpos 0.6
        ypos 1.2
    dad "[mcFirst] Sini [mom] sudah selesai masak nih, enak lohh!! ayo makan"
    mc "Iyaa yah"
    mc "Bu aku kok lapar banget ya ?"
    mom "Soalnya kemarin kamu langsung tidur dan ga bangun-bangun"
    mom "[mom] ga mau ganggu bangunin juga sepertinya kemarin kamu kecapekan"
    mom "Oiya,, Ibu sudah siapinn juga nasinya"
    mc "Hoo,, jadi begitu. Makasih bu sudah disiapin juga, kalau gitu [mcFirst] makan dulu bu"
    mom "Kemarin, cewe itu siapamu ?"
    dad "Ehhh.. Kemarin [mcFirst] bawa cewe kerumah ?"
    dad "Ho ho ho ho ho"
    mc "...."
    mc "Dia hanya teman sekolah"
    ai "Beneran teman sekolah ? hehehe"
    mc "Iyaa hanya teman sekolah saja, tapi sepertinya dia dulu juga 1 smp denganku"
    mc "Soalnya kemarin [mg2_Last] sempat bertanya masalah bullying"
    mom "Hmm.. jadi begitu"
    mc "Terus dia juga memaksaku dan mengikutiku jalan. Dia ingin mengantarku sampai ke rumah sekalian biar tau rumahku dimana ?"
    mc "Karena merepotkan akhirnya aku terima aja tawarannya"
    mom "Hahaha iya iya, Ibu percaya kok cuma tadi mau bercandain [mcFirst] aja"
    mom "Soalnya, Ibu sempat kaget kalau kamu tiba-tiba bawa teman kerumah"
    dad "Ayah juga kaget loh dengar kamu bawa cewe kemarin"
    mom "Ibu kemarin sempat bahagia kalau kamu mulai sedikit membaik"
    mc "hahahaha Iyaa bu"
    mc "Oiya, [cat] Kemana bu ?"
    mom "Itu Lagi Makan juga"
    mc "Tumben ga kekamarku kayak kemarin kemarinnya"
    dad "Soalnya [dad] kemarin waktu pulang langsung main sama [cat]"
    dad "Ibu juga ikutan hehehe"
    mc "Pagi [cat] makanmu lahap bener"
    show dad_cas at center with moveinleft:
        xpos 0.8
        ypos 1.2
    show mom at center with moveinleft:
        xpos 0.675
        ypos 1.15
        xzoom -1
    show cat_happy at center with moveoutbottom:
        ypos 0.75
    cat "Nyaaa "
    mc "Aku Cuci piring dulu ya bu setelah itu berangkat langsung"
    mom "Oiya, Bekalnya sudah [mom] siapkan ada disini"
    mc 'Iya bu'
    hide mom with dissolve
    hide dad_cas with dissolve
    hide cat_happy with dissolve
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(15.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    mc "Kalau gitu aku berangkat dulu Ayah Ibu"
    show mom at center with dissolve:
        ypos 1.15
    show dad_cas at center with dissolve:
        xpos 0.6
        ypos 1.2
    ai "Iyaa Nak hati hati dijalan"
    mc "Okie"
    mom "Ayah ga berangkat kerja juga ?"
    dad "Bentar lagi, berangkat"
    hide mom with dissolve
    hide dad_cas with dissolve

    stop music fadeout 1.0

    play music jalan_jalan fadein 1.0

    scene gerbang_sekolah with dissolve
    "Hmm.. ada yang mendekatiku mungkin sebaiknya aku diamin saja"
    $ kg = "Ketua Geng Kaya"
    $ ag = "Anggota Gengs Kaya"
    kg "yauda lah ya, ga cocok masuk gengs kita tuh sudah miskin dan tercium bau bau ga mampu"
    kg "Benar ga gengs"
    ag "Yup, Ketua emang bener emang best kaum miskin kek gini mana bisa masuk geng ini. Dih.."
    show nada_uni at center with dissolve:
        xpos 0.7
        zoom 0.5
    na "Oeee [mcFirst] Tunggu aku!!!"
    "Untunglah ada si Bodoh satu ini jadi aku bisa melewati masalah ini"
    show nada_uni at center with dissolve:
        ypos 1.2
        zoom 0.9
    na "Huufftt.. Hufft... \nSiapa itu ? [mcFirst]"
    mc "Ga tau juga aku, Mungkin kakak kelas gabut"
    mc "Abaikan aja"
    na "Hahaha, Okay dah langsung kelas aja kuy"
    kg "Hei,, kalian mengabaikanku yaa awas aja kalian dasar kaum miskin"
    hide nada_uni with moveoutleft

    scene lorong with dissolve
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Ada [mcFirst], aku kesana dulu gaes"
    ol "Hooo sudah ada incaran nih"
    mg2 "Ehh Ngga lah. Cuma teman itu"
    ol "Iyaa dah kalau gitu sana selamat sukses.. "
    ol "Ciiee ciiee"
    mg2 "Ihh Apaan sih kalian ?"
    ol "Hahahhaha,, dah dah sana"
    hide ardana_uni with moveoutleft
    "Kayaknya ada yang mau mendekat"
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Baa.."
    mc "Astaga.."
    mg2 "Kaget ga ?"
    mc "Hmmm..."
    show nada_uni at center with dissolve:
        xpos 0.7
        ypos 1.2
    na "Lahh,, ada kamu [mg2_Last] aku ikutan kaget juga njirr"
    mg2 "Hehehe maaf maaf.. "
    mg2 "Gitu aja marah \nTe hee"
    hide ardana_uni with moveoutleft
    hide nada_uni with moveoutleft

    scene kelas with dissolve
    show nada_uni at center with moveinright:
        xpos 0.7
        ypos 1.2
    na "Kuy Duduk"
    hide nada_uni with moveoutleft
    mc "Duduk disebelahku lagi ?"
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Ga suka ?"
    show nada_uni at center with moveinright:
        xpos 0.7
        ypos 1.2
    na "Akhir Akhir ini [mg2_Last] duduk ama [mcFirst] mulu"
    na "Ciiiee ciiee ada apa ini ?"
    mc "Entahlah"
    mg2 "padahal baru 2 hari"
    mc "Hmmm..."
    mg2 "Mending sekarang kita belajar deh sampai bel berbunyi hahaha"
    hide nada_uni with dissolve
    hide ardana_uni with dissolve
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
    show bu_senda at right with moveinleft:
        xpos 0.9
        ypos 1.2
    $ _skipping = False
    "~Materi Virus Lanjutan~"
    window hide dissolve
    stop music fadeout 1.0
    #Video Virus
    show ciri_virus behind sr at center with dissolve:
        xpos 0.3
        ypos 0.6
        zoom 0.5
    $ renpy.pause(39.5, hard=True)
    hide ciri_virus with dissolve
    window show dissolve
    $ _skipping = True
    play music jalan_jalan2 fadein 1.0
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Sudah bel Anak- anak kalau gitu selamat istirahat"
    hide bu_senda with moveoutright
    sk "Yeay sudah istirahat"
    ol "[mg2_Last] ga pergi ke kantin ?"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Iyaa bentar"
    mg2 "[mcFirst] ga mau pergi ke kantin juga ?"
    mc "Ga usah aku soalnya bawa bekal"
    mg2 "dihh mauu buatan Ibumu"
    mc "Emohh.. sana ikut temanmu ke kantin"
    hide ardana_uni with moveoutright
    show nada_uni at center with moveinright:
        ypos 1.2
    na "Bro Ikutan juga bareng kita ? [skco1] dan [wkk]"
    mc "Ga, duluan dah"
    na "Oke kalau begitu, Lets go kawand"
    wkk "Okay ma brader"
    hide nada_uni with moveoutright
    "Isi Bekalnya lumayan banyak juga"
    "Nyam Nyam Nyam~"
    "Kenyang juga, aku pikir akan porsi kecil ternya porsi besar"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Fuhaah Kenyangnyaa~"
    hide ardana_uni with moveoutleft
    show nada_uni at center with moveinright:
        ypos 1.2
    na "Aku Masih kurang"
    wkk "Hahaha Bisa aja kamu"
    skco1 "Sama sih aku masih kurang soalnya aku ga sarapan sama sekali"
    hide nada_uni with moveoutleft
    show nada_uni at center with moveinright:
        ypos 1.2
    na "Ini lur kubawakan Roti Sosis"
    mc "Gratis Nih ?"
    na "Bayar dong"
    mc "Ok ok"
    na "Ehh.. gratis gratis aku cuma bercanda hahahah"
    mc "Nih uangnya ambil aja"
    na "Okelah kalau gitu hehehhe"
    show ardana_uni at center with moveinleft:
        ypos 1.2
    show nada_uni at center with moveinleft:
        xpos 0.7
        ypos 1.2
    mg2 "Punyaku mana ?"
    na "ga ada lah ya beli sendiri dong"
    hide ardana_uni
    show ardana_uni_emosi at center:
        ypos 1.2
    mg2 "Dih Curang"
    mc "pfft.."
    mg2 "Ihh Ngeledek yaa"
    mc "ga sama sekali"
    na "Hahah lucu sekali melihat kalian berdua. yaudah aku kembali ke bangku dulu"
    na "Ntar Bu Senda keburu datang"
    hide ardana_uni_emosi with dissolve
    hide nada_uni with moveoutright

    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat siang anak-anak. Ibu punya soal buat kalian dikerjakan yaa! nanti ibu tinggal ke ruang guru soalnya ada rapat"
    $ kk = "Ketua Kelas"
    sr "oiyaa anak anak, kali ini ibu akan membentuk kalian kelompok, tapi sebangku aja ya biar gampang"
    kk "bu apakah sebaiknya di kocok sajaa biar Adil"
    sr "bagaimana apa kalian setuju?"
    sk "Setujuu Bu!! Biar lebih mengenal karakterisitik semuanya bu"
    "Padahal Aku tidak setuju tapi karena kurang suara apa boleh buat"
    kk "Bikin potongan kertas sesuai Absen bu Nanti anak-anak mengambilnya nomor yang diambil akan berkelompok"
    kk "Setelah itu yang sudah mendapatkan kelompok tidak perlu mengambil nomornya lagi bu"
    sr "Tapi nanti anak-anak nomor absen belakang tidak akan kebagian mengambil juga"
    sr "Aha.. Ibu punya ide kita mulai dari nomor absen awal yang mengambil selanjutnya nomor absen terakhir yang mengambil"
    sr "Bagaimana anak-anak ?"
    skco1 "Boleh juga itu bu"
    sr "Okee.. Laksanakan"
    sk "Yes Mam"
    hide bu_senda with dissolve
    "Ahh Kelompok Merepotkan sekali"
    "Moga dapat orang yang ga merepotkan"
    $ rr = "Rere"
    rr "aku sekelompok sama nomor 3 , siapa absenn nomor 3 ?"
    mc "Aku"
    rr "Oh Ok"
    mc "...."
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Kamu kelompokan sama [rr] lur. orangnya itu Nakal, Males, Sok Cool"
    na "tapi cantik juga sih hehehe"
    mc "Bodoh amat ama yang namanya cantik"
    na "aku dengar-dengar gitu sih dari teman yang 1 SMP dengannya"
    na "Oiyaa, orangnya juga pintar soalnya sering juara aku denger dengernya gitu"
    mc "dahlah. nth ini beruntung atau merugikanku"
    show nada_uni at center with moveinright:
        xpos 0.7
        ypos 1.2
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "hussh!!"
    "~Berlanjutlah pemilihan kelompok~" 
    hide nada_uni with dissolve
    hide ardana_uni with dissolve

    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Sudah dapat kelompoknya masing masing kan ya ?"
    sk "Sudah semuanya bu ga ada yang jomblo"
    sr "Kalau gitu Ibu ke ruang guru dulu ya. Soalnya jangan lupa dikerjakan loh"
    sr "kalau ada yang ga ngerjakan ada hukumannya"
    sk "Baik buu"
    hide bu_senda with moveoutright
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Aku kelompokan sama Meta anjir, kamu tau sendiri ceriwisnya minta ampun kan itu kzl .. "
    $ mt = "Meta"
    show nada_uni at center with moveinright:
        xpos 0.7
        ypos 1.2
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Hahaha sabar"
    $ tmn_mg2 = "Filo"
    ol "[mg2_Last] Kelompokan sama siapa kamu ?"
    mg2 "Aku sama [skce2] kalau kamu sama siapa [ol]?"
    ol "Aku sama [kk]"
    skce1 "Ihh.. enak banget"
    mc "Dah dah biar kelar duduk sekelompok sekarang"
    hide ardana_uni with dissolve
    hide nada_uni with dissolve
    "Mungkin aku sebaiknya kesana"
    rr "...."
    "Ternyata cukup merepotkan juga ya"
    mc "Ayo kerjakan tugasnya bersama"
    rr "ha?kamu aja sono yang ngerjakan, males aku tu, cape mau tidur aja"
    mc "Ini tugas kelompok"
    rr "Serah serah aku lah"
    mc "...."

    "~SOAL~" with dissolve
    #Initialize score
    $ quiz2_score = 0

    label quiz2:
        $ quick_menu = False

        "1. Virus dapat dianggap sebagai makhluk hidup, sebab virus:"
        menu:
            "A. Hanya dapat hidup dalam sel–sel hidup":
                $ quiz2_score += 0
            "B. Dapat dikristalkan":
                $ quiz2_score += 0
            "C. Kulitnya terdiri atas protein":
                $ quiz2_score += 0
            "D. tubuhnya terdiri atas DNA atau RNA":
                $ quiz2_score += 10

        "2. Struktur terkecil yang memuat materi genetika dan berevolusi menjadi parasit dengan mengendalikan biosintesis pada sel inang untuk menjaga keberlanjutannya adalah"
        menu:
            "A. Parasit Obligat":
                $ quiz2_score += 0
            "B. Virus":
                $ quiz2_score += 10
            "C. Archaebacteria":
                $ quiz2_score += 0
            "D. Eukariot":
                $ quiz2_score += 0 

        "Berdasarkan pernyataan di atas bentuk dari virus terdapat pada nomor" (multiple=2)
        "3. Perhatikanlah ciri-ciri struktur organisme di bawah ini !
                \n
                1. Berbentuk batang
                \n
                2. Berbentuk batang dan berujung oval seperti peluru
                \n
                3. Berbentuk bulat
                \n
                4. Berbentuk filamen atau benang
                \n
                5. Berbentuk seperti huruf T" (multiple=2)
        menu:
            "A. 2, 3, dan 5":
                $ quiz2_score += 0
            "B. Semuanya benar":
                $ quiz2_score += 10
            "C. 1, 2, dan 4":
                $ quiz2_score += 0
            "D. 3, 4, dan 5":
                $ quiz2_score += 0

        "4. Pada virus, asam nukleat yang diselubungi oleh kapsid dinamakan"
        menu:
            "A. DNA":
                $ quiz2_score += 0
            "B. Selubung membrane":
                $ quiz2_score += 0
            "C. RNA":
                $ quiz2_score += 0
            "D. Nukleokapsid":
                $ quiz2_score += 10
            
        "Berdasarkan pernyataan di atas yang bukam bentuk dari virus terdapat pada nomor" (multiple=2)
        "5. Perhatikanlah ciri-ciri struktur organisme di bawah ini !
                \n
                1. Berbentuk batang
                \n
                2. Berbentuk persegi
                \n
                3. Berbentuk bulat
                \n
                4. Berbentuk kubus
                \n
                5. Berbentuk seperti huruf T"(multiple=2)
        menu:
            "A. 2, 3, dan 5":
                $ quiz2_score += 0
            "B. 1, 3, dan 4":
                $ quiz2_score += 0
            "C. Semuanya benar":
                $ quiz2_score += 0
            "D. 2 dan 4":
                $ quiz2_score += 10

        "6. Fungsi Kaki serabut pada bakterifag yang merupakan perpanjangan ekor yaitu untuk.."
        menu:
            "A. Menancapkan diri ke berbagai substrat":
                $ quiz2_score += 0
            "B. Reproduksi virus":
                $ quiz2_score += 0
            "C. Bergeraknya bakteri":
                $ quiz2_score += 0
            "D. Bergeraknya virus":
                $ quiz2_score += 10

        "7. Berikut ini adalah struktur virus, kecuali"
        menu:
            "A. Virus bersifat aseluler":
                $ quiz2_score += 0
            "B. Virus hanya memiliki RNA dan DNA saja":
                $ quiz2_score += 10
            "C. Bisa di kristalkan":
                $ quiz2_score += 0
            "D. Tubuh tersusun dari asam nukleat":
                $ quiz2_score += 0

        "8. Kapsid pada virus yang tersusun dari subunit protein disebut dengan istilah"
        menu:
            "A. Nukleokapsid":
                $ quiz2_score += 0
            "B. Nucleoprotein":
                $ quiz2_score += 0
            "C. Kapsomer":
                $ quiz2_score += 10
            "D. Selubung protein":
                $ quiz2_score += 0

        "9. Berikut ini yang tidak termasuk dalam contoh Nukleokapsid tanpa lapisan yaitu …"
        menu:
            "A. Virus kutil":
                $ quiz2_score += 0
            "B. Adenovirus":
                $ quiz2_score += 0
            "C. Virus influenza":
                $ quiz2_score += 10
            "D. Wart virus":
                $ quiz2_score += 0

        "10. Penyakit di bawah ini disebabkan oleh Virus, kecuali.."
        menu:
            "A. Pneumonia":
                $ quiz2_score += 10
            "B. Morbili":
                $ quiz2_score += 0
            "C. Influenza":
                $ quiz2_score += 0
            "D. Rabies":
                $ quiz2_score += 0

        "Jawaban :
            \n 
            1. D \ \ \ \ 3. B \ \ \ \ 5. D \ \ \ \ 7. B \ \ \ \ 9. C
            \n
            2. B \ \ \ \ 4. D \ \ \ \ 6. D \ \ \ \ 8. C \ \ \ \ 10. A"

        "Nilaiku adalah [quiz2_score]"

    # Check the quiz 1 score
    if quiz2_score >= 75:
        # Win
        $ quick_menu = True
        show bu_senda at center with moveinright:
            ypos 1.2
        sr "Bagaimana sudah selesai ?"
        sk "Sudah bu, dikumpulkan skrng bu ?"
        sr "Iyaa dikumpulkan sekarang"
        sr "Selamat Kelompok yang Nilainya Bagus"
        sr "Kalian bebas melakukan apa saja sampai waktu pelajaran habis"
        sk "Siapp.. bu"
        hide bu senda with dissolve
        # Did he win? Yes.
        #$ quiz2_win = True
        #$ quiz2_lose = False   
    else:
        # Lose
        "Beberapa Soal ada yang ga kuisi. Lumayan susah juga"
        rr "Kamu ga bisa jawabnya ?"
        mc "Kamu tau jawabannya ?"
        menu:
            "Meemberikannya":
                rr "iya, sini dah, aku coba dulu"
                mc "Terima Kasih"
                $ quiz2_score = 0
                jump quiz2
            "Tidak Ingin Memberikannya":
                "Anda gagal sebagai murid"
                "~END~"
                return

    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    wkk "haa Akhirnya Pulang juga"
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Waktunya sudah habis kalian boleh pulang"
    hide bu_senda with moveoutright
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Haa capeknya Pusing lagi"
    mc "...."
    mc "Mau Mampir rumahku lagi ?"
    mg2 "Mauuu.. Enakk makanan gratis"
    mg2 "umm. Maksudku main main sama [cat] hehehhe"
    mc "...."
    mc "Yaudah Ayo, kutunggu di depan gerbang ya"
    mg2 "Okie"
    hide ardana_uni with moveoutright

    scene gerbang_sekolah_sore with dissolve
    skce1 "Aduuhh aku bareng siapa ya ?"
    skce1 "Aku ga dijemput lagi mana rumahku jauh"
    mc "Rumahmu dimana ?"
    skce1 "Astaga bikin kaget saja [mcFirst]"
    skce1 "Ohh rumahku ada di dekatnya Lippo. Kenapa emangnya ?"
    mc "Hmm. si Arda rumahnya dekat situ"
    mc "aku ada saran Bagaimana Kalau kamu pulangnya sama Arda aja soalnya sejalur dan rumahnya didekat situ juga"
    skce1 "Tapi mau ga ya ?"
    mc "Coba aja dulu"
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Lets go Rumahmu [mcFirst]"
    mc "Maaf hari ini ga bisa"
    mg2 "Lahh.. kenapa ?"
    mc "Mungkin Next time saja lah kalau mau main sama [cat]"
    mg2 "Hmm.. Yaudah kalau gitu aku pulang dulu aja dah"
    mc "Wait, ada yang mau ikut kamu pulang juga"
    mg2 "Sapa ?"
    skce1 "Aku Na, boleh Nebeng juga ga ?"
    skce1 "Kebetulan rumahku dekat sama rumahmu sepertinya"
    mg2 "Hmm.. Okelah kalau gitu"
    skce1 "Wah.. Thanks [mg2_Last]"
    mg2 "No Problem"
    mg2 "Kalau gitu aku balik duluan ya [mcFirst]"
    hide ardana_uni with moveoutleft
    mc "oh ok"

    stop music fadeout 1.0 

    play music sore fadein 1.0
    scene depan_rumah_sore 
    mc "Aku Pulang !"

    scene ruang_keluarga_sore with dissolve 
    mc "Ibu Kenapa keliatannya letih banget"
    show mom at center with dissolve:
        ypos 1.15
    mom "Iyaa habis main sama [cat] terus ngadem didepan kipas sama nonton tv"
    mom "Kayaknya [mom] masuk angin"
    mc "Kalau gitu aku yang siapin Makan malam nanti"
    mc "[cat] dimana ?"
    mom "itu tidur di kamarmu"
    mc "oh ok. kalau gitu Ibu istirahat dulu aja"
    mom "Iyaa"
    hide mom with moveoutleft

    scene kamar_sore with dissolve
    mc "Enak banget tidurmu [cat]"
    show cat at center with dissolve:
        ypos 0.8
    cat "Fuurr.. Furrr"
    mc "dahlah Aku tidur juga"
    hide cat with dissolve

    scene kamar_malam with dissolve
    show cat at center with dissolve:
        ypos 0.8
    cat "Meooow Meeooow"
    mc "Hoaam.. dah bangun kau [cat]"
    cat "Nyaaa~"
    mc "Sudah Malam juga kalau gitu aku siapin makanan untuk makan malam"
    hide cat with moveoutleft

    scene dapur_malam with dissolve
    mc "[cat] Makanan mu sudah kusiapin makan sini"
    show cat at center with dissolve:
        ypos 0.8
    cat "Nyaaa Nyaa~"
    hide cat with dissolve
    "Hmm.. Masak apa enaknya ya ? atau aku masak random saja lah"
    "~Beberapa jam kemudian~"
    mc "Ibuu!! sudah siapp makanannya"
    show mom at center with moveinleft:
        ypos 1.15
    mom "Iyaa Nak"
    mc "Gimana [mom] sudah enakan ?"
    mom "Sudah mendingan"
    mc "Ngomong-ngomong ayah kemana ? Lembur lagi ?"
    mom "Iyaa hari ini juga lembur kerjanya"
    mom "Soal ada Projek dari kantornya"
    mc "Hmmm.. Begitu"
    mom "Tumben [mg2_Last] ga kerumah ?"
    mc "...."
    mc "tadi anterin temannya rumahnya jauh juga"
    mom "Hmmm.. Begitu. agak sepi juga disini"
    mom "Ada anak itu jadi heboh hahahha"
    mc "...."
    mom "Oiya,, Nanti setelah selesai biar ibu aja yang beres-beres"
    mc "Ga usah biar aku saja"
    mom "Hmm.. iyadah Ibu Tidur saja kalau gitu"
    "~Makan Malam~"
    mc "Kenyangg sekali"
    mom "Ibu ke kamar dulu ya"
    hide mom with moveoutleft
    mc "Okie, Biar aku yang beresin semuanya"

    scene kamar_malam with dissolve
    mc "Haa.. Leganya. enaknya ngapain ya ?"
    show cat at center with moveoutbottom:
        ypos 0.8
    cat "Meooww"
    mc "Eh ada [cat] sini sini tidur bareng aku"
    mc "Tidur aja kalau gitu benarkan [cat]"
    cat "Nnnyaaa"
    hide cat with dissolve

    stop music fadeout 1.0

    jump day3_Kirana
    return

label day2_Miselia:

    play music pagi fadein 1.0 

    window hide dissolve
    scene sky2 with dissolve
    show day2 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day2 with dissolve
    window show dissolve

    scene kamar with dissolve
    "Sepertinya aku sudah mulai terbiasa dengan pagi hari ini"
    stop sound fadeout 1.0
    play sound burung_terbang fadein 1.0
    window hide dissolve
    pause 3.0
    window show dissolve
    play sound kentut fadein 1.0
    "~Suara Kentut~"
    stop sound fadeout 1.0
    play sound lapar fadein 1.0
    "Aakkhh.. perutku sakit seperti gara-gara kemarin makan terlalu banyak"
    stop sound fadeout 1.0

    scene ruang_keluarga with dissolve
    "Haa.. Leganyaa!!"
    "Hmm.. ada yang bersihin motor"

    scene depan_rumah with dissolve
    mc "Ayah pagi-pagi udah rajin aja nih hehhe"
    show dad_cas at center with dissolve:
        ypos 1.2
    dad "loh, nakkk sudah bangun, kok tumben kamu ga bangkong"
    mc "kan tiap pagi emang bangun pagi kan hhaha"
    mc "kalau gitu aku mandi terus siap siap dulu buat berangkat sekolah"
    dad "Iyaa nak"
    hide dad_cas with dissolve

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Makanan Sudah Siap !!!"
    hide mom with dissolve

    scene depan_rumah with dissolve
    show dad_cas at center with dissolve:
        ypos 1.2
    dad "Iyaa Bu!!"
    hide dad_cas with dissolve

    scene kamar_mandi with dissolve
    play sound mandi fadein 1.0
    mc "Iyaa !!"
    stop sound fadeout 1.0
    "Aku harus bergegas ke kamar untuk memakai baju"

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Sudah selesai siapin untuk ke sekolah ?"
    mc "Sudah bu"
    show dad_cas at center with dissolve:
        xpos 0.6
        ypos 1.2
    dad "[mcFirst] Sini [mom] sudah selesai masak nih, enak lohh!! ayo makan"
    mc "Iyaa yah"
    mc "Bu aku kok lapar banget ya ?"
    mom "Soalnya kemarin kamu langsung tidur dan ga bangun-bangun"
    mom "[mom] ga mau ganggu bangunin juga sepertinya kemarin kamu kecapekan"
    mom "Oiya,, Ibu sudah siapinn juga nasinya"
    mc "Hoo,, jadi begitu. Makasih bu sudah disiapin juga, kalau gitu [mcFirst] makan dulu bu"
    mom "Kemarin, cewe itu siapamu ?"
    dad "Ehhh.. Kemarin [mcFirst] bawa cewe kerumah ?"
    dad "Ho ho ho ho ho"
    mc "...."
    mc "Dia hanya teman sekolah"
    ai "Beneran teman sekolah ? hehehe"
    mc "Iyaa hanya teman sekolah saja, tapi sepertinya dia dulu juga 1 smp denganku"
    mc "Soalnya kemarin [mg2_Last] sempat bertanya masalah bullying"
    mom "Hmm.. jadi begitu"
    mc "Terus dia juga memaksaku dan mengikutiku jalan. Dia ingin mengantarku sampai ke rumah sekalian biar tau rumahku dimana ?"
    mc "Karena merepotkan akhirnya aku terima aja tawarannya"
    mom "Hahaha iya iya, Ibu percaya kok cuma tadi mau bercandain [mcFirst] aja"
    mom "Soalnya, Ibu sempat kaget kalau kamu tiba-tiba bawa teman kerumah"
    dad "Ayah juga kaget loh dengar kamu bawa cewe kemarin"
    mom "Ibu kemarin sempat bahagia kalau kamu mulai sedikit membaik"
    mc "hahahaha Iyaa bu"
    mc "Oiya, [cat] Kemana bu ?"
    mom "Itu Lagi Makan juga"
    mc "Tumben ga kekamarku kayak kemarin kemarinnya"
    dad "Soalnya [dad] kemarin waktu pulang langsung main sama [cat]"
    dad "Ibu juga ikutan hehehe"
    mc "Pagi [cat] makanmu lahap bener"
    show dad_cas at center with moveinleft:
        xpos 0.8
        ypos 1.2
    show mom at center with moveinleft:
        xpos 0.675
        ypos 1.15
        xzoom -1
    show cat_happy at center with moveoutbottom:
        ypos 0.75
    cat "Nyaaa "
    mc "Aku Cuci piring dulu ya bu setelah itu berangkat langsung"
    mom "Oiya, Bekalnya sudah [mom] siapkan ada disini"
    mc 'Iya bu'
    hide mom with dissolve
    hide dad_cas with dissolve
    hide cat_happy with dissolve
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(15.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    mc "Kalau gitu aku berangkat dulu Ayah Ibu"
    show mom at center with dissolve:
        ypos 1.15
    show dad_cas at center with dissolve:
        xpos 0.6
        ypos 1.2
    ai "Iyaa Nak hati hati dijalan"
    mc "Okie"
    mom "Ayah ga berangkat kerja juga ?"
    dad "Bentar lagi, berangkat"
    hide mom with dissolve
    hide dad_cas with dissolve

    stop music fadeout 1.0

    play music jalan_jalan fadein 1.0

    scene gerbang_sekolah with dissolve
    "Hmm.. ada yang mendekatiku mungkin sebaiknya aku diamin saja"
    $ kg = "Ketua Geng Kaya"
    $ ag = "Anggota Gengs Kaya"
    kg "yauda lah ya, ga cocok masuk gengs kita tuh sudah miskin dan tercium bau bau ga mampu"
    kg "Benar ga gengs"
    ag "Yup, Ketua emang bener emang best kaum miskin kek gini mana bisa masuk geng ini. Dih.."
    show nada_uni at center with dissolve:
        xpos 0.7
        zoom 0.5
    na "Oeee [mcFirst] Tunggu aku!!!"
    "Untunglah ada si Bodoh satu ini jadi aku bisa melewati masalah ini"
    show nada_uni at center with dissolve:
        ypos 1.2
        zoom 0.9
    na "Huufftt.. Hufft... \nSiapa itu ? [mcFirst]"
    mc "Ga tau juga aku, Mungkin kakak kelas gabut"
    mc "Abaikan aja"
    na "Hahaha, Okay dah langsung kelas aja kuy"
    kg "Hei,, kalian mengabaikanku yaa awas aja kalian dasar kaum miskin"
    hide nada_uni with moveoutleft

    scene lorong with dissolve
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Ada [mcFirst], aku kesana dulu gaes"
    al "Hooo sudah ada incaran nih"
    mg1 "Ehh Ngga lah. Cuma teman itu"
    al "Iyaa dah kalau gitu sana selamat sukses.. "
    al "Ciiee ciiee"
    mg1 "Ihh Apaan sih ?"
    al "Hahahhaha,, dah dah sana"
    hide miselia_uni with moveoutleft
    "Kayaknya ada yang mau mendekat"
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Baa.."
    mc "Astaga.."
    mg1 "Kaget ga ?"
    mc "Hmmm..."
    show nada_uni at center with dissolve:
        xpos 0.7
        ypos 1.2
    na "Lahh,, ada kamu [mg1_Last] aku ikutan kaget juga njirr"
    mg1 "Hehehe maaf maaf.. "
    mg1 "Gitu aja marah \nTe hee"
    hide miselia_uni with moveoutleft
    hide nada_uni with moveoutleft

    scene kelas with dissolve
    show nada_uni at center with moveinright:
        xpos 0.7
        ypos 1.2
    na "Kuy Duduk"
    hide nada_uni with moveoutleft
    mc "Duduk disebelahku lagi ?"
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Ga suka ?"
    show nada_uni at center with moveinright:
        xpos 0.7
        ypos 1.2
    na "Akhir Akhir ini [mg1_Last] duduk ama [mcFirst] mulu"
    na "Ciiiee ciiee ada apa ini ?"
    mc "Entahlah"
    mg1 "padahal baru 2 hari"
    mc "Hmmm..."
    mg1 "Mending sekarang kita belajar deh sampai bel berbunyi hahaha"
    hide nada_uni with dissolve
    hide miselia_uni with dissolve
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
    show bu_senda at right with moveinleft:
        xpos 0.9
        ypos 1.2
    $ _skipping = False
    "~Materi Fungi Lanjutan~"
    window hide dissolve
    stop music fadeout 1.0
    #Video Fungi
    show cara_hidup behind sr at center with dissolve:
        xpos 0.3
        ypos 0.6
        zoom 0.5
    $ renpy.pause(39.5, hard=True)
    hide cara_hidup with dissolve
    window show dissolve
    $ _skipping = True
    play music jalan_jalan2 fadein 1.0
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Sudah bel Anak- anak kalau gitu selamat istirahat"
    hide bu_senda with moveoutright
    sk "Yeay sudah istirahat"
    al "[mg1_Last] ga pergi ke kantin ?"
    show miselia_uni at center with dissolve:
        ypos 1.2
    mg1 "Iyaa bentar"
    mg1 "[mcFirst] ga mau pergi ke kantin juga ?"
    mc "Ga usah aku soalnya bawa bekal"
    mg1 "dihh mauu buatan Ibumu"
    mc "Emohh.. sana ikut temanmu ke kantin"
    hide miselia_uni with moveoutright
    show nada_uni at center with moveinright:
        ypos 1.2
    na "Bro Ikutan juga bareng kita ? [skco1] dan [wkk]"
    mc "Ga, duluan dah"
    na "Oke kalau begitu, Lets go kawand"
    wkk "Okay ma brader"
    hide nada_uni with moveoutright
    "Isi Bekalnya lumayan banyak juga"
    "Nyam Nyam Nyam~"
    "Kenyang juga, aku pikir akan porsi kecil ternya porsi besar"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Fuhaah Kenyangnyaa~"
    hide miselia_uni with moveoutleft
    show nada_uni at center with moveinright:
        ypos 1.2
    na "Aku Masih kurang"
    wkk "Hahaha Bisa aja kamu"
    skco1 "Sama sih aku masih kurang soalnya aku ga sarapan sama sekali"
    hide nada_uni with moveoutleft
    show nada_uni at center with moveinright:
        ypos 1.2
    na "Ini lur kubawakan Roti Sosis"
    mc "Gratis Nih ?"
    na "Bayar dong"
    mc "Ok ok"
    na "Ehh.. gratis gratis aku cuma bercanda hahahah"
    mc "Nih uangnya ambil aja"
    na "Okelah kalau gitu hehehhe"
    show miselia_uni at center with moveinleft:
        ypos 1.2
    show nada_uni at center with moveinleft:
        xpos 0.7
        ypos 1.2
    mg1 "Punyaku mana ?"
    na "ga ada lah ya beli sendiri dong"
    hide miselia_uni
    show miselia_uni_emosi at center:
        ypos 1.2
    mg1 "Dih Curang"
    mc "pfft.."
    mg1 "Ihh Ngeledek yaa"
    mc "ga sama sekali"
    na "Hahah lucu sekali melihat kalian berdua. yaudah aku kembali ke bangku dulu"
    na "Ntar Bu Senda keburu datang"
    hide miselia_uni_emosi with dissolve
    hide nada_uni with moveoutright

    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat siang anak-anak. Ibu punya soal buat kalian dikerjakan yaa! nanti ibu tinggal ke ruang guru soalnya ada rapat"
    $ kk = "Ketua Kelas"
    sr "oiyaa anak anak, kali ini ibu akan membentuk kalian kelompok, tapi sebangku aja ya biar gampang"
    kk "bu apakah sebaiknya di kocok sajaa biar Adil"
    sr "bagaimana apa kalian setuju?"
    sk "Setujuu Bu!! Biar lebih mengenal karakterisitik semuanya bu"
    "Padahal Aku tidak setuju tapi karena kurang suara apa boleh buat"
    kk "Bikin potongan kertas sesuai Absen bu Nanti anak-anak mengambilnya nomor yang diambil akan berkelompok"
    kk "Setelah itu yang sudah mendapatkan kelompok tidak perlu mengambil nomornya lagi bu"
    sr "Tapi nanti anak-anak nomor absen belakang tidak akan kebagian mengambil juga"
    sr "Aha.. Ibu punya ide kita mulai dari nomor absen awal yang mengambil selanjutnya nomor absen terakhir yang mengambil"
    sr "Bagaimana anak-anak ?"
    skco1 "Boleh juga itu bu"
    sr "Okee.. Laksanakan"
    sk "Yes Mam"
    hide bu_senda with dissolve
    "Ahh Kelompok Merepotkan sekali"
    "Moga dapat orang yang ga merepotkan"
    $ rr = "Rere"
    rr "aku sekelompok sama nomor 3 , siapa absenn nomor 3 ?"
    mc "Aku"
    rr "Oh Ok"
    mc "...."
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Kamu kelompokan sama [rr] lur. orangnya itu Nakal, Males, Sok Cool"
    na "tapi cantik juga sih hehehe"
    mc "Bodoh amat ama yang namanya cantik"
    na "aku dengar-dengar gitu sih dari teman yang 1 SMP dengannya"
    na "Oiyaa, orangnya juga pintar soalnya sering juara aku denger dengernya gitu"
    mc "dahlah. nth ini beruntung atau merugikanku"
    show nada_uni at center with moveinright:
        xpos 0.7
        ypos 1.2
    show miselia_uni at center with dissolve:
        ypos 1.2
    mg1 "hussh!!"
    "~Berlanjutlah pemilihan kelompok~" 
    hide nada_uni with dissolve
    hide miselia_uni with dissolve

    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Sudah dapat kelompoknya masing masing kan ya ?"
    sk "Sudah semuanya bu ga ada yang jomblo"
    sr "Kalau gitu Ibu ke ruang guru dulu ya. Soalnya jangan lupa dikerjakan loh"
    sr "kalau ada yang ga ngerjakan ada hukumannya"
    sk "Baik buu"
    hide bu_senda with moveoutright
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Aku kelompokan sama Meta anjir, kamu tau sendiri ceriwisnya minta ampun kan itu kzl .. "
    $ mt = "Meta"
    show nada_uni at center with moveinright:
        xpos 0.7
        ypos 1.2
    show miselia_uni at center with dissolve:
        ypos 1.2
    mg1 "Hahaha sabar"
    $ tmn_mg2 = "Filo"
    al "[mg1_Last] Kelompokan sama siapa kamu ?"
    mg1 "Aku sama [skce2] kalau kamu sama siapa [al]?"
    al "Aku sama [kk]"
    skce1 "Ihh.. enak banget"
    mc "Dah dah biar kelar duduk sekelompok sekarang"
    hide miselia_uni with dissolve
    hide nada_uni with dissolve
    "Mungkin aku sebaiknya kesana"
    rr "...."
    "Ternyata cukup merepotkan juga ya"
    mc "Ayo kerjakan tugasnya bersama"
    rr "ha?kamu aja sono yang ngerjakan, males aku tu, cape mau tidur aja"
    mc "Ini tugas kelompok"
    rr "Serah serah aku lah"
    mc "...."

    "~SOAL~"
    #Initialize score
    $ quiz_fungi2_score = 0

    label quiz_fungi2:
        $ quick_menu = False

        "1. Ciri-­ciri Deuteromycotina adalah…"
        menu:
            "A. reproduksi seksual dengan spora":
                $ quiz_fungi2_score += 0
            "B. memiliki askus yang menghasilkan askospora":
                $ quiz_fungi2_score += 0
            "C. Hifanya bercabang cabang, tidak bersekat":
                $ quiz_fungi2_score += 0
            "D. reproduksi aseksual dengan pembentukan konidia":
                $ quiz_fungi2_score += 10

        "2. Dibawah ini yang tidak masuk dalam golongan Zygomycotina adalah ..."
        menu:
            "A. Penicillium sp.":
                $ quiz_fungi2_score += 10
            "B. Glomus sp":
                $ quiz_fungi2_score += 0
            "C. Cunninghamella sp":
                $ quiz_fungi2_score += 0
            "D. Pilobolus sp":
                $ quiz_fungi2_score += 0

        "3. Penelitian tentang jamur sangat banyak diminati oleh para, penelitian tersebut termasuk ke dalam bidang ilmu ..."
        menu:
            "A. botani":
                $ quiz_fungi2_score += 0
            "B. fisiologi":
                $ quiz_fungi2_score += 0
            "C. planktonologi":
                $ quiz_fungi2_score += 0
            "D. mikologi":
                $ quiz_fungi2_score += 10

        "4. Jamur Zygomicota menyerap makanannya menggunakan …."
        menu:
            "A. sporangium":
                $ quiz_fungi2_score += 0
            "B. seluruh bagian tubuh":
                $ quiz_fungi2_score += 0
            "C. rizoid":
                $ quiz_fungi2_score += 10
            "D. stolon":
                $ quiz_fungi2_score += 0
            
        "5. Jamur yang memiliki hifa tidak bersekat termasuk dalam kelompok jamur ..."
        menu:
            "A. Zygomycota":
                $ quiz_fungi2_score += 10
            "B. Basidiomycota":
                $ quiz_fungi2_score += 0
            "C. Deuteromycota":
                $ quiz_fungi2_score += 0
            "D. Ascomycota":
                $ quiz_fungi2_score += 0

        "6. Hifa pada Oomycota mempunyai ciri …."
        menu:
            "A. reproduksi generatif dengan fertilisasi":
                $ quiz_fungi2_score += 10
            "B. hidup di darat":
                $ quiz_fungi2_score += 0
            "C. tidak memiliki selulosa":
                $ quiz_fungi2_score += 0
            "D. memiliki senositik":
                $ quiz_fungi2_score += 0

        show fungid2 at truecenter with dissolve
        "7. Gambar diatas ini merupakan fungi dari jenis…."
        menu:
            "A. Volvariella volvacea":
                $ quiz_fungi2_score += 0
            "B. Rhizopus stolonifer":
                $ quiz_fungi2_score += 10
            "C. Saccharomyces cerevisiae":
                $ quiz_fungi2_score += 0
            "D. Mocor mucedo":
                $ quiz_fungi2_score += 0
        hide fungid2 with dissolve

        "Spesies Fungi yang berkembang biak dengan membentuk spora di askus dan bermanfaat dalam industri makanan adalah ..." (multiple=2)
        "8. Berikut ini adalah jenis fungi yang berperan dalam kehidupan manusia
        \n   
                (1) Aspergillus wentii
                (5) Rhizopus oryzae
                \n
                (2) Saccharomyces cerevisiae
                (4) Volvariella volvacea
                \n
                (3) Penicillium chrysogenum
                (6) Penicillium camemberti" (multiple=2)
        menu:
            "A. 4, 5 dan 6":
                $ quiz_fungi2_score += 0
            "B. 2, 3 dan 4":
                $ quiz_fungi2_score += 0
            "C. 1, 3 dan 4":
                $ quiz_fungi2_score += 0
            "D. 1, 2 dan 6":
                $ quiz_fungi2_score += 10

        "9. Pada proses pembuatan roti, pemberian ragi membuat adonan menjadi mengembang. Hal ini disebabkan oleh ..."
        menu:
            "A. tepung dan ragi bereaksi dan menghasilkan O2":
                $ quiz_fungi2_score += 0
            "B. ragi merupakan fungi dari kelompok Ascomycota":
                $ quiz_fungi2_score += 0
            "C. hasil fermentasi glukosa menghasilkan CO2 yang dapat mengembangkan adonan":
                $ quiz_fungi2_score += 10
            "D. Pemanasan Menyebabkan radi dan tepung mengembang":
                $ quiz_fungi2_score += 0

        "10. Dinding sel pada jamur Zygomycota mengandung zat …."
        menu:
            "A. Hidup di daerah lembab":
                $ quiz_fungi2_score += 0
            "B. Bisa membuat makanan sendiri":
                $ quiz_fungi2_score += 0
            "C. Bergantung pada substrat":
                $ quiz_fungi2_score += 10
            "D. Mempunyai klorofil":
                $ quiz_fungi2_score += 0

        "Jawaban :
            \n
            1. D \ \ \ \ 3. D \ \ \ \ 5. A \ \ \ \ 7. B \ \ \ \ 9. C
            \n
            2. A \ \ \ \ 4. C \ \ \ \ 6. A \ \ \ \ 8. D \ \ \ \ 10. C"

        "Nilaiku adalah [quiz_fungi2_score]"

    # Check the quiz 1 score
    if quiz_fungi2_score >= 75:
        # Win
        $ quick_menu = True
        "Mudah Sekali"
        # Did he win? Yes.
        #$ quiz_fungi2_win = True
        #$ quiz_fungi2_lose = False   
    else:
        # Lose
        rr "Kamu kelihatanya kesusahan !"
        mc "Iyaa"
        rr "Sini Kasih soalnya"
        menu:
            "Kasih":
                $ quiz_fungi2_score = 0
                jump quiz_fungi2
            "Tidak kasih":
                "Anda gagal sebagai murid"
                "~END~"
                return

    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    wkk "haa Akhirnya Pulang juga"
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Waktunya sudah habis kalian boleh pulang"
    hide bu_senda with moveoutright
    show miselia_uni at center with dissolve:
        ypos 1.2
    mg1 "Haa capeknya Pusing lagi"
    mc "...."
    mc "Mau Mampir rumahku lagi ?"
    mg1 "Mauuu.. Enakk makanan gratis"
    mg1 "umm. Maksudku main main sama [cat] hehehhe"
    mc "...."
    mc "Yaudah Ayo, kutunggu di depan gerbang ya"
    mg1 "Okie"
    hide miselia_uni with moveoutright

    scene gerbang_sekolah_sore with dissolve
    skce1 "Aduuhh aku bareng siapa ya ?"
    skce1 "Aku ga dijemput lagi mana rumahku jauh"
    mc "Rumahmu dimana ?"
    skce1 "Astaga bikin kaget saja [mcFirst]"
    skce1 "Ohh rumahku ada di dekatnya Lippo. Kenapa emangnya ?"
    mc "Hmm. si Meiris rumahnya dekat situ"
    mc "aku ada saran Bagaimana Kalau kamu pulangnya sama Meiris aja soalnya sejalur dan rumahnya didekat situ juga"
    skce1 "Tapi mau ga ya ?"
    mc "Coba aja dulu"
    show miselia_uni at center with moveinright:
        ypos 1.2
    mg1 "Lets go Rumahmu [mcFirst]"
    mc "Maaf hari ini ga bisa"
    mg1 "Lahh.. kenapa ?"
    mc "Mungkin Next time saja lah kalau mau main sama [cat]"
    mg1 "Hmm.. Yaudah kalau gitu aku pulang dulu aja dah"
    mc "Wait, ada yang mau ikut kamu pulang juga"
    mg1 "Sapa ?"
    skce1 "Aku Na, boleh Nebeng juga ga ?"
    skce1 "Kebetulan rumahku dekat sama rumahmu sepertinya"
    mg1 "Hmm.. Okelah kalau gitu"
    skce1 "Wah.. Thanks [mg1_Last]"
    mg1 "No Problem"
    mg1 "Kalau gitu aku balik duluan ya [mcFirst]"
    hide miselia_uni with moveoutleft
    mc "oh ok"

    stop music fadeout 1.0 

    play music sore fadein 1.0
    scene depan_rumah_sore 
    mc "Aku Pulang !"

    scene ruang_keluarga_sore with dissolve 
    mc "Ibu Kenapa keliatannya letih banget"
    show mom at center with dissolve:
        ypos 1.15
    mom "Iyaa habis main sama [cat] terus ngadem didepan kipas sama nonton tv"
    mom "Kayaknya [mom] masuk angin"
    mc "Kalau gitu aku yang siapin Makan malam nanti"
    mc "[cat] dimana ?"
    mom "itu tidur di kamarmu"
    mc "oh ok. kalau gitu Ibu istirahat dulu aja"
    mom "Iyaa"
    hide mom with moveoutleft

    scene kamar_sore with dissolve
    mc "Enak banget tidurmu [cat]"
    show cat at center with dissolve:
        ypos 0.8
    cat "Fuurr.. Furrr"
    mc "dahlah Aku tidur juga"
    hide cat with dissolve

    scene kamar_malam with dissolve
    show cat at center with dissolve:
        ypos 0.8
    cat "Meooow Meeooow"
    mc "Hoaam.. dah bangun kau [cat]"
    cat "Nyaaa~"
    mc "Sudah Malam juga kalau gitu aku siapin makanan untuk makan malam"
    hide cat with moveoutleft

    scene dapur_malam with dissolve
    mc "[cat] Makanan mu sudah kusiapin makan sini"
    show cat at center with dissolve:
        ypos 0.8
    cat "Nyaaa Nyaa~"
    hide cat with dissolve
    "Hmm.. Masak apa enaknya ya ? atau aku masak random saja lah"
    "~Beberapa jam kemudian~"
    mc "Ibuu!! sudah siapp makanannya"
    show mom at center with moveinleft:
        ypos 1.15
    mom "Iyaa Nak"
    mc "Gimana [mom] sudah enakan ?"
    mom "Sudah mendingan"
    mc "Ngomong-ngomong ayah kemana ? Lembur lagi ?"
    mom "Iyaa hari ini juga lembur kerjanya"
    mom "Soal ada Projek dari kantornya"
    mc "Hmmm.. Begitu"
    mom "Tumben [mg2_Last] ga kerumah ?"
    mc "...."
    mc "tadi anterin temannya rumahnya jauh juga"
    mom "Hmmm.. Begitu. agak sepi juga disini"
    mom "Ada anak itu jadi heboh hahahha"
    mc "...."
    mom "Oiya,, Nanti setelah selesai biar ibu aja yang beres-beres"
    mc "Ga usah biar aku saja"
    mom "Hmm.. iyadah Ibu Tidur saja kalau gitu"
    "~Makan Malam~"
    mc "Kenyangg sekali"
    mom "Ibu ke kamar dulu ya"
    hide mom with moveoutleft
    mc "Okie, Biar aku yang beresin semuanya"

    scene kamar_malam with dissolve
    mc "Haa.. Leganya. enaknya ngapain ya ?"
    show cat at center with moveoutbottom:
        ypos 0.8
    cat "Meooww"
    mc "Eh ada [cat] sini sini tidur bareng aku"
    mc "Tidur aja kalau gitu benarkan [cat]"
    cat "Nnnyaaa"
    hide cat with dissolve

    stop music fadeout 1.0

    jump day3_Miselia

    return

label day2_Airin:

    play music pagi fadein 1.0

    window hide dissolve
    scene sky2 with dissolve
    show day2 at center with dissolve:
        ypos 0.55
    with dissolve
    with Pause(3)
    play sound burung_pagi fadein 1.0
    hide day2 with dissolve
    window show dissolve

    scene kamar with dissolve
    "Sepertinya aku sudah mulai terbiasa dengan pagi hari ini"
    stop sound fadeout 1.0
    play sound burung_terbang fadein 1.0
    window hide dissolve
    pause 3.0
    window show dissolve
    "Sebaiknya aku mandi dulu"

    scene kamar_mandi with dissolve
    play sound mandi fadein 1.0
    "Segarnyaa mandi pagi"
    stop sound fadeout 1.0

    scene kamar with dissolve
    "tinggal ganti baju terus siapin tas lalu sarapan dan ngasih makan [cat]"

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Pagi, [mcFirst] wihh dah siap saja"
    mc "hahha iya bu.. Oiya, [dad] kemana bu ? [cat] juga ga kelihatan"
    mc "Mulai tadi ga kelihatan [dad] sama sekali"
    mom "[dad] tadi berangkat pagi sepertinya ada pekerjaan banyak dari kantornya"
    mom "Kalau [cat] lagi makan itu"
    mc "Dasar [cat] kucari-cari ahhaha ternyata disini dah makan duluan.. ku kelitiki hayooo"
    hide mom with dissolve
    show cat at center with dissolve:
        ypos 0.775
    cat "Meeoow Meoow Meoww"
    mc "hahaha.. dah dah lanjut aja makannya"
    cat "Meooww"
    hide cat with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Nasinya sudah [mom] siapkan di meja"
    mc "Terima kasih bu"
    mom "Bekal ini lagi ibu siapin"
    mc "Iyaa bu"
    hide mom with dissolve
    mc "Kenyangnyaa~"
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(15.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    mc "Berangkat dulu, bekalnya yang ini kan ?"
    show mom at center with dissolve:
        ypos 1.15
    mom "Iyaa,, bentar ini uang sakumu"
    $ money += 30000
    mc "Terima kasih bu"
    mom "Hati-hati dijalan"
    mom "Ayo [cat] main sama [mom] Hahahaha"
    hide mom with dissolve

    stop music fadeout 1.0
    play music jalan_jalan fadein 1.0
    scene gerbang_sekolah with dissolve
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Oee Brooo tungguin"
    mc "Okk.."
    na "Tumben ga sambil jalan"
    mc "Enakan lari saja sih hahha"
    na "Lah.. Hahhahaha"
    hide nada_uni with dissolve
    
    scene kelas with dissolve
    "Lebih baik aku belajar saja sembari nunggu bel masuk"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    "Umm.. Gada gurunya sepertinya"
    "~2 Jam kemudian~"
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    "Ternyata benar emang ga ada gurunya"
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Ikut ke kantin bro ?"
    mc "Ga,, aku makan disini aja aku bawa bekal soalnya"
    na "okk kalau gitu mau titip ?"
    mc "ga usah"
    na "Okk aku duluan"
    hide nada_uni with moveoutright
    "~15 Menit kemudian~"
    mc "Kenyangnyaa Fuuhh.."
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Maaf, tadi Bu Senda ada rapat jadi pagi tadi tidak ada jam pelajaran"
    sr "Selamat Siang anak-anak sudah kah siap untuk belajar hari ini ?"
    sk "Tidak bu!!"
    sr "Kalau gitu tidur aja yaa "
    wkk "Ihh Bu Senda.. Kami Bercanda bu"
    sr "Sama Ibu juga Hahahaha"
    sr "oiyaa anak anak, kali ini ibu akan membentuk kalian kelompok, tapi sebangku aja ya biar gampang"
    $ kk = "Ketua Kelas"
    kk "bu apakah sebaiknya di kocok saja biar Adil ?"
    sr "bagaimana apa kalian setuju?"
    sk "Setujuu Bu!! Biar lebih mengenal karakterisitik semuanya bu"
    "Padahal Aku tidak setuju tapi karena kurang suara apa boleh buat"
    kk "Bikin potongan kertas sesuai Absen bu Nanti anak-anak mengambilnya nomor yang diambil akan berkelompok"
    kk "Setelah itu yang sudah mendapatkan kelompok tidak perlu mengambil nomornya lagi bu"
    sr "Tapi nanti anak-anak nomor absen belakang tidak akan kebagian mengambil juga"
    sr "Aha.. Ibu punya ide kita mulai dari nomor absen awal yang mengambil selanjutnya nomor absen terakhir yang mengambil"
    sr "Kalau yang sudah dapat kelompok ga boleh mengambil lagi"
    sr "Bagaimana anak-anak ?"
    skco1 "Boleh juga itu bu"
    sr "Okee.. Laksanakan"
    sk "Yes Mam"
    hide bu_senda with dissolve
    "Ahh Kelompok Merepotkan sekali"
    "Moga dapat orang yang ga merepotkan"
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Umm.. yang nomor absennya 15"
    mc "Aku"
    mg3 "Ohh... okk"
    hide airin_uni with dissolve
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Wiihh,, sekolompokan sama [mg3_First]"
    na "Cantik sih hahahha soalnya mulai kemarin kamu lihatin dia mulu jadi kayak ada sesuatu nih hahaha"
    mc "Ga juga"
    mc "Btw, Situ sama siapa ?"
    na "Aku kelompokan sama Meta anjir, kamu tau sendiri ceriwisnya minta ampun kan itu kzl .. "
    hide nada_uni with dissolve
    "~Berlanjutlah pemilihan kelompok~" 
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Sudah dapat kelompoknya masing masing kan ya ?"
    sr "Kalau gitu silahkan dikerjakan"
    sk "Baik buu"
    hide bu_senda with dissolve
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Ayo kerjakan tugasnya bersama"
    hide airin_uni with dissolve
    mc "Okk"

    stop music fadeout 1.0
    play music jalan_jalan2 fadein 1.0
    "~SOAL~"
    #Initialize score
    $ quiz2_klasifikasi_score = 0

    label quiz2_klasifikasi:
        $ quick_menu = False

        "1. Di dalam klasifkasi, jeruk bali (Citrus maxima), jeruk nipis (Citrus aurum tifolia), dan jeruk keprok (Citrus nobilis) termasuk dalam satu kelompok, yaitu pada tingkat …."
        menu:
            "A. spesies":
                $ quiz2_klasifikasi_score += 0
            "B. genus":
                $ quiz2_klasifikasi_score += 10
            "C. familia":
                $ quiz2_klasifikasi_score += 0
            "D. ordo":
                $ quiz2_klasifikasi_score += 0

        "2. Tingkatan takson paling rendah yang menempatkan jagung dan padi dalam satu kedudukan sistematik adalah …."
        menu:
            "A. genus":
                $ quiz2_klasifikasi_score += 0
            "B. kelas":
                $ quiz2_klasifikasi_score += 10
            "C. ordo":
                $ quiz2_klasifikasi_score += 0
            "D. familia":
                $ quiz2_klasifikasi_score += 0 

        "3. Kucing, anjing, dan harimau memiliki kesamaan antara lain struktur gigi dan jenis makanannya. Oleh karena itu, hewan tersebut dikelompokkan dalam satu takson yang sama, yaitu …."
        menu:
            "A. familia":
                $ quiz2_klasifikasi_score += 0
            "B. flum":
                $ quiz2_klasifikasi_score += 0
            "C. ordo":
                $ quiz2_klasifikasi_score += 10
            "D. genus":
                $ quiz2_klasifikasi_score += 0

        "\n \n \n Cara penulisan binomial nomenklatur yang benar adalah …."(multiple=2)
        "4. Berikut adalah beberapa cara penulisan ilmiah:
            \n
            1) Terdiri dari dua kata bahasa Latin atau yang dilatinkan.
            \n
            2) Kata pertama dimulai dengan huruf besar, kata kedua dimulai dengan huruf kecil.
            \n
            3) Penulisan kata pertama dengan kedua disambung.
            \n
            4) Penulisan kata pertama dengan kedua tidak disambung.
            \n
            5) Ditulis dengan cetak miring atau digarisbawahi secara terputus.
            \n
            6) Nama penemunya tidak boleh dicantumkan." (multiple=2)
        menu:
            "A. 1)-2)-3)-5)":
                $ quiz2_klasifikasi_score += 0
            "B. 1)-2)-3)-6)":
                $ quiz2_klasifikasi_score += 0
            "C. 1)-2)-4)-5)":
                $ quiz2_klasifikasi_score += 10
            "D. 2)-3)-5)-6)":
                $ quiz2_klasifikasi_score += 0
            
        "5. Untuk melestarikan keturunannya maka makhluk hidup perlu melakukan.."
        menu:
            "A. Perkembangbiakan":
                $ quiz2_klasifikasi_score += 10
            "B. Gerak":
                $ quiz2_klasifikasi_score += 0
            "C. Perkembangan":
                $ quiz2_klasifikasi_score += 0
            "D. Pertumbuhan":
                $ quiz2_klasifikasi_score += 0

        "6. Faktor dari dalam yang mempengaruhi pertumbuhan dan perkembangan manusia adalah.."
        menu:
            "A. Makanan":
                $ quiz2_klasifikasi_score += 0
            "B. Cahaya matahari":
                $ quiz2_klasifikasi_score += 0
            "C. Gen":
                $ quiz2_klasifikasi_score += 10
            "D. Air":
                $ quiz2_klasifikasi_score += 0

        "7. Hal berikut yang dilakukan oleh semua makhluk hidup kecuali..."
        menu:
            "A. Peka terhadap rangsang":
                $ quiz2_klasifikasi_score += 0
            "B. Bernapas":
                $ quiz2_klasifikasi_score += 0
            "C. Tumbuh":
                $ quiz2_klasifikasi_score += 0
            "D. Fotosintesis":
                $ quiz2_klasifikasi_score += 10

        "8. Zat sisa yang dikeluarkan oleh tumbuhan pada waktu bernapas adalah..."
        menu:
            "A. Co2 dan H2O":
                $ quiz2_klasifikasi_score += 0
            "B. CO2 dan O2":
                $ quiz2_klasifikasi_score += 10
            "C. CO2 dan zat gula":
                $ quiz2_klasifikasi_score += 0
            "D. Zat tepung dan O2":
                $ quiz2_klasifikasi_score += 0

        "9. Pemberian tata nama ganda diatur dalam Kode Internasional yang disebut dengan …. "
        menu:
            "A. binomial nomenklatur":
                $ quiz2_klasifikasi_score += 10
            "B. pengelompokan":
                $ quiz2_klasifikasi_score += 0
            "C. kunci determinasi":
                $ quiz2_klasifikasi_score += 0
            "D. klasifikasi":
                $ quiz2_klasifikasi_score += 0

        "10. Penulisan nama ilmiah yang benar di bawah ini adalah..."
        menu:
            "A. rhizopus oligosporus":
                $ quiz2_klasifikasi_score += 0
            "B. Rhizopus Oligosporus":
                $ quiz2_klasifikasi_score += 0
            "C. Rhizopus oligosporus":
                $ quiz2_klasifikasi_score += 10
            "D. rhizopus Oligosporus":
                $ quiz2_klasifikasi_score += 0

        "Jawaban : 
            \n
            1. B \ \ \ \ 3. C \ \ \ \ 5. A \ \ \ \ 7. D \ \ \ \ 9. A
            \n  
            2. B \ \ \ \ 4. C \ \ \ \ 6. C \ \ \ \ 8. B \ \ \ \ 10. C"

        "Nilaiku adalah [quiz2_klasifikasi_score]"

    # Check the quiz 1 score
    if quiz2_klasifikasi_score >= 75:
        # Win
        $ quick_menu = True
        show bu_senda at center with dissolve:
            ypos 1.2
        sr "Selamat Bagi yang Nilainya Bagus"
        sr "Kalian bebas melakukan apa saja sampai waktu pelajaran habis"
        hide bu_senda with dissolve
        # Did he win? Yes.
        #$ quiz2_klasifikasi_win = True
        #$ quiz2_klasifikasi_lose = False   
    else:
        # Lose
        show bu_senda at center with dissolve:
            ypos 1.2
        sr "Bagi yang Nilainya jelek bisa mengulang lagi"
        hide bu_senda with dissolve
        menu:
            "Mengulang Lagi":
                $ quiz2_klasifikasi_score = 0
                jump quiz2_klasifikasi
            "Tidak Ingin Mengulang":
                "Anda gagal sebagai murid"
                "~END~"
                return
        # Did he win? No.
        #$ quiz2_klasifikasi_win = False
        #$ quiz2_klasifikasi_lose = True

    #if quiz2_klasifikasi_win:
        #jump happylove
        
    #if quiz2_klasifikasi_lose:
        #jump breakup
    
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Oiyaa, aku boleh tanya ?"
    mc "Apa itu ?"
    mg3 "Kemarin, kamu ada di atap sekolah ?"
    mc "Ga"
    mg3 "Berarti aku salah orang tapi kamu kenapa selalu pulang akhir ?"
    mc "Malas karena terlalu ramai"
    mc "Btw, Kenapa kamu selalu bernyanyi di atap ?"
    mg3 "Itu ada alasannya"
    mc "Latihan Eskkul ?"
    mg3 "Bukan,, ada deh"
    mc "Soalnya suaramu bagus"
    mg3 "//// Bisa bisanya hahahah ga bagus-bagus amat kok"
    mc "Ga boleh gitu, tpi kenyataannya emang bagus"
    mg3 "Aku baru tau loh kalau kita ternyata sekelas"
    mc "Pasti kamu mengabaikan perkenalan di kelas ya"
    mg3 "Enak saja, aku merhatikan loh"
    mc "Tuh,, buktinya"
    mg3 "Akkhh.. kamu juga"
    mc "Kok bisa ?"
    mg3 "Waktu ketemu kok ga tau kalau itu aku sekelas sama kamu"
    mc "Ummm.. ga, aku sebenarnya sudah tahu hahahaha"
    mg3 "bohong"
    mc "Sudah sudah tugasnya dikumpulkan dulu aja"
    mg3 "Diihh,, mengalihkan pembicaraan"
    hide airin_uni with dissolve
    mc "Ini bu tugasnya"
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Terima kasih [mcFirst]"
    sr "Semuanya apa sudah ?"
    sk "Sudah bu"
    sr "Kalau gitu Bu Senda ke ruang guru. Jangan, ramai ya kalian bebas melakukan apapun tapi jangan ramai tunggu sampai bel pulang"
    sk "Siapp bu"
    sr "Ketua Kelas, Kelasnya di atur ya"
    kk "Iyaa bu"
    sr "Kalau gitu sekian dari Bu Senda"
    hide bu_senda with moveoutright
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Apa kamu nanti pulang terakhir lagi ?"
    mc "Iyaa,, Kenapa ?"
    mg3 "Mau dengarin aku bernyanyi ? Sejujurnya aku sedikit malu hahaha"
    hide airin_uni with dissolve
    mc "Boleh.."
    play sound bel_sekolah fadein 1.0
    "~Ding Dong~"
    stop sound fadeout 1.0
    "Hmmm.. Mendengarkan dia bernyanyi kah.. Baiklah menunggu kelas sepi saja"
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Bro,, Duluan"
    hide nada_uni with moveoutright
    mc "Okk"
    "~20 Menit Kemudian~"
    "Seperti sudah ga terlalu ramai, Apa aku langsung pulang saja ?"
    menu:
        "Mampir ke Atap":
            "Baiklah, Kalau gitu aku mampir dulu liat dia"
        "Langsung Pulang":
            "Kalau gitu aku pulang saja, buang - buang waktu lihat dia lagi"
            scene kamar_malam with dissolve
            "Huwaa,, Capeknya sekolah lebih baik aku tidur saja"
            "~Besoknya~"
            mg3 "Kamu Mengingkari Janji"
            mg3 "Kamu pembohong"
            mc "Ehe"
            mg3 "Ehe ga ada akhlakmu a"
            mg3 "Dahlah"
            "~END~"
            return
    stop music fadeout 1.0
    play music bersamamu fadein 1.0
    scene atap_sore with dissolve
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Kamu datang beneran yaa hahah"
    mc "Namanya, diminta datang kalau gitu aku pulang dulu"
    hide airin_uni with dissolve
    show airin_kaget_uni at center:
                ypos 1.2
    mg3 "Ehh.. Eh.. tunggu dulu"
    mg3 "Ihhh... Ngambulan"
    hide airin_kaget_uni
    mc "Ga juga.."
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Aku Mulaii.. dengarkan lohh yaa"
    mc "Iyaa"
    hide airin_uni with dissolve
    stop music fadeout 1.0
    $ _skipping = False
    play music nyanyi fadein 1.0
    "~Mendengarkan~"
    window hide dissolve
    $ renpy.pause(15.0, hard=True)
    window show dissolve
    $ _skipping = True
    "Baguss.. Enak didengerin"
    stop music fadeout 1.0
    play music kesepian fadein 1.0
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Gimana gimana ?"
    mc "Hmm.. Bagus.. Jadi tenang pas dengerinnya.."
    mc "Kamu anak Padsu ?"
    mg3 "Ahh... bukan.."
    mc "Terus ? kamu artist idol gitu ?"
    hide airin_uni
    show airin_jalan_uni at center
    mg3 "Ahh.. itu ada alasannya, kalau gitu aku pulang dulu"
    hide airin_jalan_uni with moveoutleft
    mc "Hmmmm..."

    stop music fadeout 1.0
    play music sore fadein 1.0
    scene depan_rumah_sore with dissolve
    mc "Aku Pulang !!"

    scene ruang_keluarga_sore with dissolve
    mc "Buu.. aku langsung tidur dulu"
    show mom at center with dissolve:
        ypos 1.2
    mom "Iyaa.. jangan lupa makan"
    hide mom with dissolve
    mc "Iyaa bu"

    scene kamar_sore with dissolve
    "Kenapa dia tiba-tiba langsung pulang ya ? Apa sama sepertiku ? yang dulunya ada masalah"
    "Dahlah dipikirkan terus-terusan aku bisa jadi pusing"

    scene kamar_malam with dissolve
    "Hmm.. Sudah malam kalau gitu aku makan lalu langsung tidur"

    scene dapur_malam with dissolve
    show mom at center with dissolve:
        ypos 1.2
    mom "Sudah bangun kamu sini makan bareng"
    mc "Iyaa,, Bu ngomong-ngomong ayah kemana bu ?"
    mom "Ayah Kerja Lembur jadi bakalan pulang malam"
    show mom at center with moveinleft:
        xpos 0.675
        ypos 1.2
        xzoom -1
    show cat at center with moveoutbottom:
        ypos 0.775
    cat "Meoooww"
    mc "kamu mau tambah lagi [cat] ?"
    cat "Meoooww"
    mc "Dasarr.. hahahah iyaa ini aku kasih lagi"
    mc "Nanti mau tidur di kamarku ?"
    cat "Meooww"
    hide cat with dissolve
    mc "Oiya, bu ini nasinya ?"
    show mom at center with moveinright:
        ypos 1.2
    mom "Iyaa"
    mc "Kalau gitu selamat makan"
    hide mom with dissolve
    "~Beberapa Menit kemudian~"
    "Fuuuhh.. Kenyangnya"
    play sound cuci_piring
    $ _skipping = False
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(15.0, hard=True)
    stop sound fadeout 1.0
    window show dissolve
    $ _skipping = True
    mc "Kalau gitu aku tidur lagi ya bu"
    show mom at center with dissolve:
        ypos 1.2
    mom "Iyaa.."
    mom "Oiyaa,, di sekolah ga ada sesuatu ?"
    mc "Ga ada aman-aman saja cuma aku dapat teman"
    mom "Mereka mengganggu mu ?"
    mc "Ga bu"
    mom "Ohh iyaa dah"
    hide mom with dissolve

    scene kamar_malam with dissolve
    "Saatnya tidur lagi pintunya kubuka sedikit saja lah biar [cat] bisa masuk ke kamar"

    stop music fadeout 1.0

    jump day3_Airin

    return