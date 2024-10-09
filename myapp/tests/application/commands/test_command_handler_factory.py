import unittest

from myapp.application.commands.command_handler import DeleteTask, GetToDoList, CreateToDoList, UpdateTask
from myapp.application.commands.command_handler_factory import CommandHandlerFactory
from myapp.application.commands.create_todo_list_command_handler import CreateToDoListCommandHandler
from myapp.application.commands.delete_task_command_handler import DeleteTaskCommandHandler
from myapp.application.commands.get_todo_list_command_handler import GetToDoListCommandHandler
from myapp.application.commands.update_task_command_handler import UpdateTaskCommandHandler
from myapp.domain.title import Title


class CommandHandlerFactoryTestCase(unittest.TestCase):
    def test_given_delete_task_command_when_getting_handler_then_it_is_returned(self):
        command = DeleteTask(todo_id=1, task_id=1)

        handler = CommandHandlerFactory().get_handler(command=command)

        self.assertTrue(isinstance(handler, DeleteTaskCommandHandler))

    def test_given_get_to_do_command_when_getting_handler_then_it_is_returned(self):
        command = GetToDoList(todo_id=1)

        handler = CommandHandlerFactory().get_handler(command=command)

        self.assertTrue(isinstance(handler, GetToDoListCommandHandler))

    def test_given_create_to_do_command_when_getting_handler_then_it_is_returned(self):
        command = CreateToDoList(tasks=[], category="Testing")

        handler = CommandHandlerFactory().get_handler(command=command)

        self.assertTrue(isinstance(handler, CreateToDoListCommandHandler))

    def test_given_update_task_command_when_getting_handler_then_it_is_returned(self):
        command = UpdateTask(todo_id=1, task_id=1, title=Title("Testing"), description="Description")

        handler = CommandHandlerFactory().get_handler(command=command)

        self.assertTrue(isinstance(handler, UpdateTaskCommandHandler))
