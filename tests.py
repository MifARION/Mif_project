import unittest

from homework_eleven_mif import *


class MyTestCase(unittest.TestCase):
    def test_search_finish(self):
        expected_value = True
        value = search(8, 8)
        self.assertEqual(expected_value, value)

    def test_search_wall(self):
        expected_value = False
        value = search(1, 1)
        self.assertEqual(expected_value, value)

    def test_search_way(self):
        expected_value = False
        value = search(0, 1)
        self.assertEqual(expected_value, value)

    def test_if_way(self):
        expected_value = False
        value = search(0 + 1, 1)
        self.assertEqual(expected_value, value)

    def test_or_way(self):
        expected_value = False
        value = (1 > 0 and search(2, 3 - 1))
        self.assertEqual(expected_value, value)

    def test_or_way_two(self):
        expected_value = False
        value = (1 > 0 and search(2 - 1, 3))
        self.assertEqual(expected_value, value)

    def test_or_way_three(self):
        expected_value = False
        value = (2 < len(labyrinth) - 1 and search(2, 2 + 1))
        self.assertEqual(expected_value, value)


if __name__ == '__main__':
    unittest.main()
