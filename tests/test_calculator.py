import pytest
from calculator import Calculator

# Test Addition
def test_add():
    calc = Calculator()
    result = calc.add(5, 10)
    assert result == 15, f"Expected 15, but got {result}"

# Test Subtraction
def test_subtract():
    calc = Calculator()
    result = calc.subtract(10, 5)
    assert result == 5, f"Expected 5, but got {result}"

# Test Multiplication
def test_multiply():
    calc = Calculator()
    result = calc.multiply(5, 10)
    assert result == 50, f"Expected 50, but got {result}"

# Test Division
def test_divide():
    calc = Calculator()
    result = calc.divide(20, 4)
    assert result == 5.0, f"Expected 5.0, but got {result}"

    # Division by zero test
    with pytest.raises(ValueError):
        calc.divide(10, 0)
