from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.inline.task_manage_keyboard import back_to_main
from loader import dp
from states.tasks_states import TaskState
from keyboards.inline import task_manage_keyboard


@dp.message_handler(Command("add_new"))
async def add_task(message: types.Message):
    await message.answer("🛠 Панель создания задачи:", reply_markup=task_manage_keyboard.main)


@dp.callback_query_handler(text_contains="create")
@dp.callback_query_handler(text_contains="task_name")
async def ask_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("📃 Введите название задачи", reply_markup=back_to_main)


@dp.callback_query_handler(text_contains="create:")
@dp.callback_query_handler(text_contains="main")
async def main(call: types.CallbackQuery):
    await call.message.answer("🛠 Панель создания задачи:", reply_markup=task_manage_keyboard.main)