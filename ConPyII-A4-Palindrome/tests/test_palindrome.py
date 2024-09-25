"""
test_palindrome.py

Python Development II - Assignment 4 (Palindrome)

Matthew Cunningham

Originally submitted June 25th, 2024
Modified and resubmitted June 27th, 2024
"""


import sys
import os
import pytest


def import_palindrome():
    """
    Had to use this work around to import palindrome,
    as it couldn't find it without appending the parent directory to the path.
    Then, flake8 flagged it for not being a top level import, so I had to use
    the below if statement to prevent it from flagging it.
    """
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
    sys.path.append(PARENT_DIR)

    if 'palindrome.is_palindrome' not in sys.modules:
        from palindrome import is_palindrome as is_pal
        return is_pal


is_pal = import_palindrome()


"""
Step 1:
is_palindrome raises a ValueError when not provided
with a value that is an instance of str.
"""


def test_not_str():
    """
    Asserts a pytest that the argument of is_pal
    raises a ValueError if not a string
    """
    with pytest.raises(ValueError):
        is_pal(123)
        is_pal(True)
        is_pal(123.0)
        is_pal(None)


"""
Step 2:
is_palindrome returns False when called with an empty string.
"""


def test_empty_string():
    """
    Asserts a pytest that is_pal returns False
    when passed an empty string
    """
    assert is_pal("") is False


"""
Step 3:
is_palindrome returns True if called with "a"
"""


def test_a():
    """
    Asserts a pytest that is_pal returns True
    when passed the string "a"
    """
    assert is_pal("a") is True


"""
Step 4:
is_palindrome returns True if called with "bb".
"""


def test_bb():
    """
    Asserts a pytest that is_pal returns True
    when passed the string "bb"
    """
    assert is_pal("bb") is True


"""
Step 5:
is_palindrome returns False if called with "abc".
"""


def test_abc():
    """
    Asserts a pytest that is_pal returns False
    when passed the string "abc"
    """
    assert is_pal("abc") is False


"""
Step 6:
is_palindrome returns True when called with "laval".
"""


def test_laval():
    """
    Asserts a pytest that is_pal returns True
    when passed the string "laval"
    """
    assert is_pal("laval") is True


"""
Step 7:
is_palindrome returns False when called with "toronto".
"""


def test_toronto():
    """
    Asserts a pytest that is_pal returns False
    when passed the string "toronto"
    """
    assert is_pal("toronto") is False


"""
Step 8:
is_palindrome returns True when called with
"Able was I ere I saw Elba".
"""


def test_sentence():
    """
    Asserts a pytest that is_pal returns True
    when passed the string "Able was I ere I saw Elba"
    """
    assert is_pal("Able was I ere I saw Elba") is True
