from myapp.application.commands.command_handler import Command
from myapp.application.commands.command_handler_factory import CommandHandlerFactory
from myapp.domain.todo import ToDoList
from myapp.infrastructure.repositories.to_do_repository import ToDoRepository


class ToDoService:
    def __init__(self):
        self.todo_repository = ToDoRepository()

    def execute(self, command: Command) -> ToDoList:
        handler = CommandHandlerFactory().get(command)
        return handler.handle(command)
