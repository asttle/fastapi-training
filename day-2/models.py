from sqlalchemy import Column, Integer, String, Float
from database import Base

class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    price = Column(Float, index=True)