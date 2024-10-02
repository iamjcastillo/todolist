import unittest

from myapp.domain.task import TaskFactory
from myapp.domain.todo import ToDoListFactory


class ToDoTestCase(unittest.TestCase):
    def test_when_creating_todo_then_it_is_returned(self):
        todo = ToDoListFactory.create(category="test", tasks=[])

        self.assertEqual([], todo.tasks)
        self.assertEqual("test", todo.category)

    def test_given_todo_when_adding_task_then_it_is_added(self):
        todo = ToDoListFactory.create(category="test", tasks=[])
        task = TaskFactory.create(title="title", description="description", state="state", todo_id=1)

        todo.add_task(task=task)

        self.assertEqual(1, len(todo.tasks))
        self.assertEqual(task, todo.tasks[0])
