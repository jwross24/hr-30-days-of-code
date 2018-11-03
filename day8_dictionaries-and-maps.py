# Given  names and phone numbers, assemble a phone book that maps friends'
# names to their respective phone numbers. You will then be given an unknown
# number of names to query your phone book for. For each  queried, print the
# associated entry from your phone book on a new line in the form
# name=phone_number; if an entry for  is not found, print Not found instead.

# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

if __name__ == '__main__':
    phone_book = {}
    n = int(input())
    for i in range(n):
        key, value = input().split()
        phone_book[key] = value

name = ''
while True:
    name = input()
    if not name:
        break
    if name in phone_book:
        print(name + '=' + phone_book[name])
    else:
        print('Not found')
