from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.schemas.user import User
from database.user_commands import is_subscribed
from keyboards.inline.callback_datas import subscribe_with_cargo, cargo_data, show_page_data


async def cargos_keyboard(items: list, prev_page: int, next_page: int, user: User):
    keyboard = InlineKeyboardMarkup()
    if items:
        for item in items:
            keyboard.add(
                InlineKeyboardButton(
                    text=str(
                        f'🗓 {item.from_date}, 📍 {item.from_city} - {item.to_city}, {item.volume} м^3,'
                        f' {item.type}, 💵 {item.price if await is_subscribed(user) else "Скрыто"}, '),
                    callback_data=cargo_data.new(cargo_id=item.id)
                )
            )
    navigation = [
        InlineKeyboardButton(text="⬅", callback_data=show_page_data.new(page=prev_page)),
        InlineKeyboardButton(text="Назад к фильтрам", callback_data="cargos_back"),
        InlineKeyboardButton(text="➡️", callback_data=show_page_data.new(page=next_page)),
    ]
    keyboard.add(*navigation)
    return keyboard


def cargo_keyboard(cargo_id: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💳 Оформить подписку",
                                     callback_data=subscribe_with_cargo.new(cargo_id=cargo_id))
            ],
            [
                InlineKeyboardButton(text="Назад к списку", callback_data=show_page_data.new(page=1))
            ]
        ]
    )
