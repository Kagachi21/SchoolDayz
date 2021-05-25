# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
image splash = im.Scale("BGSplash.png",1920,1080)
image kucing = im.Scale("1.png", 745,745)
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
     
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
