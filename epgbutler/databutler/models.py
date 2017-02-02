from django.db import models


# Create your models here.
class Program(object):
    def __init__(self, id, title, events):
        self.id = id
        self.events = events or []
        self.title = title


def get_programs():
    return [Program(1, 'Tennis AU Final', [[120, 'R. Federer', ' loses the game with a forehand Unforced Error.'],
                                           [368, 'R. Nadal', ' loses the game with a backhand Forced Error.'],
                                           [606, 'R. Federer', ' loses the game with a backhand Forced Error.'],
                                           [827, 'R. Nadal', ' loses the game with a backhand Forced Error.'],
                                           [973, 'R. Federer', ' loses the game with a forehand Forced Error.'],
                                           [1164, 'R. Nadal', ' loses the game with a forehand Forced Error.'],
                                           [1605, 'R. Federer', ' wins the game with an ace.'],
                                           [1841, 'R. Nadal', ' wins the game with a forehand Winner.'],
                                           [2051, 'R. Federer', ' wins the set with an ace.'],
                                           [2421, 'R. Nadal', ' wins the game with an ace.'],
                                           [3259, 'R. Federer', ' loses the game with a backhand Forced Error.'],
                                           [4101, 'R. Federer', ' wins the game with a forehand Winner.'],
                                           [4255, 'R. Federer', ' loses the game with a backhand Forced Error.'],
                                           [4459, 'R. Federer', ' wins the game with a forehand Winner.'],
                                           [4599, 'R. Federer', ' loses the set with a forehand Forced Error.'],
                                           [5136, 'R. Nadal', ' loses the game with a forehand Forced Error.'],
                                           [5576, 'R. Federer', ' wins the game with an ace.'],
                                           [6200, 'R. Nadal', ' wins the game with a forehand Winner.'],
                                           [6294, 'R. Federer', ' wins the game with a forehand Winner.'],
                                           [7039, 'R. Federer', ' wins the set with a backhand Volley Winner.'],
                                           [7452, 'R. Federer', ' loses the game with a forehand Unforced Error.'],
                                           [7632, 'R. Federer', ' wins the game with a backhand Winner.'],
                                           [7844, 'R. Federer', ' loses the game with a forehand Forced Error.'],
                                           [8550, 'R. Nadal', ' wins the game with a forehand Winner.'],
                                           [8908, 'R. Federer', ' wins the game with an ace.'],
                                           [9043, 'R. Nadal', ' wins the game with an ace.'],
                                           [9311, 'R. Nadal', ' loses the game with a forehand Forced Error.'],
                                           [9436, 'R. Federer', ' loses the set with a backhand Unforced Error.'],
                                           [10580, 'R. Federer', ' loses the game with a forehand Unforced Error.'],
                                           [10717, 'R. Federer', ' wins the game with a backhand Winner.'],
                                           [11230, 'R. Federer', ' loses the game with a backhand Forced Error.'],
                                           [11388, 'R. Nadal', ' loses the game with a backhand Unforced Error.'],
                                           [12045, 'R. Federer', ' wins the game with an ace.'],
                                           [13047, 'R. Federer', ' wins the match with a forehand Winner.']])]
