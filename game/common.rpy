
# Use with "call common_tpih", not jump

label common_tpih(loop_n):
    # "Time"

    show dave confused
    d "What year is it?"

    if loop_n > 1 and loop_n < 4:
        p "{=internal}Oh man, here we go again."

    if loop_n >= 4:

        p "{=internal}This is really getting old."

    if loop_n > 2 and loop_n < 5:

        p "{=internal}I guess I should try to be patient with him."

    if loop_n >= 6 and loop_n < 10:
        if count_impatience >= 3:

            p "{=internal}This is getting seriously annoying now."

        else:

            p "{=internal}I bet he won't even remember how hard I'm trying here."

    if loop_n == 10:

            p "{=internal}Even if Dave won't remember this, I'm proud that I've tried my absolute best to be reassuring."

    if loop_n == 1:

        menu: 
            
            "2016.":
                d "Oh, good."
            "What year do you think it is?":
                d "Uh... 2016?"
                p "Yep."

    else:

        menu:
            "2016.":
                jump .restofit

            "What happened to you?" if loop_n == 2:

                d "I don't really remember."

                stranger "One of his jump-stilts caught on the other and he tripped headfirst onto the pavement."

                p "Ouch."

            "This sucks, huh?" if loop_n == 3:

                d "Sure does."

label .restofit:

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
            p "{=internal}And to nobody's surprise, he tries to touch his head, but his helmet gets in the way."
            show dave smiling
            d "Good thing I was wearing this!"

    if location == "park" or location == "ambulance":
        "Yeah, your wrist might be sprained or broken, I'm not sure."
    else:
        "Yeah, the medics reckon your wrist is probably broken, sorry."

    $ count_patience = count_patience + 1

    return