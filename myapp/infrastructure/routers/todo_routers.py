from typing import List, TypeVar, Generic

from fastapi import APIRouter, Query
from pydantic import BaseModel

from myapp.application.services.todo_service import ToDoService
from myapp.domain.criteria import ToDoCriteria, ToDoListWithTasksCriteria
from myapp.domain.todo import ToDoListCreationRequest, TaskCreationRequest, Task, ToDoList
from myapp.infrastructure.repositories.to_do_repository import ToDoRepository
from myapp.infrastructure.db.database import DBSessionDependency, db_session

router = APIRouter()

T = TypeVar("T")


class ReturnList(BaseModel, Generic[T]):
    items: List[T]


@router.get("/health", tags=["Health"])
async def health():
    return "Healthy"


@router.get("/lists", tags=["ToDo"])
async def get_todo_lists(db: DBSessionDependency, include_tasks: bool = Query(False)):
    db_session.set(db)
    if include_tasks:
        criteria = ToDoListWithTasksCriteria()
    else:
        criteria = ToDoCriteria()

    return ReturnList[ToDoList](items=ToDoService().get(criteria))


@router.post("/lists", tags=["ToDo"])
async def create_todo_list(todo: ToDoListCreationRequest, db: DBSessionDependency) -> ToDoList:
    db_session.set(db)
    return ToDoService().create(todo)
