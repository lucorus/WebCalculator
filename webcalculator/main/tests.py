from unittest import TestCase
import operation


class TestDivideNumber(TestCase):
    def test_divide_number(self):
        self.assertEqual(operation.divide_number('42A'), [4, 2, 10])
        self.assertEqual(operation.divide_number(124), [1, 2, 4])
        self.assertEqual(operation.divide_number('ab'), [10, 11])


class TestTranslateToLetters(TestCase):
    def test_translate_to_letters(self):
        self.assertEqual(operation.translate_to_letters([1, 12, 15]), [1, 'C', 'F'])
        self.assertEqual(operation.translate_to_letters([1, 2, 3]), [1, 2, 3])


class TestConvertTo10(TestCase):
    def test_convert_to_10(self):
        self.assertEqual(operation.convert_to_10(8, '100'), 64)
        self.assertEqual(operation.convert_to_10(16, 'AB1'), 2737)
        self.assertEqual(operation.convert_to_10(16, 'ab1'), 'error')


class TestConvertToX(TestCase):
    def test_convert_to_x(self):
        self.assertEqual(operation.convert_to_x(16, 2737), ['A', 'B', 1])
        self.assertEqual(operation.convert_to_x(2, 5), [1, 0, 1])


class TestIsValid(TestCase):
    def test_validation(self):
        self.assertEqual(operation.is_valid('123', 8), True)
        self.assertEqual(operation.is_valid(123, 8), False)
        self.assertEqual(operation.is_valid('43', 2), False)
        self.assertEqual(operation.is_valid('A4', 16), True)
        self.assertEqual(operation.is_valid('a4', 16), False)
        self.assertEqual(operation.is_valid({1: 2, 3: 4}, 16), False)
        self.assertEqual(operation.is_valid('hello world!', 16), False)


class TestConvert(TestCase):
    def test_convert(self):
        self.assertEqual(operation.convertation(2, '101', 10), '5')
        self.assertEqual(operation.convertation(2, 'hello world!', 2), 'error')
        self.assertEqual(operation.convertation(2, 9, 8), 'error')
        self.assertEqual(operation.convertation(2, [1, 4, 5], 10), 'error')


class TestCalculate(TestCase):
    def test_calculate(self):
        self.assertEqual(operation.calculate(105, 10, '0', 10, '*'), 0)
        self.assertEqual(operation.calculate(100, '10', 1, '10', '*'), 'error')
        self.assertEqual(operation.calculate(100, 10, 0, 10, '/'), 'error')
        self.assertEqual(operation.calculate(100, 10, 201, 8, ' '), 'unknown operation')
        self.assertEqual(operation.calculate(100, 10, 201, 8, '+'), 229)
        self.assertEqual(operation.calculate('100', 10, '201', 8, '+'), 229)

