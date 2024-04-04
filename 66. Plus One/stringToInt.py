def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if(digits[-1] != 9):
            digits[-1] += 1
            return digits
        else:
            digits = map(str,digits)
            num = (int)(''.join(digits))
            num += 1
            res = [int(i) for i in str(num)]
            return res


        
print(plusOne([1,2,9]))