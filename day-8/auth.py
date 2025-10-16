from typing import Annotated
from pydantic import BaseModel
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models import User
from starlette import status
from database import SessionLocal
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
import os

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

SECRET_KEY = os.getenv("SECRET_KEY")  # Use a secure key in production
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # passlib context for hashing passwords
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login") # OAuth2 scheme for token retrieval

class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():  
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserRequest, db: db_dependency):
    hashed_password = bcrypt_context.hash(user.password)
    user_model = User(username=user.username, hashed_password=hashed_password)
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return {"username": user_model.username}