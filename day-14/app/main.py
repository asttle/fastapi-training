from typing import Annotated
from fastapi import FastAPI, Depends, BackgroundTasks
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)

Base.metadata.create_all(bind=engine)

@app.get("/users/")
async def get_users(db: db_dependency, background_tasks: BackgroundTasks):
    users = db.query(User).all()
    return users

@app.post("/users/")
async def create_user(name: str, db: db_dependency, background_tasks: BackgroundTasks):
    user = User(name=name)
    db.add(user)
    db.commit()
    background_tasks.add_task(print_message, name)
    return {"name": name, "message": "User created"}

def print_message(name: str):
    print(f"User {name} has been created.")

