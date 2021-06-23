label day5_Kirana:
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
    play sound cuci_piring
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    window show dissolve
    mc "Aku berangkat dulu bu"
    mom "Hati - hati dijalan"

    scene jalan

    scene gerbang_sekolah
    na "Halo Bro"
    mc "Oh Hi"
    na "mau mampir beli jajan dulu ?"
    mc "ga usah, langsung ke kelas aja"
    mc "Kan hari ini mapelnya ga sebanyak hari lainnya"
    na "Oh iya ya"

    scene kelas
    "[mg2_Last] Ternyata belum datang"
    "Kalau gitu aku belajar dulu lah"
    "~Tak Lama Kemudian~"
    mg2 "Wihh,, datang duluan langsung belajar"
    mc "...."
    mg2 "Kemarin, gimana kerkelnya ?"
    mc "Kemarin, waktu kerkel 2 anak tidak datang jadi aku sama [bl] saja yang mengerjakan"
    mc "si [st] katanya jalan-jalan ke mall kalau [ad] nthlah ga bisa dihubungi"
    mc "Nthlah, ntr waktu presentasi gimana mereka itu"
    mg2 "Biarin saja sudah yang penting tugasnya sudah selesai"
    mg2 "Misal yang dapat nilai lebih pasti kamu sama [bl]"
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
    "Setelah semuanya presentasi selesai Bu Senda Memberikan Soal untuk dikerjakan pada kami semua"

    #Initialize score
    $ quiz5_score = 0

    label quiz5:

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

        show virusd5
        "13. Perhatikan tabel di atas ini!
        \n
        Pasangan yang tepat antara virus dan peranan yang merugikan pada manusia adalah ...."
        menu:
            "A. 1B - 2A - 3D - 4E - 5C":
                $ quiz5_score += 8
            "B. 1C - 2A - 3D - 4B - 5E":
                $ quiz5_score += 0
            "C. 1D - 2B - 3A - 4E - 5C":
                $ quiz5_score += 0
            "D. 1B - 2A - 3D - 4E - 5C":
                $ quiz5_score += 0

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

        "Nilaiku adalah [quiz5_score]"

        $ quiz5_score_total = quiz5_score - 20

    # Check the quiz 1 score
    if quiz5_score_total >= 75:
        # Win
        mc "Yang rangkum buat presentasi siapa ?"
        bl "Kita selesaikan juga hari ini semuanya"
        mc "Okie"
        # Did he win? Yes.
        #$ quiz5_win = True
        #$ quiz5_lose = False   
    else:
        # Lose
        bl "Mereka ga ada sama sekali"
        bl "Biar dah ga usah di kerjakan, capek aku"
        bl "Mereka berdua ga ada lagi"
        menu:
            "Semangat":
                rr "Coba dulu lagi, Nanti kalau misal mentok yaudah tinggal aja"
                mc 'Terima Kasih'
                $ quiz5_score = 0
                jump quiz5
            "Pulang saja!":
                "Anda gagal sebagai murid"
                "~END~"
                return

    "~Ding Dong~"
    sk "Sudah Bel Pulang Yeay!!"
    sr "Yaudah kalau gitu anak-anak. Kelasnya saya akhiri sekarang"
    sk "Baik buu"
    mg2 "Kuy Pulang"
    mc "Aku yang ambil sepedamu atau gimana ?"
    mg2 "Iyaa dah kamu aja, aku tunggu di depan gerbang aja"
    mc "Kuncinya ?"
    mg2 "Ini"

    scene gerbang_sekolah_siang
    mg2 "[mcFirst]!!"
    mc "Skuy Naik, kamu mampir rumahku juga ga ?"
    mg2 "Woiya dong, kangen masakan tante hahaha"
    mc "Dasar kau ini"

    scene jalan_siang
    mg2 "Besok kamu ada dirumah ga ?"
    mc "Ada, kenapa emangnya ?"
    mg2 "Kuy, Jalan-jalan"
    mc "hah ?"
    mg2 "...."
    mg2 "Nanti saja pas sampe rumahku kita bahas"
    mc "...."
    mc "Oh Ok"

    scene depan rumah
    mc "Tadi kamu mau bahas apa ?"
    mg2 "Ihh Masuk dulu lah"
    mc "Yaudah, aku parkir dulu"

    scene ruang tamu
    mc "Aku Pulang"
    mg2 "Permisi Tanter"
    mg2 'Kok Sepi ?'
    mc "Pasti [mom] di ruang keluarga"

    scene ruang keluarga
    mg2 "Halo Tante"
    mom "Lahh,, ada kamu toh"
    mg2 "iya te hehehe"
    mom "Lama, ga kesini"
    mg2 "Ga kesempatan tante buat mampir, berhubung hari ini pulangnya lebih cepat jadi yaa mampir"
    mg2 "Lama ga ngicipin makanan tante"
    mg2 "Eh,, mau main sama [cat] aja kok te hehehe"
    mom "Astaga.. Kamu ini hahahah"
    mom "Ngomong-ngomong [mcFirst] mana ?"
    mg2 "lagi salin baju tante"
    mom "Oalah,, aku tadi pagi masak masih ada sisa banyak nih, mau ?"
    mg2 "Wah Mau tante"
    mom "Langsung ambil saja di meja makan ya ajak [mcFirst] makan juga"
    mg2 "Okie Tante"
    mom "kalu gitu Aku mau tidur dulu"
    mom "Soalnya aku capek"
    mg2 "Okie tante"

    scene depan kamar
    "Knock Knock Knock"
    mg2 "[mcFirst] Ayo makan"
    mc "Okk Aku keluar"

    scene dapur_siang
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
    mc "Okk kalu gitu"
    mg2 "yeayyy"
    mg2 "[cat] Yeayy"
    cat "Nyaaa ? "
    mc "...."

    scene depan rumah
    mg2 "Tante masih tidur ya ?"
    mc "Iyaa masih tidur"
    mg2 "Kalau gitu titip salam ke tante ya"
    mc "Okk dah"
    mg2 "Aku pulang dulu"
    mc "Hati-hati dijalan"
    mg2 "Iyaa"

    scene ruang keluarga
    "Fuhh.. Capeknyaa, tidur dulu aja lah "

    scene kamar_malam
    "Hoaamm.. sudah malam ternyata"
    
    scene dapur_malam
    mc "Loh sudah pulang yah"
    dad "Hooo.. tadi kamu ngajak cewe yang waktu itu lagi"
    dad "Sayangnya ayah baru pulang sekarang padahal ingin tahu cewenya yang mana ?"
    mc "Astaga.. tapi besok kesini lagi malam-malam minta temenin belanja"
    dad "Wihh Kerenn"
    mom "Sudah sudah makan dulu ini makanan sudah siap"
    dad "Okie doki bu hahha"
    mom "Astaga,, hahah"
    mc "Ayah kyknya habis kerasukan sesuatu bu"
    mom "Iyaa sepertinya"
    dad "yaa gimana besok ga sabar pengen lihat temenmu hahahha"
    mc "dah dah Lanjut makan lagi"

    "Kami pun lanjut makan, Setelah itu aku pergi kembali tidur lagi"

    jump day6_Kirana

