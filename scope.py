#!/usr/bin/env python3.5


# Scope: context where named references are looked up: i.e. in a function
#    Local:     Inside current function, once func completed refs are destroyed
#    Enclosing: Any and all enclosing functions
#    Global:    Top level of a module (each module brings a new global scope)
#    Built-in:  Provided by builtins module

# This is a Global reference
count = 0


def print_count(str):
    print(str)


def g_count():
    # prints global count
    global count  # reference global count
    print_count("g_count: count = {}".format(count))


def l_count(count=5):
    # prints local count
    print_count("l_count: count = {}".format(count))

print_count("count Starting Point: {} ".format(count))
g_count()
l_count()
g_count()

xl_count = l_count  # This is just a reference to the function !!
xl_count()          # you can then call the reference to the function !!
xl_count = g_count
xl_count()
