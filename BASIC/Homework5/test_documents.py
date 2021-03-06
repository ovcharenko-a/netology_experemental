import unittest
from unittest import mock
import copy
from BASIC.Homework5 import main

from parameterized import parameterized


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.documents = copy.deepcopy(main.documents)
        self.directories = copy.deepcopy(main.directories)

    @parameterized.expand([['correct_data', '11-2', 'Геннадий Покемонов'],
                           ['incorrect_data', '10', 'документ №10 не найден']])
    def test_get_people(self, name_, number, result_assert):
        result = main.get_people(number, self.documents)
        self.assertEqual(result, result_assert)

    @parameterized.expand([['correct_data', '11-2', 'документ №11-2 на полке №1'],
                           ['incorrect_data', '100', 'документ №100 не найден']])
    def test_search_document(self, name_, number, result_assert):
        result = main.search_document(number, self.directories)
        self.assertEqual(result, result_assert)

    @parameterized.expand([['correct_data', '11-2', 'документ №11-2 удалён с полки №1'],
                           ['incorrect_data', '100', 'документ №100 не найден']])
    def test_delete_line(self, name_, number, result_assert):
        result = main.delete_line(number, self.documents, self.directories)
        self.assertEqual(result, result_assert)

    @parameterized.expand([['correct_data', '5', 'Добавлено'],
                           ['incorrect_data', '1', 'Уже есть такая полка']])
    def test_add_shelf(self, name_, number, result_assert):
        result = main.add_shelf(number, self.directories)
        self.assertEqual(result, result_assert)

    @parameterized.expand([['correct_data', ('passport', 'Ivan', '111', '1'), 'Данные добавлены'],
                           ['incorrect_document_type', ('book', 'Ivan', '111', '1'), 'некорректный тип документа'],
                           ['correct_data_with_new_shelf', ('invoice', 'Ivan', '111', '6'), 'Данные добавлены'],
                           ['incorrect_dataset', ('', 'Ivan', '111', '2'), 'Введен не полный набор данных'],
                           ])
    def test_add_document(self, name_, input_data, result_assert):
        type_doc, name_person, number, direct = input_data
        with unittest.mock.patch('builtins.input', return_value='y'):
            result = main.add_document(type_doc, name_person, number, direct, self.documents, self.directories)
            self.assertEqual(result, result_assert)


if __name__ == '__main__':
    unittest.main()
