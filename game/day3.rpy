label day3_Kirana:
    scene kamar with dissolve
    "Sudah Pagi Ternyata, sebaiknya aku bergegas menuju sekolah"

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Ehh.. Sudah Mandi Ternyata"
    mc "Hehhe Iya"
    mc "[dad] kemana bu ?"
    mom "[dad]mu berangkat pagi tadi. ibu sudah siapin bekal untuk ayahmu tadi"
    mc "Kalau gitu aku makan dulu ya bu"
    mom "Iyaa nak"
    hide mom with dissolve
    "Kami pun Makan bersama walaupun [dad] sudah berangkat duluan"
    mc "Aku sudah selesai bu \nKalau gitu aku mau ambil tas dulu di kamar"
    
    scene kamar with dissolve
    "Dimana ya tasku tadi ? Mungkin disini"
    "Nahh.. ini dia \nSaatnya Pamit ke [mom]"

    scene dapur with dissolve
    mc "Bu, Aku berangkat"
    show mom at center with dissolve:
        ypos 1.15
    mom "Oiya,, Uang Sangumu sama Bekal ada di meja makan!"
    mc "Dimana bu ?"
    mom "Ini di Meja"
    mc "Iya bu, Terima kasih bu \nKalau gitu aku berangkat"
    mom "Hati-hati dijalan"
    hide mom with dissolve

    scene gerbang_sekolah with dissolve
    "Tumben ga ada yang manggil untuk bareng ke kelas. Apa Aku kepagian ya berangkatnya ? "
    "Tapi hari ini enak banget sunyi sekali pas masuk ke sekolah"
    
    scene kelas with dissolve
    "Ternyata yang baru datang hanya beberapa saja sepertinya \naku berangkatnya emang kepagian"
    "Haaa... Aku masih agak ngantuk \nsebaiknya aku tidur dulu"
    "~Beberapa Menit Kemudian~"
    "~Ding Dong~"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Hee Bangun.. "
    mc "Umm.."
    mg2 "Sudah mau mulai jam pelajarannya.. Bangunn.."
    mc "Ahh.. sudah masuk ternyata"
    mg2 "Iyaa.. sana raup dulu"
    mc "Oh Ok kalau gitu aku raup dulu"
    hide ardana_uni with dissolve

    scene lorong with dissolve
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Loh [mcFirst] mau kemana ?"
    mc "Mau ke kamar mandi bu"
    sr "Ealah, Iyaa dah sana"
    mc "Baik bu"
    hide bu_senda with dissolve

    scene kelas with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat sore anak- anak"
    kk "Loh, ini masih pagi loh bu.. kok selamat sore sih"
    sk "hahhahahhahahahhaha"
    sr "Alhamdulillah brati masih semangat ya, otak nya masih fresh. baik lah langsung saja, ibu mulai, selamat pagi semuanya"
    sk "Pagi bu"
    sr "Kalau gitu kita mulai pelajarannya"
    mc "Permisi bu"
    sr "Iya Iyaa silahkan duduk"
    show bu_senda at right with moveinleft:
        xpos 0.9
        ypos 1.2
    "~Materi Fungi lanjutan~"
    "~Ding Dong~"
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Waktunya sudah habis anak-anak \nKalian boleh istirahat sekarang"
    hide bu_senda with moveoutright
    show nada_uni at center with moveinright:
        ypos 1.2
    na "Brader ikut ke kantin ga ?"
    mc "Ohh Okk"
    show nada_uni at center with moveinleft:
        xpos 0.65
        ypos 1.2
    show ardana_uni_cuek at center with dissolve:
        ypos 1.2
    mg2 "Aku ga diajak nih ?"
    mc "Kan ada [ol]"
    ol "[mg2_Last] Ayoo Ke Kantin"
    mc "Tuhkan diajak sama [ol] Ntar ketemuan disana aja"
    ol "Okk deh.. Ayo [mg2_Last]"
    mg2 "Iya.. Iyaa.."
    mc "Kalau gitu aku duluan ke kantin"
    hide nada_uni with moveoutright
    hide ardana_uni_cuek with dissolve

    scene kantin with dissolve
    show nada_uni at center with moveinleft:
        ypos 1.2
    na "Carikan tempat duduk kosong dong ntar aku aja yang mesenin"
    na "Mau pesen apa ?"
    mc "Mungkin Bakso aja kali ya"
    na "Okk dahh, Beli berapa baksonya ?"
    mc "5000an aja dah cukup"
    mc "Kalau gitu aku cari bangku yang kosong dulu"
    hide nada_uni with dissolve
    "Mungkin sebaiknya duduk disini"
    show ardana_uni at center with moveinleft:
        ypos 1.2
    mg2 "Hooo Ternyata ada disini kamu"
    ol "Kami Numpang duduk disini juga ya"
    mc "Oh Okk"
    ol "Btw, Makananmu mana ?"
    mc "Tuh lagi dibawain sama si [na]"
    show nada_uni at center with moveinright:
        xpos 0.6
        ypos 1.2
    show ardana_uni at center with moveinright:
        xpos 0.4
        ypos 1.2
    na "Loh Loh ada [mg2_Last] sama [ol] ternyata"
    mg2 "Ya kan ketemuan di kantin"
    ol "Iyaa nih"
    mc "dah dah ayo makan setelah itu balik ke kelas"
    mc "kalian makan apa ?"
    ol "Aku beli mie ayam"
    mg2 "Kalau aku Nasi Pecel. Kalau kalian bagaimana ? "
    mc "Aku makan Bakso"
    na "Kalau aku pesen Nasi Goreng sih hahah"
    mc "Dah ah Mari Kita Makan"
    hide nada_uni with dissolve
    hide ardana_uni with dissolve

    scene kelas with dissolve
    show ardana_uni at center with moveinright:
        ypos 1.2
    mg2 "Fuuu.. Kenyangnya~"
    ol "Pesenmu banyak kali tadi Nasi Pecelnya Jumbo"
    mg2 "Hehehehe"
    "~Ding Dong~"
    ol "Aku kembali ke bangku ku dulu ya"
    mg2 "Okie"
    hide ardana_uni with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat malam anak-anak"
    sk "Lah.. tadi pagi selamat sore sekarang siang selamat malam"
    sk "Ihh Bu Senda ini"
    sr "Heheheh Becanda. Ternyata Kalian masih semangat ya"
    sr "Tumben, Biasanya siang-siang gini dah lesu"
    sk "Itu mah perasaannya Bu Senda aja kali hehehe"
    sr "Dasar kalian yaa"
    sk "hahahahha.. Ampun Bu ampun haha"
    sr "Sudah Sudah mari kita mulai saja ya"
    sr "Oiyaa, Seperti kemarin berkelompok lagi ya terus ibu mau rapat lagi kemungkinan sebentar lagi pulang"
    sr "Sekelompok 4 orang sekelas ini ada 35 orang"
    sr "Sisanya bisa bikin kelompok sendiri bisa bergabung sama temannya"
    sr "Tentuin sendiri kelompoknya ya"
    hide bu_senda with dissolve
    "Hmm... Kelompok lagi kelompok lagi. sepertinya aku ga menemukan kelompok"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Mau kelompokan sama aku ?"
    mc "Bukannya sudah cukup ?"
    mg2 "tapi kan sisanya boleh bergabung ke kelompok mana pun"
    mc "Kelompokmu ada siapa aja ?"
    $ nd = "Nindi"
    $ ad = "Ardi"
    mg2 "Ada [nd], aku, [ol], [ad]"
    mc "Kalau kelompoknya [na] ada siapa aja ?"
    mg2 "Kayaknya sudah 5"
    mc "...."
    mc "Yaudah lah aku masuk kelompokmu aja"
    mg2 "Okie"
    hide ardana_uni with dissolve
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Apa Semua sudah dapat kelompok ?"
    sr "Kalau gitu ini tugasnya"
    sk "Baik bu"
    "~Ding Dong~"
    sr "Ternyata sudah bel pulang, kalau gitu ibu akhiri saja untuk hari ini"
    sr "Oiya, Jangan lupa dikerjakan ya"
    sk "Iyaa bu"
    hide bu_senda with moveoutright
    nd "Mau kerumahnya siapa ? Kerja kelompoknya"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Dirumahku atau [ol] ? Rumahmu juga gapapa sih"
    nd "Kalau dirumahnya [mcFirst] Bagaimana ?"
    ol "Boleh juga itu"
    mc "...."
    mc "Jangan dirumahku soalnya semuanya pada keluar jadi rumahku dikunci"
    nd "Kamu ga dititpin kunci ?"
    mc "Ga soalnya setiap pulang sekolah sudah ada dirumah"
    mc "Berhubung sekarang pulang lebih awal jadi dirumahku ga ada siapa-siapa"
    mc "Saranku dirumahnya kalian aja"
    mg2 "Kalau gitu rumahmu aja Nin gimana ?"
    ol "Bagaimana kalau Kerja kelompok di taman kota ?"
    mg2 "Boleh juga itu"
    nd "Yaudah kalau gitu di taman kota aja"
    mc "Aku ngikut aja"
    ad "Aku sih ok ok aja"
    hide ardana_uni with moveoutright

    scene gerbang_sekolah_siang with dissolve
    nd "sudah rede semua ini kan ?"
    ad "Tinggal Berangkat aku"
    $ mgol = "Ardana dan Filo"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mgol "Gass dah rede nih"
    nd "Kalau gitu Joss berangkat kita"
    hide ardana_uni with moveoutleft

    scene central_park with dissolve
    ol "Yeayy Sudah sampai"
    nd "Kita kerjain langsung apa pesan sesuatu dulu ?"
    ad "Pesan dulu aja dong di FoodCourtnya sekalian kerjain disana"
    mc "Aku ngikut aja"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Yauda, Pesan aja dulu sambil nunggu camilan ama minumannya datang kita kerjain aja"
    hide ardana_uni with moveoutright

    scene foodcourt with dissolve
    ol "Kalian mau pesan apa gaes ?"
    nd "Aku minumnya pesan Es Jeruk aja"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Aku pesan jus jambu aja"
    ad "Aku pesan Es Jeruk juga"
    mc "Milkshake Vanilla"
    ol "Kalau gitu Es Jeruk 2, Jus Jambu 1, Milkshake Vanilla 1"
    ol "Kalau camilannya pesen apa ini ? yang sekiranya bisa dibuat makan bersama"
    nd "Kalau gitu Kentang Goreng 2 terus Pisang coklat 1"
    mg2 "Nugget jugaa 2 sama tempe goreng 2"
    ol "Okk dah kalau gitu aku pesanin dulu ya"
    ad "Ehh.. tunggu dulu tambah itu juga Tahu Crispy 1"
    ol "Okie Doki"
    mc "Jadi, berhubung tunggu pesanan datang kita kerjakan dulu soal dari Bu Senda"
    nd "Boleh"
    mg2 "Yok,, Keluarkan Tugasnya biar cepat selesai"
    ad "Gass Keun"
    hide ardana_uni with dissolve

    "~SOAL~"
    #Initialize score
    $ quiz3_score = 0

    label quiz3:
        $ quick_menu = False

        "1. Fag memperbanyak dan menyusun DNA merupakan fase ....... dalam infeksi secara......"
        menu:
            "A. Hanya dapat hidup dalam sel–sel hidup":
                $ quiz3_score += 0
            "B. Fase repllika - litik":
                $ quiz3_score += 5
            "C. Kulitnya terdiri atas protein":
                $ quiz3_score += 0
            "D. tubuhnya terdiri atas DNA atau RNA":
                $ quiz3_score += 0

        "2. Setelah melakukan reproduksi, virus akan menghancurkan sel induk. Pernyataan tersebut termasuk dalam infeksi secara.."
        menu:
            "A. Parasit Obligat":
                $ quiz3_score += 0
            "B. Virus":
                $ quiz3_score += 0
            "C. Litik":
                $ quiz3_score += 5
            "D. Eukariot":
                $ quiz3_score += 0 

        "3. Setelah dinding sel rusak (terhidrolis) maka DNA fag masuk ke dalam sel bakteri yang dinamakan fase ......"
        menu:
            "A. Fase pembebasan":
                $ quiz3_score += 0
            "B. Fase perakitan":
                $ quiz3_score += 0
            "C. Fase Absorbtion":
                $ quiz3_score += 0
            "D. Fase penetrasi":
                $ quiz3_score += 5
        
        show virusd3 at truecenter
        "4. Bagian a pada gambar dinamakan ….."
        menu:
            "A. Kepala":
                $ quiz3_score += 5
            "B. Ekor virus":
                $ quiz3_score += 0
            "C. RNA":
                $ quiz3_score += 0
            "D. Serabut ekor":
                $ quiz3_score += 0
            
        "5. Bagian b pada gambar dinamakan ….."
        menu:
            "A. RNA":
                $ quiz3_score += 0
            "B. DNA":
                $ quiz3_score += 0
            "C. Serabut Ekor":
                $ quiz3_score += 0
            "D. Leher":
                $ quiz3_score += 5

        "6. Bagian c pada gambar dinamakan ….."
        menu:
            "A. Kepala":
                $ quiz3_score += 0
            "B. Serabut Ekor":
                $ quiz3_score += 5
            "C. Kapsid":
                $ quiz3_score += 0
            "D. Asam nukleat":
                $ quiz3_score += 0

        hide virusd3

        "7. Pada siklus lisogenik terjadi fase penggabungan antara DNA virus dan DNA bakteri membentuk.."
        menu:
            "A. Profage":
                $ quiz3_score += 5
            "B. Reproduksi virus":
                $ quiz3_score += 0
            "C. Profase":
                $ quiz3_score += 0
            "D. Virion":
                $ quiz3_score += 0

        "8. Virus dapat digunakan sebagai vektor untuk melakukan rekombinasi bahan genetik dari sel donor ke sel reseptor yang dikenal dengan istilah..."
        menu:
            "A. Nukleokapsid":
                $ quiz3_score += 0
            "B. Nucleoprotein":
                $ quiz3_score += 0
            "C. Kapsomer":
                $ quiz3_score += 0
            "D. Transplantasi":
                $ quiz3_score += 5

        "9. Di bawah ini yang termasuk Virus pemakan bakteri yaitu ….."
        menu:
            "A. Virus paramyxovirus":
                $ quiz3_score += 0
            "B. Adenovirus":
                $ quiz3_score += 0
            "C. Bakteriofag":
                $ quiz3_score += 5
            "D. TMV":
                $ quiz3_score += 0

        "10. Di bawah ini yang tidak termasuk contoh dari Nukleokapsid yang telanjang yaitu ......"
        menu:
            "A. Wart Virus":
                $ quiz3_score += 0
            "B. Virus kutil":
                $ quiz3_score += 0
            "C. Virus influenza":
                $ quiz3_score += 5
            "D. TMV":
                $ quiz3_score += 0

        "11. Penyebab campak yaitu virus …."
        menu:
            "A. TMV":
                $ quiz3_score += 0
            "B. Paramyxovirus":
                $ quiz3_score += 5
            "C. HIV":
                $ quiz3_score += 0
            "D. Adenovirus":
                $ quiz3_score += 0

        "12. Virus mempunyai sifat sebagai benda mati yaitu…."
        menu:
            "A. dapat dikristalkan":
                $ quiz3_score += 5
            "B. Reproduksi virus":
                $ quiz3_score += 0
            "C. terdiri atas ADN atau ARN saja":
                $ quiz3_score += 0
            "D. hanya dapat hidup pada sel hidup":
                $ quiz3_score += 0

        "13. Di bawah ini merupakn pernyataan yang benar mengenai susunan tubuh virus yaitu…."
        menu:
            "A. Kapsid virus tersusun dari lipoprotein dan materi genetik berupa kromosom":
                $ quiz3_score += 0
            "B. Virus mempunyai selubung dari lemak dan materi genetik berupa DNA/RNA":
                $ quiz3_score += 0
            "C. kapsid virus tersusun dari karbohidrat polisakarida dan materi genetik berupa plasmid":
                $ quiz3_score += 0
            "D. Virus mempunyai selubung dari protein dan materi genetik DNA/RNA":
                $ quiz3_score += 5

        "14. Tubuh bakteri akan pecah karena penuh dengan virus pada fase ..."
        menu:
            "A. Adsorpsi":
                $ quiz3_score += 0
            "B. Lisogenik":
                $ quiz3_score += 0
            "C. Lisis":
                $ quiz3_score += 5
            "D. Penetrasi":
                $ quiz3_score += 0

        "15. Fase pembiakan virus yang materi genetiknya (DNA) menempel pada bakteri (sel inang), karena bakteri memiliki daya tahan dan tidak terbentuk bagian-bagiannya disebut fase…"
        menu:
            "A. Konjugasi":
                $ quiz3_score += 0
            "B. Trasnformasi":
                $ quiz3_score += 0
            "C. Lisogenik":
                $ quiz3_score += 5
            "D. Litik":
                $ quiz3_score += 0

        "16. Perbedaan antara litik dan lisogenik yaitu..."
        menu:
            "A. TMV":
                $ quiz3_score += 0
            "B. Paramyxovirus":
                $ quiz3_score += 0
            "C. DNA virus menempel pada DNA sel inang pada fase lisogenik":
                $ quiz3_score += 5
            "D. Adenovirus":
                $ quiz3_score += 0

        "17. Jenis penyakit berikut yang disebabkan oleh virus yaitu ..."
        menu:
            "A. influenza, demam berdarah, polio, AIDS, dan cacar":
                $ quiz3_score += 5
            "B. tifus, AIDS, influenza, kolera, dan cacar":
                $ quiz3_score += 0
            "C. demam berdarah, cacar, kolera, polio, dan tifus":
                $ quiz3_score += 0
            "D. influenza, tifus, Udunen, kolera, dan cacar":
                $ quiz3_score += 0

        "18. Vaksinasi bisa mencegah suatu penyakit yang dikarenakan oleh virus. Vaksinasi bisa diberikan secara oral contohnya vaksin untuk penyakit…"
        menu:
            "A. hepatitis":
                $ quiz3_score += 0
            "B. cacar":
                $ quiz3_score += 0
            "C. disentri":
                $ quiz3_score += 0
            "D. polio":
                $ quiz3_score += 5

        "19. Kapsid tersusun atas subunit-subunit protein yang disebut dengan ….."
        menu:
            "A. Nucleoprotein":
                $ quiz3_score += 0
            "B. Selubung protein":
                $ quiz3_score += 0
            "C. Kapsomer":
                $ quiz3_score += 5
            "D. Nukleokapsid":
                $ quiz3_score += 0

        "20. Virus yang menyebabkan penyakit leukemia adalah ….."
        menu:
            "A. Orthopoxvirus":
                $ quiz3_score += 0
            "B. Retrovirus":
                $ quiz3_score += 5
            "C. Papillomavirus":
                $ quiz3_score += 0
            "D. Lyssavirus":
                $ quiz3_score += 0

        "Jawaban :
            \n 
            1. A \ \ \ \ 4. A \ \ \ \ 7. A \ \ \ \ 10. C \ \ \ \ 13. D \ \ \ \ 16. C \ \ \ \ 19. C 
            \n
            2. C \ \ \ \ 5. D \ \ \ \ 8. D \ \ \ \ 11. B \ \ \ \ 14. C \ \ \ \ 17. A \ \ \ \ 20. B
            \n
            3. D \ \ \ \ 6. B \ \ \ \ 9. C \ \ \ \ 12. A \ \ \ \ 15. C \ \ \ \ 18. D"

        "Nilaiku adalah [quiz3_score]"

    # Check the quiz 1 score
    if quiz3_score >= 75:
        # Win
        $ quick_menu = True
        "Kemudian makanannya datang, tugasnya pun sudah selesai juga dan aku makan bersama teman kelas"
        "Aku pikir ini tidak begitu buruk"
        # Did he win? Yes.
        #$ quiz3_win = True
        #$ quiz3_lose = False   
    else:
        # Lose
        "Lumayan susah juga"
        ol "Nyerah nih ?"
        mc "Terserah, tapi nilainya dapat jelek"
        menu:
            "Tidak Menyerah":
                ol "Iya, dah. Istirahat dulu aja"
                mg2 "Iya bener, Istirahat dulu"
                mg2 "Setelah itu lanjut"
                $ quiz3_score = 0
                jump quiz3
            "Nyerah":
                "Anda gagal sebagai murid"
                "~END~"
                return

    ol "Capeknya ngerjakan tugasnya. Mari kita makan"
    ad "Ngomong-ngomong aku pernah kelihatan kamu dulu waktu SMP"
    ad "Kalau ga salah kamu sering dibully dulu ya"
    ad "Sampe ada kasusnya"
    mc "...."
    mc "Aku ? Kayaknya salah orang"
    nd "Dibully gimna ?"
    ad "Soalnya dulu ada yang terbully habis habisan itu seingatku"
    ol "Kejamnya, kok masih suka bully Terus gimana kabar anak itu ?"
    ad "Ntahlah, aku ga tau juga dah lupa soalnya hahahha"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Kok jadi tegang gini suasananya ?"
    ol "Bahas yang seru aja lah"
    ol "Jadi Mencekam gini suasanya kyk dirumah horror aja"
    mc "Hahahaha... Ntr kalau [ol] pulang pas malamnya di kamar hati-hati"
    ol "Dihh.. Malah Nakutin ada apa emangnya"
    mc "[mg2_Last] numpang boker lewat jendela kamarmu"
    hide ardana_uni
    show ardana_uni_emosi at center:
        ypos 1.2
    mg2 "Dihh.. Dasar kamu ya.. minta dipukul !!"
    mc "Aduh.. aduhh.. aduhh.." with hpunch
    mc "Heheh maaf maaf" 
    ad "Hahahaha ada-ada aja" 
    hide ardana_uni_emosi with dissolve
    "Meskipun suasananya sempat tegang, tapi masih bisa teratasi"

    scene foudcourt_sore with dissolve
    show ardana_uni at center with dissolve:
        ypos 1.2 
    mg2 "Sudah sore nih, Kuy Pulang"
    mc "Ahh Ok ok"
    mg2 "Kalian ga mau pulang gaes ?"
    ad "Iyaa ini aku juga mau pulang malam ini ada janjian soalnya"
    mg2 "[nd] dan [ol] ga pulang juga ?"
    $ ndol = "Nindi dan Filo"
    ndol "Yaa pulang lah, yakali mau ngesatpam disini"
    ad "Pfftt"
    ad "gapapa nambah satpam disini hahha"
    ndol "Mending kamu aja deh jadi satpam disini"
    ad "Tuh kalian berdua serasi cocok jadi satpam sini daripada aku"
    ol "dah ah Pulang aja kalau gini ga pulang - pulang"
    mg2 "Kalau gitu aku duluan"
    $ mm2 = "[mcFirst] dan [mg2_Last]"
    $ all = "[ad], [nd], dan [ol]"
    mm2 "Aku duluan gaes.. Bye Byee"
    hide ardana_uni with moveoutleft
    all "Okie.. Baibai hati-hati dijalan semuanya"

    scene depan_rumah_sore with dissolve
    mc "Terima kasih [mg2_Last]"
    show ardana_uni at center with dissolve:
        ypos 1.2
    mg2 "Gapapa no problem, aku pulang duluan titip salam ke tante"
    mc "Okk"
    hide ardana_uni with moveoutleft

    scene ruang_tamu_sore with dissolve
    mc "Aku Pulang!!"
    mom "Iyaa !!"

    scene ruang_keluarga_sore with dissolve
    mc "Ada salam dari [mg2_Last] barusan"
    show mom at center with dissolve:
        ypos 1.15
    mom "Loh ga mampir ?"
    mc "Keburu Malam katanya terus sudah capek juga"
    mc "Kalau gitu aku langsung tidur bu"
    mom "Ahh iya iyaa"
    mc "[cat] sudah dikasih makan ?"
    mom "Sudah tadi, terus nonton film sama Ibu disini sampai kamu datang hahah"
    hide mom with dissolve
    mc "[cat] mau ikut tidur ?"
    show cat_happy at center with moveinbottom:
        ypos 0.75
    cat "Meoooww"
    hide cat_happy with moveoutbottom

    scene kamar_sore with dissolve
    "Salin Baju dulu lah terus tidur, capek bener"
    "Leganya enaknya kasur ini buat rebahan"
    mc "Kuy tidur disini [cat] soalnya kamu hangat hahaha"
    show cat_happy at center with dissolve:
        ypos 0.75
    cat "Fuurrr Fuurrr"
    hide cat_happy with dissolve
    mc "Lahh cepet banget pasti kecapekan nonton tv hahahha"

    jump day4_Kirana

