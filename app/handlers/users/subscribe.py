from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.deep_linking import get_start_link

from config import WEBAPP_HOST, YM_PORT, DOMAIN_NAME_OR_IP, SUBSCRIBE_PRICE1, SUBSCRIBE_PRICE6, SUBSCRIBE_PRICE3, \
    SUBSCRIBE_PRICE1, YM_WALLET_ID
from database.schemas.user import User
from database.user_commands import set_subscription
from handlers.users.cargos import show_cargo
from keyboards.inline.callback_datas import subscribe_with_cargo, show_page_data, cargo_data
from load_all import dp


@dp.callback_query_handler(subscribe_with_cargo.filter())
async def pay_with_cargo(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)

    await state.reset_state(with_data=False)
    await state.update_data(cargo_id=callback_data.get('cargo_id'))
    start_link = await get_start_link("Done")

    await call.message.answer("Оформите подписку:",
                              reply_markup=InlineKeyboardMarkup(
                                  inline_keyboard=[[
                                      InlineKeyboardButton(text=str(f"✅ На 1 месяц - 💵 {SUBSCRIBE_PRICE1} рублей"),
                                                           url=str(f"https://money.yandex.ru/quickpay/confirm.xml?receiver={YM_WALLET_ID}&quickpay-form=shop&targets=Подписка на месяц&sum={SUBSCRIBE_PRICE1}&paymentType=type_sub&formcomment=comments&short-dest=to_dest&label={call.from_user.id}.1&successURL={start_link}"))
                                  ],
                                      [
                                      InlineKeyboardButton(text=str(f"✅ На 3 месяца - 💵 {SUBSCRIBE_PRICE3} рублей"),
                                                           url=str(f"https://money.yandex.ru/quickpay/confirm.xml?receiver={YM_WALLET_ID}&quickpay-form=shop&targets=Подписка на 3 месяца&sum={SUBSCRIBE_PRICE3}&paymentType=type_sub&formcomment=comments&short-dest=to_dest&label={call.from_user.id}.3&successURL={start_link}"))
                                      ],
                                      [
                                          InlineKeyboardButton(text=str(f"✅ На 6 месяцев - 💵 {SUBSCRIBE_PRICE6} рублей"),
                                                               url=str(f"https://money.yandex.ru/quickpay/confirm.xml?receiver={YM_WALLET_ID}&quickpay-form=shop&targets=Подписка на 6 месяцев&sum={SUBSCRIBE_PRICE6}&paymentType=type_sub&formcomment=comments&short-dest=to_dest&label={call.from_user.id}.6&successURL={start_link}"))
                                      ],
                                      [
                                          InlineKeyboardButton(text="Назад к грузу",
                                                               callback_data=cargo_data.new(
                                                                   cargo_id=callback_data.get('cargo_id')))
                                      ]]
                              ))


@dp.callback_query_handler(text="subscribe_alone")
async def pay(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.reset_state(with_data=True)
    start_link = await get_start_link("Done")
    await call.message.answer(f"Оформите подписку:",
                              reply_markup=InlineKeyboardMarkup(
                                  inline_keyboard=[[
                                      InlineKeyboardButton(text=str(f"✅ На 1 месяц - 💵 {SUBSCRIBE_PRICE1} рублей"),
                                                           url=str(f"https://money.yandex.ru/quickpay/confirm.xml?receiver={YM_WALLET_ID}&quickpay-form=shop&targets=Подписка на месяц&sum={SUBSCRIBE_PRICE1}&paymentType=type_sub&formcomment=comments&short-dest=to_dest&label={call.from_user.id}.1&successURL={start_link}"))
                                  ],
                                      [
                                      InlineKeyboardButton(text=str(f"✅ На 3 месяца - 💵 {SUBSCRIBE_PRICE3} рублей"),
                                                           url=str(f"https://money.yandex.ru/quickpay/confirm.xml?receiver={YM_WALLET_ID}&quickpay-form=shop&targets=Подписка на 3 месяца&sum={SUBSCRIBE_PRICE3}&paymentType=type_sub&formcomment=comments&short-dest=to_dest&label={call.from_user.id}.3&successURL={start_link}"))
                                      ],
                                      [
                                          InlineKeyboardButton(text=str(f"✅ На 6 месяцев - 💵 {SUBSCRIBE_PRICE6} рублей"),
                                                               url=str(f"https://money.yandex.ru/quickpay/confirm.xml?receiver={YM_WALLET_ID}&quickpay-form=shop&targets=Подписка на 6 месяцев&sum={SUBSCRIBE_PRICE6}&paymentType=type_sub&formcomment=comments&short-dest=to_dest&label={call.from_user.id}.6&successURL={start_link}"))
                                      ],
                                      [
                                          InlineKeyboardButton(text="Назад",
                                                               callback_data="cancel")
                                      ]]
                              ))


@dp.callback_query_handler(text="test_pay")
async def after_pay(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await set_subscription(call.from_user.id, 1)

    cargo_id = (await state.get_data()).get('cargo_id')
    user = await User.get_or_create(call.from_user)
    if cargo_id != "None":
        await show_cargo(call, {'cargo_id': cargo_id}, user)

    else:
        await call.message.answer("Вы успешно оплатили подписку!")
