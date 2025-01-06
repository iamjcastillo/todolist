from myapp.application.commands.command_handler import Command, DeleteTask, GetToDoList, CreateToDoList, UpdateTask, CreateTask
from myapp.application.commands.create_todo_list_command_handler import CreateToDoListCommandHandler
from myapp.application.commands.delete_task_command_handler import DeleteTaskCommandHandler
from myapp.application.commands.get_todo_list_command_handler import GetToDoListCommandHandler
from myapp.application.commands.update_task_command_handler import UpdateTaskCommandHandler
from myapp.application.commands.create_task_command_handler import CreateTaskCommandHandler


class CommandHandlerFactory:
    def get_handler(self, command: Command):
        if isinstance(command, DeleteTask):
            return DeleteTaskCommandHandler()
        if isinstance(command, GetToDoList):
            return GetToDoListCommandHandler()
        if isinstance(command, CreateToDoList):
            return CreateToDoListCommandHandler()
        if isinstance(command, UpdateTask):
            return UpdateTaskCommandHandler()
        if isinstance(command, CreateTask):
            return CreateTaskCommandHandler()
