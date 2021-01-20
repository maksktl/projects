from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def main(task_name="📃 Название задачи", task_description="📖 Описание", people="👥 Люди", location="📍 Местоположение", date="📆 День",
               time="⌚️ Время"):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=task_name, callback_data="create:task_name")],
            [InlineKeyboardButton(text=task_description, callback_data="create:task_description")],
            [InlineKeyboardButton(text=people, callback_data="create:people")],
            [InlineKeyboardButton(text=location, callback_data="create:location")],
            [
                InlineKeyboardButton(text=date, callback_data="create:date"),
                InlineKeyboardButton(text=time, callback_data="create:time"),
            ],
            [InlineKeyboardButton(text="✅ Создать", callback_data="create:create")],

        ]
    )

back_to_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад", callback_data="create:main")]
    ]
)
