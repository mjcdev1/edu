"""
test_generate_prime.py

Python Development II - Assignment 3 (Prime Factors)

Matthew Cunningham

Originally submitted June 17th, 2024
Modified June 27th, 2024
"""


import sys
import os
import pytest


def import_prime():
    """
    Had to use this work around to import prime,
    as it couldn't find it without appending the parent directory to the path.
    Then, flake8 flagged it for not being a top level import, so I had to use
    the below if statement to prevent it from flagging it.
    """
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
    sys.path.append(PARENT_DIR)

    if 'prime.generate_prime_factors' not in sys.modules:
        import prime
        return prime


prime = import_prime()


def test_not_int():
    with pytest.raises(ValueError):
        prime.generate_prime_factors("hello")
        prime.generate_prime_factors(3.5)
        prime.generate_prime_factors([2, 3])


def test_for_one():
    assert prime.generate_prime_factors(1) == []


def test_for_two():
    assert prime.generate_prime_factors(2) == [2]


def test_for_three():
    assert prime.generate_prime_factors(3) == [3]


def test_for_four():
    assert prime.generate_prime_factors(4) == [2, 2]


def test_for_six():
    assert prime.generate_prime_factors(6) == [2, 3]


def test_for_eight():
    assert prime.generate_prime_factors(8) == [2, 2, 2]


def test_for_nine():
    assert prime.generate_prime_factors(9) == [3, 3]
