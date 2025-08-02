label park:

# Please insert code to make park background art fade in.
    scene bg meadow

# Insert code to make Dave_smiling sprite appear in the centre.
    show dave smiling

    alt """
    You arrive at the park. 
    It is a sunny day and there is plenty of green space.
    Your stepbrother, Dave, is a slim white guy in his twenties. 
    He's wearing a T-shirt, tracksuit bottoms, and a helmet.
    He notices you and smiles as you come over.
    """

    p "Dave, there you are! I've been so worried!"

    d "Oh, hi [player_name]. I think I hit my head, it really hurts."

    p "...Yeah, I know you did, you told me so like ten minutes ago."

    # Change sprite from Dave_smiling to Dave_confused
    show dave confused
    alt "Dave looks puzzled."

    d "I did?"

    # Move Dave_confused to the left, add Silhouette_1 to the right.
    alt "A stranger nearby inserts themself into your conversation."
    show dave confused at left with move
    show stranger at right

    stranger "Yeah, his memory sort of loops every few minutes."

    p "What the...?"

    stranger "Don't worry, I already called an ambulance - they're on their way."

    p "Oh, uh, thank you."

    stranger "No problem."

    # Exit Silhouette_1 to the right, move Dave_confused to centre again.
    hide stranger
    show dave confused at center with move

    d "I don't remember them calling me an ambulance, either."

    # Make the next line "internal" style.

    p "Yikes, this could be really bad... but I probably shouldn't tell him that.
    I don't want him to be stressed out on top of being injured.
    I guess I'll just focus on first aid and keeping him calm till the ambulance gets here."

    # End the "internal" style.

    p "No big deal. Are you hurt anywhere other than your head?"

    d "Yeah, my wrist is really sore."

    p "Try to keep it still, then, just in case it's broken."

    # internal

    p "What on Earth happened to you?"

    # /internal

    d "...Um, this might be a weird question, but what year is it?"

    # internal

    p "Oh damn, this is not good."

    # /internal

    p "What year do you think it is?"

    d "2016?"

    # internal

    p "Thank goodness..."

    # /internal

    p "Yep, you got it."

    d "And, uh, what month is it? I'm guessing it's the summer?"

    p "Yeah. It's July."

    d "That's so weird..."

    p "What month were you expecting it to be?"

    d "I dunno, it's obviously warm out but I feel like it was literally just November."

    # internal

    p "Well, crap."

    # /internal

    p "No worries. I bet the last few months will come back to you once you've had a chance to heal up."

    # change Dave_confused to Dave_smiling

    d "Yeah!"

    # internal

    p "We settle down on a bench to bask in the sunlight while we wait. 
    A few minutes pass in comfortable silence."