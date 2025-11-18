# Day 10 — WebSockets with FastAPI

This example demonstrates a simple FastAPI app that serves a small Bootstrap UI and a WebSocket endpoint. The UI displays a generated client ID, connects to the WebSocket server, and lets the user send messages (via WebSocket when available, otherwise via an HTTP POST fallback). Messages are displayed one-by-one in the page.

## Features
- Root page (/) that serves an HTML UI:
  - Bootstrap-styled form with text input and Send button.
  - Displays a generated client ID in a span (`#ws-id`).
  - Shows a list of submissions and incoming WebSocket messages.
  - Uses WebSocket by default, falls back to POST /submit if WS isn't open.
- WebSocket endpoint: `/ws/{client_id}`
  - Accepts a path client_id (string) and associates the socket with it.
  - Echoes personal messages and broadcasts messages to connected clients (example behavior).
- HTTP fallback endpoint: `POST /submit`
  - Accepts JSON `{ "text": "<value>" }` and returns `{ "received": "<value>" }`.

## Files
- main.py — FastAPI application (serves HTML and implements WebSocket and HTTP endpoints)
- README.md — this file

## Requirements
- Python 3.8+
- Run a virtual environment (recommended)
- Install Python packages:
  - fastapi
  - uvicorn (recommended with standard extras)
  - websockets or wsproto (backend for WebSocket support) — installing `uvicorn[standard]` covers this

## Setup (macOS)
1. Create and activate a venv (example):
```bash
python3 -m venv .venv
source .venv/bin/activate