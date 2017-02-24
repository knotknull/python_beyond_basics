#!/usr/bin/env python3.5
from pprint import pprint as pp

# Generators
#
#   specify iterable sequences
#       - all generators are iterators
#
#   are lazily evaluated
#       - the next value in the sequence is computed on demand
#
#   can model infinite sequences
#       - such as data streams with no definite end
#
#   are composable into pipeline
#       - for natural stream processing

# generators defined as:  a function with at least 1 yield statement
#                      :  can have a return with no arguments
#                      :  can have implicit return at end of function
#                      :  each call to generator returns a new generator object
#   ex.     def gen123():
#               yield 1
#               yield 2
#               yield 3
#               return


def gen123():
    yield 1
    yield 2
    yield 3


def gen246():
    print("About to yield 2")
    yield 2                         # yield acts like a statefule return
    print("About to yield 4")
    yield 4                         # yield acts like a statefule return
    print("About to yield 6")
    yield 6
    print("< About to return >")    # this isn't called until after yield 6

g = gen123()
# print("g", g)         # This is a generator object, hence can use next
# print("next(g) =", next(g))
# print("next(g) =", next(g))
# print("next(g) =", next(g))
# print("next(g) =", next(g))     # returns StopIteration exception

for x in g:             # This works fine
    print("x from g = ", x)

evn = gen246()      # Function is not called here, only called on next()
# either explicitly like next(g) or implicitly

for y in evn:
    print("y from evn = ", y)
