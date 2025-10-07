from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field

from typing import Annotated, List
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from models import Question, Choice

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]

@app.post("/questions/")
async def create_question(question: QuestionBase, db: db_dependency):
    new_question = models.Question(question_text=question.question_text)
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    for choice in question.choices:
        new_choice = models.Choice(choice_text=choice.choice_text, is_correct=choice.is_correct, question_id=new_question.id)
        db.add(new_choice)
    db.commit()
    db.refresh(new_choice)
    return new_question
    
@app.get("/questions/")
async def get_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    return questions

@app.get("/choices/{question_id}")
async def get_choices(question_id: int, db: Session = Depends(get_db)):
    choices = db.query(Choice).filter(Choice.question_id == question_id).all()
    return choices
    