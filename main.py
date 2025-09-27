from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    name: str
    origin: str

todos: List[Todo] = []

app = FastAPI()
    
    
@app.get("/")
def read_root():
    return {"massage": "Welcome to our todo"}


@app.get("/todos")
def get_todos():
    return todos

#CRUD
@app.post("/todos")
def add_todo(todo: Todo):
    todos.append(todo)
    return todo

#Dynamic put todo_id(update)
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return updated_todo
    return {"error": "Todo not found"} #ERROR Message

#Delete
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted = todos.pop(index)
            return deleted
    return {"error": "Todo not found"} #ERROR Message