#!/usr/bin/env python

import sys

def quick_test(n):
    n = list(ord(x) for x in n)
    return ''.join(list(chr(x) for x in quicksort(n)))

def quicksort(n, low=None, high=None):
    if low == None and high == None:
        low = 0
        high = len(n)-1

    if low < high:
        p = partition(n, low, high)
        quicksort(n, low, p-1)
        quicksort(n, p+1, high)

    return n

def partition(n, low, high):
    pindex = low+((high-low)/2)
    pvalue = n[pindex]
    swap(n, pindex, high)
    si = low

    for i in range(low, high):
        if n[i] < pvalue:
            swap(n, i, si)
            si += 1
    swap(n, si, high)
    return si

def swap(n, i, k):
    if i == k:
        return
    t = n[i]
    n[i] = n[k]
    n[k] = t

with open(sys.argv.pop(), "r") as f:
    lines = f.readlines()

jumble = lines[0].rstrip("\n")
expect = lines[1].rstrip("\n")

if quick_test(jumble) == expect:
    print "result: success"
    sys.exit(0)
else:
    print "result: fail"
    sys.exit(1)
