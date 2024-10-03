from myapp.application.commands.command_handler import CreateToDoList
from myapp.domain.task import TaskFactory
from myapp.domain.todo import ToDoList, ToDoListFactory
from myapp.infrastructure.repositories.to_do_repository import ToDoRepository


class CreateToDoListCommandHandler:
    def __init__(self, todo_repository=ToDoRepository()):
        self.todo_repository = todo_repository

    def handle(self, command: CreateToDoList) -> ToDoList:
        todo_list = ToDoListFactory.create(category=command.category)

        for task_data in command.tasks:
            task = TaskFactory.create(
                title=task_data.title,
                description=task_data.description,
                state=task_data.state,
                todo_id=todo_list.id,
            )
            todo_list.add_task(task)

        return self.todo_repository.create(todo_list)
