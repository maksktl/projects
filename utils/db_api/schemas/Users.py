from sqlalchemy import Column, BigInteger, String, sql, Integer

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(Integer)
    user_id = Column(String(255), primary_key=True)
    username = Column(String(100))
    total_photos = Column(BigInteger)
    total_voices = Column(BigInteger)

    query: sql.Select
