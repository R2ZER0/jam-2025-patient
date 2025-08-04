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

    receptionist "Of course, please bear with me for a moment..." # BONUS add misgendering segment here?

    hide receptionist

    p "{=internal}I zone out a little while filling in Dave's medical information. I've had to do this a few times, so I know the essentials by heart."

    show dave smiling at left # TODO: minus helmet?
    show nurse at right

    nurse """
    
    Hello there [wrong_gender_formalism], the doctor said that Dave should be just fine. 
    
    Still, we'd like to keep you two here for a little while just in case.

    """

    p "{=internal}Ugh, not again... I wish public-facing staff got basic training on trans inclusion."

    d "It's [gender_formalism], actually."

    nurse "Oh, my mistake! Sorry, xir. Anyway, we don't have any free beds to offer you, but if you could just stay in that corridor..."

    p "Will do!"

    hide nurse
    show dave at center

    p "{=internal}He's such a sweetheart - ever since I told him how stressful it can be to correct people myself, he's just taken it on for me."

    p "Thanks."
    
    d "Anytime."

    return