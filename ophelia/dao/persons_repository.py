from .base_service import BaseService
from ophelia.models import Person
from .connection import get_session

class PersonsRespository(BaseService):
    """
    """

    def get(self, index):
        """
        """
        persons = self._session.query(Person)

        return persons

    def find_by_id(self, telegram_id):
        """
        """
        person = self._session.query(Person).filter_by(
            telegram_id=telegram_id).first()
        return person

    def add(self, person):
        """
        Inserta a BD la persona.
        """
        try:
            self._session.add(person)
            self._session.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def update(self, person):
        """
        """
        db_person = self.find_by_id(person.id)
        db_person.name =  person.name
        

        self._session.commit()
        return

    def delete(self, person):

        person.is_actie = False
        self._session.commit()

        return
