import unittest
from home_work_test.Hw_test import add_new_doc, delete_doc, check_document_existance


class TestFunction(unittest.TestCase):
    def test_add_foo(self):
        self.assertEquals(add_new_doc(15, 'важный', 'Олежка', 14), 14)

    def test_del_foo(self):
        self.assertTrue(delete_doc('10006'))

    def test_check_find_foo(self):
        self.assertTrue(check_document_existance('11-2'))
