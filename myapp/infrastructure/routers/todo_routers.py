from typing import List, TypeVar, Generic

from fastapi import APIRouter
from pydantic import BaseModel

from myapp.application.commands.command_handler import DeleteTask, GetToDoList, CreateToDoList, UpdateTask
from myapp.application.services.todo_service import ToDoService
from myapp.domain.kernel import ToDoID
from myapp.domain.task import TaskID, Description
from myapp.domain.title import Title
from myapp.domain.todo import ToDoList
from myapp.infrastructure.db.database import DBSessionDependency, db_session

router = APIRouter()

T = TypeVar("T")


class ReturnList(BaseModel, Generic[T]):
    items: List[T]


class TaskUpdateRequestDTO(BaseModel):
    title: Title
    description: Description


@router.get("/health", tags=["Health"])
async def health():
    return "Healthy"


@router.post("/lists", tags=["ToDo"])
async def create_todo_list(todo: CreateToDoList, db: DBSessionDependency) -> ToDoList:
    db_session.set(db)
    return ToDoService().execute(command=CreateToDoList.model_validate(todo.model_dump()))


@router.get("/lists/{id}", tags=["ToDo"])
async def get_todo_list(id: ToDoID, db: DBSessionDependency) -> ToDoList:
    db_session.set(db)
    return ToDoService().execute(command=GetToDoList(todo_id=id))


@router.delete("/lists/{id}/tasks/{task-id}", tags=["Tasks"])
async def delete_task(id: ToDoID, task_id: TaskID, db: DBSessionDependency) -> ToDoList:
    db_session.set(db)
    return ToDoService().execute(command=DeleteTask(task_id=task_id, todo_id=id))


@router.patch("/lists/{id}/tasks/{task-id}", tags=["Tasks"])
async def update_task(id: ToDoID, task_id: TaskID, request: TaskUpdateRequestDTO, db: DBSessionDependency) -> ToDoList:
    db_session.set(db)
    return ToDoService().execute(
        command=UpdateTask(task_id=task_id, todo_id=id, title=request.title, description=request.description)
    )
