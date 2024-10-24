from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config
from aiogram import Bot, Dispatcher
import logging


BOT_TOKEN = config('TOKEN')

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s %(filename)s: [%(asctime)s] - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S')
logger = logging.getLogger(__name__)

bot = Bot(BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
