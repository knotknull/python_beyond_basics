#!/usr/bin/env python3.5


# Tuples are immutables sequences of heterogenous objects
# like lists but have parens instead

def minmax(items):
    return min(items), max(items)
tpl = ("Str", 3.14, 5)
print("{} is a {}".format(tpl, type(tpl)))
print("len(tpl)={}".format(len(tpl)))

y = 0
# iterate over
for x in tpl:
    print("tpl({}) = {}".format(y, x))
    y = y + 1

# concatenate
print("tpl + (99,88) = {} ".format(tpl + (99, 88)))
print("tpl = {} ".format(tpl))

# multiply
print("tpl * 4 = {} ".format(tpl * 4))
print("tpl = {} ".format(tpl))

# nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print("nested = {}".format(nested))
print("nested[2] = {}".format(nested[2]))
print("nested[2][1] = {}".format(nested[2][1]))

# single element tuples
not_this = (25)   # << this is an int
is_this = (25,)   # << this is a  tuple
print("not_this is {}".format(type(not_this)))
print("is_this  is {}".format(type(is_this)))

# can omit tuple parens
p = 0, 1, 1, 2, 3, 5
print("p = {} is type {}".format(p, type(p)))

# tuple unpacking, unpack into named refs
miny, maxy = minmax(p)
print(miny, maxy)
(a, (b, (c, d))) = (4, (3, (2, 1)))
print ("{}, {}, {},  {} ".format(a, b, c, d))

# swap a variable via tuple unpacking
x = "xxx"
y = "yyy"
print("before swap: x={} y={}", x, y)
x, y = y, x
print("after  swap: x={} y={}", x, y)

# create tuple from other iterable objects
intupl = tuple([0, 1, 1, 2, 3, 5])
strtupl = tuple("strings")
print("intupl={}  is type {}".format(intupl,  type(intupl)))
print("strtupl={} is type {}".format(strtupl, type(strtupl)))

# check for membership
print("5 in {} == {}".format(intupl, 5 in intupl))
print("5 not in {} == {}".format(intupl, 5 not in intupl))
