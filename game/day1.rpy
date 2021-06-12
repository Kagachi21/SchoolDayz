label day1_Miselia:

    hide screen gotoMiselia
    hide screen gotoKirana
    hide screen gotoAirin

    scene jalan 
    mc "Pak Angkot pak"
    $ sa = "Sopir Angkot"
    sa "Mau kemana nak ?"
    mc "ke SMAN 05 Pak"

    scene angkot
    $ itt = "Ibu Tua Renta"
    mc "Bu sepertinya ibu kedinginan, ini saya ada jaket pakai saja"
    itt "Wah terimakasih nak, baik banget kamu,sekolah dimana kamu nak ? kok naik angkot berangkatnya "
    mc "Saya sekolah di SMA 5 bu,itu di depan sudah samapi sekolah saya"
    itt "wah, yasudah sekolah yang pinter dan rajin ya nak "

    scene lorong
    "Wah jaket ku ketinggalan di angkot , ya Allah kelupaan"
    mg1 "Hey kamau ngapain berdiri di sini?"
    mc "Itu , jaketku tertinggal di angkot yang ku naiki tadi sel"
    scene kelas
    mc "Ini kamu yang ngelempr kertasnya ?"
    sr "Selamat pagi anak2 ,bagaimana kabarnya hari ini ?"
    sk "Selamat pagi juga buu, alhamdulillah sehat "

    "Materi klasifikasi"
    mg1 "Mc ayo kita makan ke kantin , ku traktir deh "
    mc "Okey deh, ayo"

    scene kantin
    mg1 "Kamu kenapa kok diem aja ,apakah ada masalah?"
    mc "Nggak kok gk ada apa2 "
    mg1 "Makanannya enak ya , kamu suka gak"
    mc "Iya enak,ayo lekas ke kelas waktu istirahat hampir habis "
    mg1 "Huuu cpet bgt si pdhl msh kurang 10 menit "
    mc "Iya aku ada sesuatu yg mau aku kerjakan "

    "KUIS KUIS"

    scene lorong
    $ rta = "Rita"
    mg1"Hei mc , apakah kamu baik baik saja?"
    mg1"Hey mc aku ingin bertanya , apakah aku membuat kesalahan ke kamu ?"
    mc "Tidak kok tidak ada apa2 sampai jumpa ya aku buru2 ni"
    mg1 "Mc ... mc.. jangannn pergi dulu bentarrr"
    rta "Kamu manggili siapa sel, teriakanmu kok kenceng banget"
    mg1 "Iya itu , mc ku panggil malah nerus aja jalannya "

    jump day2_Miselia
    

