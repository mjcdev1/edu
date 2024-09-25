"""
Python Development II - Assignment 3 (Prime Factors)

Matthew Cunningham

Originally submitted June 17th, 2024
Modified June 27th, 2024
"""


def generate_prime_factors(n):
    if not isinstance(n, int):
        raise ValueError()

    factors = []

    div = 2

    while n > 1:
        while n % div == 0:
            factors.append(div)
            n = n // div
        div += 1

    return factors
