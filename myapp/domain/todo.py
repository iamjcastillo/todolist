from typing import NewType, List, Optional

from pydantic import BaseModel

from myapp.domain.kernel import ToDoID
from myapp.domain.task import Task, TaskID, Description
from myapp.domain.title import Title

Category = NewType("Category", str)


class ToDoList(BaseModel):
    id: Optional[ToDoID]  # Improvement. Remove nullability
    tasks: List[Task]
    category: Category
    __removed_tasks: List[Task] = []
    __updated_tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task_id: TaskID):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.__removed_tasks.append(task)
                return

    def get_removed_tasks(self) -> List[Task]:
        return self.__removed_tasks

    def get_task(self, task_id: TaskID):
        for task in self.tasks:
            if task.id == task_id:
                return task

    def update_task(self, task_id: TaskID, title: Title, description: Description):
        task = self.get_task(task_id=task_id)
        task.update_title(title)
        task.update_description(description)
        self.__updated_tasks.append(task)

    def get_updated_tasks(self) -> List[Task]:
        return self.__updated_tasks


class ToDoListFactory:
    @staticmethod
    def create(category: Category, tasks: Optional[List[Task]] = [], id: Optional[ToDoID] = None) -> 'ToDoList':
        return ToDoList(id=id, category=category, tasks=tasks)
