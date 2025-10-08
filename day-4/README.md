# Day 4: FastAPI Quiz Application

A FastAPI-based quiz application that allows creating questions with multiple choices and retrieving them from a PostgreSQL database.

## Features

- Create quiz questions with multiple choice answers
- Store questions and choices in PostgreSQL database
- RESTful API endpoints for question management
- SQLAlchemy ORM for database operations

## Project Structure

```
day-4/
├── main.py       # FastAPI application with API endpoints
├── database.py   # Database configuration and connection
├── models.py     # SQLAlchemy database models
└── README.md     # This file
```

## Database Models

### Question
- `id`: Primary key (Integer)
- `question_text`: The question text (String)

### Choice
- `id`: Primary key (Integer)
- `choice_text`: The choice text (String)
- `is_correct`: Whether this choice is correct (Boolean)
- `question_id`: Foreign key to Question (Integer)

## API Endpoints

### POST /questions/
Create a new question with choices.

**Request Body:**
```json
{
  "question_text": "What is 2 + 2?",
  "choices": [
    {"choice_text": "3", "is_correct": false},
    {"choice_text": "4", "is_correct": true},
    {"choice_text": "5", "is_correct": false}
  ]
}
```

### GET /questions/
Retrieve all questions from the database.

### GET /choices/{question_id}
Retrieve all choices for a specific question.

## Setup

1. **Install Dependencies**
   ```bash
   pip install fastapi sqlalchemy psycopg2-binary python-dotenv uvicorn
   ```

2. **Environment Variables**
   Create a `.env` file with your PostgreSQL credentials:
   ```env
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=your_password
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   POSTGRES_DB=quiz
   ```

3. **Database Setup**
   Ensure PostgreSQL is running and the database exists. The application will automatically create the required tables.

4. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000` with interactive docs at `http://localhost:8000/docs`.

## Database Configuration

The application uses PostgreSQL with the following default connection parameters:
- Host: localhost
- Port: 5432
- Database: quiz
- User: postgres
- Password: postgres

These can be customized via environment variables in the `.env` file.