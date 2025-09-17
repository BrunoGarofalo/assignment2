from app.operations import addition, division, multiplication, subtraction
import pytest

def test_addition():
    assert addition(1, 1) == 2
    assert addition(5, 4) == 9

def test_subtraction():
    assert subtraction(3, 1) == 2
    assert subtraction(2, 2) == 0

def test_division_positive():
    assert division(4, 4) == 1
    assert division(3, 1) == 3

def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)

def test_division_negative():
    assert division(6, -3) == -2
    assert division(-6, 3) == -2

def test_multiplication():
    assert multiplication(3, 1) == 3
    assert multiplication(2, 2) ==4
