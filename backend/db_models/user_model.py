from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from ..db_con import BaseMySQL

class UserDetail(BaseMySQL):
    __tablename__ = 'user_detail'

    pk_user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(500), nullable=False)
    email_id = Column(String(100), unique=True, nullable=False)
    is_active = Column(Boolean, nullable=False)
    password = Column(String(200), nullable=False)
    role = Column(String(100), nullable=False)
    record_date = Column(DateTime, server_default=func.now(), nullable=False)
    last_modified_date = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
