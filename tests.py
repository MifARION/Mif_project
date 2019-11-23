import unittest

from homework_eleven_mif import *


class MyTestCase(unittest.TestCase):
    def test_search(self):
        expected_value = True
        value = search(0, 1)
        self.assertEqual(expected_value, value)

    def test_search_wall(self):
        expected_value = False
        value = search(1, 2)
        self.assertEqual(expected_value, value)

    def test_search_way(self):
        expected_value = False
        value = search(0, 1)
        self.assertEqual(expected_value, value)




if __name__ == '__main__':
    unittest.main()
