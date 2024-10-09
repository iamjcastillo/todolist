from unittest import TestCase
from unittest.mock import MagicMock

from myapp.application.commands.command_handler import UpdateTask
from myapp.application.commands.update_task_command_handler import UpdateTaskCommandHandler
from myapp.domain.task import TaskFactory
from myapp.domain.title import Title
from myapp.domain.todo import ToDoListFactory


class TestUpdateTaskCommandHandler(TestCase):
    def test_given_command_when_handling_then_repository_called(self):
        todo = ToDoListFactory.create(category="test", tasks=[], id=1)
        task = TaskFactory.create(title="title", description="description", state="state", todo_id=1, id=2)
        todo.add_task(task=task)
        repository_mock = MagicMock()
        repository_mock.get.return_value = todo
        command = UpdateTask(todo_id=1, task_id=2, title=Title("Title"), description="description")

        UpdateTaskCommandHandler(repository_mock).handle(command=command)

        repository_mock.update.assert_called()
