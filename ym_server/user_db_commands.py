from user import User


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

    # Далее прибавляем половину реферру
    parent_ref = await User.get(user.parent_ref)
    if parent_ref:
        pr_balance = parent_ref.balance + int(amount / 2)
        await parent_ref.update(balance=pr_balance).apply()
