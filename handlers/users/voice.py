from random import randint

from aiogram import types

from loader import dp
from utils.db_api import db_commands as command


@dp.message_handler(content_types=types.ContentType.VOICE)
async def random_voice(message: types.Message):
    count = int(await command.voices_count())

    if count < 1:
        await command.add_voice(message.voice.file_id, message.from_user.username, message.from_user.id)
        return

    voice = (await command.get_voice(randint(1, count)))

    await message.answer_voice(voice=voice.file_id)
    await command.add_voice(message.voice.file_id, message.from_user.username, message.from_user.id)
