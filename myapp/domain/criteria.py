from pydantic import BaseModel


class Criteria(BaseModel):
    ...


class ToDoCriteria(Criteria):
    ...


class ToDoListWithTasksCriteria(Criteria):
    ...
