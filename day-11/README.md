# Pytest — Unit testing guide

This project uses pytest for unit testing FastAPI endpoints. This document covers setup, common commands, FastAPI testing tips, and troubleshooting.

## Prerequisites
- Python 3.8+
- A virtual environment (recommended)

## Setup (macOS)
```bash
cd /Users/asttle/Desktop/fastapi-learnings/fastapi-training/day-11
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install pytest pytest-cov fastapi[all] httpx
```
(Installing `fastapi[all]` includes testing/backends; alternatively install `uvicorn[standard]` and `httpx` as needed.)

## Run tests
- Run the full test suite:
```bash
pytest -q
```
- Run with coverage:
```bash
pip install pytest-cov
pytest --cov=.
```
- Run a single test file:
```bash
pytest tests/test_main.py -q
```
- Run a single test function:
```bash
pytest tests/test_main.py::test_create_todo -q
```

## Test naming and collection
- pytest only collects functions and classes that start with `test_`.
- Files should be named `test_*.py` or `*_test.py`.
- Ensure test functions are prefixed with `test_` (e.g. `test_update_todo`) — otherwise pytest will skip them.

## FastAPI testing tips
- Use FastAPI's TestClient for synchronous endpoint tests:
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
resp = client.get("/")
```
- For async tests that require an async HTTP client, use httpx.AsyncClient with pytest-asyncio or anyio fixtures.

## Shared state isolation
- If your app uses a module-level in-memory store (e.g., `todos` dict), clear it between tests with an autouse fixture:
```python
import pytest
from main import todos

@pytest.fixture(autouse=True)
def clear_store():
    todos.clear()
    yield
    todos.clear()
```

## Common errors & fixes
- ImportError: attempted relative import with no known parent package
  - Use absolute imports in tests:
    ```python
    # BAD: from .main import app
    from main import app, todos
    ```
  - Or run pytest as a package from the parent directory:
    ```bash
    python -m pytest day-11
    ```
  - Or add an `__init__.py` to make the directory a package.

- Missing test collection (only 3 tests collected when 4 expected)
  - Rename functions to start with `test_`.

- WebSocket backend error:
  - Install WebSocket support for uvicorn:
    ```bash
    pip install "uvicorn[standard]" websockets wsproto
    ```

## Best practices
- Keep tests deterministic and isolated.
- Use fixtures for shared setup/teardown.
- Prefer small, focused tests.
- Test both success and error cases (status codes and response bodies).

## Example minimal test file
```python
# tests/test_main.py
from fastapi.testclient import TestClient
from main import app, todos
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_store():
    todos.clear()
    yield

def test_create_todo():
    resp = client.post("/", json={"name": "Task A"})
    assert resp.status_code == 200
    assert resp.json() == {"name": "Task A", "completed": False}
```

This guide should help run and troubleshoot pytest for this FastAPI project.// filepath: /Users/asttle/Desktop/fastapi-learnings/fastapi-training/day-11/TESTING.md
# Pytest — Unit testing guide

This project uses pytest for unit testing FastAPI endpoints. This document covers setup, common commands, FastAPI testing tips, and troubleshooting.

## Prerequisites
- Python 3.8+
- A virtual environment (recommended)

## Setup (macOS)
```bash
cd /Users/asttle/Desktop/fastapi-learnings/fastapi-training/day-11
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install pytest pytest-cov fastapi[all] httpx
```
(Installing `fastapi[all]` includes testing/backends; alternatively install `uvicorn[standard]` and `httpx` as needed.)

## Run tests
- Run the full test suite:
```bash
pytest -q
```
- Run with coverage:
```bash
pip install pytest-cov
pytest --cov=.
```
- Run a single test file:
```bash
pytest tests/test_main.py -q
```
- Run a single test function:
```bash
pytest tests/test_main.py::test_create_todo -q
```

## Test naming and collection
- pytest only collects functions and classes that start with `test_`.
- Files should be named `test_*.py` or `*_test.py`.
- Ensure test functions are prefixed with `test_` (e.g. `test_update_todo`) — otherwise pytest will skip them.

## FastAPI testing tips
- Use FastAPI's TestClient for synchronous endpoint tests:
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
resp = client.get("/")
```
- For async tests that require an async HTTP client, use httpx.AsyncClient with pytest-asyncio or anyio fixtures.

## Shared state isolation
- If your app uses a module-level in-memory store (e.g., `todos` dict), clear it between tests with an autouse fixture:
```python
import pytest
from main import todos

@pytest.fixture(autouse=True)
def clear_store():
    todos.clear()
    yield
    todos.clear()
```

## Common errors & fixes
- ImportError: attempted relative import with no known parent package
  - Use absolute imports in tests:
    ```python
    # BAD: from .main import app
    from main import app, todos
    ```
  - Or run pytest as a package from the parent directory:
    ```bash
    python -m pytest day-11
    ```
  - Or add an `__init__.py` to make the directory a package.

- Missing test collection (only 3 tests collected when 4 expected)
  - Rename functions to start with `test_`.

- WebSocket backend error:
  - Install WebSocket support for uvicorn:
    ```bash
    pip install "uvicorn[standard]" websockets wsproto
    ```

## Best practices
- Keep tests deterministic and isolated.
- Use fixtures for shared setup/teardown.
- Prefer small, focused tests.
- Test both success and error cases (status codes and response bodies).

## Example minimal test file
```python
# tests/test_main.py
from fastapi.testclient import TestClient
from main import app, todos
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_store():
    todos.clear()
    yield

def test_create_todo():
    resp = client.post("/", json={"name": "Task A"})
    assert resp.status_code == 200
    assert resp.json() == {"name": "Task A", "completed": False}
```

This guide should help run and troubleshoot pytest for this FastAPI project.