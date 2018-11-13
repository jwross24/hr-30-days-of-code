# To solve this challenge, we must first take each character in s, enqueue it
# in a queue, and also push that same character onto a stack. Once that's done,
# we must dequeue the first character from the queue and pop the top character
# off the stack, then compare the two characters to see if they are the same;
# as long as the characters match, we continue dequeueing, popping, and
# comparing each character until our containers are empty (a non-match means s
# isn't a palindrome).
#
# Write the following declarations and implementations:
#
#   1. Two instance variables: one for your stack, and one for your queue.
#   2. A void pushCharacter(char ch) method that pushes a character onto a
#      stack.
#   3. A void enqueueCharacter(char ch) method that enqueues a character in
#      the queue instance variable.
#   4. A char popCharacter() method that pops and returns the character at the
#      top of the stack instance variable.
#   5. A char dequeueCharacter() method that dequeues and returns the first
#      character in the queue instance variable.


class Solution:
    # Write your code here
    stack = []
    queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.insert(0, ch)

    def popCharacter(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def dequeueCharacter(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop()


# Read the string s
s = input()
# Create the Solution class object
obj = Solution()

string_len = len(s)
# Push/enqueue all the characters of string s to stack
for i in range(string_len):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
1. Pop the top character from stack
2. Dequeue the first character from queue
3. Compare both the characters
'''
for i in range(string_len // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# Finally, print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
