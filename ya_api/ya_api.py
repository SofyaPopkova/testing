import unittest
import support_ya


class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def test_1_success(self):
        self.assertEqual(support_ya.create_folder('folder_1'), 201)

    def test_2_failure(self):
        self.assertEqual(support_ya.create_folder('folder_2'), 404)

    def test_3_failure(self):
        self.assertEqual(support_ya.create_folder('folder_3'), 401)

    def test_4_success_deletion(self):
        self.assertEqual(support_ya.delete_folder('folder_3'), 204)

    def tearDown(self):
        support_ya.delete_folder('folder_1')
        support_ya.delete_folder('folder_2')
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()
