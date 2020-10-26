from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from database.schemas.user import User
from database.user_commands import is_subscribed
from keyboards.inline.menu import default_menu, subscribed_menu
from load_all import dp


@dp.callback_query_handler(text="cancel")
async def start_cq(call: types.CallbackQuery, state: FSMContext, user: User):
    current_state = await state.get_state()
    if current_state:
        await state.finish()

    rep_menu = default_menu

    if await is_subscribed(user):
        rep_menu = subscribed_menu

    await call.message.answer("Выберите пункт в меню:", reply_markup=rep_menu)


@dp.message_handler(CommandStart())
async def start(message: types.Message, user: User, state: FSMContext):
    is_pay = True if message.text.split(' ')[-1] == 'Done' else False

    if is_pay:
        await message.answer("Ожидайте подтверждени оплаты")
        return

    current_state = await state.get_state()
    if current_state:
        await state.finish()

    rep_menu = default_menu

    if await is_subscribed(user):
        rep_menu = subscribed_menu

    await message.answer("Выберите пункт в меню:", reply_markup=rep_menu)
