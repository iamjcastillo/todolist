from typing import List, TypeVar, Generic

from fastapi import APIRouter
from pydantic import BaseModel

from myapp.application.commands.command_handler import DeleteTask, GetToDoList, CreateToDoList, UpdateTask, CreateTask
from myapp.application.services.todo_service import ToDoService
from myapp.domain.kernel import ToDoID
from myapp.domain.task import TaskID, Description, TaskCreationRequest
from myapp.domain.title import Title
from myapp.domain.todo import ToDoList, Category
from myapp.infrastructure.db.database import DBSessionDependency, db_session

router = APIRouter()

T = TypeVar("T")


class ReturnList(BaseModel, Generic[T]):
    items: List[T]


class CreateToDoListRequest(BaseModel):
    category: Category


class TaskUpdateRequestDTO(BaseModel):
    title: Title
    description: Description


@router.get("/health", tags=["Health"])
async def health():
    return "Healthy"


@router.post("/lists", tags=["ToDo"])
async def create_todo_list(request: CreateToDoListRequest, db: DBSessionDependency) -> ToDoList:
    db_session.set(db)
    command = CreateToDoList(category=request.category, tasks=[])
    return ToDoService().execute(command=command)


@router.post("/lists/{todo_id}/tasks", tags=["Tasks"])
async def create_task(todo_id: ToDoID, task: TaskCreationRequest, db: DBSessionDependency) -> ToDoList:
    db_session.set(db)
    command = CreateTask(todo_id=todo_id, task=task)
    return ToDoService().execute(command=command)


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
