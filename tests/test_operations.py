"""Unit tests for calc_utils.operations."""

import pytest

from calc_utils.operations import add, subtract, multiply, divide, power, modulo


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-2, -3) == -5


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(9, 3) == 0


def test_modulo_by_zero_raises():
    with pytest.raises(ValueError):
        modulo(10, 0)
