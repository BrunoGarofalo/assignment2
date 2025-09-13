from app.operations import addition, division, multiplication, subtraction
import pytest

def test_addition():
    assert addition(1, 1) == 2

def test_subtraction():
    assert subtraction(3, 1) == 2

def test_division_positive():
    assert division(4, 4) == 1

def test_division_negative():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)

def test_multiplication():
    assert multiplication(3, 1) == 3