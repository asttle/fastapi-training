from fastapi.testclient import TestClient
from main import app, todos
client = TestClient(app)

def clear_todos():
    todos.clear()

def test_read_todos():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_todo():
    response = client.post("/", json={"name": "Test Task"})
    assert response.status_code == 200
    assert response.json() == {"name": "Test Task", "completed": False}

def test_read_todo():
    client.post("/", json={"name": "Read Task"})
    response = client.get("/Read Task")
    assert response.status_code == 200

def test_update_todo():
    client.post("/", json={"name": "Update Task"})
    response = client.put("/Update Task", json={"name": "Update Task", "completed": True})
    assert response.status_code == 200
    assert response.json() == {"name": "Update Task", "completed": True}

def test_delete_todo():
    client.post("/", json={"name": "Delete Task"})
    response = client.delete("/Delete Task")
    assert response.status_code == 200
    assert response.json() == {"name": "Delete Task", "completed": False}