from aiogram import types
from aiogram.dispatcher import FSMContext

from bot_loader import dp
from handlers.user_info import pay


@dp.callback_query_handler(text="increase")
async def increase_count(call: types.CallbackQuery, state: FSMContext):
    await call.answer()

    current_count = int((await state.get_data()).get('count'))
    current_count += 1

    await state.update_data(count=current_count)

    await pay(call, state)


@dp.callback_query_handler(text="decrease")
async def increase_count(call: types.CallbackQuery, state: FSMContext):
    await call.answer()

    current_count = int((await state.get_data()).get('count'))
    current_count -= 1
    if current_count < 1:
        current_count = 1
    await state.update_data(count=current_count)

    await pay(call, state)


@dp.callback_query_handler(text="stale")
async def stale(call: types):
    await call.answer("Пополните свой баланс!")
