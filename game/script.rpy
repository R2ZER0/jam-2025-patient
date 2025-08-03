# The script of the game goes in this file.
default player_name = "Phoenix"
default gender = "nb"
default wrong_gender = "f"
default sibling_ref = "stepsibling"
default gender_formalism = "xir"
default wrong_gender_formalism = "ma'am"
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

    call common_tpih(1)

    call common_tpih(2)

    call common_tpih(3)

    call ambulance

    call common_tpih(4)

    call common_tpih(5)

    call interruption1

    call hospital_ae

    call hospital_corridor

    show dave smiling

    d "Thank you so much for looking after me while I was concussed!"

    d "It would've been really scary to go through by myself."

    d "You're the best, [player_name]!"

    hide dave

    "We ran out of time to wrap up this game properly, but we hope you enjoyed it!"

    "Credits"
    
    "Writing by Jo"
    
    "Coding by Rikki"

    "Dave sprites by Jo"

    "Park background by Rikki"
      
    "Silhouette art from Victeezy.com"
    
    "All other backgrounds are edited versions of free-to-use, no-attribution images from Pixabay"

    # This ends the game.
    return
