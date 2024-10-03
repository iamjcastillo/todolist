import unittest

from myapp.domain.task import TaskFactory
from myapp.domain.title import Title


class TaskTestCase(unittest.TestCase):
    def test_when_creating_task_then_it_is_returned(self):
        task = TaskFactory.create(title="title", description="description", state="state", todo_id=1)

        self.assertEqual(Title("title"), task.title)
        self.assertEqual("description", task.description)
        self.assertEqual("state", task.state)
        self.assertEqual(1, task.todo_id)

    def test_given_task_when_marking_as_completed_then_it_is_marked(self):
        task = TaskFactory.create(title="title", description="description", state="state", todo_id=1)

        task.mark_as_completed()

        self.assertEqual("COMPLETED", task.state)

    def test_given_task_when_updating_title_then_it_is_updated(self):
        task = TaskFactory.create(title="title", description="description", state="state", todo_id=1)
        updated_title = Title("Updated title")

        task.update_title(updated_title)

        self.assertEqual(updated_title, task.title)

    def test_given_task_when_updating_description_then_it_is_updated(self):
        task = TaskFactory.create(title="title", description="description", state="state", todo_id=1)
        updated_description = "updated description"

        task.update_description(updated_description)

        self.assertEqual(updated_description, task.description)