#!/usr/bin/env python3.5
import math

# String: homogeneous immutable sequence of Unicode codepoints (characters)

howlong = "How Long Am This String"
print(len(howlong))

# string concat with '+'
print (howlong + " plus one")


# string append '+='
# use sparingly because this concat can cause performance hit
# NOTE: for performance use join
howlong += " plus one"
howlong += " plus one"
howlong += " plus one"
print (howlong)

# join: joins a number of strings using the join method on the separator char
rhyme = ' '.join(('Three', 'blind', 'mice'))  # takes an interable: tuple
print(rhyme)
rhyme = ' '.join(['Three', 'blind', 'mice'])  # takes an interable: list
print(rhyme)

# join can be used to concat strings with empty string as a separator
alpha = ''.join(['a', 'b', 'c', 'd'])
print(alpha)

# split: split using the join separator character
print('split rhyme = ', rhyme.split(' '))

# partition: partition splits string and returns before, separator, after
print ("so-so".partition('-'))
# partition: partition with tuple unpacking
mon, _, yr, = "July-1776".partition('-')    # use _ as dummy var for separator
print("mon={} yr= {}".format(mon, yr))

# format: with index, unindexed or name fields
print("format string with indexes {2} .. {1} .. {0}".format(1, 2, 3))
print("format string with indexes {} .. {} .. {}".format(1, 2, 3))
print("A greeting: {greeting} and a solutation: {salutation}".format(
    greeting="Hiya!!", salutation="Yo"))
# format: with keys or indexes with square brackets
abc = ('a', 'b', 3)
print ("1st letter={abc[0]} 3rd letter={abc[2]}".format(abc=abc))
# format: pass a whole module into the formatter (module is just an object)
print ("this is e: {m.e} and this is pi {m.pi}".format(m=math))
print ("formatted e: {m.e:.3f} and this is pi {m.pi:.3f}".format(m=math))
