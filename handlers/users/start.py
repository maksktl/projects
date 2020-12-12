from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.keyboards import start_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=start_keyboard)


@dp.message_handler(text="ℹ️ Помощь")
async def bot_help(message: types.Message):
    await message.answer("Текст помощи", reply_markup=start_keyboard)
