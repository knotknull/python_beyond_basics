#!/usr/bin/env python3.5

# Range: arithmetic progression of integers

# create a range by giving it's stop value
print(range(5))
for i in range(5):
    print(i)

# range with a "stop" value
xlst = list(range(5, 10))  # stop value of range is NOT included in rtn values
print(xlst)                # xlst does not include value 10

# range with a "step value"
# stop value of range is NOT included in rtn values
xlst = list(range(1, 100, 2))
print(xlst)

# range(5)         ==>> 0, 1, 2, 3, 4
# range(5, 10)     ==>> 5, 6, 7, 8, 9 (stops at 10)
# range(10, 20, 2) ==>> 10, 12, 14, 16, 18 (stops at 20 by two)

# don't use range for iterating lists
s = [0, 1, 1, 2, 3, 5]
for i in range(len(s)):
    print(s[i])

# use iteration of iterable objects
for x in s:
    print(x)

# use enumerate for counters
for p in enumerate(s):  # enumerate returns index (ctr) and value
    print(p)
    print("{p[0]} {p[1]}".format(p=p))

# BETTER: use tuple unpacking !!
for idx, val in enumerate(s):  # enumerate returns index (ctr) and value
    print("index = {}  value = {}".format(idx, val))
