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
ALGORITHM = os.getenv("ALGORITHM", "HS256")  # Default to HS256 if not set

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # passlib context for hashing passwords
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token") # OAuth2 scheme for token retrieval

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

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not bcrypt_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        user.username, user.id, expires_delta=access_token_expires 
    )
    return {"access_token": access_token, "token_type": "bearer"}

def create_access_token(username: str, user_id: int, expires_delta: timedelta | None = None):
    to_encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user