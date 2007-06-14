#!/usr/bin/python

from sys import stdin, stdout, stderr
from time import sleep

sleep(1)
print >>stderr, "B: Reading"
line = stdin.readline()
print >>stderr, "B: Read '%s'" % line[:-1]
print >>stderr, "B: Printing two"
stdout.write("two\n")
stdout.flush()
print >>stderr, "B: Printed"
