label interruption2:

    call ring_phone

    d "Oh, my phone's ringing again. Do you mind getting it, [player_name]?"

    menu:
        "Pick up":

            hide phone
           
            p "Hi, you've reached Dave's phone but he's unavailable right now. This is his [sibling_ref], [player_name]."
           
            # move Dave left, show Louis (a silhouette) right
            show dave at left
            show louis at right

            louis "Hey [player_name], Louis here. Dave left me a voicemail saying he'd hurt his head. Is he okay?"

            p "{=internal}How many people did he call about this?"

            menu:
                
                "Don't worry, I'm with him and he's been checked over by a doctor.":

                    louis "Cool. I hope it goes well. Tell Dave I'm thinking of him!"

                    p "I will."

                    louis "Cheers, bye!"

                    hide louis
                    show dave at center 

                    p "Hey Dave."

                    d "Yeah?"

                    p "Louis says they're thinking of you."

                    d "Wow. Truly, you are a master of comic timing."

                    p "Listen, someone has to step up and make dad jokes in times like this."

                    d "Valid."

                "Yeah, he smacked his head on the pavement pretty hard.":

                    louis "Damn, that sounds serious."

                    p "Yeah, his memory's kind of on a loop."

                    # BONUS - show dave_perplexed if we have it

                    d "Wait, what?"

                    louis "I'll leave you to handle that. Thanks for the update!"

                    hide louis
                    show dave at center

                    d "My memory's looping? Like in {i}Fifty First Dates{/i}?"

                    p "Uh, don't worry about it, Dave."

                    d "How am I meant not to worry about it?!?"

                    p "Well, uh... I guess you'll forget about it soon enough."

                    d "That is {i}not{/i} reassuring."

                    p "Sorry."

        "Ignore the call":
    
            p "Actually, let's leave it. You can call them back when you're feeling better."

            d "Yeah, okay."

            hide phone

    d "Thanks - it's good to have someone else to handle this stuff."

    p "No problem."

    return