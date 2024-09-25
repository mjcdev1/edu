"""
banking.py

Python Development II - Assignment 5 (Bank Account)

Matthew Cunningham

Submitted July 10th, 2024
"""


import datetime
from typing import Union, Optional, List


def format_amount(amount: Union[int, float]) -> str:
    """
    Takes an int or float amount and formats it
    with a + or - sign and a $ sign, with decimals
    and commas as needed
    """
    if amount > 0:
        amount_formatted = "+${:,.2f}".format(amount)
    else:
        amount_formatted = "-${:,.2f}".format(abs(amount))

    return amount_formatted


def check_and_convert_amt_format(
    amount: Union[int, float],
    conversion: Optional[str] = None
) -> Union[int, float]:
    """
    Takes a positive int or float amount and an optional
    string to confirm if a number is positive or not.
    Will return either a positive or negative float,
    and raise an exception if the amount arg passed is negative
    """
    is_positive = isinstance(amount, (int, float)) and amount > 0

    if not is_positive or isinstance(amount, bool):
        raise ValueError("Amount needs to be an positive integer or float")

    return -amount if conversion == "negative" else amount


class Transaction:
    """
    Represents a transaction object
    """
    def __init__(self,
                 amount: Union[int, float],
                 timestamp: Optional[datetime.datetime] = None
                 ) -> None:
        """
        Initializes the Transaction class, including the amount
        and timestamp arguments. Raises an exception if a non
        datetime.datetime object is passed to the timestamp arg.

        Returns nothing
        """
        if timestamp:
            if not isinstance(timestamp, datetime.datetime):
                raise ValueError("Timestamp needs to be "
                                 "a datetime.datetime object")

        self.amount = amount
        self.timestamp = timestamp if timestamp else datetime.datetime.now()

    def __repr__(self) -> str:
        """
        Returns a string representation of the transaction object
        """
        return (f"Transaction(amount={self.amount}, "
                f"timestamp={repr(self.timestamp)})")

    def __str__(self) -> str:
        """
        Returns a formatted string version of the object
        """
        date_formatted = self.timestamp.strftime('%Y-%m-%d')

        amount_formatted = format_amount(self.amount)

        return f"{date_formatted}: {amount_formatted}"


class Account:
    """
    Represents an account object
    """
    def __init__(self) -> None:
        """
        Initializes the Account class, with an empty transactions list.

        Returns nothing
        """
        self.transactions: List[Transaction] = []

    def deposit(self, amount: Union[int, float]) -> None:
        """
        Takes a positive amount argument as an int or float,
        and checks that it is positive (or raises an exception
        with the called method). It then creates a new instance of the
        Transaction class and appends it to the transactions object

        Returns nothing
        """
        amount = round(check_and_convert_amt_format(amount), 4)
        transaction = Transaction(amount)
        self.transactions.append(transaction)

    def withdraw(self, amount: Union[int, float]) -> None:
        """
        Takes a positive amount argument as an int or float,
        and checks that it is positive (or raises an exception
        with the called method). It then converts the amount to a
        negative number and creates a new instance of the
        Transaction class and appends it to the transactions object

        Returns nothing
        """
        neg_amount = round(check_and_convert_amt_format(amount, "negative"), 4)
        transaction = Transaction(neg_amount)
        self.transactions.append(transaction)

    def get_balance(self) -> Union[int, float]:
        """
        Returns the sum of amounts of every transaction object
        in the transactions list
        """
        return sum(tr.amount for tr in self.transactions)
