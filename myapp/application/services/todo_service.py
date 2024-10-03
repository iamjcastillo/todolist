from pydantic import BaseModel

from myapp.domain.kernel import ToDoID
from myapp.domain.task import TaskFactory, TaskID
from myapp.domain.todo import ToDoList, ToDoListCreationRequest, ToDoListFactory
from myapp.infrastructure.repositories.to_do_repository import ToDoRepository


class command(BaseModel):
    ...


class DeleteTask(command):
    todo_id: ToDoID
    task_id: TaskID


class ToDoService:
    def __init__(self):
        self.todo_repository = ToDoRepository()

    def create(self, request: ToDoListCreationRequest) -> ToDoList:
        todo_list = ToDoListFactory.create(category=request.category)

        for task_data in request.tasks:
            task = TaskFactory.create(
                title=task_data.title,
                description=task_data.description,
                state=task_data.state,
                todo_id=todo_list.id,
            )
            todo_list.add_task(task)

        return self.todo_repository.create(todo_list)

    def get(self, id: ToDoID) -> ToDoList:
        return self.todo_repository.get(id=id)

    def execute(self, request: command) -> ToDoList:
        if isinstance(request, DeleteTask):
            todo_list = self.todo_repository.get(id=request.todo_id)
            todo_list.remove_task(task_id=request.task_id)
            return self.todo_repository.update(todo_list)
