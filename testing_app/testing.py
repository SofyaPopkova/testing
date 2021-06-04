import unittest
import app


class Testing(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_get_doc_owner_name(self):
        self.assertEqual(app.get_doc_owner_name('11-2'), 'Геннадий Покемонов')

    def test_add_new_doc(self):
        self.assertEqual(app.add_new_doc('3335', 'VAT', 'Софья', 1), str(1))

    def test_delete_doc(self):
        self.assertTrue(app.delete_doc('10006'))


if __name__ == '__main__':
    unittest.main()
