from myapp.domain.task import Task
from myapp.domain.todo import ToDoList, ToDoListFactory
from myapp.infrastructure.datasources.tasks_data_source import TasksDataSource
from myapp.infrastructure.datasources.todo_data_source import ToDoDataSource


class ToDoRepository:
    def __init__(self, todo_data_source=ToDoDataSource(), task_data_source=TasksDataSource()):
        self.todo_data_source = todo_data_source
        self.task_data_source = task_data_source

    def create(self, todo: ToDoList) -> ToDoList:
        saved_todo = self.todo_data_source.create(todo)
        saved_tasks = [
            self.task_data_source.create(
                Task(id=task.id, todo_id=saved_todo.id, title=task.title, description=task.description,
                     state=task.state)
            )
            for task in todo.tasks
        ]

        return ToDoList(id=saved_todo.id, category=saved_todo.category, tasks=saved_tasks)

    def get(self, id) -> ToDoList:
        todo = self.todo_data_source.get(id=id)
        tasks = self.task_data_source.get(to_do_id=id)
        return ToDoListFactory.create(id=todo.id, category=todo.category, tasks=tasks)

    def update(self, todo: ToDoList) -> ToDoList:
        self._delete_tasks(todo)
        self._update_tasks(todo)
        return self.get(todo.id)

    def _delete_tasks(self, todo: ToDoList):
        tasks_to_delete = todo.get_removed_tasks()
        for task in tasks_to_delete:
            self.task_data_source.delete(task_id=task.id)

    def _update_tasks(self, todo: ToDoList):
        tasks_to_update = todo.get_updated_tasks()
        for task in tasks_to_update:
            self.task_data_source.update(task)
