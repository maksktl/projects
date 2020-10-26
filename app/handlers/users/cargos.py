import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from API.api_client import CargolinkAPI
from database.schemas.user import User
from database.user_commands import is_subscribed
from keyboards.inline.callback_datas import show_page_data
from keyboards.inline.cargo_info import cargo_data, cargo_keyboard, cargos_keyboard
from load_all import dp, cargo_api
from load_cargos import get_cargos, get_cargo_by_id



@dp.callback_query_handler(show_page_data.filter())
async def search(call: CallbackQuery, callback_data: dict, state: FSMContext, user: User):
    await call.answer(cache_time=5)
    data = await state.get_data()



    cargos = get_cargos(**data)
    if cargos is None:
        await call.message.answer('Ничего не найдено.', reply_markup=(await cargos_keyboard(cargos, 1, 1, user)))
        return
    limit = 10
    total_pages = (len(cargos) // limit) + (1 if len(cargos) % limit != 0 else 0)
    current_page = int(callback_data.get('page'))
    prev_page = current_page - 1 if current_page > 1 else 1
    next_page = current_page + 1 if current_page < total_pages else total_pages

    if current_page == total_pages:
        keyboard = await cargos_keyboard(cargos[limit * (current_page - 1):len(cargos)], prev_page, next_page, user)
    elif current_page == 1:
        keyboard = await cargos_keyboard(cargos[0: limit], prev_page, next_page, user)
    else:
        keyboard = await cargos_keyboard(cargos[limit*(current_page-1): limit*current_page], prev_page, next_page, user)

    await call.message.answer(f"Найден всего {len(cargos)} грузов.\n"
                              f"Сейчас вы на {current_page} из {total_pages} страниц\n"
                              f"Выберите груз:", reply_markup=keyboard)



@dp.callback_query_handler(cargo_data.filter())
async def show_cargo(call: CallbackQuery, callback_data: dict, user: User):
    cargo_id = callback_data.get('cargo_id')


    cargo = get_cargo_by_id(cargo_id)

    text = [
        f'📍{cargo.from_city} - {cargo.to_city}',
        f'🧾 Иноформация о грузе:',
        cargo.info,
        f'🗓 {cargo.from_date} - {cargo.to_date}',
        f'💵 Цена: {"<i>Скрыто</i>" if not (await is_subscribed(user)) else cargo.price}',
        f'☎️ Контакты: \n{"<i>Скрыто</i>" if not (await is_subscribed(user)) else cargo.contact}',
    ]

    if not (await is_subscribed(user)):
        text.extend([
            '',
            'Офоримте подписку для того чтобы видеть контакт и цену за груз'
        ])
        await call.message.answer('\n'.join(text), reply_markup=cargo_keyboard(cargo_id))
        return

    await call.message.answer('\n'.join(text), reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Назад к списку", callback_data=show_page_data.new(page=1))]]
    ))
