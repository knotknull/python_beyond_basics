#!/usr/bin/env python3.5
import sys
import time
import os

def fun_def(xstr, ystr='defaulted'):
    # function declaration with a default vaule in seoncd parm
    # NOTE: Defaults must come after every non-default param
    # ystr is also a keyword argument, can be specifiec on a call
    #       i.e. fun_def("xyz", ystr='YYYY')
    print("xstr ==>> {}, ystr = {}".format(xstr, ystr))


# default values are evaluated ONLY ONCE when def statement is executed
# ONCE at the beginning of the program.
# ONLY USE IMMUTABLE OBJECT (str, int) for default values otherwise use below
def showtime(timis=None):
    if timis is None:
        timis = time.ctime()
    print("time is: ", timis)


myvar = "my test var"
fun_def(myvar)

showtime()
time.sleep(2)
showtime()
time.sleep(2)
showtime()
