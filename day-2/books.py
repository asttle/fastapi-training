from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
import database
from sqlalchemy.orm import Session

# Create all tables in the database
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

class Book(BaseModel):
    title: str = Field(default="The Great Gatsby")
    author: str = Field(default="F. Scott Fitzgerald")
    price: float = Field(default=10.99)

books = []

@app.post("/")
def create_book(book: Book, db: Session = Depends(get_db)):
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.price = book.price
    db.add(book_model)
    db.commit()
    return book

@app.get("/")
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Books).all()

@app.get("/{book_id}")
def get_book(book_id: int):
    return books[book_id]

@app.put("/{book_id}")
def update_book(book_id: int,book: Book, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail="Book not found by this ID: {book_id}")
    book_model.title = book.title
    book_model.author = book.author
    book_model.price = book.price
    db.add(book_model)
    db.commit()
    return book

@app.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail="Book not found by this ID: {book_id}")
    db.delete(book_model)
    db.commit()

