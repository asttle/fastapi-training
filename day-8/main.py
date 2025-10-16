from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from database import SessionLocal, engine
import models
from sqlalchemy.orm import Session
import auth

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

@app.get("/", status_code=200)
async def user(user: None, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"User": user}

