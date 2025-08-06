# TODO: add code to make this work

p "Hey Dave, I'm just gonna go get some fresh air - I'll be back in a minute."

# TODO: please fix indents if needed

if location == ambulance:

    d "But... we're in a moving vehicle."

    menu:

        "Good point. Never mind.":
            # TODO: return to previous point of ambulance scene

        "I do what I want!":

            paramedic "Please don't try to open the doors -"

            p "You don't control me!"

            p "{=internal}I try to leap to freedom..."

            paramedic "...Well, now we have TWO patients for A&E."

            # BONUS TODO: cue trophy art as per below, but word art reads "Most Reckless Escapee" instead

# TODO: if location == park:

    d "But we're already outside."

    p "I mean I just need a minute to myself."

    # TODO: go to the below

# TODO: if location != ambulance

d "Oh, okay."

hide dave

# hide background with fade

p """

I know it's not his fault, but talking to him right now is so damn frustrating.

Hell, if I just walked away now, would it even matter?

There'll be medical staff to look after him.

I mean, sure, they're chronically overworked from all the massive cuts to the NHS, but still.

I could just leave. Dave won't even remember that I was ever here, after all.

"""

menu:

    "Go back to looking after Dave":

        p "What am I even thinking?!? It must be all the stress. I should get back to him."

        # add code to return to where you left off and pressed the quit button

    "Leave and do literally anything else you want"

        p """
        
        He's an adult. I don't have to babysit him.

        Sure, he's not in his right mind just now, but that's his problem.
        
        I'm out of here.

        """
        # BONUS add art of a gold trophy with the words "Worst Next of Kin Ever" in obnoxious word art arcing above it

        # add code to exit game