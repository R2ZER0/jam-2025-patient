label ask_player_info:
    # ask for player's info

    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip() # remove whitespace if they accidentally typed space or tab etc
    if player_name == "":
        $ player_name = "Phoenix" # default name if none is given

menu .start_ask_gender:
    "What's your gender?"

    "Non-binary":
        $ gender = "nb"
        jump .nb_what_typical_mistake

    "Female": 
        $ gender = "f"
        $ wrong_gender = "m"
        jump .set_variables

    "Male":
        $ gender = "m"
        $ wrong_gender = "f"
        jump .set_variables

menu .nb_what_typical_mistake:
    "And what binary gender do you typically get mistaken for?"

    "Male":
        $ wrong_gender = "m"
        jump .set_variables

    "Female":
        $ wrong_gender = "f"
        jump .set_variables

    "I present myself as quite androgynous, so they tend to just panic":
        $ wrong_gender = "panic"
        jump .set_variables

label .set_variables:
    # if gender = m, stepbrother. if = f, stepsister. if = nb, stepsibling.
    if gender == "m":
        $ sibling_ref = "stepbrother"
    elif gender == "f":
        $ sibling_ref = "stepsister"
    else:
        $ sibling_ref = "stepsibling"

    return