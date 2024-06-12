def numberOfChild( n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if(k < n):
            return k
        division = k // (n-1)
        remainder = k % (n-1)
        print(division,remainder)
        if(division % 2 == 0):
            return remainder
        else:
            return n - 1 - remainder
        

print(numberOfChild(5,5))