# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
def summaryRanges(nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        if len(nums) == 1: return [str(nums[0])]
        ranges = []
        a = b = nums[0]
               
        for num in nums[1::]:
                if (num - b == 1): b = num
                else:
                    if (a == b): 
                           ranges.append(str(a))
                    else:
                           ranges.append(f"{a}->{b}")
                    a = b = num
        if (a == b): 
            ranges.append(str(a))
        else:
                ranges.append(f"{a}->{b}")
        return ranges
print(summaryRanges([1,3,4]))

                