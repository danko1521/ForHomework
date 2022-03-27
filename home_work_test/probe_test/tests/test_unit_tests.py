import unittest
from main import multiplication_int, multiplication_string


class TestFunctions(unittest.TestCase):
    def test_multiplication_int(self):
        self.assertEquals(multiplication_int(2, 3), 6)

    @unittest.skipIf(multiplication_int(1, 1), 'нам это не интересно')
    def test_multiplication_int_skipIf(self):
        self.assertEquals(multiplication_int(2, 3), 6)

    @unittest.expectedFailure
    def test_multiplication_int_expectedFailure(self):
        self.assertEquals(multiplication_int(2, 2), 5)
