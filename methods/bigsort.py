#!/usr/bin/env python
#
# Basically a count sort of single characters
# Intended for sorting a data set that is bigger than the computer memory size

import os, sys

def bigsort(infile, outfile):
    maxmem = 131072
    pos    = 0
    size    = os.path.getsize(infile)

    meta = {}
    f = open(infile, "r")

    lowest = 255
    highest = 0

    while pos < size:
        slurp = f.read(maxmem)
        n = list(ord(x) for x in slurp)

        for i in n:
            if i not in meta:
                meta[i] = 1
                lowest  = i if i < lowest else lowest
                highest = i if i > highest else highest
            else:
                meta[i] += 1
        pos += len(slurp)
    f.close()

    print "Finished reading"
    print "meta is %d bytes" % sys.getsizeof(meta)

    f = open(outfile, "w")
    print meta
    for i in range(lowest, highest+1):
        if i in meta:
            f.write("%s" % (chr(i) * meta[i]))

bigsort(sys.argv.pop(), "bigsort.out")
