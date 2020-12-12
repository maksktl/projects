from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.relations import county_file
from keyboards.default.keyboards import country_keyboard
from loader import dp
from states.states import State
from utils.e_mail.email_commands import send_email


@dp.message_handler(text="📨 Отправить письмо")
async def select_country(message: types.Message, state: FSMContext):
    await State.country.set()
    await message.answer("📍 Выберите страну:", reply_markup=country_keyboard)


@dp.message_handler(state=State.country)
async def select_product(message: types.Message, state: FSMContext):
    country = message.text
    if country not in county_file:
        await message.answer("Вы отправили страну, которой нет в списке")
    await state.update_data(file=county_file[country])
    await State.product_name.set()
    await message.answer("📃 Введите название товара:", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=State.product_name)
async def enter_link(message: types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    await State.link.set()
    await message.answer("🔗 Введите ссылку на товар:")


@dp.message_handler(state=State.link)
async def enter_email(message: types.Message, state: FSMContext):
    await state.update_data(link=message.text)
    await State.email.set()
    await message.answer("📧 Введите почту получателя:")


@dp.message_handler(state=State.email)
async def send_mail(message: types.Message, state: FSMContext):
    text = ""
    data = await state.get_data()
    file = str(data.get("file"))
    product = data.get("product")
    link = data.get("link")
    with open(file) as fl:
        for line in fl:
            text += line.encode('ascii', 'ignore').decode('ascii')
    text = text.format(product, link)
    send_email(message.text, "OLX товар", text)

    await state.reset_state(with_data=True)
