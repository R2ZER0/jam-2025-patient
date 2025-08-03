
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

                p "Ouch." # No 'Impatient' points should get added to this one.

            "What's taking that ambulance so long?" if loop_n == 3:

                d "You called an ambulance? Seems like overkill..."

                p "{=internal}I wish I could agree. I shouldn't let on how bad things are, though."

                p "Well, y'know, better safe than sorry!"

                d "I guess, but it's kind of embarrassing."

                p "{=internal}If - I mean, {u}when{/u} - you get better, I'm gonna tell all your friends how skewed your priorities are."
                
                d "Plus, won't they be annoyed we called them out over a little bump to the head?"

                p "Trust me, we're doing the right thing."

                d "If you say so..."

                # Add 'Impatient' point.

            "I've never been in an ambulance before." if loop_n == 4:

                d "Me neither. Well, not that I can remember."

                p "{=internal}Oh, the irony."

                d "I wonder if we're allowed to take selfies in here."

                p "That's what you're focusing on right now?!?"

                d "What? It'll make for a cool anecdote someday. I might as well have a picture to go with it."

                p "I can't argue with that logic."

                p "{=internal}I really hope this'll just be a funny anecdote someday..."

                d "What's that look for?"

                p "What look?"

                d "I dunno, sort of zoned-out and... sad, maybe?"

                p "{=internal}Damn, I need to work on my bedside manner."

                p "Just thinking about how I skipped lunch to be here."

                d "Ha, that is pretty tragic. I'll buy you a snack from the hospital vending machines if you want."

                # Add 'Impatient' point

            "What's going to happen when we get to the hospital?" if loop_n == 5:

                show dave center: 

                    ease 0.5 left # Need to test this, make sure it works!
                
                show paramedic right
                
                paramedic "I'll make sure Dave here gets assessed by a doctor as soon as possible."

                d "But there are always massive queues in A&E, though."

                paramedic "There are, but we prioritise urgent cases."

                d "I thought urgent cases were like heart attacks and nasty car crashes and stuff."

                paramedic "Those can be extremely urgent, yes. But some concussions are urgent too, which is why the doctor should assess you promptly."

                d "Oh. Okay."

                p "{=internal}Dave's trying to put on a brave face, but I can see through it. He's totally stressing out."

                p "{=internal}In hindsight, maybe this wasn't the most reassuring topic to bring up."

                hide paramedic

                show dave:
                    ease 0.5 center # Move Dave back to centre

                # Add 'Impatient' point

            "How long are they going to make us stay here?" if loop_n == 6:

                d "No idea, they didn't say."

                p "{=internal}Or you just instantly forgot..."

                p "I guess we just play the waiting game, then."

                d "What, you wanna play 'I Spy' or something?"

                p "No, it's just what people say."

                d "Which people?"

                p "I dunno."

                d "Seems weird to talk about a game and not play one."

                p "{=internal}He's actually pulling out his phone to look it up."
                
                p "{=internal}Never change, bro."

                d "Oh, it's a reference to tactics, apparently."
                
                d "It means holding off on doing stuff and observing so you can figure out the best course of action."

                p "{=internal}Huh, I never knew that. I always thought it was just a silly figure of speech."

                p "You're such a word nerd."

            "Do you want me to tell Mum and John about your accident?" if loop_n == 7:
                # or if this wasn't selected in loop_7, show it again in loop_8

                d "Nah. They'd only worry."

                p "Fair."

                d "Plus, you know Megan would make Dad drive her up here even if we ask her not to."

                p "Heh, that's {i}exactly{/i} what Mum would do."

                d "And you know what they're like - I don't want to inflict that on the A&E staff."

                p "Yeah, me neither."
                
                p """
                
                {=internal}He's being polite. We both know it's my mum who's the core of the issue.

                {=internal}None of us know exactly what's up with her, but she's not doing well.

                {=internal}There's something extremely unusual about how she thinks and acts.

                {=internal}She refuses to let a doctor see her, though, so who knows what's causing it!

                {=internal}It's got more obvious over the years, whatever it is.

                {=internal}She causes a scene wherever she goes and she never listens to any of us.

                {=internal}I wouldn't want to deal with that while I had a concussion, either.

                We should probably update them in a day or two, once you've had a chance to recover.

                """
                d "Good idea."

                p "{=internal}Assuming that we ever get out of this place..."

                # Do not add any points

            "How much do you remember?" if loop_n == 8: #and
            # add code for "Do you want me to tell Mum and John?" was picked in loop_7:

                d "About what?"

                p "Anything! Do you remember what movie we saw last week?"

                d "Hmm..."

                p "Don't strain yourself, they said to take it easy."

                d "But you asked, so I'm trying to remember!"

                p "Don't worry about it."

                d "What was the movie?"

                p "Ghostbusters. But I meant like, what do you remember in general?"

                d """
                
                I'm not sure what happened to me or how I got here.

                Before that... I've been living in London for a few months, working on placement for my uni course.

                It's been okay, but I miss my friends.

                """

                p "{=internal}Yeah, he came back this spring. Guess he's still only remembering up to November."

                p "That tracks."

                p "{=internal}I really hope he doesn't lose all those memories forever."

                # Add 'Impatient' point

            # Add fancy coding to make .restofit have different bits to recognise it if you're filming

            "Are you feeling okay?" if loop_n == 9:

                d "Not really. My head's sore and I'm pretty sure I'm missing a big chunk of my memories."
                
                d "In fact, I'm not even sure which year of uni I'm in... Can you tell me?"

                p "Well, all of your friends have graduated"

                # BONUS - show Dave_flabbergasted

                p "and you've just finished your... what was it called...?"

                d "Did you just say {i}all of my friends have GRADUATED{/i}?!?"

                p "Yeah, and you've just finished your placement."

                # BONUS - show Dave_dismayed

                d "Oh {i}shit!{/i}"

                p "{=internal}Oops."

                d "I've {i}finished{/i} my placement?"

                p "Yes."

                d "{i}Fucking hell!{/i}"

                p "{=internal}So much for keeping him calm..."

                p "I know this is a lot to take in, but please try to keep your voice down - we're still in A&E."

                d "{size=-10}Holy shit...{/size}"

                # BONUS - if needed, show Dave_confused again to set back to normal

            

            

                










            







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