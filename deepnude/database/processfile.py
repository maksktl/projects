from sqlalchemy import Column, String, sql, Integer, Boolean, ForeignKey

from database.db_gino import db


class ProcessFile(db.Model):
    __tablename__ = 'process_files'
    query: sql.Select

    file_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.user_id', ondelete='CASCADE'))
    input_image = Column(String(128))
    output_image = Column(String(128), default=None)
    process_completed = Column(Boolean, default=False)
