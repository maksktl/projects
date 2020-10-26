import logging
from datetime import datetime, timedelta, timezone

from database.db_gino import db
from database.schemas.user import User
from functions import replace_number


async def select_all_users():
    return await User.query.gino.all()


async def select_user(user_id: int):
    return await User.query.where(User.user_id == user_id).gino.first()


async def count_users():
    return await db.func.count(User.user_id).gino.scalar()


async def update_user_email(user_id: int, email: str):
    user = await User.get(user_id)
    await user.update(email=email).apply()


async def update_user_phone_number(user_id: int, phone_number: str):
    phone_number = int(replace_number(phone_number))
    user = await User.get(user_id)
    await user.update(phone_number=phone_number).apply()


async def set_subscription(user_id: int, months: int):
    # установка или продление подписки
    user = await User.get(user_id)
    print(f"SET_SUB {user}")
    date: datetime = user.end_subscribe_date

    if date is None:
        date = datetime.now(timezone.utc)

    date += timedelta(days=(months * 31))

    await user.update(end_subscribe_date=date, is_subscribed=True).apply()


async def update_sub_info(user_id: int):
    user = await User.get(user_id)

    if user is None:
        return
    if not user.is_subscribed:
        return
    now = datetime.now(timezone.utc)

    if now > user.end_subscribe_date:
        await user.update(is_subscribed=False, end_subscribe_date=None).apply()


async def is_subscribed(user: User):
    if user is None:
        return False
    if not user.is_subscribed:
        return False
    now = datetime.now(timezone.utc)

    if now > user.end_subscribe_date:
        await user.update(is_subscribed=False, end_subscribe_date=None).apply()
        return False

    return True
