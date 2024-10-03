from abc import abstractmethod
from typing import List

from pydantic import BaseModel

from myapp.domain.kernel import ToDoID
from myapp.domain.task import TaskID, TaskCreationRequest, Description
from myapp.domain.title import Title
from myapp.domain.todo import Category


class Command(BaseModel):
    ...


class CommandHandler:
    @abstractmethod
    def handle(self, command: Command) -> None:
        pass


class DeleteTask(Command):
    todo_id: ToDoID
    task_id: TaskID


class GetToDoList(Command):
    todo_id: ToDoID


class CreateToDoList(Command):
    tasks: List[TaskCreationRequest]
    category: Category


class UpdateTask(Command):
    todo_id: ToDoID
    task_id: TaskID
    title: Title
    description: Description