label day5_Miselia:

    scene kamar
    mc "Buk, ibukk...."
    mom "Iya naakkk, ada apa ? ibu lagi di dapur ini"
    mc "Itu buk, kepalaku pusing , badanku terus menggigil"
    mom "Ini nak, makan pisngnya terus minum obat , mupung ini masih jam set 6 , kalo ampe jam set 7 kamu masih menggigil gausa sekolh dulu"
    mc "Iya bukk,, mc minum dulu"
    mom "Loh nak, kamu mandi ? emang badanmu sudah enakan?"
    mc "Iya bu sudah alahmdulillah"
    mom "Oh iya syukur lah, jangan di paksa ya kalau nanti di sekolah kamu ga enak badan, pergi ke uks aja  atau telpon ibu, biar ibu nanti yang kesana "
    mc"Iya ibuu cantikk, anakmu ini akan baik baik saja "
    mom "Kamu iniii sudah di bilangi kokk malah ngegombalin ibukk"
    mc "Hahaha, ibuk ibukk"

    scene ruang tamu 
    mc "Bu aku berangkat sekolah dulu ya"
    mom" Iya nak, hati hati ya "

    scene jalan raya 
    mg1 "Hei , ayo berangkat bareng aku ke sekolah"
    mc "Oke, makasih ya "

    scene gerbang sekolah
    $ jno = "Jino"
    jno "Stop!!"
    mc "Ehh, ada apa ini ? kenapa kamu memberentikan aku ? "
    jno "Sok pura pura gatau lagi! kamu jangan sok tampan ya , kamu di sini tu rendahan jangan coba coba cari perkara sama kaka tingkat ."
    mc "Loh, emang aku nglakuin salah apa ?"
    jno "Kamu gatau , kalo misel ini gebetanku ? kok brani brani nya kamu boncengin dia ke sekolah , nyari mati kamu ha???"
    mc "Loh,, sell ini cuman salah paham tolong kamu bilang ke gebetanmu ini "
    mg1 "Mas aldo  , kita kan cuman temen , ya seharusnya mas aldo gausa marah marah apalagi pake cara kyak gini dong mas,"
    jno "Ya tapi liat dong , kamu itu kan punya ku"
    mg1 "Udah udah, gausa ribut dan di perpanjang, aku sama mc mau masuk kelas dulu , bentar lagi masuk"
    mg1 "Ayooo mc kita ke kelas"
    jno "Sialann.. awas kamu ya urusan kita belum selesai !"
    mg1 "Eh, maafin Jino tadi ya , udah tenang aja kamu ga bakal diapa-apain kok"
    mc "Iya sel"
    mg1 "Kamu ngasih kado ke sapa? "
    mc "Ke Bu sendra, kamu ke siapa ?"
    mg1 "Ke Pak santoso"
    sr "Hallo selamat pagii anak anak sekalian , bagaimana kabar hari ini ? ssemua sehat?"
    mg1 "Alhamduliilah bu sehat"
    sr "Mc kamu apa baik baik saja ?"
    mc  "Tidak bu , saya baik baik saja hehehe, cuman tadi agak sedikit pusing aja "
    sr "Yaudah , kalo kamu tidak kuat silahkan bisa istirahat di ruang uks ya "

    "Materi Virus"

    scene ruang guru 
    $ ss ="Bu Sari"
    mc "Assalamualaikum"
    ss "Waalaikumsalam, iya nak, ada perlu dengan guru siapa ?"
    mc "Itu bu saya sedang mencari bu senda "
    ss "Owalah , yasudah masuk saja , itu bu sendranya lagi duduk di ruangannya"
    mc "Tok tok tok"
    sr "Iya silahkan masuk aja nak"
    mc "Bu ini saya ada kado buat ibu, sederhana semga ibu suka ya"
    sr "Wah terimakasih ya nak "

    scene kelas 

    $ quiz_fungi5_score = 0

    label quiz_fungi5:

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

        show fungid5
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
        hide fungid5

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
        sr "Selamat Bagi yang Nilainya Bagus"
        sr "Kalian bebas melakukan apa saja sampai waktu pelajaran habis"
        # Did he win? Yes.
        #$ quiz_fungi5_win = True
        #$ quiz_fungi5_lose = False   
    else:
        # Lose
        sr "Bagi yang Nilainya jelek bisa mengulang lagi"
        menu:
            "Mengulang Lagi":
                $ quiz_fungi5_score = 0
                jump quiz_fungi5
            "Tidak Ingin Mengulang":
                "Anda gagal sebagai murid"
                "~END~"
                return

    scene lorong 
    mg1 "Kamu mau pulang bareng aku ga ?ayo kalo mau"
    mc "Beneran gapapa ta ? ayo deh"
    mg1 "Yauda aku ambil sepedah dulu ya"

    scene jalan 
    mg1 "Kamu mau mampir dulu ga beli es?"
    mc "Ya kalo kamu mau oke ayo beli sekalian aku"
    mg1 "Oke deh ayo kita beli"
    
    scene depan rumah 
    mc "Makasih ya sudah nganterin aku"
    mg1 "Iya, sama sama , aku pulang dulu"
  
    scene ruang tamu
    mc "Assalamualaikum bu"
    mom "Waalaikumsalam, sudh pulang nak , sana bersihkan cuci kaki, taruh tas nya di kamar dan langsung ke meja makan ya , ibu udah siapkan makannya"
    mc "Iya buk, terimakasih ya , mc ke kamar dulu"

    jump day6_Miselia

