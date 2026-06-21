"""calc_utils: a small calculator and utility library.

A learning project for practicing Git, CI, and QA workflows.
"""

from .operations import add, subtract, multiply, divide, power, modulo, sqaure
from .string_utils import is_palindrome, reverse_string, word_count, shout

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "modulo",
    "sqaure",
    "is_palindrome",
    "reverse_string",
    "word_count",
    "shout",

]
__version__ = "0.2.0"
