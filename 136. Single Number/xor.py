def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res = res ^ n
        return res

print(singleNumber([1,2,2]))