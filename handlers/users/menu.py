from aiogram import types
from aiogram.dispatcher import FSMContext

from data.relations import county_file
from keyboards.inline.keyboards import country_keyboard
from loader import dp
from states.states import State


@dp.callback_query_handler(text="send")
async def select_country(call: types.CallbackQuery, state: FSMContext):
    await State.country.set()
    await call.message.answer("Выберите страну:", reply_markup=country_keyboard)


@dp.callback_query_handler(text_contains="country", state=State.country)
async def select_product(call: types.CallbackQuery, state: FSMContext):
    country = call.data.split(":")[1]

    await state.update_data(file=county_file[country])
    await State.product_name.set()
    await call.message.answer("Введите название товара:")


@dp.message_handler(state=State.product_name)
async def enter_link(message: types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    await State.link.set()
    await message.answer("Введите ссылку на товар:")