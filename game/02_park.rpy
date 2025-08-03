label park:

    # Fade in meadows
    scene bg meadow with fade

    $ current_location = "The park."

    # show defaults to centre
    show dave smiling

    alt """
    You arrive at the park. 
    It is a sunny day and there is plenty of green space.
    Your stepbrother, Dave, is a slim white guy in his twenties. 
    He's wearing glasses, a T-shirt, tracksuit bottoms, and a helmet.
    He notices you and smiles as you come over.
    """

    p "{=internal}I can see his jump-stilts sitting abandoned on the floor next to him."

    # BONUS: display pop-up image of some jump-stilts for reference, since most people won't know what they are
    # BONUS: add alt text "The jump-stilts are a pair of contraptions with fairly complicated-looking parts.
    # Each one has a metal section to strap the user's calf, a place for their foot to rest on, and attached to various springs is a long, curved blade like a prosthetic leg with a rubber tip."

    
    p "{=internal}Guess that explains how he got hurt - those things are not the safest.
    In fact, they look almost comically unsafe for human use."


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

    p "{=internal}Yikes, this could be really bad... but I probably shouldn't tell him that.
    I don't want him to be stressed out on top of being injured.
    I guess I'll just focus on first aid and keeping him calm till the ambulance gets here."

    p "No big deal. Are you hurt anywhere other than your head?"

    d "Yeah, my wrist is really sore."

    p "Try to keep it still, then, just in case it's broken."

    p "{=internal}Like the memory loss wasn't bad enough!"

    d "...Um, this might be a weird question, but what year is it?"

    p "{=internal}Oh damn, this is not good."

    p "What year do you think it is?"

    d "2016?"

    p "{=internal}Thank goodness..."

    p "Yep, you got it."

    d "And, uh, what month is it? I'm guessing it's the summer?"

    p "Yeah. It's July."

    d "That's so weird..."

    p "What month were you expecting it to be?"

    d "I dunno, it's obviously warm out but I feel like it was literally just November."

    p "{=internal}Well, crap."

    p "No worries. I bet the last few months will come back to you once you've had a chance to heal up."

    show dave smiling

    d "Yeah!"

    p """
    
    {=internal}We settle down on a bench to bask in the sunlight while we wait. 
    I look up first aid for head injuries on my phone, just to be sure.

    {=internal}'Check if the patient is responsive and look out for signs of concussion. 
    Ensure their airways are clear and they are breathing.

    {=internal}Call an ambulance immediately if you suspect a serious head injury.

    {=internal}Don't remove their helmet if they're wearing one, unless it's absolutely necessary to clear their airway.'
    
    {=internal}Pretty much what I half-remembered from my first aid course. Good.

    {=internal}A few moments pass in comfortable silence, until...

    """

    # change Dave_smiling to Dave_confused

    d "Hey [player_name], I think I hit my head - it really hurts."

    p "Yeah, man, you did. We're just waiting for an ambulance now."

    d "Oh, okay. That makes sense."