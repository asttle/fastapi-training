from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


class TransactionBase(BaseModel):
    amount: float
    description: str
    is_income: bool
    date: str

class TransactionModel(TransactionBase):
    id: int
    class Config:
        orm_mode = True

@app.post("/transactions", response_model=TransactionModel)
async def create_transaction(transaction: TransactionBase, db: db_dependency):
    transaction_model = models.Transaction(**transaction.dict())
    db.add(transaction_model)
    db.commit()
    db.refresh(transaction_model)
    return transaction_model

@app.get("/transactions", response_model=List[TransactionModel])
async def get_transactions(db: db_dependency, skip: int = 0, limit: int = 100):
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions
    