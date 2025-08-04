label interruption3:

    call ring_phone

    d "Oh, there goes my phone. Care to do the honours, [player_name]?"

    menu:
        "Pick up":

            hide phone
           
            p "Hi, you've reached Dave's phone but he's unavailable right now. This is his [sibling_ref], [player_name]."
           
            # move Dave left, show Stuart (a silhouette) right
            show dave at left
            show stuart at right

            stuart "Hi [player_name], it's Stuart. Just got a message from Dave that he hurt his head. Was it serious?"

            p "{=internal}I'm beginning to think Dave called everyone in his contacts about this..."

            menu:
                
                "Hopefully not. Don't worry, I'm with him and he's been seen by a doctor.":

                    stuart "Nice one. I look forward to hearing about his shenanigans when he's recovered."

                    p "Me too."

                    stuart "Alright, see ya!"

                    hide stuart
                    show dave at center 

                    p "I'm glad you have pals who care about you."

                    d "Same!"

                    p "I do kinda wish you hadn't called so many of them, though!"

                    show dave confused

                    d "Huh, I can't remember calling anyone."

                    p "I mean, I'm glad you called me, otherwise I wouldn't be here. So good job, I guess."

                    show dave smiling

                    d "Thanks."

                "Might be - his memory's a bit damaged. We're at A&E and he's been checked over by a doctor.":

                    stuart "Oh damn! Keep me posted when you get a chance, yeah?"

                    p "Will do."

                    hide louis
                    show dave at center

                    # show dave_confused

                    d "You make me sound like an antique or something."

                    d "'A bit damaged but still has some value to the right person.'"

                    p "Sorry, I didn't mean it like that."

                    # show dave_smiling

        "Ignore the call":
    
            p "Actually, let's leave it. You can call them back when you're feeling better."

            d "Yeah, okay."

            hide phone

    d "Thanks - I don't really feel up to socialising."

    p "No problem."

    d "Hey, people with head injuries sometimes act pretty weird. Am I acting weird?"

    p "{=internal}Aside from the looping memory, you're like your usual self... But the memory thing is pretty weird."

    p "You could say that, yeah - a bit."

    d "Is it funny or just distressing?"

    p "...A bit of both?"

    d "You should film me, then! I want to see the funny bits when I'm feeling better."

    p "Uh, are you sure?"

    d "Yeah, do it!"

    menu:

        "Okay...":
            $ is_filming = True
            d "Awesome!"

        "I don't think that's a good idea.":
            $ is_filming = False
            d "Aww... okay."

    return