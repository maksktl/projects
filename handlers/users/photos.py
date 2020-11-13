from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.user_state import UserStep


@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=UserStep.before)
async def photo_before(message: types.Message, state: FSMContext):
    data = (await state.get_data()).get('photo_before')
    if data is None:
        data = []
    data.append(message.photo[-1].file_id)
    await state.update_data(photo_before=data)
    await message.answer(f"вы прислали {len(data)}фото")