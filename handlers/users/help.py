from aiogram import types

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler()
async def bot_help(message: types.Message):
    text = [
        'Пришли мне фото или голосовое сообщение, и получи рандомное фото/голосовое в ответ!',
        '',
        'Интерес в том, что ты каждый раз не знаешь, что тебе может прийти :з'
    ]
    await message.answer('\n'.join(text))
