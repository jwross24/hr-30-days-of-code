#!/bin/python3
#
# Given an integer, n, print its first 10 multiples. Each multiple n x i
# (where 1 <= i <= 10) should be printed on a new line in the form:
# "n x i = result".

if __name__ == '__main__':
    n = int(input())

for i in range(1, 11):
    format_spec = '{0} x {1} = {2}'
    print(format_spec.format(str(n), str(i), str(n*i)))
