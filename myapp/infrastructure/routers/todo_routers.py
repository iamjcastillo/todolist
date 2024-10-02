from typing import List, TypeVar, Generic

from fastapi import APIRouter
from pydantic import BaseModel

from myapp.application.services.todo_service import ToDoService, DeleteTask
from myapp.domain.kernel import ToDoID
from myapp.domain.task import TaskID
from myapp.domain.todo import ToDoListCreationRequest, ToDoList
from myapp.infrastructure.db.database import DBSessionDependency, db_session

router = APIRouter()

T = TypeVar("T")


class ReturnList(BaseModel, Generic[T]):
    items: List[T]


@router.get("/health", tags=["Health"])
async def health():
    return "Healthy"


@router.post("/lists", tags=["ToDo"])
async def create_todo_list(todo: ToDoListCreationRequest, db: DBSessionDependency) -> ToDoList:
    db_session.set(db)
    return ToDoService().create(todo)


@router.get("/lists/{id}", tags=["ToDo"])
async def get_todo_list(id: ToDoID, db: DBSessionDependency) -> ToDoList:
    db_session.set(db)
    return ToDoService().get(id=id)


@router.delete("/lists/{id}/tasks/{task-id}", tags=["Tasks"])
async def delete_task(id: ToDoID, task_id: TaskID, db: DBSessionDependency) -> ToDoList:
    db_session.set(db)
    return ToDoService().execute(request=DeleteTask(task_id=task_id, todo_id=id))
