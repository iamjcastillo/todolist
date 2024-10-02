from myapp.domain.criteria import Criteria
from myapp.domain.task import TaskFactory
from myapp.domain.todo import ToDoList, ToDoListCreationRequest, ToDoListFactory
from myapp.infrastructure.repositories.to_do_repository import ToDoRepository


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

    def get(self, criteria: Criteria) -> ToDoList:
        return self.todo_repository.get(criteria)
