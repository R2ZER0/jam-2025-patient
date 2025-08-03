default player_name = "Phoenix"
default gender = "nb"
default wrong_gender = "f"

label ask_player_info:
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

    "Female": 
        $ gender = "f"
        $ wrong_gender = "m"
        return

    "Male":
        $ gender = "m"
        $ wrong_gender = "f"
        return

menu nb_what_typical_mistake:
    "And what binary gender do you typically get mistaken for?"

    "Male":
        $ wrong_gender = "m"
        return

    "Female":
        $ wrong_gender = "f"
        return

    "I present myself as quite androgynous, so they tend to just panic":
        $ wrong_gender = "panic"
        return