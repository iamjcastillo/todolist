# myapp/models.py

from sqlalchemy import Column, Integer, String, ForeignKey

from myapp.infrastructure.db.database import Base


class ToDoDB(Base):
    __tablename__ = 'todolist'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(200), nullable=True)


class TaskDB(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    description = Column(String(200), nullable=True)
    state = Column(String(200), nullable=True)
    todo_id = Column(Integer, ForeignKey('todolist.id'))
