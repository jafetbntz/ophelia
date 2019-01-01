import random
from .dao.persons_repository import PersonsRespository
from .dao.message_repository import MessageRespository
from .models import Person, Message
import platform
import psutil
import requests
import json
from datetime import datetime

GREETINGS = ["Klk", "Buen día", "Hi!"]
class Ophelia(object):
    """

    
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

    def system_status(self):
        uname = platform.uname()
        memory_used = psutil.virtual_memory()[2]
        obj_Disk = psutil.disk_usage('/')
        cpu_percent = psutil.cpu_percent()



        result = """
            \nMachine: {0}
            \nNode: {1}
            \nProcesor: {2}
            \nRelease: {3}
            \nSysten: {3}
            \nVersion: {4}

            \nUsed Memory: {6}%
            \nUsed Diks: {7}%
            \nCPU: {8}%
        """.format(
            uname.machine, 
            uname.node, 
            uname.processor, 
            uname.release,
            uname.system,
            uname.version,
            memory_used,
            obj_Disk.percent,
            cpu_percent
            )


        return result

    def iss_location(self):

        api_url = "http://api.open-notify.org/iss-now.json"
        response = requests.get(api_url)
        content = response.content.decode("utf8")
        json_content = json.loads(content)
        
        if(json_content["message"] != "success"):
            return "Houston we have problems."
        now = datetime.fromtimestamp(float(json_content["timestamp"])).isoformat()
        result = "Today at {0}, ISS is over [{1}, {2}]".format(
            now, 
            json_content["iss_position"]["latitude"],
            json_content["iss_position"]["longitude"])
        
        return result
    
    def search_verse(self, verse):
        verse = verse[7:]
        print(verse)
        quote = verse.split(".")
        repository = BibleRespository()
        
        print(len(quote))
        
        if(len(quote) == 2):
            return repository.get_chapter(quote[0], quote[1])

        if(len(quote) == 3):
            return repository.get_verse(quote[0], quote[1], quote[2])
        else:
            return repository.search(verse)


