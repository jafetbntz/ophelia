
from models import Base
from sqlalchemy import create_engine
import configparser
from sqlalchemy.orm import sessionmaker


CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")

DB_USER = CONFIG.get("DATABASE", "user")
DB_PASS = CONFIG.get("DATABASE", "pass")
DB_HOST = CONFIG.get("DATABASE", "host")
DB_PORT = CONFIG.get("DATABASE", "port")
DB_NAME = CONFIG.get("DATABASE", "name")

CONN = 'postgresql://{}:{}@{}:{}/{}'.format(
    DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)

def get_connection():
    return create_engine(CONN)

def get_session():
    db = get_connection()
    session = sessionmaker(db)
    return session()
