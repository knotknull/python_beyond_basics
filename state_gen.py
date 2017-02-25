#!/usr/bin/env python3.5
from pprint import pprint as pp

"""Module for demonstrating generator execution"""
# Stateful Generators
#       - generators resume execution
#       - can maintain state in local variables
#       - complex control flow
#       - lazy evaluation
#
#   Generators are lazy, computation is done just in time when the next
#   result requested.
#
#   Can be used to model infinite (large) sequences
#       - sensor readings
#       - mathematical series
#       - massive files


def take(count, iterable):
    """Take items from the front of an iterable.

    Args:
        count:    The maximum number of items to retrieve
        iterable: The source of the series

    Yields:
        At most 'count' items from 'iterable.
    """
    xcnt = 0
    for item in iterable:
        if xcnt == count:
            return
        xcnt += 1
        yield item


def distinct(iterable):
    """return distinct items from an iterable.

    Args:
        iterable: The source of the series

    Yields:
        unique elements in order from 'iterable'
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [5, 7, 7, 7, 7, 6, 5, 4, 5, 5, 1]
    for item in distinct(items):
        print(item)

# pipeline because it calls distinct wich then calls take


def run_pipeline():
    items = [3, 6, 6, 2, 1, 0]
    for item in take(3, distinct(items)):
        print(item)


def run_take():
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alpha.reverse()
    for item in take(29, alpha):
        pp(item)


if __name__ == '__main__':
    run_pipeline()
    # run_take()

# Let's try to print a comprehension with a call to a generator ?!?
# Holy crap it works
# pp([item for item in take(2, alpha)])
# pp([item for item in take(2, alpha)])
# pp([item for item in take(4, alpha)])
