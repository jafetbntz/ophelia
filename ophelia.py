import random
from dao.persons_repository import PersonsRespository
from dao.message_repository import MessageRespository
from models import Person, Message

GREETINGS = ["Klk", "Buen día", "Hi!"]
class Ophelia(object):
    """
    Centro de actitud
    
    """
    def __init__(self, config):
        self.config = config
        pass
    

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

    
    def save_message(self, text, channel, reference):
        try:
            repository = MessageRespository()
            result = repository.add(Message(text=text, channel=channel,reference_id=reference))
            print(result)
        except Exception as e:
            print(e)
    
    def answer(self, message, channel, reference):

            #         if(text in ("/start", "hello", "hola") ):
            #     result_text = self._attitude.greetings()
            # else:
            #     result_text = self._attitude.answer(text)

            # #print(text)
            # #result_text = str(eval(text))
        try:
            self.save_message(message, channel, reference)
            context = self.get_context(reference, channel)
            message_result = ""
            for msg in context:
                message_result += "-" + msg.text + "\n"
            return message_result
        except Exception as e:
            print(e)
            return ("Sorry")
    
    def get_context(self, reference, channel):
        try:
            repository = MessageRespository()
            messages = repository.find_by_reference(reference, channel)
            return messages
        except Exception as e:
            print(e)
            return []



