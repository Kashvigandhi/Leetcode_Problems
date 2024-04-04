import tracemalloc


def mySqrt( x):
        """
        :type x: int
        :rtype: int
        """
        if(x == 0):
              return 0
        for i in range(x):
            if (i * i == x):
                  return i
            if((i+1) * (i+1) == x):
                  return i+1
            if((i * i < x) and ((i + 1) * (i + 1) > x)):
                  return i
tracemalloc.start()
print(mySqrt(2147395599))
print(tracemalloc.get_traced_memory())
