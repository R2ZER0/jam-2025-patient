# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    $ player_name = renpy.input("Sorry, who are you?")
    $ player_name = player_name.strip() # remove whitespace if they accidentally typed space or tab etc
    if player_name == "":
        $ player_name = "Person" # default name if none is given

menu start_ask_gender:
    "What's your gender?"

    "Non-binary":
        $ gender = "nb"

    "Female": 
        $ gender = "f"

    "Male":
        $ gender = "m"



label start_got_player_info:
    "DEBUG: Hello [player_name] [gender]"

    jump intro

    # This ends the game.
    return
