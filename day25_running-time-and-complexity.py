# A prime is a natural number greater than 1 that has no positive divisors
# other than 1 and itself. Given a number, n, determine and print whether
# it's "Prime" or "Not prime".

from math import ceil, sqrt


def prime_test(num):
    if num == 2:
        return 'Prime'

    if num % 2 == 0 or num == 1:
        return 'Not prime'

    sq = sqrt(num)
    # After we check 2, we don't need to check any other even numbers
    for i in range(3, ceil(sq)+1, 2):
        if num % i == 0:
            return 'Not prime'

    # If no numbers divide our given number
    return 'Prime'


# Input handler
N = int(input())
for i in range(N):
    number = int(input())
    is_prime = prime_test(number)
    print(is_prime)
