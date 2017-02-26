#!/usr/bin/env python3.5
from pprint import pprint as pp

# Generator comprehensions
#       - similar syntax to list comprehensions
#       - create a generator object
#       - concise
#       - lazy evaluation
#
#      syntax: (expr(item) for item in iterable)    NOTICE (parens)
#      NOTE: generators are single use objects

MM_squares = (x * x for x in range(1, 1000001))
print(MM_squares)           # generator object created but no squares calc'd
MM_list = list(MM_squares)  # NOTE: evaluation forced and calculated
print("len(MM_list) = ", len(MM_list))
# pp(MM_list)

# NOTE: generator just iterator, called against retrieves an empty list
new_list = list(MM_squares)
print("len(new_list) = ", len(new_list))
pp(new_list)

# Step up the stakes, compute sum of first 10MM squares using sum function
# and generator comprehensions. Sum takes an iterable hence can
# pass it in this way

# NOTE: using a list comprehension here would materialize the list and take
#       ~ 400MB of memory. Generator comprehension uses little memory and
#       returns quickly.  Also note, the generator comprehension fits within
#       the sum function parens.

print("sum(x * x for x in range(1, 10000001)) = ",
      sum(x * x for x in range(1, 10000001)))
