from aiogram.dispatcher.filters.state import StatesGroup, State


class TaskState(StatesGroup):
    name = State()
    description = State()
    people = State()
    place = State()
    date = State()
    time = State()
