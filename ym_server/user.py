from sqlalchemy import Column, BigInteger, String, sql, Boolean, DateTime

from db_gino import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    query: sql.Select

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(32))
    full_name = Column(String(512))
    email = Column(String(256))
    phone_number = Column(String(32))
    is_subscribed = Column(Boolean)
    end_subscribe_date = Column(DateTime(True))

    @staticmethod
    async def get_or_create(user_info):
        # берем информацию о пользователе

        user = await User.get(int(user_info.id))
        if user:
            return user
        else:
            new_user = await User.create(
                user_id=int(user_info.id),
                username=user_info.username,
                full_name=user_info.full_name,
                email=None,
                phone_number=None,
                is_subscribed=False,
                end_subscribe_date=None
            )
            return new_user
