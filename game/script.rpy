# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the

#Image(BG, Cat, etc)
image splash = im.Scale("BGSplash.png",1920,1080)
image kucing = im.Scale("1.png", 745,745)

#Image(Character)
image mom = im.Scale("/Character/mom.png", 1660, 950)
image side mc = "/Character/mc.png"

#image animation = Movie(play="BGSplash.webm")
# SplashScreen.
label splashscreen:
     scene splash with Dissolve(1.0)
     $ renpy.movie_cutscene("BGSplash.webm")
     pause 1.0

     hide animation with dissolve
     pause 1.0

     show text "{font=earwig factory rg.ttf}{color=#000000}{size=180}SchoolDayz{/size}{/color}{/font}" with Dissolve(1.0)
     show kucing at truecenter behind text with Dissolve(1.0)
     pause 2.0

     hide text with dissolve
     hide kucing with dissolve
     pause 1.0

     return
     
init:
    style my_input:
        is default
        color "#000"
        hover_color "#3399ff"
        size 25
        
    style input_button:
        is button
        yalign 1.0
        key_events True
        xysize (500, 50)
        
    python:
        class MyInputValue(InputValue):
            def __init__(self, var, default=""):
                self.var = var
                
                if not hasattr(store, var):
                    setattr(store, var, default)
                    
            def get_text(self):
                return getattr(store, self.var)
                
            def set_text(self, s):
                setattr(store, self.var, s)
                
            def enter(self):
                renpy.run(self.Disable())
                raise renpy.IgnoreEvent()


screen test():
    frame:
        align .5, .5
        has vbox
        spacing 15

        text "{size=+5}First Name :"
        $ input = Input(value=MyInputValue("mcFirst", "Entry your Name..."), style="my_input", length=30)
        button:
            style "input_button"
            action input.enable
            add input
                
        text "{size=+5}Last Name :"
        $ input = Input(value=MyInputValue("mcLast", "Entry your Surname..."), style="my_input", length=30)
        button:
            style "input_button"
            action input.enable
            add input
        
        textbutton "Done":
            xalign .5
            action Return()

# name of the character.
define dad = Character('Ayah')
define mom = Character('Ibu', image="mom")
define cat = Character('Kucing')
define mg1 = Character('????')
define mg2 = Character('????')
define mg3 = Character("" or "????")
define na = Character("Nada Ali")
define sr = Character("Senda Rontge")
define ol = Character('????')
define pb = Character('Pembully')
define pb2 = Character('Pembully 2')
define pb3 = Character('Pembully 3')
define sk = Character('Teman Sekelas')
define gu = Character('Guru UKS')

