#!/bin/python3

# Given a base-10 integer, n, convert it to binary (base-2). Then find and
# print the base-10 integer denoting the maximum number of consecutive 1's in
# n's binary representation.

if __name__ == '__main__':
    n = int(input())

binary_string = ''

# Convert the number to binary
while n > 0:
    remainder = n % 2
    n = n // 2
    binary_string = str(remainder) + binary_string

# Count the number of consecutive 1's
max_length = 0

ones_list = binary_string.split('0')

for item in ones_list:
    if len(item) >= max_length:
        max_length = len(item)

print(max_length)
