# Consider a database table, Emails, which has the attributes First Name and
# Email ID. Given N rows of data simulating the Emails table, print an
# alphabetically-ordered list of people whose email address ends in @gmail.com.

import re

if __name__ == '__main__':
    N = int(input())

    name_list = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        m = re.search('\w+(?=@gmail.com)', emailID)
        if m is not None:
            name_list.append(firstName)

    name_list.sort()
    [print(name) for name in name_list]
