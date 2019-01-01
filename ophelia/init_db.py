from models import Base
from dao.connection import get_connection

def init_db(self):
    Base.metadata.create_all(get_connection())

