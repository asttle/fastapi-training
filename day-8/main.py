from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from database import SessionLocal, engine
import models
from sqlalchemy.orm import Session
import auth
from auth import get_current_user

app = FastAPI()
app.include_router(auth.router)
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
# The user dependancy passed to get will help extracct the jwt token from header validate it and return the user

@app.get("/", status_code=200)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"User": user}

