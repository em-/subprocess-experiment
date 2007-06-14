#!/usr/bin/python

from sys import stdin, stdout, stderr

print >>stderr, "A: Printing one"
stdout.write("one\n")
stdout.flush()
print >>stderr, "A: Reading"
line = stdin.readline()
print >>stderr, "A: Read '%s'" % line[:-1]
