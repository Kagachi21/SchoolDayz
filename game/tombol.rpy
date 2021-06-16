init:
    transform cardSize:
        zoom 0.1

screen gotoKirana():
    imagebutton:
        xalign 0.10
        yalign 0.5
        idle "/Button_pilih/Card_Kirana.png"
        hover "/Button_pilih/Card_Kirana_Hover.png"
        action Jump("day1_Kirana")
        activate_sound "/audio/ClickSound/title_decide01.ogg"
        at cardSize

screen gotoMiselia():
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "/Button_pilih/Card_Miselia.png"
        hover "/Button_pilih/Card_Miselia_Hover.png"
        action Jump("day1_Miselia")
        activate_sound "/audio/ClickSound/title_decide01.ogg"
        at cardSize

screen gotoAirin():
    imagebutton:
        xalign 0.90
        yalign 0.5
        idle "/Button_pilih/Card_Airin.png"
        hover "/Button_pilih/Card_Airin_Hover.png"
        action Jump("day1_Airin")
        activate_sound "/audio/ClickSound/title_decide01.ogg"
        at cardSize