#!/usr/bin/env python3.5
import sys


def series_rdr(filename):
    try:
        f = open(filename, mode="rt", encoding='utf-8')
        # original code, replaced by refactored list comprhensions
        #
        #
        # series = []
        # for line in f:
        #    a = int(line.strip())
        #    series.append(a)
        #
        # Instead a list comprhension is created and returned
        return [int(line.strip()) for line in f]
    finally:
        # NOTE: Something to realize here, no matter how try block is exited,
        #       the finally block is called. So in this example:
        #       if the try block either returns or raises an exception,
        #       the finally block will always be run i.e.:
        #       1. try:      return [list comprhension]
        #       2. finally:  f.close()  # f.close always called !!
        f.close()


def cntxt_series_rdr(filename):
        # NOTE: this function does the samething as series_rdr, HOWEVER
        #       We are using a with block (context manager) to open the file
        #       and no need for try / finally / close (see below)
        #
        # Context Manager / with blocks
        # resource cleanup (close for every open)
        # NOTE: open() returns a context manager
    with open(filename, mode="rt", encoding='utf-8') as f:
        return [int(line.strip()) for line in f]
    #
    # NOTE: try / finally not needed as well as f.close because the
    # NOTE: with context handles the closing of file when with block exited!!
    #


def main(filename):
    series = series_rdr(filename)
    print(series)

if __name__ == '__main__':
    main(sys.argv[1])
