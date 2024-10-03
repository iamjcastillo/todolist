from myapp.application.commands.command_handler import Command, DeleteTask, GetToDoList
from myapp.application.commands.delete_task_command_handler import DeleteTaskCommandHandler
from myapp.application.commands.get_todo_list_command_handler import GetToDoListCommandHandler


class CommandHandlerFactory:
    def get(self, command: Command):
        if isinstance(command, DeleteTask):
            return DeleteTaskCommandHandler()
        if isinstance(command, GetToDoList):
            return GetToDoListCommandHandler()
