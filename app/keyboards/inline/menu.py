from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

default_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚚 Грузы", callback_data="cargos")
        ],
        [
            InlineKeyboardButton(text="💳 Подписаться", callback_data="subscribe_alone")
        ]
    ]
)

subscribed_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚚 Грузы", callback_data="cargos")
        ]
    ]

)
