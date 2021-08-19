# Task 1 Create your own implementation of a built - in function enumerate, named `with_index`, which takes two
# parameters: `iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function

def with_index(iterable, start=0):
    for value in iterable:
        yield start, value
        start += 1


# Task 2 Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
# `start`, `end`, and optional step. Tips: See the documentation for `range` function

def in_range(start, end, step):
    while start < end:
        yield start
        start += step


# Task 3 Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for
# retrieving elements using square brackets syntax.
from typing import Union


def calc_discount(deposit: Union [int, float], min_percent: float = 0.06, max_percent: float = 0.105,
                  step: float = 0.005) -> Union [int, float]:
    total = []
    global dep
    dep = deposit
    while min_percent < max_percent:
        total.extend([deposit + (min_percent * deposit * 0.8)])
        deposit += (min_percent * deposit * 0.8)
        min_percent += step
    return total


without_tax_expr = ((m - dep) for m in calc_discount(70))
without_tax_list = [(m - dep) for m in calc_discount(70)]

