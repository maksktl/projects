from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.keyboards import done_button
from loader import dp
from states.user_state import UserStep


@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=UserStep.before)
async def photo_before(message: types.Message, state: FSMContext):
    data = (await state.get_data()).get('photo_before')
    if data is None:
        data = []
    data.append(message.photo[-1].file_id)
    await state.update_data(photo_before=data)


@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=UserStep.after)
async def photo_after(message: types.Message, state: FSMContext):
    data = (await state.get_data()).get('photo_after')
    if data is None:
        data = []
    data.append(message.photo[-1].file_id)
    await state.update_data(photo_after=data)


@dp.message_handler(text="✅ Загрузить", state=UserStep.before)
async def upload_before(message: types.Message, state: FSMContext):
    data = (await state.get_data()).get('photo_before')
    if data is None or data == []:
        await message.answer("⚠️Вы не загрузили фото!")
        return

    await UserStep.after.set()
    await message.answer("📸 Пришлите фото после, затем нажмите на кнопку ✅Загрузить", reply_markup=done_button)


@dp.message_handler(text="✅ Загрузить", state=UserStep.after)
async def upload_after(message: types.Message, state: FSMContext):
    data = (await state.get_data()).get('photo_after')
    if data is None or data == []:
        await message.answer("⚠️Вы не загрузили фото!")
        return

    # TODO: загрузка всего в базу данных
    await state.reset_state(with_data=True)
    await message.answer("✅ Вы успешно загрузили фото до/после!", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Нажмите /start для того чтобы перейти в главное меню.")
