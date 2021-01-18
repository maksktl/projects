from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from states.tasks_states import TaskState


@dp.message_handler(Command("add_new"))
async def add_task(message: types.Message):
    await message.answer("🛠 Введите название задачи:",reply_markup=...)