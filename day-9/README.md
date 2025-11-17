# Day 9 — Redis tutorial

This folder contains a small FastAPI example that demonstrates caching an external API result in Redis.

Overview
- FastAPI application: [`main.app`](day-9/main.py)
- Key features implemented in [`day-9/main.py`](day-9/main.py):
  - Startup/shutdown lifecycle handlers: [`main.startup_event`](day-9/main.py), [`main.shutdown_event`](day-9/main.py)
  - A GET endpoint that caches API responses in Redis: [`main.read_item`](day-9/main.py)
  - Redis client helper: [`main.redis_client`](day-9/main.py)

Requirements
- Python 3.8+
- Redis server running (default: localhost:6379)
- Python packages:
  - fastapi
  - uvicorn
  - redis
  - httpx

Install dependencies (example)
```bash
pip install fastapi uvicorn redis httpx