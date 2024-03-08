# Given an integer x, return true if x is a palindrome and false otherwise.
# In this two pointer method, we convert the integer to a string. Then, we declare 2 pointers.
# The first will point to the first character while the other will point to the last character in the string
# We apply a while loop with the condition pointer1 != pointer2 and pointer1 < pointer2. This ensures that the loop terminates both when 
# the string has even number as well odd number of characters.
# This is better than the recursion method as it uses constant space
# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        pointer1 = 0
        pointer2 = len(x) - 1
        while(pointer1 != pointer2 and pointer1 < pointer2):
            if(x[pointer1] != x[pointer2]):
                return False

            else:
                pointer1 += 1
                pointer2 -= 1
        return True

print(Solution().isPalindrome(122))