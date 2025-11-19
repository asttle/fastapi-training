from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class TodoItem(BaseModel):
    name: str
    completed: bool = False

todos = {}

@app.post("/", response_model=TodoItem)
async def create_todo(item: TodoItem):
    if item.name in todos:
        raise HTTPException(status_code=400, detail="Todo item already exists")
    todos[item.name] = item
    return item

@app.get("/", response_model=List[TodoItem])
async def read_todos():
    return list(todos.values())

@app.get("/{todo_id}", response_model=TodoItem)
async def read_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return todos[todo_id]

@app.put("/{todo_id}", response_model=TodoItem)
async def update_todo(todo_id: str, item: TodoItem):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo item not found")
    todos[todo_id] = item
    return item

@app.delete("/{todo_id}", response_model=TodoItem)
async def delete_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return todos.pop(todo_id)



