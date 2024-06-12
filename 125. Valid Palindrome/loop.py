# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = [c.lower() for c in s if c.isalnum()]
    for i in range(int(len(s)/2)):
        if(s[i] != s[len(s) - i - 1]):
            return False
    return True

print(isPalindrome("A maman"))
