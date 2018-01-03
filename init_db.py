from models import Base
from dao.connection import get_connection


Base.metadata.create_all(get_connection())

