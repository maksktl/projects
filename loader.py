import smtplib

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

email_sender = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)

__all__ = ["bot", "dp", "storage", "email_sender"]