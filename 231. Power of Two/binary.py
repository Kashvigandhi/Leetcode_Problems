# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.
#Time: O(log n)
# Space: O(1)
def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    return str(bin(n)).count("1") == 1
print(isPowerOfTwo(12))

#using & operator:
# This is better as time and space comp both : O(1)
def isPowerOfTwo1(n):
    """
    :type n: int
    :rtype: bool
    """
    return n > 0 and (n & (n-1) == 0)
print(isPowerOfTwo1(16))