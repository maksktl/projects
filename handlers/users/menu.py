from aiogram import types
from aiogram.dispatcher import FSMContext

from data.relations import county_file
from keyboards.inline.keyboards import country_keyboard
from loader import dp
from states.states import State
from utils.e_mail.email_commands import send_email


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


@dp.message_handler(state=State.link)
async def enter_email(message: types.Message, state: FSMContext):
    await state.update_data(link=message.text)
    await State.email.set()
    await message.answer("Введите почту получателя:")


@dp.message_handler(state=State.email)
async def send_mail(message: types.Message, state: FSMContext):
    text = u""
    data = await state.get_data()
    file = str(data.get("file"))
    product = data.get("product")
    link = data.get("link")
    with open(file) as fl:
        for line in fl:
            text += line.encode('ascii', 'ignore').decode('ascii')
    text = text.format(product, link)
    # text = "<h1> {0} <\h1>  <h2> {1} <\h2>".format(product, link).encode('utf-8')
    send_email(message.text, "OLX товар", text)

    await state.reset_state(with_data=True)
