from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📃 Название задачи", callback_data="create:task_name")],
        [InlineKeyboardButton(text="📍 Местоположение", callback_data="create:location")],
        [
            InlineKeyboardButton(text="📆 День", callback_data="create:date"),
            InlineKeyboardButton(text="⌚️ Время", callback_data="create:time"),
        ],
    ]
)


