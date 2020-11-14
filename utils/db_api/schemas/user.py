from sqlalchemy import Column, BigInteger, String, sql, Integer

from utils.db_api.db_gino import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    query: sql.Select

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(32))
    total_before = Column(Integer)
    total_after = Column(Integer)

    @staticmethod
    async def get_or_create(user_info):

        user = await User.get(int(user_info.id))
        if user:
            return user
        else:
            new_user = await User.create(
                user_id=int(user_info.id),
                username=user_info.username,
                total_before=0,
                total_after=0
            )
            return new_user
