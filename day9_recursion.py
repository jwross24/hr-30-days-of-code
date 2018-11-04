#!/bin/python3

# Write a factorial function that takes a positive integer, N, as a parameter
# and prints the result of N! (N factorial).
import os


# Complete the factorial function below.
def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
