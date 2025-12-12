import math


def _to_number(x):
    try:
        return float(x)
    except Exception:
        raise TypeError(f"Value {x!r} is not a number")


def add(a, b):
    a = _to_number(a)
    b = _to_number(b)
    return a + b


def subtract(a, b):
    a = _to_number(a)
    b = _to_number(b)
    return a - b


def multiply(a, b):
    a = _to_number(a)
    b = _to_number(b)
    return a * b


def divide(a, b):
    a = _to_number(a)
    b = _to_number(b)
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b


def square(x):
    x = _to_number(x)
    return x * x


def sqrt(x):
    x = _to_number(x)
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)


def sin(x):
    x = _to_number(x)
    return math.sin(x)


def cos(x):
    x = _to_number(x)
    return math.cos(x)


def log(x, base=math.e):
    x = _to_number(x)
    base = _to_number(base)
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    if base <= 0 or base == 1:
        raise ValueError("Invalid log base")
    return math.log(x, base)


def percentage(part, whole):
    part = _to_number(part)
    whole = _to_number(whole)
    if whole == 0:
        raise ValueError("Whole (denominator) cannot be zero for percentage calculation")
    return (part / whole) * 100.0