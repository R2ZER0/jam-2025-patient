label ambulance:
    
    p "{=internal}The paramedic wastes no time, directing Dave into the back of the ambulance."

    p "Hey, um, I can squeeze in there too, right?"

    # show silhouette

    paramedic "Are you family?"

    p "Yeah - I'm his next of kin."

    paramedic "Right, hop in then."

    p "Thanks."

    # change background to ambulance interior

    # show Dave left, paramedic silhouette right

    p """
    
    {=internal}Phew, thank goodness I didn't have to go through the whole 'we're totally blood relatives' palaver this time.

    {=internal}I hate having to lie to people about it, but it's the only way to make sure Dave gets looked after.

    {=internal}Seriously, whoever decided on the next of kin rules was a jerk.
    
    {=internal}Partners only count if they're married or in a civil partnership - hospitals ignore them otherwise, even if you live together.
    
    {=internal}On the other hand, biological relatives get an automatic pass regardless of how you feel about each other.

    {=internal}And even the term 'next of kin' doesn't have any legal rights associated with it.
    
    {=internal}It's total nonsense. 
    
    {=internal}Even if Mum and John didn't live further away than me, I can't imagine Dave would ever want either of them as his next of kin.

    {=internal}Just trying to imagine it is stressful beyond belief.

    """

    # need misgendering coding for this bit
    # BONUS add the optional coding to skip the misgendering and instead get gendered correctly first time.
    
    paramedic "Hey," #add gendered form of address based on wronggender, if m then "sir", if f then "ma'am", if panic then "uh... um... excuse me"

    paramedic "Please can you talk with him while I sort out his wrist? Just keep him calm till we arrive."

    p """
    
    "Sure."

    {=internal}It's hard to gauge whether to mention my gender to people in situations like this.
    
    {=internal}Like, we have other priorities to deal with, and we won't be interacting for long...
    
    {=internal}but it makes me so uncomfortable when they call me the wrong thing or flounder awkwardly.

    """

    menu:

        "Speak up.":

            p "It's actually 'x', not 'y'." #insert correct version based on gender. m = sir, f = ma'am, nb = xir if you insist on being formal. insert incorrect version based on wronggender. if wronggender = panic, cut ", not y".

            p "Or you can just call me [player_name]."

            paramedic "Oh, sorry 'x'."

            p "{=Internal}I never know what to say when they apologise. 'Apology accepted' just feels passive-aggressive..."

            p "No worries."

            p "{=internal}But downplaying it also feels weird. There's just no winning, I guess."

        "Let it go.":

            p """
            
            {=internal}It's fine.

            {=internal}Well, it's not fine, but I'll live.

            {=internal}Just another little wound that will scar over with time.

            {=internal}I wish people would just {i}ask{/i} what to call me instead of assuming... 

            """

    # move Dave_confused to centre, exit right paramedic