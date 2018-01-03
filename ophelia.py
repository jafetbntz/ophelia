import random

GREETINGS = ["Klk", "Buen día", "Hi!"]
class Ophelia(object):
    """
    Centro de actitud
    
    """
    def __init__(self, config):
        self.config = config
        pass
    
    def answer(self, text):
        return "wip"
    

    def greetings(self):
        index = random.randint(0, len(GREETINGS) -1)
        return GREETINGS[index]
