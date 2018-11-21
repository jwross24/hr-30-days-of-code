# Your local library needs your help! Given the expected and actual return
# dates for a library book, create a program that calculates the fine (if any).
# The fee structure is as follows:
#
#   1. If the book is returned on or before the expected return date, no fine
#      will be charged (i.e.: fine = 0).
#   2. If the book is returned after the expected return day but still within
#      the same calendar month and year as the expected return date, fine = 15
#      Hackos x (the number of days late).
#   3. If the book is returned after the expected return month but still
#      within the same calendar year as the expected return date, the fine =
#      500 Hackos x (the number of months late).
#   4. If the book is returned after the calendar year in which it was
#      expected, there is a fixed fine of 10000 Hackos.
#
# Enter your code here. Read input from STDIN. Print output to STDOUT


def calculate_fine(rd, ed):
    if rd[2] > ed[2]:
        return 10000
    elif rd[2] == ed[2] and rd[1] > ed[1]:
        return 500*(rd[1] - ed[1])
    elif rd[2] == ed[2] and rd[1] == ed[1] and rd[0] > ed[0]:
        return 15*(rd[0] - ed[0])
    else:
        return 0


return_date = list(map(int, input().split()))
expected_date = list(map(int, input().split()))
fine = calculate_fine(return_date, expected_date)
print(fine)
