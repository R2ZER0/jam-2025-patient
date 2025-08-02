label park:


# Please insert code to make park background art fade in.
# Insert code to make Dave_smiling sprite appear in the centre.

# Insert alt text "You arrive at the park. 
# It is a sunny day and there is plenty of green space.
# Your stepbrother, Dave, is a slim white guy in his twenties. 
# He's wearing a T-shirt, tracksuit bottoms, and a helmet.
# He notices you and smiles as you come over."

    p "Dave, there you are! I've been so worried!"

    d "Oh, hi [player_name]. I think I hit my head, it really hurts."

    p "...Yeah, I know you did, you told me so like ten minutes ago."

    # Change sprite from Dave_smiling to Dave_confused
    # Add alt text "Dave looks puzzled."

    d "I did?"

    # Move Dave_confused to the left, add Silhouette_1 to the right.
    # Add alt text "A stranger nearby inserts themself into your conversation."

    s "Yeah, his memory sort of loops every few minutes."

    p "What the...?"

    s "Don't worry, I already called an ambulance - they're on their way."

    p "Oh, uh, thank you."

    s "No problem."

    # Exit Silhouette_1 to the right, move Dave_confused to centre again.

    d "I don't remember them calling me an ambulance, either."

    

    



menu:
    "It's 2016":
        p "It's 2016"

    "You don't know what year it is?!":
        "..."

    "???":
        "???"