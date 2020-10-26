from aiogram import types
from aiogram.dispatcher import FSMContext

from database.schemas.user import User
from handlers.users.start import start_cq, start
from load_all import dp


@dp.callback_query_handler(state='*')
async def error_call(call: types.CallbackQuery, state: FSMContext, user: User):
    await start_cq(call, state, user)


@dp.message_handler(state='*')
async def error_message(message: types.Message, user: User, state: FSMContext):
    await start(message, user, state)
