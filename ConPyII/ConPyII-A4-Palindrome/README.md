[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/YQAbrMQM)
# Palindrome validator

A palindrome is  a word, verse, or sentence (such as "Able was I ere I saw
Elba") or a number (such as 1881) that reads the same backward or forward
[(Merriam-Webster)](https://www.merriam-webster.com/dictionary/palindrome)

In this assignment, you will elaborate an algorithm which will validate that an
input string is a palindrome using the `deque` data type and its
unique high-performance features.


### Requirements
Using TDD to develop the algorithm, write a single function which will accept a
single parameter like so:

```python
is_palindrome(value: str) -> bool
```

###  Evaluation

* `(/2)` Write a function called `is_palindrome` in a Python module called
`palindrome.py`.
* `(/1)` Write your tests in a module called `test_palindrome.py`
* `(/1)` The `is_palindrome` function must accept a single parameter
* `(/2)` The function may return either `True` or `False`, or raise a
  `ValueError`.
* `(/4)` Use a `deque` container and its unique methods to determine if the
  value provided to the function is a palindrome

Using TDD, assert the following statements in tests. Only write one test at a
time, make it pass using code. Commit each step and push to Github before
moving on to the next assertion.  It is possible for a subsequent test to
already pass without having to write additional code.

**Do not write all the tests, then all the code or vice-versa.**

- `(/1)` `is_palindrome` raises a `ValueError` when not provided with a value
  that is  an instance of `str`.
- `(/1)` `is_palindrome` returns `False` when called with an empty string.
- `(/1)` `is_palindrome` returns `True` if called with `"a"`.
- `(/1)` `is_palindrome` returns `True` if called with `"bb"`.
- `(/1)` `is_palindrome` returns `False` is called with `"abc"`.
- `(/1)` `is_palindrome` returns `True` when called with `"laval"`.
- `(/1)` `is_palindrome` returns `False` when called with `"toronto"`.
- `(/1)` `is_palindrome` returns `True` when called with `"Able was I ere I saw
  Elba"`.

**Note**: this function must accept any value, not just respond to the
scenarios listed above.

The Travis CI build must pass. 1% will be deducted for each reported code style
error.
