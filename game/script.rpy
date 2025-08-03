# The script of the game goes in this file.
default player_name = "Phoenix"
default gender = "nb"
default wrong_gender = "f"
default sibling_ref = "stepsibling"
default gender_formalism = "xir"
default wrong_gender_formalism = None
default count_patience = 0
default count_impatience = 0

# location can be:
# * travelling
# * park
# * ambulance
# * hospital_ae
# * hospital_corridor
# Start travelling
default location = "travelling"
default location_human = "Rushing"


# The game starts here.

label start:


    # counters, variables, flags

    $ count_patience = 0
    $ count_impatience = 0

    # 
    call ask_player_info
    # Now we have the variables `player_name`, `gender` and `wrong_gender`

    define p = Character("[player_name]")
# old debug code, ignore    "DEBUG: Hello name=[player_name] gender=[gender] wrong_gender=[wrong_gender]"

    call monologue1

    call park

    call dia_loop_1

    call dia_loop_2

    call dia_loop_3

    call ambulance

    call dia_loop_4

    call dia_loop_5

    call interruption1

    # This ends the game.
    return
