from myapp.domain.task import Task, TaskID
from myapp.infrastructure.db.database import db_session
from myapp.infrastructure.db.models import TaskDB


class TasksDataSource:
    def get(self, to_do_id: TaskID):
        db = db_session.get()
        query = db.query(TaskDB).filter(TaskDB.todo_id == to_do_id)
        return [
            Task(title=task_db.title, description=task_db.description, state=task_db.state, id=task_db.id,
                 todo_id=task_db.todo_id)
            for task_db in query.all()
        ]

    def create(self, item: Task):
        db = db_session.get()
        task_db = TaskDB(title=item.title.root, description=item.description, state=item.state, todo_id=item.todo_id)
        db.add(task_db)
        db.commit()
        db.refresh(task_db)
        return Task(title=task_db.title, description=task_db.description, state=task_db.state, todo_id=item.todo_id,
                    id=task_db.id)

    def delete(self, task_id: TaskID):
        db = db_session.get()
        task_to_delete = db.query(TaskDB).filter(TaskDB.id == task_id).first()

        if task_to_delete:
            db.delete(task_to_delete)
            db.commit()

    def update(self, task: Task):
        db = db_session.get()
        task_to_update = db.query(TaskDB).filter(TaskDB.id == task.id).first()

        if task_to_update:
            task_to_update.title = task.title.root
            task_to_update.description = task.description
            task_to_update.state = task.state

            db.commit()
            db.refresh(task_to_update)

            return Task(
                title=task_to_update.title,
                description=task_to_update.description,
                state=task_to_update.state,
                todo_id=task_to_update.todo_id,
                id=task_to_update.id
            )
