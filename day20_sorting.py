# Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following 3 lines:
#
#   1. "Array is sorted in numSwaps swaps."
#      where numSwaps is the number of swaps that took place.
#
#   2. "First Element: firstElement"
#      where firstElement is the first element in the sorted array.
#
#   3. "Last Element: lastElement"
#      where lastElement is the last element in the sorted array.

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
total_swaps = 0

for _ in range(n):
    # Track number of element swaps during a single array traversal
    num_swaps = 0

    for i in range(n-1):
        # Swap adjacent elements if they are in decreasing order
        if a[i] > a[i+1]:
            a[i+1], a[i] = a[i], a[i+1]
            num_swaps += 1
        
    # If no elements were swapped, array is sorted
    if num_swaps == 0:
        break
    
    total_swaps += num_swaps

print('Array is sorted in {} swaps.'.format(total_swaps))
print('First Element:', a[0])
print('Last Element:', a[n-1])
