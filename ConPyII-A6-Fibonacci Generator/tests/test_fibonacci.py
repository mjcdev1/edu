"""
test_fibonacci.py

Python Development II - Assignment 6 (Fibonacci Sequence)

Matthew Cunningham

Submitted July 17th 2024
"""

import sys
import os
import pytest
from types import ModuleType


def import_fibonacci() -> ModuleType:
    """
    Had to use this work around to import fibonacci.py,
    as it couldn't find it without appending the parent directory to the path.
    Then, flake8 flagged it for not being a top level import, so I had to use
    the below if statement to prevent it from flagging it.
    """
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
    sys.path.append(PARENT_DIR)

    if 'fibonacci' not in sys.modules:
        import fibonacci
        return fibonacci
    else:
        return sys.modules['fibonacci']


fibonacci = import_fibonacci()


"""
Step 1:
If constructed with a value other than an integer,
the Fibonacci constructor should raise a ValueError.
"""


def test_not_int() -> None:
    """
    Tests that if the argument is not an int,
    or is a bool (because True = 1, False = 0),
    a value error is successfully raised
    """
    test_cases = ["j", True, 1.1, [1, 2, 3], {"test": "case"}]
    for case in test_cases:
        with pytest.raises(ValueError):
            fibonacci.Fibonacci(case)


"""
Step 2:
Given a constructor value of 0, the iterator should
produce the values [0] if cast as a list.
"""


def test_for_0() -> None:
    """
    Tests that if the argument is set as 0,
    it will return [0]
    """
    assert list(fibonacci.Fibonacci(0)) == [0]


"""
Step 3:
Given a constructor value of 1, the iterator should
produce the values [0, 1] if cast as a list.
"""


def test_for_1() -> None:
    """
    Tests that if the argument is set as 1,
    it will return [0, 1]
    """
    assert list(fibonacci.Fibonacci(1)) == [0, 1]


"""
Step 4:
Given a constructor value of 2, the iterator should
produce the values [0, 1, 1].
"""


def test_for_2() -> None:
    """
    Tests that if the argument is set as 2,
    it will return [0, 1, 1]
    """
    assert list(fibonacci.Fibonacci(2)) == [0, 1, 1]


"""
Step 5:
Given a value of 4, the iterator should
produce [0, 1, 1, 2, 3]
"""


def test_for_4() -> None:
    """
    Tests that if the argument is set as 4,
    it will return [0, 1, 1, 2, 3]
    """
    assert list(fibonacci.Fibonacci(4)) == [0, 1, 1, 2, 3]


"""
Step 6:
Given a value of 10, the iterator should
produce [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
"""


def test_for_10() -> None:
    """
    Tests that if the argument is set as 10,
    it will return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    assert list(fibonacci.Fibonacci(10)) == (
                [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        )


"""
Step 7:
Given a negative value, the iterator should
produce an empty list.
"""


def test_for_negative() -> None:
    """
    Tests that if the argument is a negative int,
    it will return an empty list []
    """
    assert list(fibonacci.Fibonacci(-5)) == []
