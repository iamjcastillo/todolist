from myapp.application.commands.command_handler import CreateTask
from myapp.domain.task import TaskFactory
from myapp.domain.todo import ToDoList
from myapp.infrastructure.repositories.to_do_repository import ToDoRepository

class CreateTaskCommandHandler:
    def __init__(self, todo_repository=ToDoRepository()):
        self.todo_repository = todo_repository

    def handle(self, command: CreateTask) -> ToDoList:
        todo_list = self.todo_repository.get(id=command.todo_id)
        
        task = TaskFactory.create(
            title=command.task.title,
            description=command.task.description,
            state=command.task.state,
            todo_id=todo_list.id
        )
        
        todo_list.add_task(task)
        return self.todo_repository.create(todo_list)
