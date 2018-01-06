import random
from dao.persons_repository import PersonsRespository
from models import Person

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

    def save_person(self, name, last_name, is_human, telegram_id):
        try:
            repository = PersonsRespository()

            person_in_db = repository.find_by_id(telegram_id)
            print(person_in_db)
            if not person_in_db:
                repository.add(Person(name=name, 
                last_name=last_name, is_human=is_human, 
                telegram_id=telegram_id))
            else:
                print("Exists!")
            return True
        except Exception as e:
            print(e)
            return False




