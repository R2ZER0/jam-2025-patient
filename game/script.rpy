# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


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

    # This ends the game.
    return
