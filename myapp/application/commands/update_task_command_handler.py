from myapp.application.commands.command_handler import UpdateTask
from myapp.domain.todo import ToDoList
from myapp.infrastructure.repositories.to_do_repository import ToDoRepository


class UpdateTaskCommandHandler:
    def __init__(self, todo_repository=ToDoRepository()):
        self.todo_repository = todo_repository

    def handle(self, command: UpdateTask) -> ToDoList:
        todo_list = self.todo_repository.get(id=command.todo_id)
        todo_list.update_task(task_id=command.task_id, title=command.title, description=command.description)
        return self.todo_repository.update(todo_list)
