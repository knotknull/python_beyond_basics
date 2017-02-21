#!/usr/bin/env python3.5
from pprint import pprint as pp  # import pprint func from pprint module

# set  : unordered collection of unique, immutable objects
#        collection is mutable but EACH ELEMENT MUST BE IMMUTABLE
#        i.e. numbers, str, tuples only
#        delcared like a dictionary but with only values;
#            xset = { 5, 10, 15, 20, 3.14}
#
#  Order is arbitrary!!
xset = {5, 10, 15, 20, 3.14}
pp("xset={} type={}".format(xset, type(xset)))

# create an empty set, remember {} is an empty dictionary
# hence use set()
mt_dict = {}
mt_set = set()
pp("mt_dict={} type={},   mt_set={} type={}".format(mt_dict, type(mt_dict),
                                                    mt_set, type(mt_set)))

# can create a set from any iterable series of values, removes duplicates
# good way of getting unique values
fib_list = [0, 0, 1, 1, 2, 3, 5, 8]
fib_set = set([0, 0, 1, 1, 2, 3, 5, 8])
pp("fib_set={} type={}".format(fib_set, type(fib_set)))

# sets are iterable, order is arbitrary
for x in fib_set:
    print("x = {}".format(x))

# membership test
print("0 in fib_set: {}".format(0 in fib_set))
print("-0 in fib_set: {}".format(-0 in fib_set))
print("-1 in fib_set: {}".format(-1 in fib_set))

# add an element to set, duplicates are ignored
fib_set.add(13)
fib_set.add(-0)
pp("fib_set={}".format(fib_set, ))

# add multiple elements using update and passing iterable items
fib_set.update([-0, 13, 21, 0, 34, -0])
pp("fib_set={}".format(fib_set))

# two ways to delete an item:
#   remove(item)  - item MUST be in set, else throws KeyError
#   discard(item) - item MAY be in set, always succeeds
fib_set.remove(34)
# fib_set.remove(35) # KeyError: 35
fib_set.discard(-1)
fib_set.discard(-0)
pp("fib_set={}".format(fib_set))

# Create SHALLOW copies via set.copy() or set(xset)
my_fib_set = fib_set.copy()
pp("my_fib_set={}".format(my_fib_set))
fib_set2 = set(fib_set)
pp("fib_set2={}".format(fib_set2))

# Let's do some set algebra
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# union: a or b or a and b -- commutative
print("blue eyes OR blond hair or both (union): {}".format(
    blue_eyes.union(blond_hair)))

# intersection: blond and blue eyes -- commutative
print("blue eyes AND blond hair (intersection): {}".format(
    blue_eyes.intersection(blond_hair)))

# difference: blond and NOT blue eyes. all elements in 1st set and NOT in 2nd
#             -- NOT commutative
print("blond hair NOT blue eyes (difference): {}".format(
    blond_hair.difference(blue_eyes)))

# symmetric_difference: all in first set or second set but not both
#             (exclude intersection) -- commutative
print("blond hair or blue eyes NOT BOTH (symmetric_difference): {}".format(
    blond_hair.symmetric_difference(blue_eyes)))

# check issubset x.issubset(z) = x is a subset of z
print("smell_hcn.issubset(o_blood) = {}".format(smell_hcn.issubset(o_blood)))
print("smell_hcn.issubset(blond_hair) = {}".format(
    smell_hcn.issubset(blond_hair)))

# check issuperset x.issuperset(z) = x is a superset of z
print("taste_ptc.issuperset(smell_hcn) = {}".format(
    taste_ptc.issuperset(smell_hcn)))
print("smell_hcn.issubset(taste_ptc) = {}".format(
    smell_hcn.issubset(taste_ptc)))

# check no members in common; isdisjoint
print("a_blood.isdisjoint(ab_blood) = {}".format(
    a_blood.isdisjoint(ab_blood)))
