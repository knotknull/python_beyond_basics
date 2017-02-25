#!/usr/bin/env python3.5
from pprint import pprint as pp

# Use the force generator Luke

# Lucas series, maybe how you should watch Star Wars

"""Module for Lucas servies """
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


def lucas():
    """Return SW watch order

    Args:
        None:

    Yields:
        At watch order
    """
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


def run_lucas():
    for x in lucas():
        print("Start Watching Vol {}", x)
        if x > 9:
            break


if __name__ == '__main__':
    run_lucas()
    # run_take()

# Let's try to print a comprehension with a call to a generator ?!?
# Holy crap it works
# pp([item for item in take(2, alpha)])
# pp([item for item in take(2, alpha)])
# pp([item for item in take(4, alpha)])
