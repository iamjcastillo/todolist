from unittest import TestCase
from unittest.mock import MagicMock

from myapp.application.commands.command_handler import CreateToDoList
from myapp.application.commands.create_todo_list_command_handler import CreateToDoListCommandHandler


class TestCreateToDoListCommandHandler(TestCase):
    def test_given_command_when_handling_then_repository_called(self):
        repository_mock = MagicMock()
        command = CreateToDoList(category="category", tasks=[])

        CreateToDoListCommandHandler(repository_mock).handle(command=command)

        repository_mock.create.assert_called()
