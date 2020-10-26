import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TGBOT_TOKEN
from middlewares import AccessMiddleware

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG)


sys.path.append('botsource/')

# инициализируем бота

storage = MemoryStorage()

bot = Bot(token=TGBOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)

dp.middleware.setup(AccessMiddleware())

__all__ = ['bot', 'dp']

# db.clear_all()