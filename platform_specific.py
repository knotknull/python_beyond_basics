#!/usr/bin/env python3.5
import sys  # to write to std error
from math import log

# Exceptions can not be ignored but error codes can ...
# Let's demonstrate some exceptions
"""A module for deomonstrating exceptions"""


def string_log(s):
    v = convert(s)
    return log(v)


def old_old_convert(s):
    """Convert to an integer."""
    x = int(s)
    return x


# rewrite convert func with try / except
def old_convert(s):
    """Cleanly convert to an integer."""
    try:
        x = int(s)
        print("Conversion succeeded x= ", x)
    except ValueError:
        print("Conversion failed, ValueError = ", s)
        x = -1
    except TypeError:
        print("Conversion failed, TypeError = ", s)
        x = -1
    return x


# rewrite convert func with try / except REFACTORED
def convert(s):
    """Cleanly convert to an integer."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:  # collapse exceptions and capture
        # pass by itself would allow non-empty except block that does nothing
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        # return -1    # Don't return just re-raise exception
        raise
    return x

xint = convert("5")
# xnot = convert("A")  # This is going to throw a ValueError
# xnot = convert(['1', '2', '3'])  # This is going to throw a TypeError
print(string_log("25"))
# print(string_log("dog"))
print(string_log(["cat", "dog", "mouse"]))
