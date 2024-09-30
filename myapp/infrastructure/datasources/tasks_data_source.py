from myapp.domain.todo import Task
from myapp.infrastructure.db.database import db_session
from myapp.infrastructure.db.models import TaskDB


class TasksDataSource:
    def get(self):
        db = db_session.get()
        return [
            Task(title=data.title, description=data.description, state=data.state, id=data.id, todo_id=data.todo_id)
            for data in db.query(TaskDB).all()
        ]

    def create(self, item: Task):
        db = db_session.get()
        task_db = TaskDB(title=item.title, description=item.description, state=item.state, todo_id=item.todo_id)
        db.add(task_db)
        db.commit()
        db.refresh(task_db)
        return Task(title=task_db.title, description=task_db.description, state=task_db.state, todo_id=item.todo_id,
                    id=task_db.id)
