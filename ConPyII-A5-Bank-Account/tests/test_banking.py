"""
test_banking.py

Python Development II - Assignment 5 (Bank Account)

Matthew Cunningham

Submitted July 10th, 2024
"""


import sys
import os
import pytest
import datetime
from types import ModuleType


def import_banking() -> ModuleType:
    """
    Had to use this work around to import banking,
    as it couldn't find it without appending the parent directory to the path.
    Then, flake8 flagged it for not being a top level import, so I had to use
    the below if statement to prevent it from flagging it.
    """
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
    sys.path.append(PARENT_DIR)

    if 'banking' not in sys.modules:
        import banking
        return banking
    else:
        return sys.modules['banking']


banking = import_banking()


TEST_TIMESTAMP_STR = ("timestamp=datetime.datetime"
                      "(2024, 7, 9, 15, 37, 9, 910727))")


def test_transaction_timestamp_for_value_error() -> None:
    """
    Tests that the Transaction class timestamp attribute is
    passed in the right format (datetime.datetime object)
    """
    test_cases = ["j", True, 1, 1.1, [1, 2, 3]]
    for case in test_cases:
        with pytest.raises(ValueError):
            banking.Transaction(5, case)


def test_transaction_is_self_bound() -> None:
    """
    Tests that amount and timestamp are bound to self in the
    Transaction class
    """
    transaction = banking.Transaction(
                        5,
                        datetime.datetime(2024, 7, 9, 0, 0, 0)
                  )

    assert transaction.amount == 5
    assert transaction.timestamp == datetime.datetime(2024, 7, 9, 0, 0, 0)


def test_transaction_with_no_date() -> None:
    """
    Tests the case where no datetime is passed to the transaction class,
    and that the default value is properly set as datetime.datetime object
    """
    transaction = banking.Transaction(5)

    assert isinstance(transaction.timestamp, datetime.datetime)


def test_transaction_repr() -> None:
    """
    Tests that the Transaction class __repr__ correctly produces
    the expected result
    """
    test_datetime = datetime.datetime(2024, 7, 9, 15, 37, 9, 910727)

    transaction_pos = banking.Transaction(5, timestamp=test_datetime)
    transaction_neg = banking.Transaction(-5, timestamp=test_datetime)

    assert repr(transaction_pos) == ("Transaction(amount=5, "
                                     f"{TEST_TIMESTAMP_STR}")
    assert repr(transaction_neg) == ("Transaction(amount=-5, "
                                     f"{TEST_TIMESTAMP_STR}")


def test_transaction_str() -> None:
    """
    Tests that the Transaction class __str__ correctly
    produces the expected result
    """
    test_datetime = datetime.datetime(2024, 7, 9, 15, 37, 9, 910727)

    transaction_pos = banking.Transaction(5, timestamp=test_datetime)
    transaction_neg = banking.Transaction(-5, timestamp=test_datetime)

    assert str(transaction_pos) == "2024-07-09: +$5.00"
    assert str(transaction_neg) == "2024-07-09: -$5.00"


def test_account_amount_for_value_error() -> None:
    """
    Tests that the Account class methods are correctly passed
    the amount argument in the correct format (positive int or float)
    """
    test_cases = ["j", False, [1, 2, 3], -5, -5.3]

    account = banking.Account()

    for case in test_cases:
        with pytest.raises(ValueError):
            account.deposit(case)

    for case in test_cases:
        with pytest.raises(ValueError):
            account.withdraw(case)


def test_amount_conversion_works() -> None:
    """
    Tests that the amount checking and converting utility function
    correct converts the amount argument
    """
    assert banking.check_and_convert_amt_format(5000) == 5000
    assert banking.check_and_convert_amt_format(5000, "negative") == -5000


def test_account_for_single_arguments() -> None:
    """
    Tests that the methods in Account class are only able
    to accept a single argument
    """
    account = banking.Account()

    with pytest.raises(TypeError):
        account.deposit()
        account.deposit(1, 1)
        account.withdraw()
        account.withdraw(1, 1)


def test_append_to_transactions_list() -> None:
    """
    Tests that when a new transaction is completed,
    it properly appends it to the transactions list in Account
    """
    account = banking.Account()

    assert len(account.transactions) == 0

    account.deposit(5)
    assert len(account.transactions) == 1

    account.withdraw(5)
    assert len(account.transactions) == 2


def test_transaction_sum() -> None:
    """
    Tests the Account class get_balance() method that
    it properly sums the amounts of all transaction objects in
    the transactions list
    """
    account = banking.Account()

    assert account.get_balance() == 0

    account.deposit(100)
    assert account.get_balance() == 100

    account.withdraw(90)
    assert account.get_balance() == 10

    account.deposit(10)
    assert account.get_balance() == 20
