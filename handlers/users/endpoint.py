from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.users.start import bot_start
from loader import dp


@dp.message_handler(state='*')
async def error_message(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    await bot_start(message)