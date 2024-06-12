# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
#MEMORY LIMIT EXCEEDED IN ONE TESTCASE
# can increase recursion depth by sys.setrecursionlimit() 

#Tail recursion: recursion where recursive statement is last statement of func. nothing else to do afterware\ds

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    def helper(s):
        if s == "":
            return True
        return s[0] == s[-1] and helper(s[1:len(s) - 1])

    s = [c.lower() for c in s if c.isalnum()]
    return helper("".join(s))

