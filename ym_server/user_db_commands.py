from datetime import datetime, timedelta, timezone

from user import User


async def set_subscription(user_id: int, months: int):
    # установка или продление подписки
    user = await User.get(user_id)

    date: datetime = user.end_subscribe_date

    if date is None:
        date = datetime.now(timezone.utc)

    date += timedelta(days=(months * 31))

    await user.update(end_subscribe_date=date, is_subscribed=True).apply()
