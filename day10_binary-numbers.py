#!/bin/python3

# Given a base-10 integer, n, convert it to binary (base-2). Then find and
# print the base-10 integer denoting the maximum number of consecutive 1's in
# n's binary representation.

if __name__ == '__main__':
    n = int(input())

count = 0
max_count = 0

while n > 0:
    # Convert the number to binary
    remainder = n % 2
    n = n // 2

    # Count the number of 1's in a row
    if remainder == 1:
        count = count + 1
        if count >= max_count:
            max_count = count
    else:
        count = 0

print(max_count)
