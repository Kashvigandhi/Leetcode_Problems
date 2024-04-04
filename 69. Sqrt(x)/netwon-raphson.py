import tracemalloc

def mySqrt( x):
        """
        :type x: int
        :rtype: int
        """
        epsilon = 0.0000005
        guess = x/2
        while(abs(guess**2 - x) >= epsilon):
                guess = guess - (guess**2 - x)/(2*guess)
        return int(guess)
tracemalloc.start()
print(mySqrt(2147395599));            
print(tracemalloc.get_traced_memory())