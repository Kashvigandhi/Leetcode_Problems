# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# In this approach, we create an empty dictionary. We loop through the given array and check if the element is a key in the dictionary. if not we add its complement(target-element) as the key to the dictionary and the index of the element as the value.
# This means that when we encounter that complement in the array and check the dictionary for its presence and find it,we have both required indices: one is stored as the value of the complement in the dictionary and the other is of the element being currently visited in the loop.
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index,element in enumerate(nums):
            if(element in dict):
                return [dict[element],index]
            dict[target - element] = index

print("twoSum:",twoSum([2,7,15,22,1],22))
# For eg, to find two numbers whose sum is 22 in the above array, we start by looping through the array. nums[0] = 2 and is not in dict and we add its complement(22-2=20) to the dict 
# as the key and the index of 2 (0) as the value. If we encounter 4 later, we know the index of its complement is in the dict. Same goes for every element. When we add 7's complement(22-7=15) tp the dict
# and then encounter 15, we find that 15 is in dict and return the index of 7 and 15.