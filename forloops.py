#!/usr/bin/python3.5
import math
# for loop : visit each item in an interable series
# for item in iterable:
#       ... body of loop ...
#
charlist = list("ZYXWVUTABCDEFGHIJ")
print(charlist)

# iterate over list
for letter in charlist:
    print(letter)

numz_dict = {'zero': 0, 'one': 1, 'neg1': -1, 'pi': math.pi, 'e': math.e, }

# iterate over dictionary
for key in numz_dict:
    print(key, numz_dict[key])
