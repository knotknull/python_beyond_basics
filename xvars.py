#!/usr/bin/env python3.5
import sys


def printme(nm, var):
    print("{} = {}   id(x) = {}".format(nm,  var, id(var)))

# hacky script to review what is happening with vars a function

print("set x = 100")
x = 100  # x points to int object=100.  int objects are immutable
printme("x", x)

print("set y = x")
y = x    # y points to the object reference that x is pointing, assign by ref
printme("x", x)
printme("y", y)
print("x is y ==> %s ", (x is y))

print("set x = 200")
x = 200  # x points to int object=200.  int objects are immutable
printme("x", x)
printme("y", y)
print("x is y ==> %s ", (x is y))

print("set x = 500")
x = 500  # x now points to int object=500. NOTE: nothing points to int=200
printme("x", x)
printme("y", y)
print("x is y ==> %s ", (x is y))

# NOTE: python does not have variables ... it has named references to objects
xlist = [1, 1, 2, 3, 5]
ylist = xlist
printme("xlist", xlist)
printme("ylist", ylist)
print("xlist is ylist ==> %s ", (xlist is ylist))
ylist[0] = 0  # Mutable object, both xlist and ylist point to it
print("ylist[0] = 0")
ylist = xlist
printme("xlist", xlist)
printme("ylist", ylist)
print("xlist is ylist ==> %s ", (xlist is ylist))

# NOTE: Value equality vs. identiy
#       Value    = equivalent "contents" i.e. items in xlist and ylist
#       Identity = same object, xlist and ylist point to separte object
xlist = [1, 2, 4]
ylist = [1, 2, 4]
printme("xlist", xlist)
printme("ylist", ylist)
print("xlist == ylist ==> %s ", (xlist == ylist))
print("xlist is ylist ==> %s ", (xlist is ylist))
