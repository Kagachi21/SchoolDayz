label pengenalan:

    scene kamar with dissolve
    "Seperti biasanya pagi yang cerah sekali, cuaca yang paling aku benci"
    "Harus pergi ke sekolah dan berinteraksi dengan lainnya"
    "Tapi aku sudah memilih jalan ini mau tidak mau ya harus lanjut meskipun terpaksa"
    "Oiya, Kucing yang kemarin apa baik - baik saja ya ? aku  lupa membawa kucing kemarin pulang kerumah"
    "Sebelum menuju sekolah sebaiknya aku beli makanan kaleng kucing dulu"
    
    scene dapur with dissolve
    show mom at center:
        ypos 1.15
    mom "Makan yang banyak yaaa, biar sehat"
    mc "...."
    mom "Nanti Ibu sama Ayah menyiapkan untuk kucing yg kamu bawa pulang nanti"
    show mom at right with moveinright:
        xpos 0.8
        ypos 1.15
        xzoom -1
    show dad at center:
        ypos 1.2
    dad "Iyaa benar, ta-tapii Ayah ga bisa lihat langsung karena nanti pulang kerjanya malam"
    mc "Iyaa, terima kasih Ayah Ibuu"
    mc "aku sudah selesai, aku langsung berangkat"
    show dad at right with moveinright:
        xpos 0.8
        ypos 1.2
    show mom at center:
        ypos 1.15
    mom "Ini uang sangu mu"
    $ money += 10000
    show dad at center:
        ypos 1.2
    show mom at right with moveinright:
        xpos 0.8
        ypos 1.15
        xzoom -1
    dad "Iya hati - hati dijalan"
    hide mom with dissolve
    hide dad with dissolve

    scene depan mini market
    "Mungkin disini ada makanan kucing juga"
    scene mini market 
    ks "Selamat Datang di Alkamart"
    "kayaknya ada di bagian sini"
    ks "Mau tambah kak ? sekalian pulsa, ini ada diskon juga beli 1 Kariroti gratis 1 susu Ultraman"
    mc "Ga usah"
    ks "Pake kresek kak ?"
    mc "Ga usah"
    $ wk1 = 3000
    ks "Harganya total 5 bungkus Waskhis 15 ribu"
    $ wk = 5 * wk1
    mc "Ini"
    $ money = money - wk
    ks "Ini Kembaliannya kak %(money)d"
    ks "Terima Kasih kak Selamat berbelanja kembali"

    scene jalan with dissolve
    "Ternyata sudah ada seseorang yang memberi makanan kucing"
    "Apa itu Majikannya ? Seragamnya sama denganku"
    "Kalau gitu aku ga perlu mengganggunya"
    show miselia_uniform at center:
        ypos 1.2 
    mg1 "Heii,,, Tunggu sebentar" 
    mg1 "Heii Jangan diabaikann, Sini duluuu"
    mg1 "hmmphh!!"
    show miselia_uniform at right with moveinright:
        xpos 0.9
        ypos 1.2
    mc "Ada Apa ? sudah lepaskan ga usah menarik bajuku"
    mc "aku ga akan kemana-mana"
    show miselia_uniform at center:
        ypos 1.2
    mg1 "Hehehehehehe.. maaf"
    mg1 "Kamu orang yang kemarin memberi makan ke kucing ini kan ?"
    show miselia_uniform at right with moveinright:
        xpos 0.9
        ypos 1.2
    mc "Entahlah.."
    show miselia_uniform at center:
        ypos 1.2
    mg1 "Kemarin, aku melihatmu setelah memberi makanan ke kucing ini"
    mg1 "Apa Kamu suka Kucing juga ?"
    show miselia_uniform at right with moveinright:
        xpos 0.9
        ypos 1.2
    mc "...."
    mc "Kalau ga penting aku duluan"
    show miselia_uniform at center:
        ypos 1.2
    mg1 "Tunggu Bentar, kamu kyknya sekelas denganku aku lupaa namamu"
    mg1 "ummm.. aha aku ingatt. Loh loh sudah hilangg"
    mg1 "humph Dasar. Tunggu aku kan kita sekelas"
    mg1 "Tunggu akuu!!! [mcFirst]"
    hide miselia_uniform with moveoutleft

    scene gerbang_sekolah with dissolve
    show nada_uni at center with zoomin:
        ypos 1.2
    na "Oeee [mcFirst], wihhh dahh akrab aja nih sama [mg1_First]"
    na "Kalian dah jadiann yaa ? Baru Masukk sekolahh sudah jadian aja Hebat"
    show nada_uni at right with moveinright:
        xpos 0.9
        ypos 1.2
    mc "...."
    show miselia_uniform at center:
        ypos 1.2
    mg1 "ehhh.. Ngg-ngg-gaakk akuu ga pacaran Bukan pa-pacarkuu !"
    show nada_uni at center with moveinright:
        ypos 1.2
    show miselia_uniform at right with moveinleft:
        xpos 0.9
        ypos 1.2
    na "ajarin dongg [mcFirst] hehhehe"
    mc "...."
    na "ayo ayo ajarinn.."
    mc "Dia bukan pacarku, aku ga punya sama sekali"
    na "heee Dingin seperti biasaa hahhahaha"
    "~Ding Dong~~"
    mc "Bell Sudah Berbunyi itu"
    $ tg = "Nada" +" & "+ mg1_First
    tg "Tungguin akuu !!!"
    hide nada_uni with moveoutleft
    hide miselia_uniform with moveoutleft

    scene kelas 
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Selamat Pagi Anak-anak, Untuk saat ini ibu ga akan langsung terjun ke pelajaran"
    sr "Ibu mulai dengan pengenalan materi dulu yang akan dipelajari ya"
    $ sk = "Sekelas"
    sk "Baikk,, Bu"
    show bu_senda at right with moveinleft:
        xpos 0.9
        ypos 1.2
    "~Sesi Pengenalan Pelajaran~"
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Waktunya sudah habis anak-anak"
    sr "Saatnya istirahat"
    sk "Iyaa buu"
    hide bu_senda with moveoutright

    scene kantin
    "Ramai sekali kupikir ga bakalan terlalu ramai kayak gini"
    "Mungkin Lebih baik aku melihat Menunya dulu"

    $ rsp = 3500
    $ rism = 2000
    $ mgj = 7000
    $ ngj = 8000
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
                    kt "Totalnya [mgj]"

                    if (money >= mgjt):
                        $ money = money - mgjt
                        kt "Terima kasih sudah membeli, Ini Kembaliannya %(money)d"
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
                    else:
                        "Uangku tidak Cukup..."
                "Maaf, Tidak jadi..":
                    kt "Iya Gapapa"

    "Aku sudah dapat yang ku mau tinggal pergi ke atap sekolah aja"
    show ardana_uni at center with hpunch:
        ypos 1.2
    "Brakk ~"
    hide ardana_uni with dissolve
    show ardana_uni_emosi at center:
        ypos 1.2
    mg2 "Hati-hati kalau jalan, untung tidak tumpah minumanku"
    mc "Maaf.."
    hide ardana_uni_emosi with dissolve
    show ardana_uni at center:
        ypos 1.2
    mg2 "Aku penasaran, kamu bukannya si [mc] yang dulunya sering dibul--"
    "Bagaimana dia bisa tau ?"
    $ tmn_mg2 = "Temannya [mg2]"
    ol "Kamu Gpp kan ? Siapa itu tadi na ? minta maafnya kyk ga ikhlas"
    mg2 "Teman Sekelas kita" 
    ol "Ehh.. iyakah ?"
    mg2 "Iyaa.. Biarin aja.. Aku gapapa kok"
    hide ardana_uni with dissolve

    "Sepertinya orang tadi satu sekolah denganku dulu"
    "Kalau ga satu sekolah ga mungkin dia bisa tau"
    "...."
    "Mending aku habiskan dulu makanan yang ku beli tadi"
    "Kayaknya makan diatas Atap Sekolah Enak"

    scene atap with dissolve
    "Tenangnya di atap sekolah"
    "~Ding Dong~"
    "Saatnya aku masuk kelas huh"

    scene kelas with dissolve
    show bu_senda at center with moveinright:
        ypos 1.2       
    sr "Selamat siang Anak-anak, mari kita lanjutkan pengenalan materi selanjutnya"
    sr "Ibu mulai ya kelasnya"
    sk "Baikk,, Bu"
    show bu_senda at right with moveinleft:
        xpos 0.9
        ypos 1.2
    "~Sesi Pengenalan Pelajaran ke 2~"
    "~Ding Dong~"
    show bu_senda at center with moveinright:
        ypos 1.2       
    sr "Waktunya sudah habis anak-anak"
    sr "Saatnya istirahat"
    sk "Baiikk Bu!!"
    hide bu_senda with moveoutright
    "Hmmm.. aku ngantuk"
    "Aku harus tidur dimana ?"
    menu:
        "Atap Sekolah":
            scene atap_siang with dissolve
            "Begitu Tenang dan sejuk"
            "Kalau gitu aku tidur disini sampai Bel Berbunyi"
            show airin_jalan_uni at center with moveinright
            mg3 "Hmmm.. ada orang ternyata"
            hide airin_jalan_uni
            show airin_uni at center:
                ypos 1.2
            mg3 "Kayaknya dia tertidur pulas"
            hide airin_uni
            show airin_kaget_uni at truecenter:
                ypos 0.5
            mg3 "Bangunn.. "
            mg3 "Bangunn...."
            hide airin_kaget_uni
            show airin_uni at center:
                ypos 1.2
            mg3 "Sepertinya Beneran pulas tidurnya"
            hide airin_uni
            "Seperti ada orang yang memanggilku, mungkin aku salah dengar"
            
        "Kelas":
            mc "Kalau gitu aku tidur disini aja sampai Bel Berbunyi"

    "~Ding Dong~"
    show airin_uni at center:
                ypos 1.2
    mg3 "Ahh.. sudah bell masuk ternyata"
    mg3 "Dia tidurnya nyenyak, apa sebaiknya kubangunkan ya ?"
    hide airin_uni
    show airin_jalan_uni at center
    mg3 "aku sebaiknya langsung ke kelas aja "
    hide airin_jalan_uni with moveoutleft

    "10 Menit setelah bell berbunyi"
    mc "Hoamm.. Jam berapa ini ?"
    mc "Weh.. Ternyata aku tidurnya kelebihan"
    mc "Lebih baik langsung ke kelas aja"

    scene lorong sekolah with dissolve
    "Ternyata belum ada gurunya"

    scene kelas with dissolve
    show nada_uni at center with moveinright:
        ypos 1.2
    na "Dari mana aja brader ?"
    show nada_uni at right with moveinleft:
        xpos 0.9
        ypos 1.2
    mc "atap"
    na "Weh.. ngapain ?"
    mc "Tidur"
    hide nada_uni with moveoutleft
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Siang anak-anak, mari kita mulai saja ya biar cepat selesai"
    sr "Maaf tadi ada rapat dadakan mangkanya jadi agak lama"
    sr "Sekarang pengenalan materi yang ke-3"
    sk "Baikk.. Bu"
    show bu_senda at right with moveinleft:
        xpos 0.9
        ypos 1.2
    "Sesi Pengenalan Materi ke 3"
    "~Ding Dong~"
    show bu_senda at center with moveinright:
        ypos 1.2
    sr "Waktunya sudah habis anak-anak"
    sr "Saatnya pulang"
    sr "Silahkan pulang anak-anak"
    hide bu_senda with moveoutright
    "Ahh.. ramainya"
    show nada_uni at center with moveinright:
        ypos 1.2
    na "ga pulang [mcFirst] ?"
    mc "Duluan"
    na "Okay,, aku duluan brader"
    hide nada_uni with moveoutright

    "~15 Menit kemudian~"
    "Kayaknya sudah sepi ini sekolah, sebaiknya aku pulang dan membawa kucing itu"
    "Moga aja ada"

    scene lorong sekolah with dissolve
    "Ahh.. Ada Suara Nyanyian"
    "Suara siapa itu ?"
    "Sepertinya datangnya dari atas mungkin ada di atap sekolah"
    "Aku penasaran. Mungkin aku akan coba ke atap"

    scene atap_sore
    "Wahh... "
    show airin_jalan_uni at center with moveinright
    hide airin_jalan_uni
    show airin_kaget_uni at truecenter:
        ypos 0.5
    mg3 "aahh.. kamu melihatnya kan ?"
    hide airin_kaget_uni
    show airin_uni at left with moveinleft:
        xpos 0.7
        ypos 1.2
    mc "iyaa.. aku melihatnya, suaramu bagus"
    hide airin_uni
    show airin_kaget_uni at truecenter with vpunch:
        ypos 0.5
    mg3 "AWAWAAWAWAWAWA"
    hide airin_kaget_uni
    show airin_uni at center:
        ypos 1.2
    mg3 "M.maaf,, bisa kau lupakan hal tadi ?"
    mg3 "umm.. dan jangan bilang ke siapa-siapa"
    show airin_uni at left with moveinright:
        xpos 0.7
        ypos 1.2
    mc "...."
    mc "Okk, aku akan lupakan hal barusan"
    mc "kalau gitu aku pulang dulu.. "
    mc "Maaf, kalau mengganggu.."
    show airin_uni at center:
        ypos 1.2
    mg3 "ahh.. tunggu.."
    mg3 "...."
    hide airin_uni with moveoutright

    scene depan rumah
    "ahh.. aku hampir lupa membawa kucing ituu"
    "Sebaiknya aku kembali dan melihatnya"

    scene jalan_sore with dissolve
    mc "Ternyata kamu masih ada kukira tadi sudah dibawa oleh cewe tadi pagi"
    show cat_box with moveinbottom
    cat "meooow ??"
    hide cat_box with moveoutbottom
    mc "kalau gitu ikut kerumahku ya"
    show cat_box_relived with moveinbottom
    cat "Meoowww"
    hide cat_box_relived with dissolve

    scene depan rumah
    mc "Aku pulang.."

    scene ruang keluarga
    "Ternyata sudah dibelikan kandangnya"
    mc "tunggu sini, aku ganti baju dulu"
    mc "setelah itu aku memandikanmu"
    show cat at center with moveinbottom:
        ypos 0.85
    cat "meoow meooww"
    mc "Aku sudah ganti baju. Saatnya mandiin kamu"
    cat "meoow ?"
    hide cat with dissolve

    scene kamar mandi
    mc "akkhh,, kau tidak suka air yaa. Susah sekali memandikanmu"
    show cat_angry at center with vpunch:
        ypos 0.85
    cat "grrrrrr"
    hide cat_angry with dissolve
    mc "Sini kau.. Bagian sini belum digosok"
    mc "fuuhh~"
    mc "ternyata kamu awalnya memberontak ya tapi lama lama jadi tenang"
    show cat_happy at center:
        ypos 0.75
    cat "meooww"
    mc "Setelah ini aku akan memberimu makan"
    cat "Meooww ^_^"
    mc "Sepertinya kamu tau apa yang kuucapkan"
    hide cat_happy with dissolve

    scene dapur_sore
    mc "ini makananmu, kau pasti suka kan"
    show cat_happy at center:
        ypos 0.75
    cat "Meoow :3"
    hide cat_happy with moveoutbottom
    show mom at center with moveinright:
        ypos 1.15
    mom "Aku Pulang!!"
    mom "Loh sudah pulang [mcFirst] ini kucingnya ?"
    mom "Imuuutt sekalii Lucuu Aaaaa"
    mom "Oiya, Ini ibu bawakan persedian makanan untuk kucing"
    mom "Aww.. Lucu sekali siapa nama Kucing ini ?"
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    show cat at center with moveoutbottom:
        ypos 0.85
    cat "Nyaaa ?"
    hide cat with moveoutbottom
    show mom at center with moveinright:
        ypos 1.15
    mom "Apa kau sudah memberi nama kucing ini ?"
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    mc "Belum,, memiliki nama"
    mc "...."
    mc "Terima kasih sudah menyiapkan dan mengijinkan memelihara kucing"
    mc "Aku mau tidur dulu"
    show mom at center with moveinright:
        ypos 1.15
    mom "Ehhh.. Iyaa"
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    show cat at center with moveoutbottom:
        ypos 0.85
    cat "Nyaaa?"
    hide cat with moveoutbottom
    show mom at center with moveinright:
        ypos 1.15
    mom "Tenang ada Ibu disini yang akan bermain denganmu"
    mom "Mungkin [mcFirst] Lelah"
    mom "aku ada mainan iniii"
    mom "Tadaaa !! Laser sama pancingan bulu"
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    show cat at center with moveoutbottom:
        ypos 0.85
    cat "meoooww ^o^"
    hide cat with moveoutbottom
    show mom at center with moveinright:
        ypos 1.15
    mom "Habiskan dulu makananmu"
    hide mom with dissolve

    scene kamar_sore
    "benar, juga kalau tidak ada nama kurang enak klo manggil kucingnya"
    "sebaiknya aku tidur dulu mungkin bisa dapet ide"
    "~Beberapa jam kemudian~"
    
    scene kamar_malam
    mc "Hoaamm,, Jam berapa ini ?"
    mc "sebaiknya aku cuci muka dulu lalu ke tempat makan"

    scene kamar mandi

    scene dapur_malam
    mc "Ayah masih belum pulang"
    show mom at center with moveinright:
        ypos 1.15
    mom "Masih belum sepertinya lembur"
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    mc "Ealah"
    show mom at center with moveinright:
        ypos 1.15
    mom "Sini makan dulu makanan sudah siap"
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    mc "Okk bu"
    show mom at center with moveinright:
        ypos 1.15
    mom "Ibu juga sudah siapin makanan untuk kucingnya"
    mom "Ngomong ngomong kucingnya kamu mau kasih nama apa ?"
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    mc "Aku sudah dapat"
    mc "Mungkin aku akan menamainya Feliz"
    $ kucing = "Feliz"
    show mom at center with moveinright:
        ypos 1.15
    mom "Hoooo Baguss jugaa tapi itu artinya apa ?"
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    mc "Artinya Bahagia dari Bahasa Galician, karena [cat] selalu bahagia meskipun sudah dibuang oleh majikannya"
    show mom at center with moveinright:
        ypos 1.15
    mom "Ohh, Feliz ini Nama yang bagus Karena kucingnya juga menggemaskan bisa bikin orang bahagia, benar kan [cat] ?"
    "[mom] mulai mengangkat [cat]"
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    show cat at center with moveoutbottom:
        ypos 0.85
    cat "Nyaaa Nyaa"
    mc "Aku sudah selesai kalau gitu aku mau kembali ke kamar"
    hide cat with moveoutbottom
    show mom at center with moveinright:
        ypos 1.15
    mom "Iyaa.. nanti biar ibu yang cuci piringnya"
    hide mom with dissolve

    "~Esok Paginya~"
    scene kamar
    "Apa ini berat di perutku ?"
    mc "...."
    mc "Ternyata [cat]"
    mc "Bagaimana bisa kamu masuk ?"
    mc "Mungkin [mom] yang membuka pintunya"
    show cat at center with moveoutbottom:
        ypos 0.85
    cat "Nyaaahhh"
    cat "Meooww ?"
    hide cat with moveoutbottom
    mc "Ayo kita ke ruang makan dulu"

    scene dapur
    show dad at center:
        ypos 1.2
    dad "kalian sudah bangun ya"
    show dad at right with moveinleft:
        xpos 0.8
        ypos 1.2
    show mom at center with moveinright:
        ypos 1.15
    mom "Sini makan dulu sudah ibu siapkan semuanya"
    show dad at center:
        ypos 1.2
    show mom at right with moveinleft:
        xpos 0.8
        ypos 1.15
        xzoom -1
    dad "Ayah dengar dari ibu kucingnya kamu kasih nama [cat] ya ?"
    show dad at right with moveinleft:
        xpos 0.8
        ypos 1.2
    show mom at right with moveinleft:
        xpos 0.9
        ypos 1.15
        xzoom -1
    mc "Iya"
    show dad at center:
        ypos 1.2
    hide mom with dissolve
    dad "Nama yang baguss Ayah juga suka arti namanya juga bagus"
    mc "...."
    dad "Felizz Menggemaskann :3"
    show dad at right with moveinleft:
        xpos 0.8
        ypos 1.2
    show cat_happy at center:
        ypos 0.75
    cat "Meeeoooww ^-^' ?"
    mc "aku sudah selesai"
    hide cat_happy with dissolve
    hide dad with dissolve
    play sound cuci_piring
    "~Cuci Piring~"
    window hide dissolve
    $ renpy.pause(35.0, hard=True)
    window show dissolve
    mc "aku mau bersiap siap berangkat sekolah"
    show mom at center with moveinright:
        xpos 0.5
        ypos 1.15
    show dad at center:
        xpos 0.6
        ypos 1.2
    ai "Iyaaa"

    scene depan rumah
    mc "Aku berangkat dulu"
    show mom at center with moveinright:
        ypos 1.15
    mom "ini Uang sangumu"
    $ money += 15000
    show mom at center with moveinright:
        xpos 0.5
        ypos 1.15
    show dad at center:
        xpos 0.6
        ypos 1.2
    ai "iya nakk hati-hati dijalann"
    hide mom with dissolve
    hide dad with dissolve
    show cat at center with moveoutbottom:
        ypos 0.85
    cat "Nyaa~ :')"
    show dad at center:
        xpos 0.6
        ypos 1.2
    hide cat with dissolve
    dad "Kalau gitu aku berangkat juga bu"
    show dad at right with moveinleft:
        xpos 0.8
        ypos 1.2
    show mom at center with moveinright:
        ypos 1.15
    mom "Iyaa yahh"
    mom "Hati - hati dijalan"
    hide dad with moveoutleft
    mom "[cat] main sama ibu aja dirumah yaa"
    show mom at right with moveinleft:
        xpos 0.9
        ypos 1.15
        xzoom -1
    show cat_happy at center:
        ypos 0.75
    cat "Nyaaa ^o^"
    hide mom with moveoutright
    hide cat_happy with moveoutright

label pemilihan:
    
    scene sky

    window hide dissolve

    $ renpy.choice_for_skipping()
    
    show screen gotoKirana

    show screen gotoMiselia

    show screen gotoAirin

    $ renpy.pause(hard=True)

    #z = renpy.input("Please enter a NUMBER: ")
    #$ z = renpy.input("", "", allow="0123456789")
    #$ z = renpy.input("Berikan Uang yang mau dibayarkan: ", prompt="", default="", allow="0123456789")
    
#label roti_sosis:
    #$ z = renpy.input("Berikan Uang yang mau dibayarkan: ", "", allow="0123456789")
    #$ z = int(z)

    #$ money = z - rsp
    #kt "ini kembaliannya [money]"
