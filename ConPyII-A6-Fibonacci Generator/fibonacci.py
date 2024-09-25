"""
fibonacci.py

Python Development II - Assignment 6 (Fibonacci Sequence)

Matthew Cunningham

Submitted July 17th 2024
"""

from typing import List


class Fibonacci:
    """
    Represents a Fibonacci Iterable object
    """
    def __init__(self, length: int):
        """
        Initializes the Fibonacci class with an int
        param called length. Will raise a value error
        if not an int or if it's a bool (because
        True = 1 and False = 0)

        Returns nothing
        """
        if not isinstance(length, int) or isinstance(length, bool):
            raise ValueError()

        self.seq_length = length
        self.current_index = -1
        self.num_list: List[int] = []

    def __iter__(self) -> "Fibonacci":
        """
        Returns an iterator object of the Fibonacci
        class
        """
        def _reset_iter() -> None:
            """
            Added this function since, after the first
            time calling the class, and then trying to
            print another list Fibonacci sequence,
            the new list would return empty. By resetting
            the values everytime an iterator is returned,
            we can reuse the function
            """
            self.current_index = -1
            self.num_list = []

        _reset_iter()
        return self

    def __next__(self) -> int:
        """
        Returns the element that is next up
        in the iteration sequence. Will stop
        the sequence by raising StopIteration
        once the current index has exceeded
        the length
        """

        if self.current_index < self.seq_length:
            self.current_index += 1
            if self.current_index < 2:
                self.num_list.append(self.current_index)
            else:
                self.num_list.append(
                        self.num_list[self.current_index - 1] +
                        self.num_list[self.current_index - 2]
                    )

            return self.num_list[self.current_index]
        else:
            raise StopIteration


fib = Fibonacci(10)
result = [number for number in fib]
print(result)

"""
Changes to final result:
========================================================

- Removed the below lines and rewrote them to be one concise line (line 68):
    prev_num = self.num_list[self.current_index - 1]
    prev_prev_num = self.num_list[self.current_index - 2]
    self.current_num = prev_num + prev_prev_num
    self.num_list.append(self.current_num)

- Removed self.current_num variable
    - It was no needed, realized I could just use the self.current_index
      variable and get the same result
========================================================
"""
