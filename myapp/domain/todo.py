from typing import NewType, List, Optional

from pydantic import BaseModel

from myapp.domain.exceptions import TitleTooLongException

Title = NewType("Title", str)  # This could be a class with a create method
Description = NewType("Description", str)
State = NewType("State", str)
TaskID = NewType("TaskID", int)
Category = NewType("Category", str)
ToDoID = NewType("ToDoId", int)


# class State(Enum):
#    PENDING: "PENDING"
#    COMPLETED: "COMPLETED"


class Task(BaseModel):
    id: Optional[TaskID]
    title: Title  # Improvement check length
    description: Description
    state: State  # Improvement: Use enum
    todo_id: Optional[ToDoID]

    @classmethod
    def create(cls, title: Title, description: Description, state: State, todo_id: ToDoID) -> 'Task':
        if len(title) > 50:  # This can be done using pydantic model_validator decorator
            raise TitleTooLongException()
        return cls(id=None, title=title, description=description, state=state, todo_id=todo_id)

    def mark_as_completed(self):
        self.state = "COMPLETED"  # Improvement. Use enum here


class ToDoList(BaseModel):
    id: Optional[ToDoID]  # Improvement. Remove nullability
    tasks: List[Task]
    category: Category

    @classmethod
    def create(cls, category: Category) -> 'ToDoList':
        return cls(id=None, category=category, tasks=[])

    def add_task(self, task: Task):
        self.tasks.append(task)


class TaskCreationRequest(BaseModel):
    title: Title  # Improvement check length
    description: Description
    state: State  # Improvement: Use enum


class ToDoListCreationRequest(BaseModel):
    tasks: List[TaskCreationRequest]
    category: Category
