# The script of the game goes in this file.
default player_name = "Phoenix"
default gender = "nb"
default wrong_gender = "f"
default sibling_ref = "stepsibling"
default gender_formalism = "xir"
default wrong_gender_formalism = "ma'am"
default count_patience = 0
default count_impatience = 0
default count_filmed_loops = 0

# choice flags
default chose_tell_option = False
default chose_feeling_ok_option = False
default is_filming = False

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
    $ chose_tell_option = False
    $ chose_feeling_ok_option = False
    $ is_filming = False
    $ count_filmed_loops = 0

    # 
    call ask_player_info
    # Now we have the variables `player_name`, `gender` and `wrong_gender`

    define p = Character("[player_name]", color="#229379")
# old debug code, ignore    "DEBUG: Hello name=[player_name] gender=[gender] wrong_gender=[wrong_gender]"

    call monologue1

    call park

    call common_tpih(1)

    call common_tpih(2)

    call common_tpih(3)

    call ambulance

    call common_tpih(4)

    call common_tpih(5)

    call interruption1

    call hospital_ae

    call hospital_corridor

    call common_tpih(6)

    call interruption2

    call common_tpih(7)

    call common_tpih(8)

    call interruption3 

    call common_tpih(9)
  
    call interruption4

    call common_tpih(10)

    call monologue7

    call home

    

    # This ends the game.
    return
