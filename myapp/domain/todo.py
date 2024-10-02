from typing import NewType, List, Optional

from pydantic import BaseModel

from myapp.domain.kernel import ToDoID
from myapp.domain.task import Task, TaskCreationRequest

Category = NewType("Category", str)


class ToDoList(BaseModel):
    id: Optional[ToDoID]  # Improvement. Remove nullability
    tasks: List[Task]
    category: Category

    @classmethod
    def create(cls, category: Category) -> 'ToDoList':
        return cls(id=None, category=category, tasks=[])

    def add_task(self, task: Task):
        self.tasks.append(task)


class ToDoListCreationRequest(BaseModel):
    tasks: List[TaskCreationRequest]
    category: Category
