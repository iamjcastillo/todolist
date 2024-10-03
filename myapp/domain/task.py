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

    def mark_as_completed(self):
        self.state = "COMPLETED"

    def update_title(self, title: Title):
        self.title = title


class TaskFactory:
    @staticmethod
    def create(title: Title, description: Description, state: State, todo_id: Optional[ToDoID] = None,
               id: Optional[TaskID] = None) -> 'Task':
        return Task(id=id, title=title, description=description, state=state, todo_id=todo_id)


class TaskCreationRequest(BaseModel):
    title: Title
    description: Description
    state: State
