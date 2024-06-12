# You are given two integers n and k.

# Initially, you start with an array a of n integers where a[i] = 1 for all 0 <= i <= n - 1. After each second, you simultaneously update each element to be the sum of all its preceding elements plus the element itself. For example, after one second, a[0] remains the same, a[1] becomes a[0] + a[1], a[2] becomes a[0] + a[1] + a[2], and so on.

# Return the value of a[n - 1] after k seconds.

# Since the answer may be very large, return it modulo 109 + 7.
def valueAfterKSeconds( n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        a = [1 for i in range(n)]
        for i in range(k):
            for j in range(1,n):
                  a[j] = a[j] + a[j - 1]
        return a


                



valueAfterKSeconds(5,1)