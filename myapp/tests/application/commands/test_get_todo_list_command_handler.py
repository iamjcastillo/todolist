from unittest import TestCase
from unittest.mock import MagicMock

from myapp.application.commands.command_handler import GetToDoList
from myapp.application.commands.get_todo_list_command_handler import GetToDoListCommandHandler


class TestGetToDoListCommandHandler(TestCase):
    def test_given_command_when_handling_then_repository_called(self):
        repository_mock = MagicMock()
        command = GetToDoList(todo_id=1)

        GetToDoListCommandHandler(repository_mock).handle(command=command)

        repository_mock.get.assert_called_once_with(id=1)
