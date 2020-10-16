from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsAdmin
from loader import dp
from utils.db_api import db_commands as command


@dp.message_handler(IsAdmin(), Command('load'))
async def load(message: types.Message):
    await command.load_users()
    await message.answer("Загрузка завершена успешно")


@dp.message_handler(IsAdmin(), Command('statistics'))
async def statistics(message: types.Message):
    users = await command.get_all_users()
    users = sorted(users, key=lambda x: (x.total_photos + x.total_voices))
    users = reversed(users)
    text = ['Статистика пользователей\n']
    for user in users:
        text.append(f"@{user.username}({user.user_id}) - {user.total_photos} фото, {user.total_voices} голосовых")

    await message.answer("\n".join(text))


@dp.message_handler(IsAdmin(), Command('photo'))
async def photos(message: types.Message):
    photos = await command.get_all_photos()

    for photo in photos:
        caption = str(f"@{photo.username}, {photo.user_id}")
        await message.answer_photo(photo=photo.file_id, caption=caption)


@dp.message_handler(IsAdmin(), Command('voice'))
async def voices(message: types.Message):
    voices = await command.get_all_voices()

    for voice in voices:
        caption = str(f"@{voice.username}, {voice.user_id}")
        await message.answer_voice(voice=voice.file_id, caption=caption)
