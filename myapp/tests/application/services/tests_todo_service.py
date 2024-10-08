import unittest
from unittest.mock import MagicMock

from myapp.application.commands.command_handler import Command
from myapp.application.services.todo_service import ToDoService


class ToDoServiceTestCase(unittest.TestCase):
    def test_given_command_when_executing_then_handler_called(self):
        factory_mock = MagicMock()
        handler_mock = MagicMock()
        factory_mock.get_handler.return_value = handler_mock
        service = ToDoService(factory_mock)
        command = Command()

        service.execute(command=command)

        self.assertTrue(handler_mock.handle.called)
        handler_mock.handle.assert_called_once_with(command)