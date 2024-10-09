from unittest import TestCase
from unittest.mock import MagicMock

from myapp.application.commands.command_handler import DeleteTask
from myapp.application.commands.delete_task_command_handler import DeleteTaskCommandHandler
from myapp.domain.task import TaskFactory
from myapp.domain.todo import ToDoListFactory


class TestDeleteTaskCommandHandler(TestCase):
    def test_given_command_when_handling_then_repository_called(self):
        todo = ToDoListFactory.create(category="test", tasks=[], id=1)
        task = TaskFactory.create(title="title", description="description", state="state", todo_id=1, id=2)
        todo.add_task(task=task)
        repository_mock = MagicMock()
        repository_mock.get.return_value = todo
        command = DeleteTask(todo_id=1, task_id=2)

        DeleteTaskCommandHandler(repository_mock).handle(command=command)

        repository_mock.update.assert_called()
