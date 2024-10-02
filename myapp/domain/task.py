from typing import Optional, NewType

from pydantic import BaseModel

from myapp.domain.exceptions import TitleTooLongException
from myapp.domain.todo import ToDoID

Title = NewType("Title", str)
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
        if len(title) > 50:  # This can be done using pydantic model_validator decorator
            raise TitleTooLongException()
        return cls(id=None, title=title, description=description, state=state, todo_id=todo_id)

    def mark_as_completed(self):
        self.state = "COMPLETED"


class TaskCreationRequest(BaseModel):
    title: Title
    description: Description
    state: State
