import unittest
from home_work_test.Hw_test import add_new_doc, delete_doc


class TestFunction(unittest.TestCase):
    def test_add_foo(self):
        self.assertEquals(add_new_doc())