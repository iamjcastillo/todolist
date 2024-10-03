from myapp.application.commands.command_handler import Command
from myapp.application.commands.command_handler_factory import CommandHandlerFactory
from myapp.domain.todo import ToDoList


class ToDoService:
    def __init__(self, command_handler_factory=CommandHandlerFactory()):
        self.command_handler_factory = command_handler_factory

    def execute(self, command: Command) -> ToDoList:
        handler = self.command_handler_factory.get_handler(command)
        return handler.handle(command)