label day3_Miselia:

    scene kamar with dissolve
    mc  "Huuhh, hari sudah senin lagi"
    mom "Naak.?"
    mc "Iya buu, kenapa?"
    mom  "Oohh, kirain kamu belum bangun nak"
    mc "Heheh, sudah kok bukk, bentar lagi aku mandi"

    scene depan_rumah with dissolve
    mc " Bu, aku berangkat ke sekolah dulu ya "
    mom "Iya nak , hati hati di jalan ya, sekolah yang pinter"

    scene lorong with dissolve
    kk"Heh dasar sok kegantengan! awas ya sampek kamu ganggu cewekku lagi"
    mc "Ehh  maksudnya apa ya mas ? emang aku salah apa "
    kk "Halah, sok pura pura gatau lagi ! "
    mc "Beneran mas, saya ga tau apa apa "
    mg1"Heh mau di bawa kemana mc?"
    kk "Kamu bocil jangan ikut campur ya!!! ini urusan aku sama si penggoda ini"
    mg1 "Hehh. ga bisa gitu dong , mc sini ikut aku ke kealas."
    kk "Ehhh sudah sudahh, nanti pak saiful mergoki kita lagi , ayokk kabur"
    mg1"Kamu gapapa bro?emang kamu ada masalah apa sama dia"
    mc "Aku pun juga gatau , ada masalah apa , tiba tiba aku di berhentikan tadi di depan gerbang terus mau di seret ke toilt tadi"
    mg1 "Huhh dasar ya , cari maslaah tu orang , yaudaahh gapapa , bu sendra talagi datag , mendng kita ke kelas"
    
    scene kelas with dissolve
    sr "Selamat pgi anak2 ,sudah siap memulai pelajaran !"
    sk "Siap bu!"
    sr "Oke kalo begitu buka  bab virus"

    "Materi Virus"
    mg1 "Hey mc apa kamu bisa mengerjakan soal nomor 3?"
    mc "Oohh okey makasih y"
    sr "Anak2 jam ibu sudah selesai , kalo belum selesei diuat pr minggu depan dikumpulkan ya"
    sk "Okey bu siap"
    mg1 "Hey mc ayo makan ke kantin"
    mc "Duluan deh aku ingn mengerjakan pr yg tadi dulu ."
    mg1 "Huuu kmu ni rajin2 amat padahal dikumpulin minggu depan"
    mc "Seharusnya kita tidak boleh menunda- nunda , selagi bisa sekarang kenapa tidak"
    mg1 "iyeudah terserah lu, aku mau ke kantin dlu laper perutku , makan tuh nomor satu"
    
    scene kantin with dissolve
    $ Ik = "Ibu kantin"
    mg1 "Bk, saya beli tahu koceknya 2 ya pedes semua"
    Ik "iya nak , fi tunggu ya "

    scene kelas with dissolve
    mg1 "Nih , aku punya tahu kocek, tadi aku beli 2"
    mc "Wah , terimakassih ya "

    #Initialize score
    $ quiz_fungi3_score = 0

    label quiz_fungi3:

        "1. Sifat jamur jika ditinjau sebagai makhluk heterotrof adalah … "
        menu:
            "A. mampu memproduksi makanan sendiri":
                $ quiz_fungi3_score += 0
            "B. hidupnya sangat tergantung pada inangnya":
                $ quiz_fungi3_score += 10
            "C. hidup di wilayah yang memiliki kelembapan":
                $ quiz_fungi3_score += 0
            "D. mampu berfotosintesis":
                $ quiz_fungi3_score += 0

        "2. Berikut ini yang merupakan contoh spesies dari deuteromycotina ialah … "
        menu:
            "A. Penicillium sp.":
                $ quiz_fungi3_score += 0
            "B. neurospora sitophila":
                $ quiz_fungi3_score += 0
            "C. gigaspora":
                $ quiz_fungi3_score += 0
            "D. gonoderma sp":
                $ quiz_fungi3_score += 10

        "3. Berikut ini contoh bereproduksi jamur secara begetatif adalah … "
        menu:
            "A. Konjungsi":
                $ quiz_fungi3_score += 0
            "B. Basidium":
                $ quiz_fungi3_score += 0
            "C. Budding":
                $ quiz_fungi3_score += 10
            "D. Membelah diri":
                $ quiz_fungi3_score += 0

        "jika didasarkan pada uraian di atas, sifat fungi ditunjukkan oleh nomor … " (multiple=2)
        "4. Perhatikan uraian berikut!
            \n
            1) autotrof
            \n
            2) heterotrof
            \n
            3) mutual
            \n
            4) berklorofil
            \n
            5) saprofit" (multiple=2)
        menu:
            "A. 3, 1, dan 4":
                $ quiz_fungi3_score += 10
            "B. 2, 1, dan 4":
                $ quiz_fungi3_score += 0
            "C. 2, 3, dan 4":
                $ quiz_fungi3_score += 0
            "D. 1, 3, dan 5":
                $ quiz_fungi3_score += 0
            
        "5. Di bawahi ini adalah beberapa hal yang membedakan antara jamur dengan tumbuhan lainnya, kecuali … "
        menu:
            "A. pola pertumbuhan":
                $ quiz_fungi3_score += 0
            "B. struktur tubuhnya":
                $ quiz_fungi3_score += 0
            "C. melakukan pergerakan pasif":
                $ quiz_fungi3_score += 10
            "D. cara reproduksi":
                $ quiz_fungi3_score += 0

        "6. Deuteromycotina memiliki nama lain yakni jamur … "
        menu:
            "A. tiram merah":
                $ quiz_fungi3_score += 0
            "B. tak sempurna":
                $ quiz_fungi3_score += 10
            "C. tiram putih":
                $ quiz_fungi3_score += 0
            "D. lendir":
                $ quiz_fungi3_score += 0

        "7. Berikut ini yang merupakan salah satu bentuk simbiosis jamur ialah … "
        menu:
            "A. Basidiomycotina":
                $ quiz_fungi3_score += 0
            "B. Miselium":
                $ quiz_fungi3_score += 10
            "C. Zygomycotina":
                $ quiz_fungi3_score += 0
            "D. Mikoriza":
                $ quiz_fungi3_score += 0

        "8. Berikut ini adalah jamur-jamur yang bermanfaat bagi manusia, kecuali … "
        menu:
            "A. Saccharomyces":
                $ quiz_fungi3_score += 0
            "B. Lycoperdon perlatum":
                $ quiz_fungi3_score += 0
            "C. Volyariella volvacea":
                $ quiz_fungi3_score += 10
            "D. Albugo":
                $ quiz_fungi3_score += 0

        "9. Berikut ini adalah jenis jamur yang merugikan manusia ialah … "
        menu:
            "A. Albugo":
                $ quiz_fungi3_score += 10
            "B. Lycoperdon perlatum":
                $ quiz_fungi3_score += 0
            "C. saccharomyces":
                $ quiz_fungi3_score +=  0
            "D. Higroporus":
                $ quiz_fungi3_score += 0

        "10. Jamur darat mampu menghasilkan spora yang dibentuk dari sel khusus. Sel khusus tersebut disebut dengan … "
        menu:
            "A. basidium":
                $ quiz_fungi3_score += 0
            "B. askus":
                $ quiz_fungi3_score += 10
            "C. hifa":
                $ quiz_fungi3_score += 0
            "D. miselium":
                $ quiz_fungi3_score += 0

        "Jawaban :
            \n 
            1. B \ \ \ \ 3. C \ \ \ \ 5. C \ \ \ \ 7. B \ \ \ \ 9. A
            \n
            2. D \ \ \ \ 4. A \ \ \ \ 6. B \ \ \ \ 8. C \ \ \ \ 10. B"

        "Nilaiku adalah [quiz_fungi3_score]"

    # Check the quiz 1 score
    if quiz_fungi3_score >= 75:
        # Win
        sr "Selamat Bagi yang Nilainya Bagus"
        sr "Kalian bebas melakukan apa saja sampai waktu pelajaran habis"
        # Did he win? Yes.
        #$ quiz_fungi3_win = True
        #$ quiz_fungi3_lose = False   
    else:
        # Lose
        sr "Bagi yang Nilainya jelek bisa mengulang lagi"
        menu:
            "Mengulang Lagi":
                $ quiz_fungi3_score = 0
                jump quiz_fungi3
            "Tidak Ingin Mengulang":
                "Anda gagal sebagai murid"
                "~END~"
                return

    scene gerbang_sekolah_sore with dissolve
    mt "Eh , kamu pulang sama siapa ?"
    mc "Aku pulang naik angkota met, kenapa ?"
    mt "Oh gapapa , yaudah ayo breng , aku juga mau naik angkot"
    mc "Okedeh"

    jump day4_Miselia

