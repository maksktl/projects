import time
import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from API.api_client import CargolinkAPI
from database.filter_commands import get_artype_by_id, get_load_by_id
from keyboards.inline.callback_datas import artype_data, loadtype_data
from keyboards.inline.filters_menu import filter_menu, cancel_button
from load_all import dp, cargo_api
from states import FilterSettings


@dp.message_handler(state=FilterSettings.from_city)
async def set_from_city(message: types.Message, state: FSMContext):
    city, city_id = get_city(message.text)

    if city:
        await state.update_data(from_city=city, place_id_from=city_id)
        await state.reset_state(with_data=False)

        await message.answer("Фильтра груза:", reply_markup=filter_menu(**(await state.get_data())))
    else:
        await message.answer("Город не найден")
        await message.answer("Напишите город:", reply_markup=cancel_button)


@dp.message_handler(state=FilterSettings.to_city)
async def set_to_city(message: types.Message, state: FSMContext):
    city, city_id = get_city(message.text)

    if city:
        await state.update_data(to_city=city, place_id_to=city_id)
        await state.reset_state(with_data=False)

        await message.answer("Фильтра груза:", reply_markup=filter_menu(**(await state.get_data())))

    else:
        await message.answer("Город не найден")
        await message.answer("Напишите город:", reply_markup=cancel_button)


@dp.message_handler(state=FilterSettings.from_date)
async def set_from_date(message: types.Message, state: FSMContext):
    input_date = message.text

    try:
        time.strptime(input_date, "%d.%m.%Y")
    except ValueError:
        await message.answer("Невераня дата")
        await message.answer("Напишите дату в формате dd.mm.yyyy", reply_markup=cancel_button)
        return
    date = int(time.mktime(datetime.datetime.strptime(input_date, "%d.%m.%Y").timetuple()))
    await state.update_data(date_from=date, from_date=input_date)
    await state.reset_state(with_data=False)

    await message.answer("Фильтра груза:", reply_markup=filter_menu(**(await state.get_data())))


@dp.message_handler(state=FilterSettings.radius_from)
async def set_to_date(message: types.Message, state: FSMContext):
    try:
        int(message.text)
    except ValueError:
        await message.answer("Неверный радиус")
        await message.answer("Введите числовое значение:", reply_markup=cancel_button)
        return

    await state.reset_state(with_data=False)
    await state.update_data(radius_from=message.text)

    await message.answer("Фильтра груза:", reply_markup=filter_menu(**(await state.get_data())))


@dp.message_handler(state=FilterSettings.radius_to)
async def set_to_date(message: types.Message, state: FSMContext):
    try:
        int(message.text)
    except ValueError:
        await message.answer("Неверный радиус")
        await message.answer("Введите числовое значение:", reply_markup=cancel_button)
        return

    await state.reset_state(with_data=False)
    await state.update_data(radius_to=message.text)

    await message.answer("Фильтра груза:", reply_markup=filter_menu(**(await state.get_data())))


@dp.message_handler(state=FilterSettings.to_date)
async def set_to_date(message: types.Message, state: FSMContext):
    input_date = message.text

    try:
        time.strptime(input_date, "%d.%m.%Y")
    except ValueError:
        await message.answer("Невераня дата")
        await message.answer("Напишите дату в формате dd.mm.yyyy", reply_markup=cancel_button)
        return

    date = int(time.mktime(datetime.datetime.strptime(input_date, "%d.%m.%Y").timetuple()))
    await state.update_data(date_to=date, to_date=input_date)
    await state.reset_state(with_data=False)

    await message.answer("Фильтра груза:", reply_markup=filter_menu(**(await state.get_data())))


@dp.callback_query_handler(artype_data.filter())
async def set_ar_type(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(artype=(await get_artype_by_id(int(callback_data.get('id')))).type,
                            car_type=callback_data.get('id'))

    await call.message.answer("Фильтра груза:", reply_markup=filter_menu(**(await state.get_data())))


@dp.callback_query_handler(loadtype_data.filter())
async def set_load_type(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(loadtype=(await get_load_by_id(int(callback_data.get('id')))).type,
                            loadtypes=callback_data.get('id'))

    await call.message.answer("Фильтра груза:", reply_markup=filter_menu(**(await state.get_data())))


@dp.message_handler(state=FilterSettings.weight)
async def set_weight(message: types.Message, state: FSMContext):
    try:
        float(message.text)
    except ValueError:
        await message.answer("Неверный вес")
        await message.answer("Введите вес в тоннах:", reply_markup=cancel_button)
        return

    await state.reset_state(with_data=False)
    await state.update_data(weight_max=message.text)

    await message.answer("Фильтра груза:", reply_markup=filter_menu(**(await state.get_data())))


@dp.message_handler(state=FilterSettings.volume)
async def set_volume(message: types.Message, state: FSMContext):
    try:
        float(message.text)
    except ValueError:
        await message.answer("Неверный объем")
        await message.answer("Введите объем груза в кубических метрах:", reply_markup=cancel_button)
        return

    await state.reset_state(with_data=False)
    await state.update_data(v_qube_max=message.text)
    await message.answer("Фильтра груза:", reply_markup=filter_menu(**(await state.get_data())))


def get_city(text: str):
    city = text.capitalize()

    try:
        respone = cargo_api.search_city(city)
        return respone[0].get('name'), respone[0].get('city_id')
    except IndexError or TypeError:
        return None, None
    # try:
    #     logging.info(api.search_city(city))
    # except Exception:
    #     return city

