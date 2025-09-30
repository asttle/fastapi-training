# FastAPI Training - Day 3

## Overview
This directory contains the Day 3 exercises for FastAPI training, focusing on MongoDB integration and modular application architecture with a Todo API.

## Files
- `main.py` - Main FastAPI application entry point
- `config/database.py` - MongoDB connection and configuration
- `models/todos.py` - Pydantic models for data validation
- `routes/route.py` - API route definitions and handlers
- `schema/schemas.py` - Data serialization utilities for MongoDB documents

## What's Covered

### MongoDB Integration
- MongoDB Atlas cloud database connection using PyMongo
- Document-based NoSQL data storage
- BSON ObjectId handling for document identification

### Modular Application Architecture
The application follows a clean, modular structure with:
- Separated concerns across different modules
- Route handlers in dedicated files
- Database configuration isolation
- Schema serialization utilities

### API Endpoints
The Todo API includes the following MongoDB-integrated endpoints:

- **GET /** - Retrieve all todos from MongoDB
- **POST /** - Create a new todo (stored in MongoDB)
- **PUT /{id}** - Update a todo by ObjectId in MongoDB
- **DELETE /{id}** - Delete a todo by ObjectId from MongoDB

### Todo Model
```python
class Todo(BaseModel):
    title: str
    description: str
    completed: bool
```

### MongoDB Document Structure
```python
{
    "_id": ObjectId("..."),
    "title": "Sample Todo",
    "description": "Todo description",
    "completed": false
}
```

## Key Learning Points
1. **MongoDB Integration**: Connecting FastAPI to MongoDB Atlas using PyMongo
2. **Document Database**: Working with NoSQL document storage and BSON ObjectIds
3. **Modular Architecture**: Organizing code into logical modules (config, models, routes, schemas)
4. **Data Serialization**: Converting MongoDB documents to JSON-serializable formats
5. **Router Organization**: Using APIRouter for cleaner route management
6. **Cloud Database**: Integrating with MongoDB Atlas cloud service

## Database Configuration
- **Database**: MongoDB Atlas (Cloud)
- **Driver**: PyMongo
- **Collection**: `todo_collection` in `todo_db` database
- **Connection**: MongoDB Atlas cluster with authentication via environment variables

## Environment Setup
1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Update the `.env` file with your MongoDB credentials:
   ```bash
   MONGODB_USERNAME=your_username_here
   MONGODB_PASSWORD=your_password_here
   MONGODB_CLUSTER_URL=your-cluster.mongodb.net
   MONGODB_APP_NAME=your-app-name
   ```

3. Install required dependencies:
   ```bash
   pip install python-dotenv
   ```

## Running the Application
```bash
uvicorn main:app --reload
```

The application will connect to the configured MongoDB Atlas cluster using environment variables and handle Todo operations.

## Architecture Improvements from Day 2
- **NoSQL Database**: Transitioned from SQLite to MongoDB for flexible document storage
- **Modular Structure**: Better code organization with separate modules for different concerns
- **Cloud Integration**: Using MongoDB Atlas instead of local database files
- **Document Serialization**: Custom serializers for MongoDB document handling
- **Router Separation**: API routes organized in dedicated router modules

## Security Features
- **Environment Variables**: Database credentials are securely stored in `.env` files
- **Git Security**: `.env` files are excluded from version control via `.gitignore`
- **Credential Isolation**: Sensitive information is separated from source code

## Files Added
- `.env.example` - Template file showing required environment variables
- Updated `.gitignore` - Excludes environment files from version control