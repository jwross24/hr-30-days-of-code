#!/bin/python3

if __name__ == '__main__':
    n = int(input())

for i in range(1, 11):
    format_spec = '{0} x {1} = {2}'
    print(format_spec.format(str(n), str(i), str(n*i)))
