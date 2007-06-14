#!/usr/bin/python

from sys import stdin, stdout, stderr
from time import sleep

sleep(2)
print >>stderr, "A: Printing one"
stdout.write("one\n")
print >>stderr, "A: Reading"
line = stdin.readline()
print >>stderr, "A: Read"
