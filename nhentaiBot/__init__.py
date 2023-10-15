from telegram.ext import Updater
import logging
BOT_TOKEN = "5811956762:AAGlP4ZHkTfE8X6fcKBvzwESobjWJ5thhoE"


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
logger.info(msg="Logging started...")

updater = Updater(BOT_TOKEN)
dp = updater.dispatcher
