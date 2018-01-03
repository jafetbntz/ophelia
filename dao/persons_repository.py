from dao.base_service import BaseService
from models import Person

class PersonsRespository(BaseService):
    """
    """

    def get(self, index):
        """
        """
        persons = self._session.query(Person)

        return persons

    def find_by_id(id):
        """
        """

        return

    def add(index):
        """
        """
        person = Person(title="Doctor Strange",
                              director="Scott Derrickson", year="2016")
        _session.add(person)
        _session.commit()
        return

    def update(person):
        """
        """
        db_person = find_by_id(person.id)
        db_person.name =  person.name
        

        _session.commit()
        return

    def delete(person):

        person.is_actie = False
        _session.commit()

        return
