import logging
from datetime import datetime, timedelta, timezone

from database.db_gino import db
from database.schemas.user import User


async def select_all_users():
    """Выбрать всех пользователей из БД"""
    return await User.query.gino.all()


async def select_user(user_id: int):
    """Выбрать пользователя по user_id"""
    return await User.query.where(User.user_id == user_id).gino.first()


async def change_balance(user_id: int, amount: int):
    """Добавить на счет пользователя amount рублей"""
    user = await User.get(user_id)
    new_balance = user.balance + amount
    await user.update(balance=new_balance).apply()
