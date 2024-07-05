class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while (9 - num < 0):
            sum = 0
            while num:
                lastDigit = num % 10
                sum += lastDigit
                num = num // 10
            num = sum
        return num
        
        