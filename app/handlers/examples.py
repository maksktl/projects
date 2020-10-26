from aiogram import types
from aiogram.dispatcher import FSMContext

from bot_loader import dp
from keyboards.menu import menu_keyboard


@dp.callback_query_handler(text="examples")
async def menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    text = "ВНИМАНИЕ 🔞 Примеры обработаны цензурой! На выходе получаются фото без цензуры!"
    await call.message.answer(text)
    await call.message.answer_photo(open("examples/1.jpg", 'rb'))
    await call.message.answer_photo(open("examples/2.jpg", 'rb'))
    await call.message.answer_photo(open("examples/3.jpg", 'rb'))
    await call.message.answer_photo(open("examples/4.jpg", 'rb'))
    await call.message.answer_photo(open("examples/5.jpg", 'rb'))
    await call.message.answer_photo(open("examples/6.jpg", 'rb'))
    await call.message.answer("Меню:", reply_markup=menu_keyboard)
