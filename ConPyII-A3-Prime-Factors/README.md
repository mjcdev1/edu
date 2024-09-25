
# Module 2 Assignment: Prime Factors

In this assignment, you will build an algorithm that will generate a list of
the prime factors for a given number.

Prime factors (also known as prime numbers or a prime) are numbers which cannot
be formed as the result of a multiplication
(https://en.wikipedia.org/wiki/Prime_number).

Using the Three Rules of TDD, develop the algorithm based on each assertion
listed below. After each step **commit your work** using `git commit`.


## Completing the assignment
There are 8 steps to complete. For each step, the following is expected:

1. A **test** to be written with the specified assertion before any code is
  written.
2. Only enough code is written to **make the test pass**.
3. A git **commit** exists for each step


## Evaluation

This assignment is marked out of 30.

| Points | Description|
| ------ | ---------- |
| 24     | Functionality (see matrix) |
| 6      | Code style (-1 per reported linting error) |
| **30** | **Total** |



There are 8 steps to this assignment. Each step is worth 3 points for a total
of 24 points.

**Note:** The function your write must calculate prime factors for any number
given. It is not enough to return the expected values using if statements and
will be considered incomplete / not accepted.

### Evaluation Matrix

| Step | Test assertion | Code to pass | Commit Exists |
| ---- | ---- | ---- | ------ |
| **#1** | | | |
| **#2** | | | |
| **#3** | | | |
| **#4** | | | |
| **#5** | | | |
| **#6** | | | |
| **#7** | | | |
| **#8** | | | |



## Requirements

Write a function called `generate_prime_factors` in the module `prime.py`. This
function will accept an integer as an argument, and return a list of integers.

E.g.
```python
>>> generate_prime_factors(6)
[2, 3]
```


### Step 1:
Write a test that asserts that when `generate_prime_factors` is called with a
data type that is not an integer (e.g. a string or float), a ValueError is
raised. Write the appropriate code to solve this and then commit the changes.


### Step 2:
Write a test that asserts that when `generate_prime_factors` is called with
`1`, an empty list is returned. Solve & commit.


### Step 3:
Write a test that asserts that when `generate_prime_factors` is called with
`2`, the list `[2]` is returned. Solve & commit.


### Step 4:
Write a test that asserts that when `generate_prime_factors` is called with
`3`, the list `[3]` is returned. Solve & commit.


### Step 5:
Write a test that asserts that when `generate_prime_factors` is called with
`4`, the list `[2, 2]` is returned. Solve & commit.


### Step 6:
Write a test that asserts that when `generate_prime_factors` is called with
`6`, the list `[2, 3]` is returned. Solve & commit.


### Step 7:
Write a test that asserts that when `generate_prime_factors` is called with
`8`, the list `[2, 2, 2]` is returned. Solve & commit.


### Step 8:
Write a test that asserts that when `generate_prime_factors` is called with
`9`, the list `[3, 3]` is returned. Solve & commit.
