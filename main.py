from ophelia import Ophelia
from channels.telegram import Telegram
import configparser

#Carga de configuraciones
CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")

#Inicializar Actitud
OPHELIA = Ophelia(CONFIG)



#Inicializar canal;es de comunicación  
TELEGRAM = Telegram(OPHELIA)

#Inicio de servicio
TELEGRAM.serve()



#TODO: Hacer multihilo los canales

