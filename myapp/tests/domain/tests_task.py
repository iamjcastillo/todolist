import unittest

from myapp.domain.task import Task
from myapp.domain.title import Title


class TaskTestCase(unittest.TestCase):
    def test_when_creating_task_then_it_is_returned(self):
        task = Task.create(title="title", description="description", state="state", todo_id=1)

        self.assertEqual(Title("title"), task.title)
        self.assertEqual("description", task.description)
        self.assertEqual("state", task.state)
        self.assertEqual(1, task.todo_id)

    def test_given_task_when_marking_as_completed_then_it_is_marked(self):
        task = Task.create(title="title", description="description", state="state", todo_id=1)

        task.mark_as_completed()

        self.assertEqual("COMPLETED", task.state)
