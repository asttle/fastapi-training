# FastAPI Training - Day 2

## Overview
This directory contains the Day 2 exercises for FastAPI training, focusing on database integration with SQLAlchemy and SQLite for persistent data storage.

## Files
- `books.py` - Main FastAPI application with database-integrated CRUD operations
- `database.py` - Database configuration and connection setup
- `models.py` - SQLAlchemy ORM models
- `books.db` - SQLite database file (created automatically)

## What's Covered

### Database Integration
- SQLAlchemy ORM setup with SQLite
- Database session management with dependency injection
- Automatic table creation from models

### Enhanced API Architecture
The application follows a more structured approach with:
- Separate database configuration
- ORM models for data persistence
- Database session dependency injection

### API Endpoints
The books API includes the following database-integrated endpoints:

- **POST /** - Create a new book (persisted to database)
- **GET /** - Retrieve all books from database
- **GET /{book_id}** - Get a specific book by ID *(Note: currently using in-memory list)*
- **PUT /{book_id}** - Update a book by ID in database
- **DELETE /{book_id}** - Delete a book by ID from database

### Database Model
```python
class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    price = Column(Float, index=True)
```

### Pydantic Model
```python
class Book(BaseModel):
    title: str = Field(default="The Great Gatsby")
    author: str = Field(default="F. Scott Fitzgerald")
    price: float = Field(default=10.99)
```

## Key Learning Points
1. **SQLAlchemy Integration**: Setting up database connections and ORM
2. **Database Sessions**: Using dependency injection for session management
3. **Model Definition**: Creating SQLAlchemy models with proper column definitions
4. **CRUD Operations**: Implementing database operations (Create, Read, Update, Delete)
5. **Error Handling**: Proper HTTP exception handling for missing resources
6. **Database Configuration**: Separating database setup from application logic

## Database Configuration
- **Database**: SQLite (`books.db`)
- **ORM**: SQLAlchemy
- **Connection**: Local SQLite file with thread safety configurations

## Running the Application
```bash
uvicorn books:app --reload
```

The application will automatically create the `books.db` SQLite database file and the necessary tables on startup.

## Architecture Improvements from Day 1
- **Persistent Storage**: Data survives application restarts
- **Structured Code**: Separation of concerns with dedicated files for database and models
- **Dependency Injection**: Proper database session management
- **ORM Benefits**: Type-safe database operations and automatic table creation

## Known Issues
- The `GET /{book_id}` endpoint still uses the in-memory list instead of database queries
- Inconsistent data sources between endpoints (some use database, one uses in-memory list)