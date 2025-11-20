# Day 12 — FastAPI + Async SQLModel (CQRS-style) README
// filepath: /Users/asttle/Desktop/fastapi-learnings/fastapi-training/day-12/README.md

## Overview
This example shows a small FastAPI app using SQLModel + SQLAlchemy async engine and a simple CQRS-style separation via an `ItemService`. The app:
- exposes REST endpoints to create/read items
- uses async DB engine (sqlite+aiosqlite) and creates tables on startup
- demonstrates dependency injection for DB session and service
- runs a background task after creating an item

## Project structure (relevant)
- `main.py` — FastAPI app, SQLModel data models, async engine, `ItemService` (query + command methods), endpoints.

## Key concepts / CQRS mapping
- Command (write):
  - `ItemService.create_item(...)` — constructs and persists a new Item (command).
- Query (read):
  - `ItemService.get_item(...)` and `ItemService.get_items()` — perform read-only queries.
- The `ItemService` centralizes application behavior; endpoints obtain it via FastAPI Depends (DI). This mirrors a simple CQRS separation: queries and commands are implemented as separate service methods even though they share the same service in this small example.

## Models
- `ItemBase` — base SQLModel with `name`, `description`.
- `Item` — table model with `id` primary key.
- `ItemCreate` / `ItemRead` — DTOs used in endpoints / responses.

## Async DB & lifecycle
- DATABASE_URL: `sqlite+aiosqlite:///./test.db`
- `create_async_engine` is used with a `sessionmaker` producing `AsyncSession`.
- `lifespan` asynccontextmanager creates DB schema on app startup:
  - `async with engine.begin() as conn: await conn.run_sync(SQLModel.metadata.create_all)`

## Endpoints
- POST /items/ — create new item (request body: `ItemCreate`), returns `ItemRead`
  - Background task `log_item_creation` is scheduled after create
- GET /items/{item_id} — read a single item
- GET /items/ — read all items

Example curl:
```bash
# create
curl -s -X POST http://127.0.0.1:8000/items/ \
  -H "Content-Type: application/json" \
  -d '{"name":"My item","description":"desc"}' | jq

# get single
curl -s http://127.0.0.1:8000/items/1 | jq

# list
curl -s http://127.0.0.1:8000/items/ | jq
```

## Dependencies
Install in a virtualenv:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install fastapi "uvicorn[standard]" sqlmodel sqlalchemy aiosqlite
```
- `uvicorn[standard]` provides an async server and WebSocket/backends.
- `sqlmodel` builds on SQLAlchemy + Pydantic.

## Run
From the `day-12` directory:
```bash
uvicorn main:app --reload
```
Open: `http://127.0.0.1:8000/docs` for interactive API docs.

## Notes & suggestions
- Current `get_db` in `main.py` yields an `AsyncSession` from `AsyncSessionLocal`. Consider converting `get_db` to an async generator for clarity:
  ```py
  async def get_db():
      async with AsyncSessionLocal() as session:
          yield session
  ```
  This ensures proper async session lifecycle and cleanup.
- For production:
  - Move DATABASE_URL to env vars.
  - Use a robust RDBMS (Postgres) for concurrency and scaling.
  - Split command/query services into separate classes/modules when complexity grows.
  - Add proper error handling, logging and transactional boundaries where needed.
- For multi-process or multi-instance broadcast behavior, use an external messaging / event bus.

## Troubleshooting
- If the SQLite file or DB schema does not appear, ensure the app startup ran (lifespan runs on first server start). Check Uvicorn logs for migration/create table messages.
- If you need sync testing, prefer `TestClient` for endpoint tests; for async tests use `httpx.AsyncClient` with pytest-asyncio.

---
This README summarizes the app, how CQRS is reflected, how to run and common improvements. Place this file next to `main.py` in the `day-12` folder.
```# Day 12 — FastAPI + Async SQLModel (CQRS-style) README
// filepath: /Users/asttle/Desktop/fastapi-learnings/fastapi-training/day-12/README.md

## Overview
This example shows a small FastAPI app using SQLModel + SQLAlchemy async engine and a simple CQRS-style separation via an `ItemService`. The app:
- exposes REST endpoints to create/read items
- uses async DB engine (sqlite+aiosqlite) and creates tables on startup
- demonstrates dependency injection for DB session and service
- runs a background task after creating an item

## Project structure (relevant)
- `main.py` — FastAPI app, SQLModel data models, async engine, `ItemService` (query + command methods), endpoints.

## Key concepts / CQRS mapping
- Command (write):
  - `ItemService.create_item(...)` — constructs and persists a new Item (command).
- Query (read):
  - `ItemService.get_item(...)` and `ItemService.get_items()` — perform read-only queries.
- The `ItemService` centralizes application behavior; endpoints obtain it via FastAPI Depends (DI). This mirrors a simple CQRS separation: queries and commands are implemented as separate service methods even though they share the same service in this small example.

## Models
- `ItemBase` — base SQLModel with `name`, `description`.
- `Item` — table model with `id` primary key.
- `ItemCreate` / `ItemRead` — DTOs used in endpoints / responses.

## Async DB & lifecycle
- DATABASE_URL: `sqlite+aiosqlite:///./test.db`
- `create_async_engine` is used with a `sessionmaker` producing `AsyncSession`.
- `lifespan` asynccontextmanager creates DB schema on app startup:
  - `async with engine.begin() as conn: await conn.run_sync(SQLModel.metadata.create_all)`

## Endpoints
- POST /items/ — create new item (request body: `ItemCreate`), returns `ItemRead`
  - Background task `log_item_creation` is scheduled after create
- GET /items/{item_id} — read a single item
- GET /items/ — read all items

Example curl:
```bash
# create
curl -s -X POST http://127.0.0.1:8000/items/ \
  -H "Content-Type: application/json" \
  -d '{"name":"My item","description":"desc"}' | jq

# get single
curl -s http://127.0.0.1:8000/items/1 | jq

# list
curl -s http://127.0.0.1:8000/items/ | jq
```

## Dependencies
Install in a virtualenv:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install fastapi "uvicorn[standard]" sqlmodel sqlalchemy aiosqlite
```
- `uvicorn[standard]` provides an async server and WebSocket/backends.
- `sqlmodel` builds on SQLAlchemy + Pydantic.

## Run
From the `day-12` directory:
```bash
uvicorn main:app --reload
```
Open: `http://127.0.0.1:8000/docs` for interactive API docs.

## Notes & suggestions
- Current `get_db` in `main.py` yields an `AsyncSession` from `AsyncSessionLocal`. Consider converting `get_db` to an async generator for clarity:
  ```py
  async def get_db():
      async with AsyncSessionLocal() as session:
          yield session
  ```
  This ensures proper async session lifecycle and cleanup.
- For production:
  - Move DATABASE_URL to env vars.
  - Use a robust RDBMS (Postgres) for concurrency and scaling.
  - Split command/query services into separate classes/modules when complexity grows.
  - Add proper error handling, logging and transactional boundaries where needed.
- For multi-process or multi-instance broadcast behavior, use an external messaging / event bus.

## Troubleshooting
- If the SQLite file or DB schema does not appear, ensure the app startup ran (lifespan runs on first server start). Check Uvicorn logs for migration/create table messages.
- If you need sync testing, prefer `TestClient` for endpoint tests; for async tests use `httpx.AsyncClient` with pytest-asyncio.

---
This README summarizes the app, how CQRS is reflected, how to run and common improvements. Place this file next to `main.py` in the `day-12` folder.