#!/usr/bin/env python3.5
import sys


def pusher(lst, nm):
    # reference passed in, update object directly
    lst.append(str(len(lst) + 1))
    print("id({}) = {}".format(nm, id(xlist)))
    printme(nm, xlist)


def printme(nm, var):
    print("{} = {}   id(x) = {}".format(nm,  var, id(var)))

# passing reference to function
xlist = ['zero']
print("id(xlist) = {}".format(id(xlist)))
printme("xlist", xlist)

pusher(xlist, "xlist")
pusher(xlist, "xlist")
pusher(xlist, "xlist")
pusher(xlist, "xlist")

# NOTE: function argument is Passed By Object Reference.
#       value of the REFERENCE is copied, not the value of the OBJECT.
