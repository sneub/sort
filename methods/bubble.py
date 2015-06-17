#!/usr/bin/env python

import sys

def bubblesort(string):
    n = list(ord(x) for x in string)
    l = len(n)
    for k in range(l):
        swaps = False
        for i in range(l-1):
            if n[i] > n[i+1]:
                t = n[i]
                n[i] = n[i+1]
                n[i+1] = t
                swaps = True
        if not swaps:
            break
    return ''.join(list(chr(x) for x in n))

with open(sys.argv.pop(), "r") as f:
    lines = f.readlines()

jumble = lines[0].rstrip("\n")
expect = lines[1].rstrip("\n")

if bubblesort(jumble) == expect:
    print "result: success"
    sys.exit(0)
else:
    print "result: fail"
    sys.exit(1)
