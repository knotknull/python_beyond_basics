#!/usr/bin/env python3.5
from pprint import pprint as pp
import sys
from contextlib import closing  # This wraps a context manager around

# the wrapped object

# Having a class / module act like a contxt manager  with / as


class FridgeRaider:
    """raid a fridge"""

    def open(self):
        print("Open the fridge door ...")

    def take(self, food):
        print("Finding {}...".format(food))
        if food == 'broccoli':
            raise RuntimeError("Taste Warning!")
        print("Taking {}...".format(food))

    def close(self):
        print("Close fridge door (goodnight)")


def raid(food):
    # This wraps a context manager around the wrapped object
    with closing(FridgeRaider()) as r:
        r.open()
        r.take(food)
        # Don't have to call close because context mgr will do it
        #  r.close()
