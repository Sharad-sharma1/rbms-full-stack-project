from sqlalchemy import Column, Integer, String, DECIMAL, Enum, DateTime, func, Boolean
from ..db_con import BaseMySQL

class Mortgage(BaseMySQL):
    __tablename__ = 'mortgages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    credit_score = Column(Integer, nullable=False)
    loan_amount = Column(DECIMAL(50, 2), nullable=False)
    property_value = Column(DECIMAL(50, 2), nullable=False)
    annual_income = Column(DECIMAL(50, 2), nullable=False)
    debt_amount = Column(DECIMAL(50, 2), nullable=False)
    loan_type = Column(Enum('fixed', 'adjustable'), nullable=False)
    property_type = Column(Enum('single_family', 'condo'), nullable=False)
    is_active = Column(Boolean, nullable=False, server_default='1')
    created_at = Column(DateTime, server_default=func.current_timestamp(), nullable=False)
    modified_at = Column(
        DateTime,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=False
    )
