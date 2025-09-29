# FastAPI Training - Day 1

## Overview
This directory contains the Day 1 exercises for FastAPI training, focusing on building basic CRUD operations with an in-memory data store.

## Files
- `books.py` - Main FastAPI application implementing a books API

## What's Covered

### Basic FastAPI Application Structure
- FastAPI app initialization
- Pydantic models for data validation
- In-memory data storage using Python lists

### API Endpoints
The books API includes the following endpoints:

- **POST /** - Create a new book
- **GET /** - Retrieve all books
- **GET /{book_id}** - Get a specific book by ID
- **PUT /{book_id}** - Update a book by ID
- **DELETE /{book_id}** - Delete a book by ID

### Book Model
```python
class Book(BaseModel):
    id: int = Field(default=1)
    title: str = Field(default="The Great Gatsby")
    author: str = Field(default="F. Scott Fitzgerald")
    price: float = Field(default=10.99)
```

## Key Learning Points
1. Setting up a FastAPI application
2. Creating Pydantic models with Field validation
3. Implementing CRUD operations
4. Using HTTP exception handling
5. Working with in-memory data storage

## Running the Application
```bash
uvicorn books:app --reload
```

## Next Steps
Day 1 covers the fundamentals of FastAPI with in-memory storage. Day 2 will introduce database integration and more advanced features.