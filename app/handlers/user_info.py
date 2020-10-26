from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.deep_linking import get_start_link

from bot_loader import dp

from config import SUBSCRIBE_PRICE, WORKS_DIR
from database.photo_commands import get_photo_list
from database.schemas.processfile import ProcessFile
from database.schemas.user import User
from keyboards.callback_datas import show_page_data, show_photo as sp
from keyboards.menu import back_button, buy_button, show_personal_page


@dp.callback_query_handler(text="balance")
async def show_balance(call: types.CallbackQuery, user: User):
    await call.answer()

    await call.message.edit_text(f"Баланс: {user.balance} ₽")
    await call.message.edit_reply_markup(reply_markup=back_button)


@dp.callback_query_handler(text="pay")
async def pay(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    count = data.get('count')
    if count is None:
        count = 1
        await state.update_data(count=count)
    count = int(count)
    start_link = await get_start_link("Done")
    await call.message.edit_text(f"Раздеть {count} девушек - {count * int(SUBSCRIBE_PRICE)} рублей.\n"
                                 f"Вы ожете пополнить баланс по кнопке ниже:")
    await call.message.edit_reply_markup(
        reply_markup=(await buy_button(call.from_user.id, start_link, count * int(SUBSCRIBE_PRICE), count)))


@dp.callback_query_handler(text="referral_link")
async def show_ref(call: types.CallbackQuery, user: User):
    await call.answer()
    start_link = await get_start_link(call.from_user.id)

    await call.message.edit_text(f"Вы привлекли {user.referrals} рефералов.\nВаша ссылка:\n{start_link}")
    await call.message.edit_reply_markup(reply_markup=back_button)


@dp.callback_query_handler(show_page_data.filter())
async def show_personal_data(call: types.CallbackQuery, callback_data: dict, user: User):
    photo_list = await get_photo_list(user.user_id)

    limit = 10
    total_pages = (len(photo_list) // limit) + (1 if len(photo_list) % limit != 0 else 0)
    current_page = int(callback_data.get('page'))
    prev_page = current_page - 1 if current_page > 1 else 1
    next_page = current_page + 1 if current_page < total_pages else total_pages

    if photo_list is None or len(photo_list) == 0:
        keyboard = await show_personal_page([], 1, 1, 1)
    elif current_page == total_pages:
        keyboard = await show_personal_page(photo_list[limit * (current_page - 1):len(photo_list)], prev_page,
                                            next_page, current_page)
    elif current_page == 1:
        keyboard = await show_personal_page(photo_list[0: limit], prev_page, next_page, current_page)
    else:
        keyboard = await show_personal_page(photo_list[limit * (current_page - 1): limit * current_page], prev_page,
                                            next_page, current_page)

    await call.message.edit_text(f"Всего {len(photo_list)} фото вы отправили.\n"
                              f"Сейчас вы на {current_page} из {total_pages} страниц\n"
                              f"Выберите фото:")

    await call.message.edit_reply_markup(keyboard)


@dp.callback_query_handler(sp.filter(state="True"))
async def show_photo(call: types.CallbackQuery, callback_data: dict, user: User):
    photo = await ProcessFile.get(int(callback_data.get('file_id')))
    path_to_image = WORKS_DIR + photo.output_image
    await call.message.answer_photo(open(path_to_image, 'rb'), caption=photo.file_id)


@dp.callback_query_handler(sp.filter(state="False"))
async def show_not_ready(call: types.CallbackQuery):
    await call.answer("Фото не готово!")
