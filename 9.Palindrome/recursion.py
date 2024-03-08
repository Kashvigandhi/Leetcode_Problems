# Given an integer x, return true if x is a palindrome, and false otherwise.'
# This approach uses recursion to solve the problem
# We first convert the input into a string. if it is empty, return true since an empty string is a palindrome.
# If it is not empty, we return the boolean of equality of first and last character of the string, as well as the return value of the string by removing the first and last characters.
# Thus, we recursively check each pair of complement characters in the string and return true if the complement pairs are same.
# Time complexity: O(n)
# Space complexity: O(n)
# However, recursion puts extra load on the CPU and is complicated. Other approaches should be used instead.
def isPalindrome(x):
    x = str(x)
    if len(x) == 0:
        return True
    else:
        return x[0] == x[-1] and isPalindrome(x[1:-1])

print(isPalindrome(121))