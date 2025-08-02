# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip() # remove whitespace if they accidentally typed space or tab etc
    if player_name == "":
        $ player_name = "Phoenix" # default name if none is given

menu start_ask_gender:
    "What's your gender?"

    "Non-binary":
        $ gender = "nb"
        jump nb_what_typical_mistake
        jump start_got_player_info

    "Female": 
        $ gender = "f"
        $ wrong_gender = "m"
        jump start_got_player_info

    "Male":
        $ gender = "m"
        $ wrong_gender = "f"
        jump start_got_player_info

menu nb_what_typical_mistake:
    "And what binary gender do you typically get mistaken for?"

    "Male":
        $ wrong_gender = "m"
        jump start_got_player_info

    "Female":
        $ wrong_gender = "f"
        jump start_got_player_info

    "They tend to just panic":
        $ wrong_gender = "panic"
        jump start_got_player_info


label start_got_player_info:
    define p = Character("[player_name]")
    "DEBUG: Hello name=[player_name] gender=[gender] wrong_gender=[wrong_gender]"

    jump intro

    # This ends the game.
    return
