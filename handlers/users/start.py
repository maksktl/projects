from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.keyboards import tech_type
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Выберите тип техники:", reply_markup=tech_type)
