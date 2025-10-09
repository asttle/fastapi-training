from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String)
    is_income = Column(Boolean)
    date = Column(String)