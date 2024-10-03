from myapp.application.commands.command_handler import CommandHandler, DeleteTask
from myapp.infrastructure.repositories.to_do_repository import ToDoRepository


class DeleteTaskCommandHandler(CommandHandler):
    def __init__(self):
        self.todo_repository = ToDoRepository()

    def handle(self, command: DeleteTask) -> None:
        todo_list = self.todo_repository.get(id=command.todo_id)
        todo_list.remove_task(task_id=command.task_id)
        return self.todo_repository.update(todo_list)
