label interruption1:

    call ring_phone

    d "Oh, my phone's ringing. Could you answer it, [player_name]?"

    menu:
        "Pick up":

            hide phone
           
            p "Hi, you've reached Dave's phone but he's unavailable right now. This is his [sibling_ref]."
           
            # move Dave left, show Kristina (a silhouette) right
            show dave at left
            show kristina at right

            kristina "Um, hi. Is Dave okay? He left me a voice note about having hurt his head..."

            p "{=internal}Guess I wasn't the only one he called."

            menu:
                
                "Don't worry, I'm with him and I'm taking him to hospital to get checked over.":

                    kristina "That's a relief. Thanks, [player_name] - I'll leave you to it!"

                    hide kristina
                    show dave at center 

                "We're in an ambulance on our way to A&E.":

                    kristina "Oh my God, is he gonna be okay?"

                    p "I think so. He's still conscious and talking and stuff."

                    kristina "Jesus, you really had me worried for a second there! Alright, I'll leave you to it."

                    hide kristina
                    show dave at center

        "Ignore the call":
    
            p "Actually, let's leave it. You can call them back when you're feeling better."

            d "Yeah, okay."

            hide phone

    d "Thanks - I don't really feel well enough to update people just now."

    p "No problem."
    
    p "{=internal}We've made it to the hospital."

    return