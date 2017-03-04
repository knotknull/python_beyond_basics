#!/usr/bin/env python3.5
import sys
from itertools import count, islice

# file objects support iterator protocol


def rseq():
    """Reaman's sequence generator (notice the yield)"""
    already_seen = set()
    a = 0
    for n in (count(1)):
        yield a
        already_seen.add(a)
        c = a - n
        if c < 0 or c in already_seen:
            c = a + n
        a = c


def write_rseq_old(filename, num):
    # write a "Recaman" sequence: http://oeis.org/A005132

    f = open(filename, mode='wt', encoding='utf-8')
    # writelines writes a sequence of strings
    # That seequence of strings comes from  islice and rseq
    # rseq is a gernator or "Recaman values"
    # islice is an iterator slice, makes calls to an iterator num+1 times
    #
    f.writelines("{0}\n".format(r) for r in islice(rseq(), num + 1))
    f.close()


def write_rseq(filename, num):
    # updated write_seq that uses a with block, no close needed

    with open(filename, mode='wt', encoding='utf-8') as f:
        # writelines writes a sequence of strings
        # That seequence of strings comes from  islice and rseq
        # rseq is a gernator or "Recaman values"
        # islice is an iterator slice, makes calls to an iterator num+1 times
        #
        f.writelines("{0}\n".format(r) for r in islice(rseq(), num + 1))

if __name__ == '__main__':
    write_rseq(filename=sys.argv[1],
               num=int(sys.argv[2]))
