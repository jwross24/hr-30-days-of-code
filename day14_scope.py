# Complete the Difference class by writing the following:
#
#   A class constructor that takes an array of integers as a parameter and
#   saves it to the elements instance variable.
#
#   A computeDifference method that finds the maximum absolute difference
#   between any 2 numbers in N and stores it in the maximumDifference instance
#   variable.


class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        self.maximumDifference = 0
        for i in range(0, len(self.__elements)-1):
            for j in range(i+1, len(self.__elements)):
                difference = abs(self.__elements[i] - self.__elements[j])
                if difference > self.maximumDifference:
                    self.maximumDifference = difference


# Input handler
_ = input()  # not necessary in Python
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
