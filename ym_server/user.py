from sqlalchemy import Column, BigInteger, String, sql

from db_gino import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    query: sql.Select

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(32))
    balance = Column(BigInteger)
    referrals = Column(BigInteger)
    parent_ref = Column(BigInteger)

    @staticmethod
    async def get_or_create(user_info, parent_ref=None):
        # берем информацию о пользователе
        user = await User.get(int(user_info.id))
        if user:
            return user
        else:
            new_user = await User.create(
                user_id=int(user_info.id),
                username=user_info.username,
                balance=0,
                parent_ref=None,
                referrals=0
            )
            if parent_ref:
                await User.set_ref_parent(new_user.user_id, parent_ref)
            return new_user

    @staticmethod
    async def set_ref_parent(user_id: int, referr_id: int):
        """Установить пользователю реферра"""
        user = await User.get(user_id)

        await user.update(parent_ref=referr_id).apply()
        await User.add_referral(referr_id)

    @staticmethod
    async def add_referral(user_id: int):
        """Добавить пользователю реферрала"""
        user = await User.get(user_id)

        ref_count = user.referrals
        ref_count += 1
        await user.update(referrals=ref_count).apply()
