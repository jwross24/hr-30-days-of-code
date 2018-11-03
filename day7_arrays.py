#!/bin/python3

# Given an array, A, of N integers, print A's elements in reverse order as a
# single line of space-separated numbers.

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

arr_out = []
for i in range(n-1, -1, -1):
    arr_out.append(str(arr[i]))

print(' '.join(arr_out))
