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
