label interruption4:

    call ring_phone

    d "Oh hey' someone's calling me. Would you mind getting that?"

    menu:
        "Pick up":

            hide phone
           
            p "Hi, you've reached Dave's phone but he's unavailable right now. This is his [sibling_ref], [player_name]."
           
            # move Dave left, show alex (a silhouette) right
            show dave at left
            show alex at right

            alex "Hi there, I'm Alex - one of Dave's friends."
            
            alex "Apparently he's hurt his head. Was that for real or some kind of prank?"

            p "{=internal}That would be a pretty messed-up thing to joke about... but Dave {u}is{/u} a bit of a prankster."

            menu:
                
                "For real, unfortunately. Don't worry, I'm with him and we're just waiting to be discharged from the hospital.":

                    alex "Oh dear. Well, I'm glad he's got you with him. I'll let you get on with things!"

                    p "Thanks, have a nice day!"

                    p "{internal}Customer service reflexes never die, I guess."

                    hide stuart
                    show dave at center 

                    d "'Have a nice day'? You sound like a chatbot or something.'"

                    p "Rude. Just wait till you've had to work customer service - it becomes ingrained over time."

                    d "Must be pretty repetitive."

                    p "You have no idea. It's kind of nice when customers treat you like a real person, at least."

                    d "...You're really not selling the experience."

                "Not a prank, I'm afraid. We're in A&E.":

                    alex "Crap! Is he going to be okay?"

                    p "I hope so. I'll update you when we know more, if you want."

                    alex "Yes, please do. Thanks for getting him to hospital!"

                    p "No problem. Honestly, the ambulance driver's doing all of the work on that front."

                    alex "You're in an ambulance?!?"

                    p "{=internal}Maybe this was not the best thing to mention, now that I think of it."

                    p "Uh, yep. Just to be on the safe side, you know?"

                    alex "...Right. Well, good luck with it all. Bye for now!"

                    hide alex
                    show dave at center

                    # show dave_confused

                    d "I think you stressed them out a bit."

                    p "I didn't mean to!"

                    d "Yeah, I know. Don't worry about it."

                    # show dave_smiling

        "Ignore the call":
    
            p "Actually, let's leave it. You can call them back when you're feeling better."

            d "Yeah, okay."

            hide phone

    d "Thanks for handling that."

    p "No problem."

    return