import uuid

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from database.filter_commands import select_all_artypes, select_all_loadtypes
from keyboards.inline.ar_load_types import artype_keyboard, loadtypes_keyboard
from keyboards.inline.callback_datas import show_page_ar, show_page_load
from keyboards.inline.filters_menu import filter_menu, cancel_button
from load_all import dp
from states import FilterSettings


@dp.callback_query_handler(text="from_city", state=None)
async def from_city(call: CallbackQuery):
    await call.answer(cache_time=5)

    await FilterSettings.from_city.set()
    await call.message.answer("Напишите город:", reply_markup=cancel_button)


@dp.callback_query_handler(text="to_city", state=None)
async def to_city(call: CallbackQuery):
    await call.answer(cache_time=5)

    await FilterSettings.to_city.set()
    await call.message.answer("Напишите город:", reply_markup=cancel_button)


@dp.callback_query_handler(text="radius_from", state=None)
async def to_city(call: CallbackQuery):
    await call.answer(cache_time=5)

    await FilterSettings.radius_from.set()
    await call.message.answer("Напишите радиус поиска:", reply_markup=cancel_button)


@dp.callback_query_handler(text="radius_to", state=None)
async def to_city(call: CallbackQuery):
    await call.answer(cache_time=5)

    await FilterSettings.radius_to.set()
    await call.message.answer("Напишите радиус поиска:", reply_markup=cancel_button)

@dp.callback_query_handler(text="from_date", state=None)
async def from_date(call: CallbackQuery):
    await call.answer(cache_time=5)

    await FilterSettings.from_date.set()
    await call.message.answer("Напишите дату в формате dd.mm.YYY", reply_markup=cancel_button)


@dp.callback_query_handler(text="to_date", state=None)
async def to_date(call: CallbackQuery):
    await call.answer(cache_time=5)

    await FilterSettings.to_date.set()
    await call.message.answer("Напишите дату в формате dd.mm.YYYY", reply_markup=cancel_button)


@dp.callback_query_handler(show_page_ar.filter())
async def ar_type(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=5)

    ar_list = await select_all_artypes()

    limit = 10
    total_pages = (len(ar_list) // limit) + 1
    current_page = int(callback_data.get('page'))
    prev_page = current_page - 1 if current_page > 1 else 1
    next_page = current_page + 1 if current_page < total_pages else total_pages

    if current_page == total_pages:
        keyboard = artype_keyboard(ar_list[limit * (current_page - 1):len(ar_list)], prev_page, next_page)
    elif current_page == 1:
        keyboard = artype_keyboard(ar_list[0: limit], prev_page, next_page)
    else:
        keyboard = artype_keyboard(ar_list[limit * (current_page - 1): limit * current_page], prev_page, next_page)

    await call.message.answer("Выберите тип кузова", reply_markup=keyboard)


@dp.callback_query_handler(show_page_load.filter())
async def load_type(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=5)

    load_list = await select_all_loadtypes()

    limit = 10
    total_pages = (len(load_list) // limit) + 1
    current_page = int(callback_data.get('page'))
    prev_page = current_page - 1 if current_page > 1 else 1
    next_page = current_page + 1 if current_page < total_pages else total_pages

    if current_page == total_pages:
        keyboard = loadtypes_keyboard(load_list[limit * (current_page - 1):len(load_list)], prev_page, next_page)
    elif current_page == 1:
        keyboard = loadtypes_keyboard(load_list[0: limit], prev_page, next_page)
    else:
        keyboard = loadtypes_keyboard(load_list[limit * (current_page - 1): limit * current_page], prev_page, next_page)

    await call.message.answer("Выберите тип выгрузки", reply_markup=keyboard)


@dp.callback_query_handler(text="weight", state=None)
async def weight(call: CallbackQuery):
    await call.answer(cache_time=5)

    await FilterSettings.weight.set()
    await call.message.answer("Введите вес в тоннах:", reply_markup=cancel_button)


@dp.callback_query_handler(text="volume", state=None)
async def volume(call: CallbackQuery):
    await call.answer(cache_time=5)

    await FilterSettings.volume.set()
    await call.message.answer("Введите объем груза в кубических метрах:", reply_markup=cancel_button)
