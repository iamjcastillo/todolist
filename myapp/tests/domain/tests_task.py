import unittest

from myapp.domain.exceptions import TitleTooLongException
from myapp.domain.task import Task


class TaskTestCase(unittest.TestCase):
    def test_when_creating_task_then_it_is_returned(self):
        task = Task.create(title="title", description="description", state="state", todo_id=1)

        self.assertEqual("title", task.title)
        self.assertEqual("description", task.description)
        self.assertEqual("state", task.state)
        self.assertEqual(1, task.todo_id)

    def test_given_task_when_marking_as_completed_then_it_is_marked(self):
        task = Task.create(title="title", description="description", state="state", todo_id=1)

        task.mark_as_completed()

        self.assertEqual("COMPLETED", task.state)

    def test_given_long_title_when_creating_task_then_error_returned(self):
        with self.assertRaises(TitleTooLongException):
            Task.create(
                title="title longer thant 50 characters that should raise an exception",
                description="description",
                state="state",
                todo_id=1,
            )
