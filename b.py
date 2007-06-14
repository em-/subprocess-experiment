#!/usr/bin/python

from sys import stdin, stdout, stderr
from time import sleep

sleep(1)
print >>stderr, "B: Reading"
line = stdin.readline()
print >>stderr, "B: Read"
print >>stderr, "B: Printing two"
stdout.write("two\n")
print >>stderr, "B: Printed"
