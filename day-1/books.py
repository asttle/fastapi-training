from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()

class Book(BaseModel):
    id: int = Field(default=1)
    title: str = Field(default="The Great Gatsby")
    author: str = Field(default="F. Scott Fitzgerald")
    price: float = Field(default=10.99)

books = []

@app.post("/")
def create_book(book: Book):
    books.append(book)
    return book

@app.get("/")
def get_books():
    return books

@app.get("/{book_id}")
def get_book(book_id: int):
    return books[book_id]

@app.put("/{book_id}")
def update_book(book_id: int):
    for x in books:
        if x.id == book_id:
            x.title = "The Great Gatsby"
            x.author = "F. Scott Fitzgerald"
            x.price = 10.99
            return x
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/{book_id}")
def delete_book(book_id: int):
    for x in books:
        if x.id == book_id:
            books.remove(x)
            return books
    raise HTTPException(status_code=404, detail="Book not found")
    return books

