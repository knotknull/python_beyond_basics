#!/usr/bin/env python3.5
from pprint import pprint as pp

# Generator comprehensions
#       - similar syntax to list comprehensions
#       - create a generator object
#       - concise
#       - lazy evaluation
#
#      syntax: (expr(item) for item in iterable)    NOTICE (parens)


def even(xcnt):
    """ return number of even number in order.

    Args:
         int: number of even numbers to return

    Yields:
        x number of evens starting from 2 to ... 2x
    """
    even_iter = list(range(2, 2 * (xcnt + 1), 2))
    for item in even_iter:
        print("even: {}".format(item))
        yield item


def odd_first(iterbl):
    """ return an odd first number then iterable .

    Args:
         int: number of odd numbers to return
         iterable: number of odd numbers to return

    Yields:
        odd first and then even numbers
    """
    odd_cnt = 1
    for item in iterbl:  # lazy eval: making call to even() here
        print("odd_first: {}".format(odd_cnt))
        yield odd_cnt
        print("odd_first: {}".format(item))
        yield item
        odd_cnt += 2


def run_odd_even(icnt):
    for item in odd_first(even(icnt)):     # combined generators
        print(item)


if __name__ == '__main__':
    run_odd_even(11)

# Let's try to print a comprehension with a call to a generator ?!?
# Holy crap it works
# pp([item for item in take(2, alpha)])
# pp([item for item in take(2, alpha)])
# pp([item for item in take(4, alpha)])
