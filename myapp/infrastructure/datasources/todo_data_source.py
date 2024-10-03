from myapp.domain.exceptions import ToDoListNotFoundException
from myapp.domain.kernel import ToDoID
from myapp.domain.todo import ToDoList, ToDoListFactory
from myapp.infrastructure.db.database import db_session
from myapp.infrastructure.db.models import ToDoDB


class ToDoDataSource:  # Improvement. Use DTOs instead of domain objects
    def get(self, id: ToDoID) -> ToDoList:
        db = db_session.get()
        query = db.query(ToDoDB).filter(ToDoDB.id == id)
        todo = query.one_or_none()
        if not todo:
            raise ToDoListNotFoundException()
        return ToDoListFactory.create(id=todo.id, category=todo.category)

    def create(self, todo: ToDoDB) -> ToDoList:
        db = db_session.get()
        todo_db = ToDoDB(category=todo.category)
        db.add(todo_db)
        db.commit()
        db.refresh(todo_db)
        return ToDoList(id=todo_db.id, category=todo_db.category, tasks=[])
