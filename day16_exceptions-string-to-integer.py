# Read a string, S, and print its integer value; if S cannot be converted to
# an integer, print "Bad String".

S = input().strip()

try:
    int_S = int(S)
    print(int_S)
except ValueError:
    print("Bad String")
