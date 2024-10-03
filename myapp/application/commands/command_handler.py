from abc import abstractmethod

from pydantic import BaseModel

from myapp.domain.kernel import ToDoID
from myapp.domain.task import TaskID


class Command(BaseModel):
    ...


class CommandHandler:
    @abstractmethod
    def handle(self, command: Command) -> None:
        pass


class DeleteTask(Command):
    todo_id: ToDoID
    task_id: TaskID
