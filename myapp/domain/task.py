from typing import Optional, NewType

from pydantic import BaseModel

from myapp.domain.kernel import ToDoID
from myapp.domain.title import Title

Description = NewType("Description", str)
State = NewType("State", str)
TaskID = NewType("TaskID", int)


class Task(BaseModel):
    id: Optional[TaskID]
    title: Title
    description: Description
    state: State
    todo_id: Optional[ToDoID]

    @classmethod
    def create(cls, title: Title, description: Description, state: State, todo_id: ToDoID) -> 'Task':
        return cls(id=None, title=title, description=description, state=state, todo_id=todo_id)

    def mark_as_completed(self):
        self.state = "COMPLETED"


class TaskCreationRequest(BaseModel):
    title: Title
    description: Description
    state: State
