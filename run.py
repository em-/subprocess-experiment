#!/usr/bin/python

from subprocess import Popen, PIPE

a = Popen(["python", "a.py"], stdin=PIPE, stdout=PIPE)
print "Started A"
b = Popen(["python", "b.py"], stdin=a.stdout, stdout=a.stdin)
print "Started B"

print "Waiting A"
a.wait()
print "Waiting B"
b.wait()
