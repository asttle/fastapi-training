from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    choices = Column(JSON, index=True)

class Choice(Base):
    __tablename__ = "choices"
    id = Column(Integer, primary_key=True, index=True)