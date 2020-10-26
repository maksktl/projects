from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import SUBSCRIBE_PRICE, YM_WALLET_ID
from functions.get_pay_url import get_pay_url
from keyboards.callback_datas import show_page_data, show_photo

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📷 Примеры", callback_data="examples")],
        [
            InlineKeyboardButton(text="👅 Раздеть девушку", callback_data="to_nude"),
            InlineKeyboardButton(text="🎁 Реферальная система", callback_data="referral_link")
        ],
        [
            InlineKeyboardButton(text="💰 Баланс", callback_data="balance"),
            InlineKeyboardButton(text="💶 Пополнить", callback_data="pay")
        ],
        [
            InlineKeyboardButton(text="🏠 Личный кабинет", callback_data=show_page_data.new(page=1))
        ]
    ]
)

back_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="menu")]
    ]
)


async def buy_button(user_id, start_link, price, current_count):
    return InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="⬇️", callback_data="decrease"),
            InlineKeyboardButton(text=current_count, callback_data="stale"),
            InlineKeyboardButton(text="⬆️", callback_data="increase")

        ],
            [
                InlineKeyboardButton(text="✅ Оплатить",
                                     url=str(await get_pay_url("Пополнение баланса", price, user_id, YM_WALLET_ID,
                                                               redirect_url=start_link)))
            ],
            [
                InlineKeyboardButton(text="Назад", callback_data="menu")
            ]
        ]
    )


async def show_personal_page(items: list, prev_page, next_page, curr_page):
    ret_key = InlineKeyboardMarkup()
    cnt = 0
    if items and len(items) > 0:
        for item in items:
            cnt += 1
            ret_key.add(
                InlineKeyboardButton(
                    text=f'{"✅" if item.process_completed else "🚫"} Фото № {(curr_page - 1) * 10 + cnt}',
                    callback_data=show_photo.new(state=item.process_completed, file_id=item.file_id)
                )

            )

    navigation = [
        InlineKeyboardButton(text="⬅", callback_data=show_page_data.new(page=prev_page)),
        InlineKeyboardButton(text="Назад", callback_data="menu"),
        InlineKeyboardButton(text="➡️", callback_data=show_page_data.new(page=next_page)),
    ]

    ret_key.add(*navigation)
    return ret_key
