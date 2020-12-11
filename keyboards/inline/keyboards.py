from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ℹ️ Помощь", callback_data="help")],
        [InlineKeyboardButton(text="📨 Отправить письмо", callback_data="send")],
    ]
)

country_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🇵🇱 Польша", callback_data="country:Polish")],
        [InlineKeyboardButton(text="🇺🇦 Украина", callback_data="country:Ukraine")],
        [InlineKeyboardButton(text="🇰🇿 Казахстан", callback_data="country:Kazakhstan")],
        [InlineKeyboardButton(text="🇺🇿 Узбекистан", callback_data="country:Uzbekistan")],
        [InlineKeyboardButton(text="🇧🇬 Болгария", callback_data="country:Bulgaria")],
        [InlineKeyboardButton(text="🇷🇴 Румыния", callback_data="country:Rumania")],
        [InlineKeyboardButton(text="🇵🇹 Португалия", callback_data="country:Portugal")],
    ]
)
