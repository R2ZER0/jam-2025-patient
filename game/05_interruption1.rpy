label interruption1:

    call ring_phone

    d "Oh, my phone's ringing. Could you answer it, [player_name]?"

    menu:
        "Pick up":

            hide phone
           
            p "Hi, you've reached Dave's phone but he's unavailable right now. This is his [sibling_ref], [player_name]."

            p "{=internal}Oops, I should've left out the 'step' part... but the paramedic isn't listening. Phew."

            p "{=internal}They probably aren't allowed to kick people out of a moving vehicle anyway."

            show dave confused at center:
                ease 0.5 left

            show kristina at offscreenright:
                ease 0.5 right


            kristina "Um, hi. Is Dave okay? He left me a voice note about having hurt his head..."

            p "{=internal}Guess I wasn't the only one he called."

            menu:
                
                "Don't worry, I'm with him and I'm taking him to hospital to get checked over.":

                    kristina "That's a relief. Thanks, [player_name] - I'll leave you to it!"

                    show kristina at right:
                        ease 0.5 offscreenright

                    show dave at left:
                        ease 0.5 center

                    pause 0.5

                "We're in an ambulance on our way to A&E.":

                    kristina "Oh my God, is he gonna be okay?"

                    p "I think so. He's still conscious and talking and stuff."

                    kristina "Jesus, you really had me worried for a second there! Alright, I'll leave you to it."

                    show kristina at right:
                        ease 0.5 offscreenright

                    show dave at left:
                        ease 0.5 center

                    pause 0.5

        "Ignore the call":
    
            p "Actually, let's leave it. You can call them back when you're feeling better."

            d "Yeah, okay."

            hide phone

    d "Thanks - I don't really feel well enough to update people just now."

    p "No problem."
    
    p "{=internal}The ambulance finally stops moving. We've made it to the hospital."

    return