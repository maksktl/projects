from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from handlers.users.start import bot_start
from keyboards.inline import task_manage_keyboard
from keyboards.inline.task_manage_keyboard import back_to_main
from loader import dp
from states.tasks_states import TaskState


@dp.message_handler(Command("add_new"))
async def add_task(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer("🛠 Нажмите на нужную кнопку, чтобы задать необходимую конфигурацию:",
                         reply_markup=(await task_manage_keyboard.main(**data)))


@dp.callback_query_handler(state='*', text_contains="create:cancel")
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(with_data=True)
    await bot_start(call.message)


@dp.callback_query_handler(text_contains="create:task_name")
async def ask_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("📃 Введите название задачи", reply_markup=back_to_main)
    await TaskState.name.set()


@dp.callback_query_handler(text_contains="create:task_description")
async def ask_task_description(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("📖 Введите описание задачи", reply_markup=back_to_main)
    await TaskState.description.set()


@dp.message_handler(state=TaskState.description)
async def set_task_description(message: types.Message, state: FSMContext):
    task_description = message.text
    await state.update_data(task_description=task_description)
    await state.reset_state(with_data=False)
    await add_task(message, state)


@dp.message_handler(state=TaskState.name)
async def set_name(message: types.Message, state: FSMContext):
    task_name = message.text
    await state.update_data(task_name=task_name)
    await state.reset_state(with_data=False)
    await add_task(message, state)


@dp.callback_query_handler(text_contains="create:main", state='*')
async def main(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await state.reset_state(with_data=False)
    await call.message.answer("🛠 Панель создания задачи:", reply_markup=(await task_manage_keyboard.main(**data)))
