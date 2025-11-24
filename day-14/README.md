# Day 14 — User Management (FastAPI + Async SQLModel)

This example implements a minimal user management API using FastAPI and async SQLModel backed by SQLite (aiosqlite). It demonstrates:

- async DB setup and schema creation on startup
- dependency-injected async DB sessions
- simple user create/get/list endpoints
- basic (non-production) password hashing
- background task example

## Files
- main.py — FastAPI app, models, DB setup and endpoints
- day14.db — SQLite file created at runtime (in project folder)

## Models
- UserCreate — input payload for creating users: { username, email?, password }
- User — DB table model with id, username, email, password_hash, created_at
- UserRead — response model for user data (excludes password_hash)

## Endpoints
- POST /users/ — create a new user  
  - Request body: UserCreate JSON  
  - Responses:
    - 201 Created: returns UserRead
    - 400 Bad Request: username already exists
- GET /users/{user_id} — get a single user by id  
  - 200 OK: returns UserRead  
  - 404 Not Found: user missing
- GET /users/ — list all users  
  - 200 OK: returns list[UserRead]

## Security note
- Passwords are hashed with SHA-256 in this example for simplicity. This is NOT suitable for production.
- Use a strong password hasher (bcrypt/argon2 via passlib) and add proper authentication/authorization before exposing real user data.

## Requirements
- Python 3.10+ (recommended)
- Packages:
  - fastapi
  - uvicorn
  - sqlmodel
  - sqlalchemy
  - aiosqlite

Install in a virtual environment (macOS example):
```bash
cd /Users/asttle/Desktop/fastapi-learnings/fastapi-training/day-14
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install fastapi "uvicorn[standard]" sqlmodel sqlalchemy aiosqlite
```

## Run (development)
```bash
uvicorn main:app --reload --port 8000
```
Open interactive docs: http://127.0.0.1:8000/docs

## Example requests
Create user:
```bash
curl -s -X POST http://127.0.0.1:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@example.com","password":"s3cret"}' | jq
```

Get user:
```bash
curl http://127.0.0.1:8000/users/1 | jq
```

List users:
```bash
curl http://127.0.0.1:8000/users/ | jq
```

## Notes & Improvements
- Persisting plain hashed passwords is not enough: add salt, use adaptive hashing and secure storage.
- Add validation (unique email, allowed username chars) using Pydantic/SQLModel fields.
- Add migrations (Alembic) for schema evolution.
- Add tests (pytest + TestClient or httpx.AsyncClient).
- Consider environment/config management for DATABASE_URL and secrets.

## Troubleshooting
- If SQLModel metadata is not created on startup, ensure the app's lifespan hook runs (start via uvicorn normally).
- For dependency or Python version errors (e.g., click, uvicorn), upgrade your base Python image or use compatible package versions.

License: example code for learning purposes.
```# filepath: /Users/asttle/Desktop/fastapi-learnings/fastapi-training/day-14/README.md

# Day 14 — User Management (FastAPI + Async SQLModel)

This example implements a minimal user management API using FastAPI and async SQLModel backed by SQLite (aiosqlite). It demonstrates:

- async DB setup and schema creation on startup
- dependency-injected async DB sessions
- simple user create/get/list endpoints
- basic (non-production) password hashing
- background task example

## Files
- main.py — FastAPI app, models, DB setup and endpoints
- day14.db — SQLite file created at runtime (in project folder)

## Models
- UserCreate — input payload for creating users: { username, email?, password }
- User — DB table model with id, username, email, password_hash, created_at
- UserRead — response model for user data (excludes password_hash)

## Endpoints
- POST /users/ — create a new user  
  - Request body: UserCreate JSON  
  - Responses:
    - 201 Created: returns UserRead
    - 400 Bad Request: username already exists
- GET /users/{user_id} — get a single user by id  
  - 200 OK: returns UserRead  
  - 404 Not Found: user missing
- GET /users/ — list all users  
  - 200 OK: returns list[UserRead]

## Security note
- Passwords are hashed with SHA-256 in this example for simplicity. This is NOT suitable for production.
- Use a strong password hasher (bcrypt/argon2 via passlib) and add proper authentication/authorization before exposing real user data.

## Requirements
- Python 3.10+ (recommended)
- Packages:
  - fastapi
  - uvicorn
  - sqlmodel
  - sqlalchemy
  - aiosqlite

Install in a virtual environment (macOS example):
```bash
cd /Users/asttle/Desktop/fastapi-learnings/fastapi-training/day-14
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install fastapi "uvicorn[standard]" sqlmodel sqlalchemy aiosqlite
```

## Run (development)
```bash
uvicorn main:app --reload --port 8000
```
Open interactive docs: http://127.0.0.1:8000/docs

## Example requests
Create user:
```bash
curl -s -X POST http://127.0.0.1:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@example.com","password":"s3cret"}' | jq
```

Get user:
```bash
curl http://127.0.0.1:8000/users/1 | jq
```

List users:
```bash
curl http://127.0.0.1:8000/users/ | jq
```

## Notes & Improvements
- Persisting plain hashed passwords is not enough: add salt, use adaptive hashing and secure storage.
- Add validation (unique email, allowed username chars) using Pydantic/SQLModel fields.
- Add migrations (Alembic) for schema evolution.
- Add tests (pytest + TestClient or httpx.AsyncClient).
- Consider environment/config management for DATABASE_URL and secrets.

## Troubleshooting
- If SQLModel metadata is not created on startup, ensure the app's lifespan hook runs (start via uvicorn normally).
- For dependency or Python version errors (e.g., click, uvicorn), upgrade your base Python image or use compatible package versions.

License: example code for learning purposes.