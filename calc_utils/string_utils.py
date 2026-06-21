"""String utility functions for calc_utils."""

import re


def is_palindrome(text: str) -> bool:
    """Return True if text is a palindrome, ignoring case and non-letters."""
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


def reverse_string(text: str) -> str:
    """Return the reverse of text."""
    return text[::-1]


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


def shout(text: str) -> str:
    """Return text in uppercase with an exclamation mark appended."""
    return text.upper() + "!"
