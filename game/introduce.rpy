label pengenalan:

    scene kamar
    "Seperti biasanya pagi yang cerah sekali, cuaca yang paling aku benci"
    "Harus pergi ke sekolah dan berinteraksi dengan lainnya"
    "Tapi aku sudah memilih jalan ini mau tidak mau ya harus lanjut meskipun terpaksa"
    "Oiya, Kucing yang kemarin apa baik - baik saja ya ? aku  lupa membawa kucing kemarin pulang kerumah"
    "Sebelum menuju sekolah sebaiknya aku beli makanan kaleng kucing dulu"
    
    scene ruang makan
    mom "Makan yang banyak yaaa, biar sehat"
    mc "...."
    mom "Nanti Ibu sama Ayah menyiapkan untuk kucing yg kamu bawa pulang nanti"
    dad "Iyaa benar, ta-tapii Ayah ga bisa lihat langsung karena nanti pulang kerjanya malam"
    mc "Iyaa, terima kasih Ayah Ibuu"
    mc "aku sudah selesai, aku langsung berangkat"
    mom "Ini uang sangu mu 10000"
    $ money += 10000
    dad "Iya hati - hati dijalan"

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

    scene jalan
    "Ternyata sudah ada seseorang yang memberi makanan kucing"
    "Apa itu Majikannya ? Seragamnya sama denganku"
    "Kalau gitu aku ga perlu mengganggunya"
    mg1 "Heii,,, Tunggu sebentar" 
    mg1 "Heii Jangan diabaikann, Sini duluuu"
    mg1 "hmmphh!!"
    mc "Ada Apa ? sudah lepaskan ga usah menarik bajuku"
    mc "aku ga akan kemana-mana"
    mg1 "Hehehehehehe.. maaf"
    mg1 "Kamu orang yang kemarin memberi makan ke kucing ini kan ?"
    mc "Entahlah.."
    mg1 "Kemarin, aku melihatmu setelah memberi makanan ke kucing ini"
    mg1 "Apa Kamu suka Kucing juga ?"
    mc "...."
    mc "Kalau ga penting aku duluan"
    mg1 "Tunggu Bentar, kamu kyknya sekelas denganku aku lupaa namamu"
    mg1 "ummm.. aha aku ingatt. Loh loh sudah hilangg"
    mg1 "humph Dasar. Tunggu aku kan kita sekelas"
    mg1 "Tunggu akuu!!! [mcFirst]"

    scene gerbang sekolah
    na "Oeee [mcFirst], wihhh dahh akrab aja nih sama [mg1_First]"
    na "Kalian dah jadiann yaa ? Baru Masukk sekolahh sudah jadian aja Hebat"
    mc "...."
    mg1 "ehhh.. Ngg-ngg-gaakk akuu ga pacaran Bukan pa-pacarkuu !"
    na "ajarin dongg [mcFirst] hehhehe"
    mc "...."
    na "ayo ayo ajarinn.."
    mc "Dia bukan pacarku, aku ga punya sama sekali"
    na "heee Dingin seperti biasaa hahhahaha"
    "~Ding Dong~~"
    mc "Bell Sudah Berbunyi itu"
    $ tg = "Nada" +" & "+ mg1_First
    tg "Tungguin akuu !!!"

    scene kelas 
    sr "Selamat Pagi Anak-anak, Untuk saat ini ibu ga akan langsung terjun ke pelajaran"
    sr "Ibu mulai dengan pengenalan materi dulu yang akan dipelajari ya"
    $ sk = "Sekelas"
    sk "Baikk,, Bu"
    "~Sesi Pengenalan Pelajaran~"

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
    "Brakk ~"
    mg2 "Hati-hati kalau jalan, untung tidak tumpah minumanku"
    mc "Maaf.."
    mg2 "Aku penasaran, kamu bukannya si [mc] yang dulunya sering dibul--"
    "Bagaimana dia bisa tau ?"
    $ tmn_mg2 = "Temannya [mg2]"
    ol "Kamu Gpp kan ? Siapa itu tadi na ? minta maafnya kyk ga ikhlas"
    mg2 "Teman Sekelasku" 
    mg2 "Biarin aja.. Aku gapapa kok"

    "Sepertinya orang tadi satu sekolah denganku dulu"
    "Kalau ga satu sekolah ga mungkin dia bisa tau"
    "...."
    "Mending aku habiskan dulu makanan yang ku beli tadi"
    "Kayaknya makan diatas Atap Sekolah Enak"
    scene atap
    "Tenangnya di atap sekolah"
    "~Ding Dong~"
    "Saatnya aku masuk kelas huh"

    scene kelas 
    sr "Selamat siang Anak-anak, mari kita lanjutkan pengenalan materi selanjutnya"
    sr "Ibu mulai ya kelasnya"
    sk "Baikk,, Bu"
    "~Sesi Pengenalan Pelajaran ke 2~"
    "~Ding Dong~"
    "Hmmm.. aku ngantuk"
    "Aku harus tidur dimana ?"
    menu:
        "Atap Sekolah":
            scene atap
            "Begitu Tenang dan sejuk"
            "Kalau gitu aku tidur disini sampai Bel Berbunyi"
            mg3 "Hmmm.. ada orang ternyata"
            mg3 "Kayaknya dia tertidur pulas"
            mg3 "Bangunn.. "
            mg3 "Sepertinya Beneran pulas tidurnya"
            "Seperti ada nyanyian, mungkin aku salah dengar"
            
        "Kelas":
            mc "Kalau gitu aku tidur disini aja sampai Bel Berbunyi"

    "~Ding Dong~"
    mg3 "Ahh.. sudah bell masuk ternyata"
    mg3 "Dia tidurnya nyenyak, apa sebaiknya kubangaunkan ya ?"
    mg3 "aku sebaiknya langsung ke kelas aja "
    "10 Menit setelah bell berbunyi"
    mc "Hoamm.. Jam berapa ini ?"
    mc "Weh.. Ternyata aku tidurnya kelebihan"
    mc "Lebih baik langsung ke kelas aja"

    scene lorong sekolah
    "Ternyata belum ada gurunya"

    scene kelas
    na "Dari mana aja brader ?"
    mc "atap"
    na "Weh.. ngapain ?"
    mc "...."
    sr "Siang anak-anak, mari kita mulai saja ya biar cepat selesai"
    sr "Sekarang pengenalan materi yang ke-3"
    sk "Baikk.. Bu"
    "Sesi Pengenalan Materi ke 3"
    "~Ding Dong~"

    "Ahh.. ramainya"
    na "ga pulang [mcFirst] ?"
    mc "Duluan"
    na "Okay,, aku duluan brader"

    "~15 Menit kemudian~"
    "Kayaknya sudah sepi ini sekolah, sebaiknya aku pulang dan membawa kucing itu"
    "Moga aja ada"
    "~Ada Suara Nyanyian~"
    "Suara siapa itu ?"
    "Sepertinya datanganya dari atas mungkin ada di atap sekolah"
    "Aku penasaran. Mungkin aku akan coba ke atap"

    scene atap sekolah
    "Wahh... "
    mg3 "aahh.. kamu melihatnya kan ?"
    mc "iyaa.. aku melihatnya, suaramu bagus"
    mg3 "M.maaf,, bisa kau lupakan hal tadi ?"
    mg3 "umm.. dan jangan bilang ke siapa-siapa"
    mc "...."
    mc "Okk, aku akan lupakan hal barusan"
    mc "kalau gitu aku pulang dulu.. "
    mc "Maaf, kalau mengganggu.."
    mg3 "ahh.. tunggu.."
    mg3 "...."

    scene Jalan
    "ahh.. aku hampir lupa membawa kucing ituu"
    "Sebaiknya aku kembali dan melihatnya"
    mc "ternyata kamu masih ada kukira tadi sudah dibawa oleh cewe tadi pagi"
    cat "meooow ??"
    mc "kalau gitu ikut kerumahku ya"
    cat "Meoowww"

    scene rumah
    mc "Aku pulang.."
    "Ternyata sudah dibelikan kandangnya"
    mc "tunggu sini, aku ganti baju dulu"
    mc "setelah itu aku memandikanmu"
    cat "meoow meooww"
    mc "Aku sudah ganti baju. Saatnya mandiin kamu"
    cat "meoow ?"

    scene kamar mandi
    mc "akkhh,, kau tidak suka air yaa. Susah sekali memandikanmu"
    cat "grrrrrr"
    mc "Sini kau.. Bagian sini belum digosok"
    mc "fuuhh~"
    mc "ternyata kamu awalnya memberontak ya tapi lama lama jadi tenang"
    cat "meoow ////"
    mc "Setelah ini aku akan memberimu makan"
    cat "Meooww ^_^ "
    mc "Sepertinya kamu tau apa yang kuucapkan"

    scene dapur
    mc "ini makananmu, kau pasti suka kan"
    cat "Meoow :3"
    mom "Aku Pulang!!"
    mom "Loh sudah pulang [mcFirst] ini kucingnya ?"
    mom "Imuuutt sekalii Lucuu Aaaaa"
    mom "Oiya, Ini ibu bawakan persedian makanan untuk kucing"
    mom "Aww.. Lucu sekali siapa nama Kucing ini ?"
    cat "Nyaaa ?"
    mom "Apa kau sudah memberi nama kucing ini ?"
    mc "Belum,, memiliki nama"
    mc "...."
    mc "Terima kasih sudah menyiapkan dan mengijinkan memelihara kucing"
    mc "Aku mau tidur dulu"
    mom "Ehhh.. Iyaa"
    cat "Nyaaa?"
    mom "Tenang ada Ibu disini yang akan bermain denganmu"
    mom "Mungkin [mcFirst] Lelah"
    mom "aku ada mainan iniii"
    mom "Tadaaa !! Laser sama pancingan bulu"
    cat "meoooww ^o^"
    mom "Habiskan dulu makananmu"

    scene kamar
    "benar, juga kalau tidak ada nama kurang enak klo manggil kucingnya"
    "sebaiknya aku tidur dulu mungkin bisa dapet ide"
    "~Beberapa jam kemudian~"
    mc "Hoaamm,, Jam berapa ini ?"
    mc "sebaiknya aku cuci muka dulu lalu ke tempat makan"

    scene kamar mandi

    scene dapur
    "Ayah masih belum pulang"
    mom "Sini makan dulu makanan sudah siap"
    mom "Ibu juga sudah siapin makanan untuk kucingnya"
    mom "Ngomong ngomong kucingnya kamu mau kasih nama apa ?"
    mc "Aku sudah dapat"
    mc "Mungkin aku akan menamainya Feliz"
    $ kucing = "Feliz"
    mom "Hoooo Baguss jugaa tapi itu artinya apa ?"
    mc "Artinya Bahagia dari Bahasa Galician, karena [cat] selalu bahagia meskipun sudah dibuang oleh majikannya"
    mom "Ohh, Feliz ini Nama yang bagus Karena kucingnya juga menggemaskan bisa bikin orang bahagia, benar kan [cat] ?"
    "[mom] mulai mengangkat [cat]"
    cat "Nyaaa Nyaa"
    mc "[dad] belum pulang ?"
    mom "Sepertinya Ayahmu bakalan kerja lembur"
    mc "...."
    mc "Aku sudah selesai kalau gitu aku mau kembali ke kamar"
    mom "Iyaa.. nanti biar ibu yang cuci piringnya"

    "~Esok Paginya~"
    scene kamar
    "Apa ini berat di perutku ?"
    mc "...."
    mc "Ternyata [cat]"
    mc "Bagaimana bisa kamu masuk ?"
    mc "Mungkin [mom] yang membuka pintunya"
    cat "Nyaaahhh"
    cat "Meooww ?"
    mc "Ayo kita ke ruang makan dulu"

    scene dapur
    dad "kalian sudah bangun ya"
    mom "Sini makan dulu sudah ibu siapkan semuanya"
    dad "Ayah dengan dari ibu kucingnya kamu kasih nama [cat] ya ?"
    mc "Iya"
    dad "Nama yang baguss Ayah juga suka arti namanya juga bagus"
    mc "...."
    dad "Felizz Menggemaskann :3"
    cat "Meeeoooww ^-^' ?"
    mc "aku sudah selesai"
    "~Cuci Piring~"
    mc "aku mau bersiap siap berangkat sekolah"
    ai "Iyaaa"

    scene depan rumah
    mc "Aku berangkat dulu"
    mom "ini Uang sangumu"
    $ money += 15000
    ai "iya nakk hati-hati dijalann"
    cat "Nyaa~ :')"
    dad "Kalau gitu aku berangkat juga bu"
    mom "Iyaa yahh"
    mom "Hati - hati dijalan"
    mom "[cat] main sama ibu aja dirumah yaa "
    cat "Nyaaa ^o^"

label pemilihan:
    
    scene sky

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
