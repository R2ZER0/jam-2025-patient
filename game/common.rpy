
# Use with "call common_tpih()", not jump

label common_tpih():
    # "Time"

    # Set sprite to Dave_confused

    d "What year is it?"

menu: 
    "2016.":
        d "Oh, good."
    "What year do you think it is?":
        d "Uh... 2016?"
        p "Yep."

    d "What month is it?"

menu:
    "July.":
        d "Weird."
    "Have a guess.":
        d "Um... June?"
        p "Close."
        d "July?"
        p "Yep."
        d "Nailed it."

    # "Place"

    d "Where are we?"

menu:
    "[currentlocation]":
        # If "Park"
        d "What am I doing here?"

    "Injuries"
    "Helmet"
    "Etc"
return