from myapp.domain.criteria import Criteria, ToDoCriteria
from myapp.domain.todo import ToDoList
from myapp.domain.task import Task
from myapp.infrastructure.datasources.tasks_data_source import TasksDataSource
from myapp.infrastructure.datasources.todo_data_source import ToDoDataSource


class ToDoRepository:
    def __init__(self):
        self.todo_data_source = ToDoDataSource()
        self.task_data_source = TasksDataSource()

    def create(self, todo: ToDoList) -> ToDoList:
        saved_todo = self.todo_data_source.create(todo)
        saved_tasks = [
            self.task_data_source.create(
                Task(id=task.id, todo_id=saved_todo.id, title=task.title, description=task.description, state=task.state)
            )
            for task in todo.tasks
        ]

        return ToDoList(id=saved_todo.id, category=saved_todo.category, tasks=saved_tasks)

    def get(self, criteria: Criteria) -> ToDoList:
        if isinstance(criteria, ToDoCriteria):
            return self.todo_data_source.get()
        else:
            raise NotImplementedError()
