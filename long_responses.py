import random

R_EATING = "I don't eat becuase I am a bot!"


def unknown():
    response = [ 'Could you please re-phrase that?',
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]

    return response