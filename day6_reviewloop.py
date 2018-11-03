# Task
# Given a string, S, of length N that is indexed from 0 to N-1, print its even-
# indexed and odd-indexed characters as 2 space-separated strings on a single
# line.
#
# Note: 0 is considered to be an even index.


def oddEvenString(s):
    odd_string = ''
    even_string = ''
    for i in range(len(s)):
        if i % 2 == 0:
            even_string += s[i]
        else:
            odd_string += s[i]
    return even_string + ' ' + odd_string


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        string = oddEvenString(s)
        print(string)
