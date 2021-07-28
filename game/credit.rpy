label credits:
    image splash2 = Text("{size=90}Politeknik Negeri Jember", text_align=0.5, ypos=0.5) #Placeholder code if you don't have anything to use as a splash image or are just pure lazy.
#    image splash = "images/Company-Logo.png" #This is usually going to be located in an init block executed early in the code to show it when the game loads up as a splash screen.
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image poltek = "poltek.png"
    image grats = Text("{size=160}Terima Kasih{/size}", text_align=0.5, color="#000000")
    image sambutan = Text("{size=60}Koordinator TA \nDosen Pembimbing \nDosen-Dosen Lainnya \nSemua Penghuni JTI \nSemua yang mendukung{/size} ", text_align=0.5, color="#000000")
    image grats2 = Text("{size=160}Terima Kasih{/size}", text_align=0.5, color="#000000")
    image sambutan2 = Text("{size=50}Arseniy Chebynkin From ArtStation and DeviantArt \ngiaonp From DeviantArt \nSemua Creator DeviantArt \nLove, Money, Rock'n'Roll From Project Soviet
    \nSummer Pockets From Key Project{/size}\n", text_align=0.5, color="#000000")
    image cred = Text(credits_s, text_align=0.5, color="#000000")
    image theend = Text("{font=earwig factory rg.ttf}{size=150}~The End~", text_align=0.5, color="#000000")
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5, color="#000000")
    $ credits_speed = 25 #scrolling speed in seconds

    $ quick_menu = False
    $ _skipping = False
    stop music fadeout 1.0
    window hide dissolve
    scene sky #replace this with a fancy background
    play music kesepian fadein 1.0
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(5)
    hide theend
    with dissolve
    with Pause(credits_speed - 5)
    show grats at center:
        ypos 0.2
    show sambutan at center behind grats:
        ypos 0.65
    with dissolve
    with Pause(3)
    hide grats
    hide sambutan
    with dissolve
    with Pause(1)
    show grats2 at center:
        ypos 0.2
    show sambutan2 at center behind grats:
        ypos 0.75
    with dissolve
    with Pause(3)
    hide grats2
    hide sambutan2
    with dissolve
    with Pause(1)
    show splash2 at center:
        xpos 0.55
        ypos 0.5
    show poltek at center behind splash2:
        ypos 0.55
        zoom 0.5
        xpos 0.2
    with dissolve
    with Pause(3)
    hide poltek
    hide splash2
    with dissolve
    with Pause(1)
    show poltek at truecenter
    with dissolve
    with Pause(3)
    hide poltek
    with dissolve
    with Pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve

    $ _skipping = True
    $ quick_menu = True

    stop music fadeout 1.0
    $ renpy.full_restart()
    return

init python:
    credits = ('Backgrounds', 'Michel Meirisca Heniaty - E31182133'), ('Backgrounds', 'Hernando Farazi Herrera - E31182235'), ('Characters', 'Michel Meirisca Heniaty - E31182133'), ('GUI', 'Hernando Farazi Herrera - E31182235'), ('Writing', 'Nina Ardana - E31180941'), ('Writing', 'Hernando Farazi Herrera - E31182235'), ('Programming', 'Hernando Farazi Herrera - E31182235'), ('Music', 'Hernando Farzi Herrera - E31182235')
    credits_s = "{font=earwig factory rg.ttf}{size=160}SchoolDayz{/size}{/font}\n\n\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()
