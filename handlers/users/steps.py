from aiogram import types

from keyboards.inline.keyboards import bulldozer_num, excavator_num, exc_remont_list, bull_remont_list
from loader import dp


@dp.callback_query_handler(text="bulldozers")
def bulldozers(call: types.CallbackQuery):
    await call.message.answer("Выберите номер техники <i>Бульдозер</i>:", reply_markup=bulldozer_num)


@dp.callback_query_handler(text="excavator")
def excavator(call: types.CallbackQuery):
    await call.message.answer("Веберите номер техники <i>Эксковаторы</i>:", reply_markup=excavator_num)


@dp.callback_query_handler(text_contains="bull:")
def bull_type(call: types.CallbackQuery):
    await call.message.answer("Выберите ремонт для Бульдозера:", reply_markup=bull_remont_list)


@dp.callback_query_handler(text_contains="exc:")
def exc_type(call: types.CallbackQuery):
    await call.message.answer("Выберите ремонт для Эксковатора:", reply_markup=exc_remont_list)

