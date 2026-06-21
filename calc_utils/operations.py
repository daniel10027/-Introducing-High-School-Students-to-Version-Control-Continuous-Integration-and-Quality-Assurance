"""Core arithmetic operations for calc_utils."""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ValueError: if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the power of exponent."""
    return base ** exponent


def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b.

    Raises:
        ValueError: if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot compute modulo with divisor zero")
    return a % b

def square(n: float) -> float:
    """Return n squared."""
    return n ** 2