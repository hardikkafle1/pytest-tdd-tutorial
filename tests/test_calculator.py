import pytest
from src.calculator import Calculator

class TestCalculator:

    def test_add_two_positive_numbers(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5

    def test_add_negative_numbers(self):
        calc = Calculator()
        assert calc.add(-2, -3) == -5

    def test_subtract_numbers(self):
        calc = Calculator()
        assert calc.subtract(5, 3) == 2

    def test_multiply_numbers(self):
        calc = Calculator()
        assert calc.multiply(4, 3) == 12

    def test_divide_numbers(self):
        calc = Calculator()
        assert calc.divide(10, 2) == 5.0

    def test_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.divide(10, 0)