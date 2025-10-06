"""
Unit tests for calculator module.
"""
import pytest
import sys
import os

from calculator import add, subtract, multiply, divide, power

def test_add_positive_numbers():
    """Test adding two positive numbers."""
    result = add(5, 3)
    assert result == 8

def test_subtract_numbers():
    """Test subtracting two numbers."""
    result = subtract(10, 4)
    assert result == 6

def test_multiply_numbers():
    """Test multiplying two numbers."""
    result = multiply(6, 7)
    assert result == 42

def test_divide_numbers():
    """Test dividing two numbers."""
    result = divide(15, 3)
    assert result == 5.0

def test_power_calculation():
    """Test raising a number to a power."""
    result = power(2, 3)
    assert result == 8

def test_divide_by_zero_raises_error():
    """Test that dividing by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_add_negative_numbers():
    """Test adding negative numbers."""
    result = add(-5, -3)
    assert result == -8

def test_subtract_negative_result():
    """Test subtraction resulting in negative number."""
    result = subtract(3, 7)
    assert result == -4