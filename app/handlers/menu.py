from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from bot_loader import dp
from keyboards.menu import menu_keyboard


@dp.message_handler(CommandStart())
@dp.message_handler(CommandHelp())
async def menu(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)

    is_pay = True if message.text.split(' ')[-1] == 'Done' else False

    if is_pay:
        await message.answer("Ожидайте подтверждение оплаты")
        return

    await message.answer(f"Привет {message.from_user.first_name}!\nДержи меню:", reply_markup=menu_keyboard)


@dp.callback_query_handler(text="menu")
async def menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.reset_state(with_data=True)

    await call.message.edit_text(f"Привет {call.from_user.first_name}!\nДержи меню:")
    await call.message.edit_reply_markup(reply_markup=menu_keyboard)
