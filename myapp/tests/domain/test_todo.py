import unittest

from myapp.domain.exceptions import TitleTooLongException
from myapp.domain.todo import ToDoList, Task


class ToDoTestCase(unittest.TestCase):
    def test_when_creating_todo_then_it_is_returned(self):
        todo = ToDoList.create(category="test")

        self.assertEqual([], todo.tasks)
        self.assertEqual("test", todo.category)

    def test_when_creating_task_then_it_is_returned(self):
        task = Task.create(title="title", description="description", state="state", todo_id=1)

        self.assertEqual("title", task.title)
        self.assertEqual("description", task.description)
        self.assertEqual("state", task.state)
        self.assertEqual(1, task.todo_id)

    def test_given_todo_when_adding_task_then_it_is_added(self):
        todo = ToDoList.create(category="test")
        task = Task.create(title="title", description="description", state="state", todo_id=1)

        todo.add_task(task=task)

        self.assertEqual(1, len(todo.tasks))
        self.assertEqual(task, todo.tasks[0])

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