label day1_Kirana:
    
    scene jalan

    hide screen gotoMiselia
    hide screen gotoKirana
    hide screen gotoAirin

    scene lorong kelas
    "Akhh.. Aku Menabrak sesuatu"
    mc "ahh.. Maaf Kak, aku tidak sengaja"
    $ kk = "Kakak Kelas"
    kk "Kamu anak kelas kamu anak kelas brapa ? kalo jalan tuh pakai mata dong !!"
    mc "iiya kak,, aku kelas 10, sekali lagi aku minta maaf ya"
    "Mungkin aku harus lari saja agar terhindar dari masalah"
    kk "loh eh eh mau kemana kamu ?"
    kk "Anak Baru Banyak belagu sekarang ya !!"

    scene depan kelas 
    "Huft.. Huftt.. Hufft.."
    "Sudah aman kah ? sepertinya sudah aman"

    scene kelas
    "Seperti biasa suasananya sangat ramai.. Sigh.."
    "Lebih baik aku duduk dulu dan menggambar sembari nunggu bel masuk"
    "~Tuingg"
    "Hmm apa Botol ? Siapa yang melempar ? Biar dah"
    skce2 "Ehhh... Maaf Maaf aku ga sengaja, ngelempar kena kamu"
    mc "hmm.. iyaa gapapa"
    "AKu Melihat ada cewe menghampiriku"
    mg2 "Kamu gapapa ?"
    mg2 "Pusing tidak ?"
    mg2 "Ikut aku ke UKS ya"
    mc "gapapa, aman"
    mg2 "oh okey baiklah kalo kamu gakenapa-napa. aku duduk sini ya sebelahmu oke ?"
    mc "haa ?"
    mg2 "Emang Kenapa ?"
    mc "Hmm.. Ok"
    mg2 "Makasih"
    na "Cie cie ada apa ini ? kok Duduknya sebelahan"
    mc "Diam Kau"
    "~Ding Dong~"
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
    #Materi Fungi
    "~Sesi Materi~"
    "~Ding Dong~"
    "Aku malas sekali mau pergi ke kantin"
    na "[mcFirst] ikut ke kantin ?"
    mc "Ga ikut"
    na "Titip Lur ?"
    mc "Ga usah"
    na "Kalau gitu aku ke kantin dulu bro"

    mg2 "Kamu ga mau ikut nada ke kantin ?"
    mc "Ga"
    mg2 "Lahh Kenapa ?"
    mc "Mager, terlalu banyak orang orang"
    mg2 "Beneran ga ikut ? Soalnya, aku dengar dengar ada pentol enak di kantin"
    mg2 "ayoo , ikut ke kantin, beli pentol enduls"
    mc "Ga mau"
    mg2 "kamu harus ikut lah"
    mc "aku titip aja ya na, gappa kan ? Aku capek soalnya."
    mg2 "nggakk, kamu harus ikuutt!!"
    "Merepotkan.."

    scene kantin
    mg2 "Sana cari tempat tunggu sana biar aku yang pesenin"
    mc "...."
    "Terlalu Ramai disini Hmm.. "
    "AKu Menyesal ikut kesini, kalau gitu aku ke [mg2_First] aja"
    mg2 "eehhhh,, ngapainn kesini? katanya males, disuruh tunggu sana , malah milih kesini hm. ini loh udah selesai"
    mg2 "nanti malah ga ketemu tempat duduk"
    kt "Ini mbak Pentol Pedesnya"
    mg2 "makasih bu "
    mg2 "Mana ya tempat duduk ?"
    mg2 "Tuhkan ga ada "
    mc "M-maaf"
    mg2 "dah lah ayok balik ke kelas aja"

    scene kelas
    mg2 "Oiyaa, Kamuu itu murid yang dibully parah waktu smp dulu kan ?"
    mc "...."
    mc "Siapa itu ?"
    mc "Sudah sudah, nanti pentolnya jadi ga enak karena dingin Mending kita makan"
    mg2 "hmm... Iyaa"
    "Ternyata rasanya enak, ga begitu buruk juga"
    "Aku pikir rasanya biasa biasa aja"
    "~Ding Dong~"

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

    #Initialize score
    $ quiz1_score = 0

    label quiz1:

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
            1. A    3. C    5. A    7. B    9. D
            2. C    4. B    6. D    8. C    10. A"

        "Nilaiku adalah [quiz1_score]"

    # Check the quiz 1 score
    if quiz1_score >= 75:
        # Win
        sr "Selamat Bagi yang Nilainya Bagus"
        sr "Kalian bebas melakukan apa saja sampai waktu pelajaran habis"
        # Did he win? Yes.
        #$ quiz1_win = True
        #$ quiz1_lose = False   
    else:
        # Lose
        sr "Bagi yang Nilainya jelek bisa mengulang lagi"
        menu:
            "Mengulang Lagi":
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

    "~Ding Dong~"
    sk "Yeay Sudah Pulang"
    sr "Baik Anak - Anak sekian dari Ibu"
    sr "Kalian sudah boleh pulang"
    
    mg2 "Pulangg yuuk [mcFirst]"
    mg2 "Aku bawa Sepeda Motor, biar makin cepet gitu"
    mc "Ga usah, Rumahku ga begitu jauh juga"
    mg2 "Aku sekalian biar tau rumahmu Hehehe"
    mc "...."
    mc "ga usah repot repot, Terima kasih atas tawarannya aku jalan saja"

    scene jalan 
    mc "Ngapain ikutin aku segala ?"
    mg2 "Aku pengen tau rumahmu juga"
    mc "...."
    mc "Yaudah, sini sini aku yang nyetir"
    mg2 "Yeayyy"

    scene depan rumah
    mc "Makasih ya.. sudah sana pulang"
    mg2 "Hai.. Haii.."
    mom "Lohh,, [mcFirst] temannya ga disuruh mampir dulu ?"
    mc "ehh, gak gak gak, gausa bu, biarin arda pulang "
    mc "Dia terburu - terburu"
    mg2 "heh, apa an si kamu ? iyaa te arda mampir dulu"
    mg2 "arda parkir motor dulu ya "
    mom "Iyaa Parkir disana ya "
    mom "Siapa Namamu ?"
    mg2 "Nama Saya [mg2] te"
    mom "Tante baru tau kalau [mcFirst] ternyata sudah punya teman"
    mg2 "Hehehe.. Iya te"
    mc "...."
    mom "Marii Masuk Tante siapkan Makanan dulu. Pasti kalian lapar kan ?"
    mg2 "Yeayy, Iya te hehhe"
    mc "...."
    mc "Aku mau ganti baju dulu"

    scene ruang tamu
    mom "Nak Arda tunggu sini ya"
    mg2 "Iyaa te hehe"
    mom "[mcFirst] Kalau sudah ganti baju temani dulu si [mg2_Last] !!"
    mc "Iya !!!"
    mg2 "Kalau gitu aku lihat lihat hal sekitar ya te"
    mom "Iyaa nak"

    scene dapur
    mg2 "Tante Tante ini foto siapa ? "
    mom "Itu Fotonya [mcFirst]"
    mg2 "Hahahahah Lucu Banget te"
    mom "Bener kan"
    "Ada apa ini ramai ramai di dapur ?"
    mg2 "Ahhh Orangnya sudah ada disini"
    mg2 "Lihat - Lihat fotomu masih kecil lucu sekali"
    mg2 "Hahahaha"
    mc "...."
    mc "kan resek banget sih jadi cewe"
    mc "Mana Fotonya ?"
    mg2 "Maaf maaf.. Habisnya lucu banget"
    mg2 "ini Fotonya"
    mc "kalau gitu aku taruh ini dulu"
    mom "Makanannya sudah siap"
    mg2 "Okay te Makasih banyak tante"

    scene ruang tamu
    mc "Bisa bisanya dia lihat fotoku"
    mc "Merepotkan"

    scene dapur 
    mg2 "Sini Sini Makan. maaf aku makan duluann hehhe"
    mg2 "Habisnya terlihat enak sih"
    mc "...."
    mc "Kalau sudah selesai segera pulang ya"
    mc "Biar ga kemalaman"
    mg2 "ahahaha Iyaa"
    mom "Gimana [mg2_Last] makanannya ?"
    mg2 "Wuiihh Enakk Tante masakannya tante"
    mg2 "Top Markotop !!"
    mom "Bisa aja kamu ini"
    "Kami pun makan dengan lahap. Lalu [mom] bermain bersama [cat]"
    mg2 "Kenyangnyaa~"
    mg2 "Saatnya cuci Piring"
    mom "Ga usah nak arda biar tante aja yang cuci piringnya"
    mg2 "Gapapa te soalnya Arda sudah ngerepotin Tante dan [mcFirst] juga"
    mg2 "[mcFirst] ayoo temenin aku cuci piring"
    mc "Iya"
    mg2 "Fuuhh Sudah selesai Cuci Piringnya "
    mg2 "Kalau gitu aku pulang dulu"
    mg2 "Aku mau pamit sama Tante dulu"
    mc "Mungkin ada di Ruang Keluarga"

    scene ruang keluarga
    mg2 "Tante Tante"
    mg2 "Arda Pulang dulu ya takut kelamaan terus ganggu tante sama [mcFirst]"
    mom "Gapapa kok ga ngerepotin malah tante senang"
    mg2 "Iyaa te arda sampai kenyang padahal pertama kali arda kesini loh te"
    mg2 "Tapi sama tante sudah disuguhi banyak makanan"
    mom "Hahaha Iyaa gapapa"
    mg2 "Heheheh Kalau gitu Arda pulang dulu ya te "
    mom "Iyaa hati - hati dijalan"
    mom "makasih juga udah mau nganteri,, anak ibu yang ganteng ini sampai rumah "
    mg2 "Iya te Heheh"

    scene depan rumah
    mc "Terima Kasih [mg2_Last]"
    mc "Hati - Hati dijalan"
    "~Bruumm Brumm~"
    "Lelahnya lebih baik aku tidur saja"

    jump day2_Kirana

label day1_Airin:
    
    scene jalan

    hide screen gotoMiselia
    hide screen gotoKirana
    hide screen gotoAirin
    "Test"
