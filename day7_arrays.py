#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

arr_out = []
for i in range(n-1, -1, -1):
    arr_out.append(str(arr[i]))

print(' '.join(arr_out))
