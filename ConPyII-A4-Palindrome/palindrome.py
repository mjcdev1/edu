"""
palindrome.py

Python Development II - Assignment 4 (Palindrome)

Matthew Cunningham

Originally submitted June 25th, 2024
Modified and resubmitted June 27th, 2024
"""


from collections import deque


def is_palindrome(string):
    """
    Takes a string parameter and checks if it is a palindrome

    Params:
    string (str): The string to check

    Returns:
    Bool: True or False
    """
    if not isinstance(string, str):
        raise ValueError()

    despaced_string = string.replace(" ", "")

    dq = deque(despaced_string.lower())

    same = True

    while len(dq) > 1:
        left = dq.popleft()
        right = dq.pop()

        same = left == right
        if not same:
            break

    return string != "" and same


is_pal = is_palindrome("Able was I ere I saw Elba")


def get_palindrome_results(strings):
    for string in strings:
        res = is_palindrome(string)
        output = (f'"{string}" is a palindrome!' if res else
                  f'"{string}" is not a palindrome!')
        print(output)


strings_to_test = ["", "a", "bb", "abc",
                   "laval", "toronto", "Able was I ere I saw Elba"]
get_palindrome_results(strings_to_test)