# The game starts here.
label start:

    #Input Type Biasa
    #$ mcFirst = renpy.input("What is your first name ?", length=30) or "default name"
    #$ mcLast = renpy.input("What is your last name ?", length=30) or "default surname"
    
    #Input Type Screen
    scene bg langit
    call screen test
    $ mc = Character(mcFirst +" "+mcLast, image="mc")
    
    scene bg jendela kamar terlihat burung
    mc "Hari yang sangat ku tidak sukai, yaitu hari pertama sekolah. Diriku seperti sebuah wadah yang tidak ada isinya. Apakah hari pertama sekolah akan lancar - lancar saja? Aku tidak yakin, atau akan menjadi seperti dulu ketika aku masih Sekolah Menengah Pertama"
    mc "Pengalaman yang buruk sekali dan inginku berhenti sekolah, bahkan aku tidak ingin mengingatnya lagi kenangan yang buruk itu. Tapi, kenapa masih saja teringat ? apa yang tuhan inginkan kepadaku hingga selalu memberikanku ingatan buruk tersebut"
    mc "Mungkin tidak salahnya harus mencoba untuk berangkat mungkin saja berbeda"
    scene dapur
    dad "Apa kamu sudah menyiapkan semuanya ?"
    mc "....."
    "~Awkward~"
    show mom at right
    mom "Mau tambah lagi ?"
    mc "Ga usah, aku sudah kenyang dan aku sudah menyiapkan semuanya untuk ke sekolah"
    "~Cuci Piring~"
    mom "Ga usah, Ibu aja yang cuci piringnya. Kamu berangkat aja"
    mc "....."
    mc "Gapapa, sudah terlanjur"
    mom "Oiya, Bekalnya sudah ibu siapkan juga, jangan lupa dibawa ya"
    mc "...."
    mc "Iya"
    mc "Aku berangkat dulu"

    scene depan rumah
    show mom at right
    mom and dad "Iya, Hati - hati di jalan"
    mom "Apakah anak kita akan baik - baik saja ya pa ?"
    dad "Kita harus percaya, semoga kejadian yang dulu tidak menimpa anak kita. Kejadian yang sangat mengerikan sekali. Bahkan kita sebagai orang tua tidak tahan melihatnya dan menangis"
    mom "iya pa, kita harus percaya dan berdoa untuk anak kita."

    scene jalan
    mc "Apakah benar hari ini akan baik - baik saja ?"
    mc "...."
    mc "Aku mendengar suara kucing mungkin berada didalam kerdus"
    mc "Kasihan sekali hidupmu, di buang oleh pemilikmu sendiri! sama sepertiku yang dulu pernah merasakan kesakitan karena kejadian ketika aku masih SMP"
    cat "Meoooowwwww"
    mc "Kenapa kamu masih bisa tersenyum meskipun sudah dibuang oleh majikanmu. Ataukah hanya diriku saja yang lemah atau tidak sepertimu yang polos tanpa mengetahui dunia ini kejam"
    cat "meeoooooo ?"
    mc "Ini aku ada makanan, makan ini saja dulu"
    mc "Hmmm.. mungkin aku bisa merawatmu dirumahku. Jika, aku meminta ijin orang tuaku"
    mc "Setelah pulang sekolah aku akan membawamu kerumahku"
    mg1 "Hmmm.. siapa laki - laki itu ? seragam yang sama denganku"
    mg1 "Ternyata dia sudah memberimu makanan duluan ya puss"
    mg1 "Syukurlah, aku berangkat dulu ya puss"
    cat "Meooow"

    scene gerbang
    mc "Setelah berada di depan gerbang pun tetap saja memiliki keraguan yang tinggi, jika saja berbalik mungkin akan masih sempat untuk tidak bersekolah"
    mc "Apa aku harus melakukan hal itu ? lalu, bagaimana orang tuaku melihat diriku yang masih terkekang dalam keadaan masa lalu ?"
    mc "Jika, aku berbalik arah sekarang dan menuju kerumah pasti akan membuat orangtuaku kecewa. Kalau aku selalu begini, kedepannya tidak akan ada masa depan yang indah"
    mc "Hanya terpuruk dan meratapi nasib lalu terjebak dalam masa lalu terus menerus, hingga aku meninggal pun tetap takut akan trauma itu. Mungkin setidaknya mencoba dulu tidak salah juga"
    mg2 "Ahh.. Bukankah itu MC ?"
    ol "Ada apa ?"
    mg2 "Ahh.. tidak apa-apa, aku hanya melamun saja tadi"

    scene aula sekolah
    mc "Ceramah dari kepala sekolah, dan ketua Osis ini sangat membosankan."
    mc "Hmmm.. Aku ingin segera pulang"

    scene lorong sekolah 
    mg3 "Kyaaaa"
    mc "Ahh.. kamu tidak apa - apa ? Apakah ada yang terluka ? Maaf, Aku tadi tidak melihat jalannya"
    mg3 "Ahh.. tidak apa-apa. Aku tidak ada yang terluka sama sekali. Maaf, aku tadi juga tidak fokus kedepan"
    mc "Tidak apa-apa"

    scene kelas
    mc "Semoga kehidupan SMA ku baik baik saja dan membuat orang tuaku tidak merasa sedih"
    na "Haii,, banyak orang bersosialisasi. aku lihat kamu mulai tadi diam saja sambil menatap keluar jendela"
    mc "...."
    na "Kenapa ga ikut bersosialisasi dengan yang lainnya ?"
    mc "Oiya,, aku lupa perkenalan diri. Namaku Nada Ali bisa dipanggil Nada atau Ali, umm bisa juga panggil aku Nali atau Dali ahahahha"
    na "Kalau namamu siapa ?"
    mc "...."
    mc "aku [mc] terserah mau dipanggil apa saja"
    na "ahahhaa, ok aku akan memanggilmu [mcFirst]"
    "Ding~ Dong~"
    na "Aku kembali ke bangkuku dulu ya"
    sr "Hai.. dimohon perhatiannya. Nama ibu Senda Rontge, ibu adalah guru materi biologi dan sekaligus yang akan menjadi wali kelas di kelas ini"
    sr "kalau gitu mari kita semuanya perkenalan, meskipun kalian sudah melakukan perkenalan diawal tadi. Ibu juga ingin mengenal kalian"
    "~Sesi Perkenalan diri~"
    sr "Terima Kasih sudah memperkenalkan diri semuanyaa. Saat ini, ibu tidak mau memulai mata pelajaran jadi sudah ibu siapkan game / permainan simple"
    sr "Disini ibu punya 2 bola, jadi ibu lempar secara random tanpa melihat nanti yang terkena lemparan bola pertama disuruh maju kedepan menampilkan sesuatu"
    sr "Sedangkan, bola kedua yang menentukan penampilan yg terkena bola pertama dengan mengambil kertas yang berisi perintah"
    sr "Oiyaa,, ibu lupaa anak - anak silahkan bikin sobekan kertas yang berisi perintah lalu digulung bawa ke meja ibu. bikin 10 yaa, terserah mau siapa yang bikin"
    "Kemudian anak -  anak membuat kertas sobekan berisi perintah dan ditaruh kedepan, Setelah itu permainannya dimulai. Ada yang menyanyi, Menari, lawak, dll. hingga kelas ini menjadi heboh. [mc] pun bersyukur karena tidak pernah dapat giliran tampil di depan"
    "~Ding - Dong~"
    sr "Ya, Bel istirahat sudah berbunyi, sampai jumpa lagi di lain waktu"
    mc "Untunglah aku tidak kena bola yang dilempar. aku ingin tetap diam dan tidak bersosialisasi. haaa.."
    mc "ahhh.. aku ngantuk sebaiknya aku tidur saja"

    scene kelas Hitam putih 
    pb "Diaa belum datang, kasih paku payung di tempat duduknya cepat"
    pb2 "Ok, yang banyak sekalian hahahhah"
    pb3 "sekalian kasih lem di loker mejanya, mumpung aku lagi bawa lem"
    pb "[mc] dah datang kembali ke bangku cepat"
    pb2 pb3 "Ok ok"
    mc "...."
    mc "Hmm.. Pakunya banyak sekali. bawa kerumah aja lah"
    mc "Apa ini di Loker ? tanganku ga bisa keluar"
    "[mc] terjatuh"
    mc "Gyahhh.. Aduh duh duh"
    sk "Hahahhahahahaha, bisa bisanya [mc] ngelawak"
    mc "Ahh.. Kakiku luka dan tanganku berdarah"
    sk "[mc] mau kemana ? ga mau bikin sesuatu yang lucu lagi ?"
    mc "...."
    sk "dia keluar, hahahha pasti rasanya malu sekali sampai keluar kelas"

    scene uks hitam putih
    gu "Kamu kembali lagi kesini, nanti kalau sudah segera kembali ke kelas"
    mc "...."
    mc "aku mau diam disini sampai jam pertama habis"
    gu "sigh.. tapi setelah itu segera kembali ke kelas"
    mc "Iya"
    "~Ding Dong~"

    scene kelas kelas Hitam putih
    mc "Buku ku tidak ada, mungkin ada di tempat sampah"
    mc "Ternyata ada di-"

    "~Ding Dong~"
    scene kelas
    mc "haa haa haa.. aku menangis ? Mimpi itu lagii"
    mc "Untung aku tidak ketauhan kalau aku tertidur. Ternyata sudah jam pulang juga. aku harus bergegas pulang"
    
    scene lorong 

    scene depan rumah

    scene kamar

    scene ruang makan 
    mc "Ibu, Ayah, Boleh memlihara kucing ?"
    mom dad "Tentu saja Boleh"
    mc " Besok aku akan membawanya"
    dad "Nanti ayah belikan kandang juga buat kucingnya"
    mc "aku sudah selesai"
    "~Cuci Piring~"
    mc "aku kembali ke kamar dulu"
    mom "Pa,  aku kaget anak kita setelah sekian lama meminta sesuatu, aku sangat bersyukur anak kita perlahan juga membaik"
    dad "Iyaa.. Ma, aku juga sangat bersyukur. Tadi aku juga sampai terharu ma"
    mom "iyaa aku juga paa, Mari kita berdoa supaya selalu terjadi hal baik untuk anak kitaa sekarang untuk kedepannya"
    mom dad "Aamiin"

    return
