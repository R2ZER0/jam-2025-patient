label hospital_ae:
    $ location = "hospital_ae"
    $ location_human = "A&E."

    scene bg waitingroom with fade  # change background to waiting room

    p """

    {=internal}The paramedic bundles Dave off to be seen by a doctor.

    {=internal}While I'm glad that he's going to be seen quickly, it's not a good sign to be a high priority in triage.

    {=internal}Well, the only thing I can do now is check in with the receptionist and wait.

    """

    show receptionist

    receptionist "Hi there, how can I help you?"

    p "My brother's got a head injury and probably a concussion. Can I fill out his paperwork?"

    receptionist "Of course, please bear with me for a moment [wrong_gender_formalism]..." 
    
    p """
    
    {=internal}Part of me always thinks 'you should be used to this by now - toughen up and move on'.

    {=internal}But that part of me is the product of years of societal pressure to shut up and suffer unobtrusively, so screw that!

    {=internal}If cisgender people's identities can be treated with respect all the time, why should the rest of us settle for any less?

    {=internal}...On the other hand, though, having to have this conversation over and over again can be really draining.

    {=internal}And sometimes people get aggressive when I try to correct them, even though I'm always polite about it.

    {=internal}I've had numerous occasions where they try to debate me about the validity of trans people, which is gross.

    {=internal}Worse, some of them just start throwing slurs around or yelling at me.

    {=internal}I've got friends who have faced worse than that, too.

    {=internal}Sometimes it's just easier to put up with the misgendering than to deal with the stress of not knowing how someone might react to being corrected.

    {=internal}But whatever I do in the moment, I have to remind myself that things won't always be this bad. People can learn. They can improve.

    """

    menu:
        "Speak up":

            p "Actually, I'm a [gender_formalism], not a [wrong_gender_formalism]."

            receptionist "...Right."

            p "..."

            p """
            
            {=internal}Ugh. No apology, no correction, and a tone that's verging on sarcasm. Delightful.
            
            {=internal}I almost prefer the outspoken transphobes to the ones who hide it just enough to keep their jobs.

            {=internal}At least they're upfront about their bigotry.

            {=internal}Plus, it's harder to get management to take complaints seriously in less obvious cases.

            {=internal}...Not impossible, though. Especially if the manager cares about equality in general.

            {=internal}I don't know if I'll have the time or energy to chase it up on this occasion, though, given Dave's condition.
           
            """
            receptionist "Here are the forms you need to fill in."

            p "Thanks."

        "Let it go":

            p """
            
            {=internal}One of the many reasons emergencies are miserable is having to interact with so many strangers.

            {=internal}Even if I'd happened to be wearing a pronouns badge, it probably wouldn't have made much difference.
            
            {=internal}Whatever. I know who I am. 
            
            {=internal}Their ignorance is their own problem to deal with. I'm not responsible for educating them.

            {=internal}Deep breath in...

            {=internal}Hold it...

            {=internal}Deep breath out.

            {=internal}Aaand repeat.

            {=internal}Okay. I'm okay.

            {=internal}It does suck that I've been getting misgendered so much today, but I can get through this.

            """

            receptionist "Excuse me, [wrong_gender_formalism]? Here are the forms you need to fill in."

            p "{=internal}...This is so tiring."

            p "Thanks."
        
    hide receptionist

    p "{=internal}I zone out a little while filling in Dave's medical information. I've had to do this a few times, so I know the essentials by heart."

    show dave smiling at left
    show nurse at right

    nurse "Hello there [wrong_gender_formalism], the doctor said that Dave should hopefully make a good recovery."

    p "{=internal}Ugh, not again... I wish public-facing staff got basic training on trans inclusion."

    d "It's [gender_formalism], actually."

    nurse """
    
    Oh, my mistake! Sorry, [gender_formalism].

    We've given Dave some painkillers with an anti-inflammatory effect. 
    
    Please make sure he doesn't have any more for at least four hours.

    His short-term memory processing issue is likely to resolve with some rest, once the inflammation goes down.
    
    Still, we'd like to keep him here under observation for a little while just in case.

    The longer-term memory loss may well get better with time, but it's hard to predict how much.
    
    Anyway, we don't have any free beds to offer you, but if you could just stay in that corridor for now...

    """

    p "Will do!"

    hide nurse
    show dave at center # TODO: ease this? currently he just teleports

    p """
    
    {=internal}Thank goodness he's going to be okay.

    {=internal}Dave is such a sweetheart - ever since I told him how stressful it can be to correct people myself, he's just taken it on for me.

    {=internal}If every trans person had an ally like him, the world would be a much nicer place.

    Thanks.

    """
    
    d "Anytime."

    return