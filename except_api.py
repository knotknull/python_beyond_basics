#!/usr/bin/env python3.5
import sys  # to write to std error


def sqrt(x):
    """ Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for which the square root is to be computed

    Returns:
         The square root of x.

    Raises:
        ValueError:  If x is negative
     """
    if x < 0:
        raise ValueError("Cannot compute square root "
                         "of negative number {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        print("sqrt: guess={}, x={}, i={}".format(guess, x, i))
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(25))
        print(sqrt(9))
        print(sqrt(8))
        print(sqrt(2))
        print(sqrt(-1))        # Returns ZeroDivisionError
        print("Never Hits Here ....")
    except ValueError as e:
        print(e, file=sys.stderr)
    print("Program execution continues normally here")
    # Types of errors
    # IndexError:
    # z = [1, 4, 3]
    # z[4]
    # ValueError:
    # y = int("cat")
    # KeyError:
    # say = dict(eenie=1, meenie=2, minie=3, moe=4)
    # say['hi']

    # NOTE: AVOID Protecting Against TypeErrors!!  Just let it fail

if __name__ == '__main__':
    main()
