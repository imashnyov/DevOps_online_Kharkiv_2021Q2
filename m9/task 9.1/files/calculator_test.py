import unittest
from calculator import Calculator


class CalculatorTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()
    def test_sum_5_and_5_equal_10(self):
        result = self.calc.add(5, 5)
        self.assertEqual(result, 10)

    def test_sum_float(self):
        result = self.calc.add(2.5, 2.5)
        self.assertEqual(result, 5.0)

    def test_subtract_10_adn_3_equal_7(self):
        result = self.calc.subtract(10,3)
        self.assertEqual(result, 7)

    def test_multiply_2_and_5_equal_10(self):
        result = self.calc.multiply(2, 5)
        self.assertEqual(result, 10)

    def test_divide_10_by_2_equal_5(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_0_by_2_equal_0(self):
        result = self.calc.divide(0, 2)
        self.assertEqual(result, 0)

    def test_division_by_zero_error(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()