import unittest
from unittest import mock
import copy
from BASIC.Homework5 import main

from parameterized import parameterized


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.documents = copy.deepcopy(main.documents)
        self.directories = copy.deepcopy(main.directories)

    @parameterized.expand([['11-2', 'Геннадий Покемонов'], [10, 'документ №10 не найден']])
    def test_get_people(self, number, result_assert):
        result = main.get_people(number, self.documents)
        self.assertEqual(result, result_assert)

    @parameterized.expand([['11-2', 'документ №11-2 на полке №1'], [100, 'документ №100 не найден']])
    def test_search_document(self, number, result_assert):
        result = main.search_document(number, self.directories)
        self.assertEqual(result, result_assert)

    @parameterized.expand([['11-2', 'документ №11-2 удалён с полки №1'], [100, 'документ №100 не найден']])
    def test_delete_line(self, number, result_assert):
        result = main.delete_line(number, self.documents, self.directories)
        self.assertEqual(result, result_assert)

    @parameterized.expand([['5', 'Добавлено'], ['1', 'Уже есть такая полка']])
    def test_add_shelf(self, number, result_assert):
        result = main.add_shelf(number, self.directories)
        self.assertEqual(result, result_assert)

    @parameterized.expand([[('passport', 'Ivan', '111', '1'), 'Данные добавлены'],
                           [('book', 'Ivan', '111', '1'), 'некорректный тип документа'],
                           [('invoice', 'Ivan', '111', '6'), 'Данные добавлены'],
                           [('', 'Ivan', '111', '2'), 'Введен не полный набор данных'],
                           ])
    def test_add_document(self, input_data, result_assert):
        type_doc, name_person, number, direct = input_data
        with unittest.mock.patch('builtins.input', return_value='y'):
            result = main.add_document(type_doc, name_person, number, direct, self.documents, self.directories)
            self.assertEqual(result, result_assert)


if __name__ == '__main__':
    unittest.main()