label day3_Airin:
    scene kamar with dissolve
    "Sudah Pagi Ternyata, sebaiknya aku bergegas menuju sekolah"

    scene dapur with dissolve
    show mom at center with dissolve:
        ypos 1.2
    mom "Ehh.. Sudah Mandi Ternyata"
    mc "Hehhe Iya"
    mc "[dad] kemana bu ?"
    mom "[dad]mu berangkat pagi tadi. ibu sudah siapin bekal untuk ayahmu tadi"
    mc "Kalau gitu aku makan dulu ya bu"
    mom "Iyaa nak"
    hide mom with dissolve
    "Kami pun Makan bersama walaupun [dad] sudah berangkat duluan"
    mc "Kalau gitu aku ambil tas dulu di kamar"
    show mom at center with dissolve:
        ypos 1.2
    mom "Oiya,, Uang Sangumu sama Bekal ada di meja makan!!"
    mc "Dimana bu ?"
    mom "Ini di Meja"
    hide mom with dissolve
    mc "Iya bu, kalau gitu aku berangkat"
    $ money += 15000
    mc "[cat] Berangkat dulu"

    scene gerbang_sekolah with dissolve
    "Tumben ga ada yang manggil untuk bareng ke kelas. Apa Aku kepagian ya berangkatnya ? "
    "Tapi hari ini enak banget sunyi sekali pas masuk ke sekolah"
    
    scene kelas with dissolve
    "Ternyata yang baru datang hanya beberapa saja sepertinya emang kepagian"
    "Mungkin kalau gitu sebaiknya aku tidur dulu"
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Umm.. Dia tertidur lagi, sering sekali dia tertidur"
    hide airin_uni with dissolve
    "~Beberapa Menit Kemudian~"
    "~Ding Dong~"
    show airin_jalan_uni at center with moveinright
    mg3 "Dia belum bangun sama sekali"
    hide airin_jalan_uni
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Hee Bangun.. "
    mc "Umm.."
    mg3 "Sudah mau mulai jam pelajarannya.. Bangunn.."
    mc "Ahh.. sudah masuk ternyata"
    mg3 "Iyaa.. sana raup dulu"
    mc "Oh Ok kalau gitu aku raup dulu"
    show airin_uni at center with moveinright:
        xpos 0.3
        ypos 1.2
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Cie cie"
    mc "Apaa ?"
    na "Gapapa hahahha.. raup dulu lur bentar lagi Bu Senda masuk"
    mg3 "Hooh Raup dulu sana"
    mc "Iya Iya.. Kalau gitu aku ke kamar mandi dulu"
    na "Btw, kamu tiba-tiba akrab sama [mcFirst] pasti ini alasannya [mcFirst] pulangnya lebih lama nih"
    na "Ciee ciee"
    mg3 "Ahh.. ga ga bukan apa-apa"
    hide airin_uni with dissolve
    hide nada_uni with dissolve

    scene lorong with dissolve 
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Loh [mcFirst] mau kemana ?"
    mc "Mau ke kamar mandi bu"
    sr "Ealah, Iyaa dah sana"
    mc "Baik bu !!"
    hide bu_senda with dissolve

    scene kelas with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat sore anak- anak"
    kk "Loh, ini masih pagi loh bu.. kok selamat sore sih"
    sk "hahhahahhahahahhaha"
    sr "Alhamdulillah brati masih semangat ya, otak nya masih fresh. baik lah langsung saja, ibu mulai, selamat pagi semuanya"
    sk "Pagi bu"
    sr "Kalau gitu kita mulai pelajarannya"
    mc "Permisi bu"
    sr "Iya Iyaa silahkan duduk"
    show bu_senda at center with moveinleft:
        xpos 0.7
        ypos 1.2
    "~Materi Klasifikasi~"
    "~Ding Dong~"
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Waktunya sudah habis anak-anak kalau gitu kalian boleh istirahat"
    sk "Baik bu!!"
    hide bu_senda with moveoutright
    show nada_uni at center with dissolve:
        ypos 1.2
    na "Brader ikut ke kantin ga ?"
    mc "Ohh Okk"
    hide nada_uni with moveoutright

    scene kantin with dissolve
    $ wkk = "Wakil Ketua Kelas"
    $ bl = "Bella"
    show nada_uni at center with moveinleft:
        ypos 1.2
    na "Carikan tempat duduk kosong dong ntar aku aja yang mesenin"
    na "Mau pesen apa ?"
    mc "Mungkin Bakso aja kali ya"
    na "Okk dahh, Beli berapa baksonya ?"
    mc "5000an aja dah cukup"
    mc "Kalau gitu aku cari bangku yang kosong dulu"
    hide nada_uni with dissolve
    "Mungkin sebaiknya duduk disini"
    show nada_uni at center with moveinright:
        ypos 1.2
    na "Hooo.. Duduk disini"
    kk "Ohh.. kalian ada disini"
    na "Lohh ada [kk] juga sendirian ? gabung sini sama kita"
    kk "Boleh-boleh [mcFirst] Ga keberatan kita join juga ?"
    mc "Silahkan.."
    kk "Bentar lagi [wkk] dan [bl] kesini.. mereka lagi order soalnya"
    na "Wiihhh.. bakalan ramai nihh"
    kk "Heii Kalian sinii"
    wkk "Ealah,, disini toh loh ada Nada sama [mcFirst] juga"
    na "Yooo"
    bl "Lahh,, aku kok ditinggal [wkk]"
    wkk "Hahahha Maaf-maaf"
    bl "Jarang loh liat [mcFirst] datang ke kantin"
    mc "Soalnya aku sering bawa bekal"
    kk "Hooo.. Pantes saja kamu selalu di kelas meskipun waktunya istirahat"
    mc "Hahahah"
    na "Dah dah Skuy makan"
    bl "Okk dah"
    "Hmm Ini tidak begitu buruk makan bersama teman-teman andaikan dulu aku waktu smp seperti ini"
    kk "Ada apa ? [mcFirst] mulai tadi melamun saja"
    mc "Ahh.. gapapa"
    "~Kami pun makan bersama setelah itu kami pun langsung kembali ke kelas~"
    mc "Bentar aku mau beli camilan buat nanti takut habis"
    na "okk kalau gitu aku duluan balik ke kelas"
    mc "Mungkin aku bisa membelikannya Sesuatu sebagai rasa terima kasih membangunkanku"
    hide nada_uni with dissolve

    label minuman:
        $ sc = 3000
        $ ss = 3000
        $ fn = 3000
        $ ip = 3000
        $ gm = 4500

        menu:
            "Susu Coklat":
                "Harga Rp. [sc],-"
                menu:
                    "Aku beli Susu Coklatnya":
                        kt "Mau Beli Berapa ?"
                        $ jm = renpy.input("Masukkan Jumlah yang ingin dibeli: ", "", allow="0123456789")
                        $ jm = int(jm)
                        $ sct = jm * sc
                        mc "Beli [jm] Berapa totalnya ? "
                        kt "Totalnya [sct]"

                        if (money >= sct):
                            $ money = money - sct
                            kt "Terima kasih sudah membeli, Ini Kembaliannya %(money)d"
                            kt "Mau Tambah apa lagi ?"
                            menu:
                                "Makanan":
                                    jump makanan
                                "Minuman":
                                    jump minuman
                                "Tidak usah":
                                    kt "Baiklah, kalau gitu"
                        else:
                            "Uangku tidak Cukup..."
                    "Maaf, Tidak jadi..":
                        kt "Iya Gapapa"
            "Susu Strawberry":
                "Harga Rp. [ss],-"
                menu:
                    "Aku beli Susu Strawberrynya":
                        kt "Mau Beli Berapa ?"
                        $ jm = renpy.input("Masukkan Jumlah yang ingin dibeli: ", "", allow="0123456789")
                        $ jm = int(jm)
                        $ sst = jm * ss
                        mc "Beli [jm] Berapa totalnya ? "
                        kt "Totalnya [sst]"

                        if (money >= sst):
                            $ money = money - sst
                            kt "Terima kasih sudah membeli, Ini Kembaliannya %(money)d"
                            kt "Mau Tambah apa lagi ?"
                            menu:
                                "Makanan":
                                    jump makanan
                                "Minuman":
                                    jump minuman
                                "Tidak usah":
                                    kt "Baiklah, kalau gitu"
                        else:
                            "Uangku tidak Cukup..."
                    "Maaf, Tidak jadi..":
                        kt "Iya Gapapa"
            "Floridana":
                "Harga Rp. [fn],-"
                menu:
                    "Aku beli Floridana":
                        kt "Mau Beli Berapa ?"
                        $ jm = renpy.input("Masukkan Jumlah yang ingin dibeli: ", "", allow="0123456789")
                        $ jm = int(jm)
                        $ fnt = jm * fn
                        mc "Beli [jm] Berapa totalnya ? "
                        kt "Totalnya [fnt]"

                        if (money >= fnt):
                            $ money = money - fnt
                            kt "Terima kasih sudah membeli, Ini Kembaliannya %(money)d"
                            kt "Mau Tambah apa lagi ?"
                            menu:
                                "Makanan":
                                    jump makanan
                                "Minuman":
                                    jump minuman
                                "Tidak usah":
                                    kt "Baiklah, kalau gitu"
                        else:
                            "Uangku tidak Cukup..."
                    "Maaf, Tidak jadi..":
                        kt "Iya Gapapa"
            "GoodMaut":
                "Harga Rp. [gm],-"
                menu:
                    "Aku beli GoodMaut":
                        kt "Mau Beli Berapa ?"
                        $ jm = renpy.input("Masukkan Jumlah yang ingin dibeli: ", "", allow="0123456789")
                        $ jm = int(jm)
                        $ gmt = jm * gm
                        mc "Beli [jm] Berapa totalnya ? "
                        kt "Totalnya [gmt]"

                        if (money >= gmt):
                            $ money = money - gmt
                            kt "Terima kasih sudah membeli, Ini Kembaliannya %(money)d"
                            kt "Mau Tambah apa lagi ?"
                            menu:
                                "Makanan":
                                    jump makanan
                                "Minuman":
                                    jump minuman
                                "Tidak usah":
                                    kt "Baiklah, kalau gitu"
                        else:
                            "Uangku tidak Cukup..."
                    "Maaf, Tidak jadi..":
                        kt "Iya Gapapa"
            "Ifresh Person":
                "Harga Rp. [ip],-"
                menu:
                    "Aku beli Ifresh Person":
                        kt "Mau Beli Berapa ?"
                        $ jm = renpy.input("Masukkan Jumlah yang ingin dibeli: ", "", allow="0123456789")
                        $ jm = int(jm)
                        $ ipt = jm * ip
                        mc "Beli [jm] Berapa totalnya ? "
                        kt "Totalnya [ipt]"

                        if (money >= ipt):
                            $ money = money - ipt
                            kt "Terima kasih sudah membeli, Ini Kembaliannya %(money)d"
                            kt "Mau Tambah apa lagi ?"
                            menu:
                                "Makanan":
                                    jump makanan
                                "Minuman":
                                    jump minuman
                                "Tidak usah":
                                    kt "Baiklah, kalau gitu"
                        else:
                            "Uangku tidak Cukup..."
                    "Maaf, Tidak jadi..":
                        kt "Iya Gapapa"

    label makanan:

        $ rsp = 3500
        $ rism = 2000
        $ mgj = 7000
        $ ngj = 8000
        $ rtp = 5000
        menu:
            "Roti Sosis Panggang":
                "Harga Rp. [rsp],-"
                menu:
                    "Aku beli Roti Sosisnya":
                        kt "Mau Beli Berapa bungkus ?"
                        $ jm = renpy.input("Masukkan Jumlah yang ingin dibeli: ", "", allow="0123456789")
                        $ jm = int(jm)
                        $ rspt = jm * rsp
                        mc "Beli [jm] Berapa totalnya ? "
                        kt "Totalnya [rspt]"

                        if (money >= rspt):
                            $ money = money - rspt
                            kt "Terima kasih sudah membeli, Ini Kembaliannya %(money)d"
                            kt "Mau Tambah apa lagi ?"
                            menu:
                                "Makanan":
                                    jump makanan
                                "Minuman":
                                    jump minuman
                                "Tidak usah":
                                    kt "Baiklah, kalau gitu"
                        else:
                            "Uangku tidak Cukup..."
                    "Maaf, Tidak jadi..":
                        kt "Iya Gapapa"
            "Roti Isi Selai Melon":
                "Harga Rp. [rism],-"
                menu:
                    "Aku beli Roti Isi Selai Melonnya":
                        kt "Mau Beli Berapa bungkus ?"
                        $ jm = renpy.input("Masukkan Jumlah yang ingin dibeli: ", "", allow="0123456789")
                        $ jm = int(jm)
                        $ rismt = jm * rism
                        mc "Beli [jm] Berapa totalnya ? "
                        kt "Totalnya [rismt]"

                        if (money >= rismt):
                            $ money = money - rismt
                            kt "Terima kasih sudah membeli, Ini Kembaliannya %(money)d"
                            kt "Mau Tambah apa lagi ?"
                            menu:
                                "Makanan":
                                    jump makanan
                                "Minuman":
                                    jump minuman
                                "Tidak usah":
                                    kt "Baiklah, kalau gitu"
                        else:
                            "Uangku tidak Cukup..."
                    "Maaf, Tidak jadi..":
                        kt "Iya Gapapa"
            "Mie Goreng Jawa":
                "Harga Rp. [mgj],-"
                menu:
                    "Aku beli Mie Goreng Jawa":
                        kt "Mau Beli Berapa bungkus ?"
                        $ jm = renpy.input("Masukkan Jumlah yang ingin dibeli: ", "", allow="0123456789")
                        $ jm = int(jm)
                        $ mgjt = jm * mgj
                        mc "Beli [jm] Berapa totalnya ? "
                        kt "Totalnya [mgjt]"

                        if (money >= mgjt):
                            $ money = money - mgjt
                            kt "Terima kasih sudah membeli, Ini Kembaliannya %(money)d"
                            kt "Mau Tambah apa lagi ?"
                            menu:
                                "Makanan":
                                    jump makanan
                                "Minuman":
                                    jump minuman
                                "Tidak usah":
                                    kt "Baiklah, kalau gitu"
                        else:
                            "Uangku tidak Cukup..."
                    "Maaf, Tidak jadi..":
                        kt "Iya Gapapa"
            "Nasi Goreng Jawa":
                "Harga Rp. [ngj],-"
                menu:
                    "Aku beli Nasi Goreng Jawa":
                        kt "Mau Beli Berapa bungkus ?"
                        $ jm = renpy.input("Masukkan Jumlah yang ingin dibeli: ", "", allow="0123456789")
                        $ jm = int(jm)
                        $ ngjt = jm * ngj
                        mc "Beli [jm] Berapa totalnya ? "
                        kt "Totalnya [ngjt]"

                        if (money >= ngjt):
                            $ money = money - ngjt
                            kt "Terima kasih sudah membeli, Ini Kembaliannya %(money)d"
                            kt "Mau Tambah apa lagi ?"
                            menu:
                                "Makanan":
                                    jump makanan
                                "Minuman":
                                    jump minuman
                                "Tidak usah":
                                    kt "Baiklah, kalau gitu"
                        else:
                            "Uangku tidak Cukup..."
                    "Maaf, Tidak jadi..":
                        kt "Iya Gapapa"
            "Roti isi Pentol":
                "Harga Rp. [rtp],-"
                menu:
                    "Aku beli Roti Isi Pentol":
                        kt "Mau Beli Berapa bungkus ?"
                        $ jm = renpy.input("Masukkan Jumlah yang ingin dibeli: ", "", allow="0123456789")
                        $ jm = int(jm)
                        $ rtpt = jm * rtp
                        mc "Beli [jm] Berapa totalnya ? "
                        kt "Totalnya [rtpt]"

                        if (money >= rtpt):
                            $ money = money - rtpt
                            kt "Terima kasih sudah membeli, Ini Kembaliannya %(money)d"
                            kt "Mau Tambah apa lagi ?"
                            menu:
                                "Makanan":
                                    jump makanan
                                "Minuman":
                                    jump minuman
                                "Tidak usah":
                                    kt "Baiklah, kalau gitu"
                        else:
                            "Uangku tidak Cukup..."
                    "Maaf, Tidak jadi..":
                        kt "Iya Gapapa"

    "~Ding Dong~"
    "Ternyata sudah Bel Aku harus bergegas"

    scene lorong_siang with dissolve
    "Huufftt... Hufftt... Hufttt..."
    "Mungkin ini sudah cukup, sebagai rasa terima kasih membangunkanku"
    
    scene kelas with dissolve
    mc "Ini sebagai rasa terima kasihku telah membangunkanku tadi"
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Ga usah repot-repot"
    mc "Gapapa ambil saja.. "
    mg3 "Baiklah kalau gitu"
    hide airin_uni with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat malam anak-anak"
    sk "Lah.. tadi pagi selamat sore sekarang siang selamat malam"
    sk "Ihh Bu Senda ini"
    sr "Heheheh Becanda. Ternyata Kalian masih semangat ya"
    sr "Tumben, Biasanya siang-siang gini dah lesu"
    sk "Itu mah perasaannya Bu Senda aja kali hehehe"
    sr "Dasar kalian yaa"
    sk "hahahahha.. Ampun Bu ampun haha"
    sr "Sudah Sudah mari kita mulai saja ya"
    sr "Oiyaa, Seperti kemarin berkelompok lagi ya terus ibu mau rapat lagi kemungkinan sebentar lagi pulang"
    sr "Sekelompok 4 orang sekelas ini ada 35 orang"
    sr "Sisanya bisa bikin kelompok sendiri bisa bergabung sama temannya"
    sr "Tentuin sendiri kelompoknya ya"
    hide bu_senda with dissolve
    "Hmm... Kelompok lagi kelompok lagi. sepertinya aku ga menemukan kelompok"
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Mau kelompokan sama aku ?"
    mc "Bukannya sudah cukup ?"
    mg3 "tapi kan sisanya boleh bergabung ke kelompok mana pun"
    mc "Kelompokmu ada siapa aja ?"
    $ nd = "Nindi"
    $ st = "Shinta"
    mg3 "Ada aku, [nd], [skce2], [st]"
    mc "Aku aja nih lakinya ? Kalau kelompoknya [na] ada siapa aja ?"
    mg3 "Kayaknya sudah 5"
    mc "...."
    mc "Yaudah lah aku masuk kelompokmu aja"
    mg3 "Okie"
    hide airin_uni with dissolve
    show bu_senda at center with dissolve:
        ypos 1.2
    sr "Apa Semua sudah dapat kelompok ?"
    sr "Kalau gitu ini tugasnya"
    sk "Baik bu.."
    "~Ding Dong~"
    sr "Ternyata sudah bel pulang, kalau gitu ibu akhiri saja untuk hari ini"
    sr "Oiya, Jangan lupa dikerjakan ya"
    sk "Baik Buu"
    sr "Kalau gitu Ibu ke ruang guru dulu"
    hide bu_senda with moveoutright
    sk "Iyaa bu"
    nd "Mau kerumahnya siapa ? Kerja kelompoknya"
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Dirumahku atau [st] ? Rumahmu juga gapapa sih"
    nd "Kalau dirumahnya [mcFirst] Bagaimana ?"
    skce2 "Boleh juga itu"
    mc "...."
    mc "Jangan dirumahku soalnya semuanya pada keluar jadi rumahku dikunci"
    nd "Kamu ga dititpin kunci ?"
    mc "Ga soalnya setiap pulang sekolah sudah ada dirumah"
    mc "Berhubung sekarang pulang lebih awal jadi dirumahku ga ada siapa-siapa"
    mc "Saranku dirumahnya kalian aja"
    mg3 "Kalau gitu rumahmu aja Nin gimana ?"
    skce2 "Bagaimana kalau Kerja kelompok di taman kota ?"
    mg3 "Boleh juga itu"
    nd "Yaudah kalau gitu di taman kota aja"
    mc "Aku ngikut aja"
    st "Aku sih ok ok aja"
    hide airin_uni with dissolve

    scene gerbang_sekolah_siang with dissolve
    nd "sudah rede semua ini kan ?"
    st "Tinggal Berangkat saja ini"
    show airin_uni at center with dissolve:
        ypos 1.2
    $ mgol = "[mg3_First] dan [skce2]"
    mgol "Gass dah rede nih"
    nd "Kalau gitu Joss berangkat kita"
    hide airin_uni with dissolve

    scene central_park with dissolve
    skce2 "Yeayy Sudah sampai"
    nd "Kita kerjain langsung apa pesan sesuatu dulu ?"
    st "Pesan dulu aja dong di FoodCourtnya sekalian kerjain disana"
    mc "Aku ngikut aja"
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Yauda, Pesan aja dulu sambil nunggu camilan ama minumannya datang kita kerjain aja"
    hide airin_uni with dissolve

    scene foodcourt with dissolve
    skce2 "Kalian mau pesan apa gaes ?"
    nd "Aku minumnya pesan Es Jeruk aja"
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Aku pesan jus jambu aja"
    st "Aku pesan Es Jeruk juga"
    mc "Milkshake Vanilla"
    skce2 "Kalau gitu Es Jeruk 2, Jus Jambu 1, Milkshake Vanilla 1"
    skce2 "Kalau camilannya pesen apa ini ? yang sekiranya bisa dibuat makan bersama"
    nd "Kalau gitu Kentang Goreng 2 terus Pisang coklat 1"
    mg3 "Nugget jugaa 2 sama tempe goreng 2"
    skce2 "Okk dah kalau gitu aku pesanin dulu ya"
    st "Ehh.. tunggu dulu tambah itu juga Tahu Crispy 1"
    skce2 "Okie Doki"
    mc "Jadi, berhubung nunnggu pesanan datang kita kerjakan dulu soal dari Bu Senda"
    nd "Boleh"
    mg3 "Yok,, Keluarkan Tugasnya biar cepat selesai"
    st "Skuy"
    hide airin_uni with dissolve

    "~SOAL~" with dissolve
    #Initialize score
    $ quiz3_klasifikasi_score = 0

    label quiz3_klasifikasi:
        $ quick_menu = False

        "1. Pada taksonomi dari kingdom ke spesies, jumlah makhluk hidup yang berbeda dalam setiap takson akan …."
        menu:
            "A. semakin banyak":
                $ quiz3_klasifikasi_score += 0
            "B. semakin sedikit":
                $ quiz3_klasifikasi_score += 10
            "C. berubah-ubah":
                $ quiz3_klasifikasi_score += 0
            "D. tetap":
                $ quiz3_klasifikasi_score += 0

        "2. Padi memiliki nama ilmiah Oryza sativa. Kata Oryza merupakan petunjuk nama …. "
        menu:
            "A. spesies":
                $ quiz3_klasifikasi_score += 0
            "B. kelas":
                $ quiz3_klasifikasi_score += 0
            "C. familia":
                $ quiz3_klasifikasi_score += 0
            "D. genus":
                $ quiz3_klasifikasi_score += 10 

        "3. Semakin dekat hubungan kekerabatan makhluk hidup, maka akan semakin banyak …. "
        menu:
            "A. perbedaan sifat":
                $ quiz3_klasifikasi_score += 0
            "B. keragamannya":
                $ quiz3_klasifikasi_score += 0
            "C. persamaan sifat":
                $ quiz3_klasifikasi_score += 10
            "D. keunikannya  j":
                $ quiz3_klasifikasi_score += 0

        "4. Kelompok yang memiliki jumlah individu paling banyak adalah …."
        menu:
            "A. genus":
                $ quiz3_klasifikasi_score += 0
            "B. kelas":
                $ quiz3_klasifikasi_score += 0
            "C. spesies":
                $ quiz3_klasifikasi_score += 10
            "D. familia":
                $ quiz3_klasifikasi_score += 0
            
        "5. Euglena kurang cocok jika hanya dimasukkan dalam animalia, karena Euglena juga memiliki ciri yang dimiliki oleh Plantae, yaitu …."
        menu:
            "A. cara makannya autotrof":
                $ quiz3_klasifikasi_score += 10
            "B. selalu bergerak":
                $ quiz3_klasifikasi_score += 0
            "C. cara hidup berkoloni":
                $ quiz3_klasifikasi_score += 0
            "D. cara makannya heterotrof j":
                $ quiz3_klasifikasi_score += 0

        "6. Spora pada tumbuhan paku apabila jatuh pada tempat yang cocok akan tumbuh menjadi..."
        menu:
            "A. Tumbuhan paku":
                $ quiz3_klasifikasi_score += 0
            "B. Generasi sporofit":
                $ quiz3_klasifikasi_score += 0
            "C. Protonema":
                $ quiz3_klasifikasi_score += 0
            "D. Protalium":
                $ quiz3_klasifikasi_score += 10

        "7. Berikut ini ciri-ciri tumbuhan lumut Salah satu ciri khas yang membedakan ganggang dengan jamur adalah …. "
        menu:
            "A. ganggang tidak berklorofil":
                $ quiz3_klasifikasi_score += 0
            "B. jamur tidak berklorofil":
                $ quiz3_klasifikasi_score += 10
            "C. jamur berklorofil":
                $ quiz3_klasifikasi_score += 0
            "D. ganggang bersel satu":
                $ quiz3_klasifikasi_score += 0

        "8. Lumut kerak merupakan tumbuhan …. "
        menu:
            "A. hasil hidup bersama askiometes dengan ganggang":
                $ quiz3_klasifikasi_score += 0
            "B. hasil simbiosis antara jamur dengan lumut ":
                $ quiz3_klasifikasi_score += 10
            "C. gabungan antara tumbuhan paku dengan jamur ":
                $ quiz3_klasifikasi_score += 0
            "D. hasil hidup bersama antara dua jamur":
                $ quiz3_klasifikasi_score += 0

        "9. Bagian pada tumbuhan paku yang menghasilkan sel kelamin jantan adalah …. "
        menu:
            "A. arkegonium ":
                $ quiz3_klasifikasi_score += 0
            "B. protalium ":
                $ quiz3_klasifikasi_score += 0
            "C. antheridium ":
                $ quiz3_klasifikasi_score += 10
            "D. sporogonium  j":
                $ quiz3_klasifikasi_score += 0

        "10. Daun tumbuhan paku yang dapat menghasilkan spora disebut daun yang …. "
        menu:
            "A. steril":
                $ quiz3_klasifikasi_score += 0
            "B. hidup":
                $ quiz3_klasifikasi_score += 0
            "C. besar":
                $ quiz3_klasifikasi_score += 0
            "D. fertil  j":
                $ quiz3_klasifikasi_score += 10

        "Jawaban : 
            \n
            1. B \ \ \ \ 3. C \ \ \ \ 5. A \ \ \ \ 7. B \ \ \ \ 9. C
            \n  
            2. D \ \ \ \ 4. C \ \ \ \ 6. D \ \ \ \ 8. B \ \ \ \ 10. D"

        "Nilaiku adalah [quiz3_klasifikasi_score]"

    # Check the quiz 1 score
    if quiz3_klasifikasi_score >= 75:
        # Win
        $ quick_menu = True
        "Kemudian makanannya datang, tugasnya pun sudah selesai juga dan aku makan bersama teman kelas"
        "Aku pikir ini tidak begitu buruk"
        # Did he win? Yes.
        #$ quiz3_win = True
        #$ quiz3_lose = False   
    else:
        # Lose
        "Lumayan susah juga"
        skce2 "Nyerah nih ?"
        mc "Terserah, tapi nilainya dapat jelek"
        menu:
            "Tidak Menyerah":
                skce2 "Iya, dah. Istirahat dulu aja"
                show airin_uni at center with dissolve:
                    ypos 1.2
                mg3 "Iya bener, Istirahat dulu"
                mg3 "Setelah itu lanjut"
                hide airin_uni with dissolve
                $ quiz3_klasifikasi_score = 0
                jump quiz3_klasifikasi
            "Nyerah":
                "Anda gagal sebagai murid"
                "~END~"
                return

    scene foodcourt_sore with dissolve
    skce2 "Capeknyaa Fuuhh.. Makanannya  ga kerasa tinggal segini hahahha"
    mc "[mg3_First] Makannya paling banyak nih hahahhaha"
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Enak saja, makanku yang paling dikit tauu!!"
    mg3 "Kamu itu yang makannya paling banyak"
    st "Iya bener [mcFirst] yang makannya paling banyak"
    mc "Padahal ga"
    nd "Pfffttt.... hahahahhahaha"
    mg3 "Hahhahaa bisa bisanya"
    skce2 "dah dah.."
    nd "Ngomong-ngomong jam berapa ini ?"
    mg3 "Jam 4 sepertinya.. \n Eh sudah sore saja"
    st "Ga nyangka kita selama itu hahaha"
    nd "Hooh"
    skce2 "Kuy,, habisin makanannya setelah itu pulang"
    mc "Sekalian, beres-beres dulu aja"
    skce2 "Iya ya"
    mg3 "Sudah selesai semua kan ?"
    nd "Sudah"
    mg3 "Kuy Pulang.."
    st "Gass"
    skce2 "Bye Bye Kalian"
    nd "Byee.."
    hide airin_uni
    show airin_jalan_uni at center:
        ypos 0.95
    mg3 "Bye bye"
    hide airin_jalan_uni with moveoutleft

    scene jalan_sore with dissolve
    mc "Maaf, aku merepotkanmu"
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Gapapa, ga masalah kok"
    mc "Nanti aku turun di daerah sekolah gapapa, rumahku sudah dekat soalnya"
    mg3 "Gapapa kok sampai rumahmu"
    mc "Hmm.. Yuadah kalau kamu memaksa"
    hide airin_uni with dissolve

    scene depan_rumah_sore with dissolve
    show airin_uni at center with dissolve:
        ypos 1.2
    mg3 "Jadi, ini rumahmu sejalur ya dengan rumahku terus dekat sekali dengan sekolah pantas saja kamu sering kulihat jalan kaki kalau pulang"
    mc "Hahahha Memang dekat.. \n kalau rumahmu dimana ?"
    mg3 "Tinggal lurus saja, kalau mau jalan kaki bisa sih"
    mc "Ahh.. okk, mau mampir ?"
    mg3 "ga usah aku langsungan saja"
    mc "Yaudah,, kalau gitu aku masuk ke rumah dulu"
    mc "Hati-hati dijalan"
    hide airin_uni
    show airin_jalan_uni at center:
        ypos 0.95
    mg3 "Iyaa. sama-sama"
    hide airin_jalan_uni with moveoutleft

    scene ruang_tamu_sore with dissolve
    mc "Aku pulang!!"
    show cat at center with moveoutbottom:
        ypos 0.775
    cat "Meooww"
    mc "Woahh,, [cat] hahahaha"
    hide cat with dissolve

    scene ruang_keluarga_sore with dissolve
    show mom at center with dissolve:
        ypos 1.15
    mom "Selamat datang"
    mc "Bu,, Mungkin aku akan skip makan malam ahhah"
    mom "Loh,, kenapa ? kamu sakit ?"
    mc "Ga kok bu.. cuma kekenyangan saja tadi makan banyak sekali"
    mom "hoooo.. syukurlah [mom] kira kamu sakit"
    mc "ga kok bu Hahahha"
    mc "Kalau gitu aku tidur dulu ya bu"
    mom "Iyaa nak.."
    mom "Kalau mau ikut makan malam nanti Ibu siapkan juga tinggal ambil di kulkas"
    mc "Iyaa bu hehehhe"
    hide mom with dissolve

    scene kamar_sore with dissolve
    "Saatnya tidur.. Fuuhh"

    jump day4_Airin