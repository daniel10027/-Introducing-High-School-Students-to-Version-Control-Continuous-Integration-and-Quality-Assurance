"""Unit tests for calc_utils.string_utils."""

from calc_utils.string_utils import is_palindrome, reverse_string, word_count, shout


def test_is_palindrome_true():
    assert is_palindrome("racecar") is True
    assert is_palindrome("Was it a car or a cat I saw?") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""


def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("  one   two three  ") == 3
    assert word_count("") == 0


def test_shout():
    assert shout("hello") == "HELLO!"
