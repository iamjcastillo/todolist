from myapp.domain.task import Task
from myapp.domain.todo import ToDoList, ToDoListFactory
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
        return self._delete_tasks(todo)

    def _delete_tasks(self, todo: ToDoList) -> ToDoList:
        stored_tasks = self.task_data_source.get(to_do_id=todo.id)
        stored_tasks_id = {task.id for task in stored_tasks}
        task_ids = {task.id for task in todo.tasks}
        task_ids_to_delete = stored_tasks_id - task_ids

        for task_id in task_ids_to_delete:
            self.task_data_source.delete(task_id)

        return todo
