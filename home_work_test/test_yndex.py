import unittest
import user_service

class TestApiYa(unittest.TestCase):
    def setUp(self):
        print('method setUp')

    def test_create_folder(self):
        self.assertEqual(user_service.create_folder('test'), 201)

    def test_delete_folder(self):
        self.assertTrue(user_service.delete_folder('test')

    def tearDown(self):
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()