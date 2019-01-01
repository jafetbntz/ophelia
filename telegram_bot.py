from telegram.ext import Updater, CommandHandler
from ophelia.ophelia import Ophelia
import configparser
import logging 
FORMAT = '%(asctime)-15s -  %(message)s'
logging.basicConfig(format=FORMAT)

_logger = logging.getLogger('tcpserver')


#Carga de configuraciones
CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")

#Inicializar Actitud
OPHELIA = Ophelia(CONFIG)

    
def verse(bot, update):
    try:
        update.message.reply_text(
        OPHELIA.search_verse(update.message))
    except Exception as e:
        _logger.error(e)

def iss(bot, update):
    update.message.reply_text(
            OPHELIA.iss_location())

def system_status(bot, update):
    update.message.reply_text(
            OPHELIA.system_status())

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))



updater = Updater(OPHELIA.config.get("TELEGRAM", "token"))

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('verse', verse))
updater.dispatcher.add_handler(CommandHandler('system_status', system_status))
updater.dispatcher.add_handler(CommandHandler('iss', iss))


updater.start_polling()
updater.idle()
