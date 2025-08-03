# Usage:
#
# call ring_phone
# ...
# hide phone

label ring_phone:
    # Play phone animation with a ringtone sound effect
    play sound ringtone
    show phone at center:
        # Shake the phone a bit
        rotate 15
        pause 0.1
        rotate -15
        pause 0.1
        repeat 10
    return