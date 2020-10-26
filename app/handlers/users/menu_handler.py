from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.filters_menu import filter_menu
from load_all import dp


@dp.callback_query_handler(text="cargos_back", state='*')
async def traffic_cb(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await state.reset_state(with_data=False)
    await call.message.answer("Фильтр груза:", reply_markup=filter_menu(**(await state.get_data())))


@dp.callback_query_handler(text="cargos")
async def traffic(call: types.CallbackQuery, state: FSMContext):
    # await call.answer(cache_time=60)
    await state.reset_state(with_data=True)
    await call.message.answer("Фильтр груза:", reply_markup=filter_menu())
