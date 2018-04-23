from dao.base_service import BaseService
from models import Message
from dao.connection import get_session
from datetime import datetime

class MessageRespository(BaseService):


    def get(self, index):

        messages = self._session.query(Message)

        return messages

    def find_by_reference(self, reference_id, channel):

        messages = self._session.query(Message).filter_by(
            reference_id=reference_id, channel=channel)
        return messages

    def add(self, message):
        try:
            message.time = datetime.now()
            self._session.add(message)
            self._session.commit()
        except Exception as e:
            print(e)
            return False
        return True



