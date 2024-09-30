from myapp.domain.todo import ToDoList
from myapp.infrastructure.db.database import db_session
from myapp.infrastructure.db.models import ToDoDB


class ToDoDataSource:  # Improvement. Use DTOs instead of domain objects
    def get(self) -> ToDoList:
        db = db_session.get()
        return [ToDoList(id=i.id, category=i.category, tasks=[]) for i in db.query(ToDoDB).all()]

    def create(self, todo: ToDoDB) -> ToDoList:
        db = db_session.get()
        todo_db = ToDoDB(category=todo.category)
        db.add(todo_db)
        db.commit()
        db.refresh(todo_db)
        return ToDoList(id=todo_db.id, category=todo_db.category, tasks=[])
