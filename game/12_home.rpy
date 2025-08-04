label home:

    scene bg home with fade # TODO: check this works!

    pause 1.0 # FIXME: 1-second pause just to check that the scene loads, replace with actual content?

    # tally up Patient and Impatient points, direct to appropriate ending
    $ patience_difference = count_patience - count_impatience
 
    # patience_differences is positive if they were more patient, or negative if more impatient

    if patience_difference >= 2:
        call best_end

    elif patience_difference <= -3:
        call worst_end

    else:
        call mid_end

    return