# Day 15 — User Auth & Management (FastAPI + SQLAlchemy)

A small FastAPI example that demonstrates user creation, authentication and basic user lookup backed by SQLite using SQLAlchemy. This project uses a simple synchronous SQLAlchemy setup (SessionLocal) and Passlib for password hashing.

## Features
- SQLite database (./test.db) with SQLAlchemy ORM
- Dependency-injected DB session per request
- User registration (password hashing) and login (authentication)
- Endpoints to create and retrieve users
- Guidance to avoid bcrypt 72-byte limitation and recommended hashing options

## Files
- backend/database.py — SQLAlchemy engine, SessionLocal and Base
- backend/main.py — FastAPI application: endpoints, password hashing, auth helpers
- backend/models.py (expected) — ORM models (User)
- README.md — this file

## Quick setup (macOS)
```bash
cd /Users/asttle/Desktop/fastapi-learnings/fastapi-training/day-15
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
# Recommended packages:
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] bcrypt
# Or, for stronger modern hashing:
# pip install passlib[argon2] argon2-cffi