import time

from aiogram import types

from bot_loader import dp
from database import user_commands
from database.schemas.user import User
from functions.deepfake import prepare_to_do
from keyboards.menu import menu_keyboard, back_button
from config import SUBSCRIBE_PRICE


@dp.callback_query_handler(text="to_nude")
async def nude(call: types.CallbackQuery, user: User):
    await call.answer()

    if user.balance >= int(SUBSCRIBE_PRICE):
        await call.message.edit_text("Пришлите мне фото девушки, которую желаете раздеть 👸 Фотография будет обработана с помощью ИИ 🤖")
        await call.message.edit_reply_markup(reply_markup=back_button)
    else:
        await call.message.answer(f"Пополните баланс, чтобы продолжить!\nЦена обработки: {SUBSCRIBE_PRICE}р")
        await call.message.answer("Меню:", reply_markup=menu_keyboard)


@dp.message_handler(content_types=['photo'])
async def node_photo(message: types.Message, user: User):

    if user.balance >= int(SUBSCRIBE_PRICE):
        await user_commands.change_balance(user.user_id, -int(SUBSCRIBE_PRICE))
        check_and_save = await prepare_to_do(message)

        await message.answer("Фото в обработке! Ожидайте. Когда будет обработано, "
                             "оно будет доступно в личном кабинете.")
        await message.answer("Меню:", reply_markup=menu_keyboard)
    else:
        await message.answer(f"Пополните баланс, чтобы продолжить!\nЦена обработки: {SUBSCRIBE_PRICE}р")
        await message.answer("Меню:", reply_markup=menu_keyboard)
