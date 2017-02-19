#!/usr/bin/env python3.5
import sys



def printme(var):
    print("{} = {}   id(x) = {}".format(var.__class__,  var, id(var)))

# passing reference to function
xlist = ['zero']
print("id(xlist) = {}".format(id(xlist)))
printme(xlist)
xlist="zero"
printme(xlist)

# NOTE: function argument is Passed By Object Reference.
#       value of the REFERENCE is copied, not the value of the OBJECT.
