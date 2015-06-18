#!/usr/bin/env python

import sys

def countsort(s):
    output = []
    n = list(ord(x) for x in s)
    d = {}
    lowest = 255
    highest = 0
    for i in n:
        if i not in d:
            d[i] = 1
            lowest  = i if i < lowest else lowest
            highest = i if i > highest else highest
        else:
            d[i] += 1
    #for k, v in d.iteritems():
    #    output.append( "%s" % (chr(k) * d[k]) )
    for i in range(lowest, highest+1):
        if i in d:
            output.append( "%s" % (chr(i) * d[i]) )
    return ''.join(output)

with open(sys.argv.pop(), "r") as f:
    lines = f.readlines()

jumble = lines[0].rstrip("\n")
expect = lines[1].rstrip("\n")

if countsort(jumble) == expect:
    print "result: success"
    sys.exit(0)
else:
    print "result: fail"
    sys.exit(1)
