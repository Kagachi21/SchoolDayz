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
    mom "Giamana ayah ?"
    mc "Katanya duluan aja, sebentar lagi kesini"
    mc "Aku duluan aja kalau gitu bu"
    mc "Mau berangkat ke sekolah"
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
    "~Cuci Piring~"
    mc "Aku berangkat dulu bu"
    mom "Hati - hati dijalan"

    scene jalan

    scene gerbang sekolah
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
    sr "Kelompok 1 silahkan maju duluan"
    "~Presentasi~"
    sr "Okay, selanjutnya kelompok 4 maju"
    "~Presentasi~"

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
            1. C    3. B    5. A    7. A    9. C    11. D   13. A   15. C
            2. C    4. D    6. A    8. D    10. C   12. B   14. D"

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

    scene gerbang sekolah
    mg2 "[mcFirst]!!"
    mc "Skuy Naik, kamu mampir rumahku juga ga ?"
    mg2 "Woiya dong, kangen masakan tante hahaha"
    mc "Dasar kau ini"

    scene jalan
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

    scene dapur 
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

    scene kamar malam
    "Hoaamm.. sudah malam ternyata"
    
    scene dapur
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
    "Kuis Virus"

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