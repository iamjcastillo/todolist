from myapp.application.commands.command_handler import GetToDoList
from myapp.domain.todo import ToDoList
from myapp.infrastructure.repositories.to_do_repository import ToDoRepository


class GetToDoListCommandHandler:
    def __init__(self):
        self.todo_repository = ToDoRepository()

    def handle(self, command: GetToDoList) -> ToDoList:
        return self.todo_repository.get(id=command.todo_id)
