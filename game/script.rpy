# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:


    # counters, variables, flags

    $ count_patience = 0
    $ count_impatience = 0


    # ask for player's info

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
    "And which binary gender do you typically get mistaken for?"

    "Male":
        $ wrong_gender = "m"
        jump start_got_player_info

    "Female":
        $ wrong_gender = "f"
        jump start_got_player_info

    "I present myself as quite androgynous, so cisnormative people tend to just panic":
        $ wrong_gender = "panic"
        jump start_got_player_info


label start_got_player_info:
    define p = Character("[player_name]")
# old debug code, ignore    "DEBUG: Hello name=[player_name] gender=[gender] wrong_gender=[wrong_gender]"

    call monologue1

    call park

    call 

    # This ends the game.
    return
