from inspect import isgenerator
from typing import Iterable

START_NUMBER = 2


def is_prime_number(num: int) -> bool:
    """Check if a number is prime"""
    divisor_limit = int(num ** 0.5) + 1

    if num < START_NUMBER:
        return False

    for divisor in range(START_NUMBER, divisor_limit):
        if num % divisor == 0:
            return False

    return True


def prime_generator(end: int) -> Iterable[int]:
    """Generate prime numbers up to a given end"""
    for number in range(START_NUMBER, end + 1):
        if is_prime_number(number):
            yield number


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
