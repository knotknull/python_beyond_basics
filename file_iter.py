#!/usr/bin/env python3.5
from pprint import pprint as pp
import sys

# file objects support iterator protocol


def printit(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        # print(line)           # don't use print because it adds a newline
        sys.stdout.write(line)  # use stdout.write()
    f.close()

if __name__ == '__main__':
    printit(sys.argv[1])
