from fastapi import APIRouter
from schema.schemas import list_serial
from config.database import collection_name
from models.todos import Todo
from bson import ObjectId

router = APIRouter()

@router.get("/")
def get_todos():
    return list_serial(collection_name.find())

@router.post("/")
def create_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    return list_serial(collection_name.find())

@router.put("/{id}")
def update_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return list_serial(collection_name.find())

@router.delete("/{id}")
def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return list_serial(collection_name.find())