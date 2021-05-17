import unittest
from unittest import mock
import copy
from BASIC.Homework5 import main

from parameterized import parameterized


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.documents = copy.deepcopy(main.documents)
        self.directories = main.directories.copy()

    @parameterized.expand([['11-2', 'Геннадий Покемонов'], [10, 'документ №10 не найден']])
    def test_get_people(self, number, result_assert):
        result = main.get_people(number, self.documents)
        self.assertEqual(result, result_assert)

    @parameterized.expand([['11-2', 'документ №11-2 на полке №1'], [100, 'документ №100 не найден']])
    def test_search_document(self, number, result_assert):
        result = main.search_document(number, self.directories)
        self.assertEqual(result, result_assert)

if __name__ == '__main__':
    unittest.main()

    # with unittest.mock.patch('builtins.input', return_value='y'):
    #     y = input()
    #     self.assertEqual(y, "y")
