import unittest

from myapp.domain.exceptions import TitleTooLongException
from myapp.domain.title import Title


class TitleTestCase(unittest.TestCase):

    def test_given_long_title_when_creating_then_error_returned(self):
        with self.assertRaises(TitleTooLongException):
            Title("title longer thant 50 characters that should raise an exception")

    def test_given_title_when_creating_then_it_is_returned(self):
        title = Title("testing")

        self.assertIsInstance(title, Title)
        self.assertEqual("testing", title.root)
