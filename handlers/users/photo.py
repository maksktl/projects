from random import randint

from aiogram import types

from loader import dp
from utils.db_api import db_commands as command


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def random_photo(message: types.Message):
    count = int(await command.photos_count())
    await command.add_user(message.from_user.id, message.from_user.username)
    if count < 1:
        await command.add_photo(message.photo[-1].file_id, message.from_user.username, (message.from_user.id))
        await command.add_photo_to_user(str(message.from_user.id))
        return

    photo = (await command.get_photo(randint(1, count)))

    await message.answer_photo(photo=photo.file_id)
    await command.add_photo(message.photo[-1].file_id, message.from_user.username, message.from_user.id)
    await command.add_photo_to_user(str(message.from_user.id))