from aiogram.dispatcher.filters.state import StatesGroup, State


class TaskState(StatesGroup):
    name = State()
    place = State()
    date_from = State()
    date_to = State()
    time_from = State()
    time_to = State()
