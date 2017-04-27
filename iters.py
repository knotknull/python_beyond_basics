#!/usr/bin/env python3.6
from pprint import pprint as pp

# Iteration Protocols
#
#  Iterable Protocol                        Iterator Protocol
#  -----------------                        -----------------
#  iterable objects can be                  iterator objects can be passed
#  passed to built-in iter()                to the built-in next()
#  to get an iterator                       to fetch the next item
#
#  ex. iterator = iter(iterable)            ex.  item = next(iterator)


def first(v_iterable):                # for loops based on this logic
    v_iterator = iter(v_iterable)
    try:
        return next(v_iterator)
    except StopIteration:
        raise ValueError("v_iterable is empty")

x_iterable = ['Spring', 'Summer', 'Fall', 'February']
x_iterator = iter(x_iterable)
print ("x_iterable = ['Spring', 'Summer', 'Fall', 'February']")
print ("x_iterator = iter(x_iterable)")
# for x in x_iterator:
#     print ("next(x_iterator)  = {}".format(x))
print ("next(x_iterator)  = {}".format(next(x_iterator)))
print ("next(x_iterator)  = {}".format(next(x_iterator)))
print ("next(x_iterator)  = {}".format(next(x_iterator)))
print ("next(x_iterator)  = {}".format(next(x_iterator)))

# !! Returns StopIteration exception !!
# print ("next(x_iterator)  = {}".format(next(x_iterator)))

y_iterator = iter(x_iterable)
print("first(y_iterator) = {}".format(first(y_iterator)))
print("first(set() = {}".format(first(set(y_iterator))))