label day5_Airin:

    scene kamar
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
    mom "Dimana [dad] ?"
    mc "Katanya [dad] duluan saja"
    mc "Kalau gitu aku duluan makan aja bu soalnya mau masuk sekolah"
    dad "Ayo makan Hehhe maaf nungguin aku"
    mom "Dasar.. ayoo makan"
    "Kami pun makan bersama tak lupa dengan [cat] juga"
    mc "Bu Aku sudah selesai.."
    play sound cuci_piring
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    window show dissolve
    mom "Bentar Ibu siapkan bekalnya.."
    dad "Ini uang sangumu"
    $ money += 10000
    mc "Terima kasih [ai]"
    mom "Ini bekalmu"
    mc "Kalau gitu aku berangkat dulu [ai]"
    ai "Iyaa nak hati-hati dijalan"

    scene jalan
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

    scene gerbang_sekolah
    na "Oee oeee"
    na "Barengan lagi nih berangkatnya"
    mg3 "Iyaa,, seru juga jalan kaki berhubung Sekolahnya deket juga dari arah rumah"
    na "Ha  hahahaha Berarti rumah kalian dekat"
    mc "Ga terlalu dekat agak jauh dikit"

    scene kelas
    sr "Selamat pagi anak-anak"
    sk "Pagi bu"
    sr "Hari ini kita mulai saja ya"
    sk "Iya bu"
    "~Materi Klasifikasi~"
    "~Ding Dong~"
    sr "Waktunya sudah habis anak-anak kalian boleh istirahat"
    sk "Terima kasih bu Senda"
    sr "Kalau gitu Bu senda pergi dulu"
    sk "Baik bu"
    na "Nanti main kerumahmu bro"
    mc "Hmmmm.. Okk"
    na "Bentar aku ajak yang lain juga"
    mc "Hah ? jangan rame-rame"
    na "Gapapa biar heboh"
    mc "Sigh..."
    na "[mg3_First] mau ikut kerumah [mcFirst] ?"
    mg3 "Boleh ada siapa aja ?"
    na "Aku, kamu, [wkk], [kk], [bl] kayaknya ini"
    na "Aku ajak mereka dulu"
    mg3 "Okk"
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
    mc "Aku ga ikut sekarang bawa bekal \n Ehh.. tapi titip aja ini uangnya \n Terserah mau dibelikan apa"
    $ money -= 10000
    na "Okk Bro"
    mc "[mg3_First] mungkin mau titip juga"
    na "Dia ke kantin kayaknya sudah ga ada orangnya"
    mc "ehh.. iya yaudah"
    na "aku duluan bro"
    mc "Okk"
    "Sudahh sepi Huh.. Saatnya aku makan bekalku"
    mc "Fuuh.. Kenyangnya"
    "~Ding Dong~"
    "Sudah bel masuk ternyata"
    na "Broo ini titipnya"
    mc "Makasih,, Kembaliannya ambil saja lur"
    na "Mantap Lucky"
    sr "Hayoo duduk duluu"
    sk "Heheheh Iya bu"
    sr "Selamat Siang anak-anak sudah kah siap untuk belajar lagi siang hari ini ?"
    sk "Tidak bu!!"
    sr "Kalau gitu tidur aja yaa "
    wkk "Ihh Bu Senda.. Kami Bercanda bu"
    sr "Sama Ibu juga Hahahaha"
    sr "Sebelumnya bikin kelompok dulu ya bebas. 1 kelompok terdiri 4 orang"
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
    "Setelah itu kelas ramai dengan memilih kelompok masing-masing"
    sr "Apa sudah membuat kelompok semuanya ?"
    sk "Sudah bu"
    sr "Kalau gitu Bu Senda kasih soalnya.. \n kerjakan dirumah yaa karena ada rapat ntar lagi mungkin sebentar lagi akan pulang"
    sr "Dikumpulkan Besok semuanya harus sudah selesai.. sama bikin presentasi materi ya"
    sk "Baik buu"
    na "Tuhkan, aku instingku benar hahahha \n Jadi,, nanti sekalian ngerjain di rumah [mcFirst]"
    "~Ding Dong~"
    sr "Sudah bel anak-anak kalian boleh pulang"
    sk "Yeayy.. Baik bu.."
    wkk "Kita berangkat sekarang ini ?"
    bl "Ayo-ayo aja sih aku"
    mc "Nunggu sepi baru pulang"
    bl "Heee.. kok gitu"
    mc "gapapa"
    na "Sudah sudah.. \n kalau gitu ada yang beli camilan sisanya langsung ke rumah [mcFirst]"
    wkk "Aku aja kalau gitu"
    bl "Aku ikut juga dong"
    wkk "Okk dah kalau gitu"
    wkk "Aku sama [bl] duluan beli camilan dulu"
    na "Okk dah"
    mg3 "Ayo [mcFirst]"
    mc "Haii.. Haii.."

    scene jalan_siang
    mc "Nanti jangan lupa kabarin mereka \n Shareloc ke mereka"
    mg3 "Iyaa, kalau ga di shareloc nanti bisa tersesat hahaha"
    na "Nanti kalau sudah sampe rumahmu aku shareloc ke mereka"

    scene depan rumah
    mc "Aku Pulang!!"
    $ nmg3 = "Nada dan [mg3_First]"
    nmg3 "Permisi"

    scene ruang tamu
    cat "Miiaauuuww"
    mc "Ahhh... [cat]"
    na "Kamu pnya kucing ? Astaga Lucu bro"
    mg3 "Aaaaa [cat].."
    cat "Miaauuww"
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

    scene ruang keluarga
    mom "Loh,, sudah pulang ? ada teman-temanmu juga"
    na "Halo te"
    mc "Iya bu sekalian kerja kelompok"
    mom "Hohohoh.... \n ehh.. ada [mg3_First] lagi"
    mg3 "Iya te hehheh berhubung sekelompok sama [mcFirst]"
    mc "Ayoo sini ke kamar"
    mom "Hohohoho"
    mc "Oiya,, bu nanti ada temanku lagi 2 mau datang kesini"
    mom "Okie Doki"
    mom "Kalau gitu Ibu siapkan cemilan dulu"
    na "waduh ga usah repot-repot tante"
    mc "Halah gayamu"
    na "Hehehe"

    scene kamar_siang
    mg3 "Baru kali ini aku masuk kamar cowo \n kamarmu rapi sekali ya"
    na "dah biasa cowo kamarnya rapilah kamarku ya juga rapi hahaha"
    mg3 "Kukira kamar cowo itu berantakan"
    mc "ga juga \n Semuanya itu tergantung orangnya juga"
    mg3 "Bener sih"
    "~[mcFirst]!!!!! ~[mcFirst]!!!!! ~[mcFirst]!!!!!"
    mc "Kayaknya mereka sudah datang"

    scene rumah depan
    mom "OyaaOyaa... Temannya [mcFirst]"
    wkk "Iya te.. [mcFirst] ada ?"
    mom "Ada silahkan masuk.. "
    bl "Kalau gitu permisi tante"
    wkk "Permisi tante"
    wkk "[mcFirst] ada dimana te?"
    mom "Langsung aja ke kamarnya"
    bl "Kalau gitu permisi dulu tante"
    mom "Silahkan silahkan"

    scene kamar_siang
    bl "Kami Boleh masuk ini ?"
    wkk "Hayoo.. Kalian lagi ngapain ?"
    mc "Masuk saja"
    bl "Wahh... Rapi banget.. \n bahkan kamarku ga serapi ini"
    mc "Biasa aja"
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
    mg3 "Iyaa biar cepet selesai"
    cat "Miaauuuuwww"
    mg3 "Lohh ada kamu dibelakangku"
    bl "Aaaaaa... Kucingnya comel"
    bl "Siapa namanya ?"
    mc "Namanya [cat]"
    bl "Artinya apa ?"
    mc "Bahagia"
    bl "heeee.. baguss.."
    mom "Ini Cemilan sudah tante siapin"
    mom "Dimakan yaa"
    wkk "Ehh.. Tanter ga usah repot-repot kami sudah beli cemilan"
    mom "Tak apa,, ini Home madenya tante sendiri"
    wkk "Wahh.. kalau gitu terima kasih tante"
    mom "Oyaoya Tante baru tau banyak temen kesini tau gitu tante masak besar"
    mom "Yaudah,, kalau gitu selamat mengerjakan \n Sini [cat].."
    cat "Miauuuww hssss"
    mom "Ehh.. jadi ganas"
    $ all = "Semuanya"
    all "Hahahahha"
    mg3 "[cat] maunya sama aku te hahahah"
    mom "Huhuhuuhuhu... Sedih..."
    mom "Hehehhe silahkan menikmati waktunya"
    mc "Dah dah.. Mari Kerjakan.."
    na "Ayoo.. ada camilan juga ini bakal semangat"
    mg3 "Lets go!!"

    #Initialize score
    $ quiz5_klasifikasi_score = 0

    label quiz5_klasifikasi:

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
        bl "Akhirnya sudah selesai.."
        wkk "Jajannya enak"
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
    "Kami pun bermain Kartu hingga sore"
    wkk "Wahh.. sudah jam segini.. Aku pulang dulu kalau gitu"
    bl "Ehh.. iya sudah jam segini.. kalau gitu aku pulang dulu"
    na "Aku juga"
    mc "Okayy.."
    
    scene ruang keluarga
    mc "Bu, Temanku pulang"
    mom "Ehh.. kok cepet ? \n Ga sampai malam ?"
    wkk "hehehhe Ga tante"
    mom "Yaudah kalau gitu"
    bl "Maaf ngerepotin tante"
    mom "Gapapa, tante malah senang kalian datang"
    bl "Hehehe.. iya te"
    $ wbn = "[wkk], [bl], dan Nada"
    wbn "Kalau gitu kami pulang dulu tante dan [mcFirst]"
    mom "Iyaa Hati-hati"
    mom "Oyaoya... [mg3_First] ga pulang juga ?"
    mg3 "Sebentar lagi tante, Rumahku juga ga jauh dari sini kok te"
    mom "Pulang setelah makan malam ya"
    mg3 "Iyaa te.. mau main sama [cat] juga tapi sudah ketiduran gara-gara tadi main"
    mom "Yaudah kalau gitu.. bantuin tante nyiapin ya.."
    mg3 "Okie Tante"
    mc "Yaudah kalau gitu aku tidur dulu"

    scene dapur_sore
    mom "Kerjaanya jadi lebih cepat kalau ada kamu"
    mg3 "Ahh.. bisa saja Tante"
    "~Aku Pulang !!!"
    mom "Kayaknya, Om sudah pulang"
    dad "Loh Loh,, Calon Mantu ini bu ?"
    mom "Oyaoya.. Iyaa. ada Calon Mantu jadi cepat"
    mg3 "awawawawaw.. Tante sama Om ada ada saja"
    dad "Hahahahhaha"
    mom "Oiya,, bisa minta tolong bangunkan [mcFirst] ?"
    mg3 "Boleh te"

    scene kamar_malam
    mg3 "[mcFirst] Bangunn !!"
    mc "Hai.. Haii.. sudah bangun"
    mg3 "Kalau gitu kita makan kuy"
    mc "Iyaa aku mau raup dulu"

    scene dapur_malam
    mom "Gimana ?"
    mg3 "Katanya duluan masih cuci wajah"
    mc "Ayo makan"
    dad "Nah,, ini sudah datang"
    "~AKhirnya Kami semua makan bersama meskipun lebih ramai tapi aku suka setelah itu aku mengantarkan [ng3_First] pulang kerumahnya~"

    scene jalan_malam
    mg3 "Oiya,, ceritain masalahmu ketika dulu lah sepertinya ada hal yang ga begitu baik"
    mc "Kamu sendiri ga mau ceritain"
    mg3 "yaudah gimana kalau besok kita saling bercerita"
    mc "Boleh kalu gitu"

    scene depan rumah Airin
    mg3 "Sudah sampai.. \n Terima kasih atas semuanya"
    mc "Aku juga kalu gitu aku pulang dulu ya"
    mg3 "Iya hati-hati dijalan"

    jump day6_Airin
