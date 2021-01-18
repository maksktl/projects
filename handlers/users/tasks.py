from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from states.tasks_states import TaskState
from keyboards.inline import task_manage_keyboard

@dp.message_handler(Command("add_new"))
async def add_task(message: types.Message):
    await message.answer("🛠 Панель создания задачи:", reply_markup=task_manage_keyboard.main)

