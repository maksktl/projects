from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def main(task_name="Название задачи", task_description="Описание", people="Люди", location="Местоположение", date="День",
               time="Время", **kwargs):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"📃 {task_name}", callback_data="create:task_name")],
            [InlineKeyboardButton(text=f"📖 {task_description}", callback_data="create:task_description")],
            [InlineKeyboardButton(text=f"👥 {people}", callback_data="create:people")],
            [InlineKeyboardButton(text=f"📍 {location}", callback_data="create:location")],
            [
                InlineKeyboardButton(text=f"📆 {date}", callback_data="create:date"),
                InlineKeyboardButton(text=f"⌚️ {time}", callback_data="create:time"),
            ],
            [InlineKeyboardButton(text="✅ Создать", callback_data="create:create")],
            [InlineKeyboardButton(text="🚫 Отменить", callback_data="create:cancel")],

        ]
    )

back_to_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад", callback_data="create:main")]
    ]
)
