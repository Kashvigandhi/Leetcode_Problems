# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not 0 in nums: return 0
        length = len(nums)
        sum = (length * (length + 1)) / 2
        for i in nums:
                sum = sum - i
        return sum
print(missingNumber([3,2,0,1]))