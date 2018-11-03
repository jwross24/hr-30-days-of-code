#!/bin/python3
#
# Given an integer, n, perform the following conditional actions:
#
#   If n is odd, print "Weird"
#
#   If n is even and in the inclusive range of 2 to 5, print "Not Weird"
#
#   If n is even and in the inclusive range of 6 to 20, print "Weird"
#
#   If n is even and greater than 20, print "Not Weird"

if __name__ == '__main__':
    N = int(input())

if N % 2 == 0:
    if N >= 2 and N <= 5:
        print("Not Weird")
    if N >= 6 and N <= 20:
        print("Weird")
    if N > 20:
        print("Not Weird")
else:
    print("Weird")
