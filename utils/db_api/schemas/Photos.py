from sqlalchemy import Column, BigInteger, String, sql, Integer

from utils.db_api.db_gino import TimedBaseModel


class Photo(TimedBaseModel):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    file_id = Column(String(255))
    username = Column(String(100))
    user_id = Column(BigInteger)

    query: sql.Select
