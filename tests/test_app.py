import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

import math
import pytest

from app import (
    add,
    subtract,
    multiply,
    divide,
    square,
    sqrt,
    sin,
    cos,
    log,
    percentage,
)


def test_add():
    assert add(5, 6) == 11


def test_add2():
    assert add(5, 6) != 10


def test_subtract():
    assert subtract(10, 3) == 7


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_square():
    assert square(3) == 9


def test_sqrt():
    assert sqrt(9) == 3


def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-1)


def test_sin_cos():
    assert sin(math.pi / 2) == pytest.approx(1.0)
    assert cos(0) == pytest.approx(1.0)


def test_log():
    assert log(math.e) == pytest.approx(1.0)


def test_log_invalid():
    with pytest.raises(ValueError):
        log(0)
    with pytest.raises(ValueError):
        log(-1)


def test_percentage():
    assert percentage(50, 200) == 25


def test_percentage_zero_whole():
    with pytest.raises(ValueError):
        percentage(1, 0)


def test_non_numeric_inputs_raise_typeerror():
    with pytest.raises(TypeError):
        add("a", 1)
    with pytest.raises(TypeError):
        subtract(1, "b")


def test_log_with_base_10_and_invalid_bases():
    assert log(100, 10) == pytest.approx(2.0)
    with pytest.raises(ValueError):
        log(10, 1)
    with pytest.raises(ValueError):
        log(10, 0)


def test_percentage_negative_values():
    # percentage should handle negative numbers
    assert percentage(-50, 200) == -25


def test_trigonometric_non_numeric():
    with pytest.raises(TypeError):
        sin("x")
    with pytest.raises(TypeError):
        cos(None)