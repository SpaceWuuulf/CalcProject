import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 5, 4) == 9

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 9) == 1

    def test_division_success(self):
        assert self.calc.division(self, 99, 9) == 11

    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 2) == 6