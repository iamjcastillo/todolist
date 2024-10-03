from myapp.application.commands.command_handler import Command, DeleteTask
from myapp.application.commands.delete_task_command_handler import DeleteTaskCommandHandler


class CommandHandlerFactory:
    def get(self, command: Command):
        if isinstance(command, DeleteTask):
            return DeleteTaskCommandHandler()
