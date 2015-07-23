#!/usr/bin/env python

import sys

def merge_test(n):
    n = list(ord(x) for x in n)
    return ''.join(list(chr(x) for x in mergesort(n)))

def mergesort(n):
    if len(n) <= 1:
        return n

    left = []
    right = []
    middle = len(n)/2

    for x in n[0:middle]:
        left.append(x)

    for x in n[middle:]:
        right.append(x)

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(l, r):
    result = []

    while len(l) and len(r):
        if l[0] <= r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))
    result = result + l + r
    return result

with open(sys.argv.pop(), "r") as f:
    lines = f.readlines()

jumble = lines[0].rstrip("\n")
expect = lines[1].rstrip("\n")

if merge_test(jumble) == expect:
    print "result: success"
    sys.exit(0)
else:
    print "result: fail"
    sys.exit(1)
