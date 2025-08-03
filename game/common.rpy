
# Use with "call common_tpih", not jump

label common_tpih:
    # "Time"

    show dave confused
    d "What year is it?"

    menu: 
        "2016.":
            d "Oh, good."
        "What year do you think it is?":
            d "Uh... 2016?"
            p "Yep."

        d "What month is it?"

    menu:
        "July.":
            d "Weird."
        "Have a guess.":
            d "Um... June?"
            p "Close."
            d "July?"
            p "Yep."
            d "Nailed it."

    # "Place"

    d "Where are we?"

    p "[location_human]"

    if location == "park":
        d "What am I doing here?"
        p "I'm pretty sure you were jump-stilting and hit your head."
        d "...Oops."
    else:
        d "Right. That's probably good - I think I hit my head."

    # "Injuries"

    d "My head really hurts. So does my wrist."

    menu:
        "Yeah, I'm pretty sure you have a concussion.":
            # "Helmet"
            # internal "And to nobody's surprise, he tries to touch his head, but his helmet gets in the way."
            show dave smiling
            d "Good thing I was wearing this!"

    if location == "park" or location == "ambulance":
        "Yeah, your wrist might be sprained or broken, I'm not sure."
    else:
        "Yeah, the medics reckon your wrist is probably broken, sorry."

    $ count_patience = count_patience + 1

    return