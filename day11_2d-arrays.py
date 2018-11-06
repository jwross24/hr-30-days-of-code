#!/bin/python3

# Given a 6 x 6 2D Array, A, we define an hourglass in A to be a subset of
# values with indices falling in this pattern in A's graphical representation:
#
#   a b c
#     d
#   e f g
#
# Calculate the hourglass sum for every hourglass in A, then print the maximum
# hourglass sum.

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

hourglass_sum = -64
max_hourglass_sum = -64

for row in range(1, 5):
    for col in range(1, 5):
        hourglass_sum = sum(arr[row-1][col-1:col+2]) + \
              arr[row][col] + sum(arr[row+1][col-1:col+2])
        if hourglass_sum >= max_hourglass_sum:
            max_hourglass_sum = hourglass_sum

print(max_hourglass_sum)
