def mySqrt( x):
        """
        :type x: int
        :rtype: int
        """

        l = 0
        r = x/2
        mid = 0
        res = 0
        while(l <= r):
            mid = int((l + r + 1)/2)
            if((mid * mid) == x):
                  return mid
            if((mid * mid) > x):
                  r = mid - 1
            elif((mid * mid) < x):
                  l = mid + 1
                  res = mid
        return res
print(mySqrt(100))