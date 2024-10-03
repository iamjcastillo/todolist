from typing import NewType, List, Optional

from pydantic import BaseModel

from myapp.domain.kernel import ToDoID
from myapp.domain.task import Task, TaskCreationRequest, TaskID

Category = NewType("Category", str)


class ToDoList(BaseModel):
    id: Optional[ToDoID]  # Improvement. Remove nullability
    tasks: List[Task]
    category: Category
    _removed_tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task_id: TaskID):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self._removed_tasks.append(task)
                return

    def get_removed_tasks(self) -> List[Task]:
        return self._removed_tasks


class ToDoListFactory:
    @staticmethod
    def create(category: Category, tasks: Optional[List[Task]] = [], id: Optional[ToDoID] = None) -> 'ToDoList':
        return ToDoList(id=id, category=category, tasks=tasks)


class ToDoListCreationRequest(BaseModel):
    tasks: List[TaskCreationRequest]
    category: Category
