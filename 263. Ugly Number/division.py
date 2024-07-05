# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.
def isUgly(n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        while ((n % 5 == 0) or (n % 3 == 0) or (n % 2 == 0)):
            if (n % 2 == 0):
                n = n//2
            if (n % 3 == 0):
                n = n//3
            if (n % 5 == 0):
                n = n//5
        return n == 1
print(isUgly(14))
        