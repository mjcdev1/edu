[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Z-CIz5TQ)
# Assignment 6: A Fibonacci series iterable


Write an iterable which produces an iterator of the Fibonacci series for a
given value.

Example:

```python
>>> [number for number in Fibonacci(10)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### `(/7)` Structure & naming
- `(/1)` Write a test module called `test_fibonacci.py`
- `(/1)` Write a module called `fibonacci.py`
- `(/5)` Create an iterable class called `Fibonacci` which requires a single
  positional argument. Remember, an iterable class has to:
    - Have an `__iter__`
    - Have a `__next__`
    - Raise a `StopIteration` exception when there are no more items


### Requirements & build steps
Using TDD methodology, develop an algorithm to assert the following test
cases.

Note: iterables return iterators and not lists, so to build a proper assertion,
cast the result as a list.

```python
assert list(Fibonacci(2)) == [0, 1, 1]
```

1. If constructed with a value other than an integer, the Fibonacci constructor
  should raise a ValueError.
1. Given a constructor value of 0, the iterator should produce the values `[0]`
   if cast as a list.
1. Given a constructor value of 1, the iterator should produce the values
`[0, 1]` if cast as a list.
1. Given a constructor value of 2, the iterator should produce the values
`[0, 1, 1]`.
1. Given a value of 4, the iterator should produce `[0, 1, 1, 2, 3]`
1. Given a value of 10, the iterator should produce
`[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]`
1. Given a negative value, the iterator should produce an empty list.

**Note:** Any integer must be accepted and calculate a correct Fibonacci
sequence. Building a function which only handles the above cases is
insufficient and will not be accepted.

### `(/21)` Development matrix
| Step | Test assertion | Code written to pass | Commit Exists |
| ---- | ---- | ---- | ------ |
| **#1** | | | |
| **#2** | | | |
| **#3** | | | |
| **#4** | | | |
| **#5** | | | |
| **#6** | | | |
| **#7** | | | |


### Code style

Tests & codestyle must pass. -1% will be deducted for each code style
violation.
