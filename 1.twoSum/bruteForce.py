# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
def twoSum(nums,target):
    for index1 in range(len(nums)):
        for index2 in range(len(nums)):
            if index2+1  < len(nums) and nums[index1] + nums[index2+1] == target:
                return [index1,index2+1]

print("twoSum:",twoSum([2,7,15,22,1],23))

# using brute force to loop through the array to check the sum of each pair of elements for target
# time complexity: 
# outer for loop: O(n)
# inner for loop: O(n)
# Thus, total time: O(n^2)
# Space complexity: O(1) - constant space is used for index1 and index2
# Mistakes:
# 1) cannot mess with indexing of inner loop (eg: for index2 in range(index1+1:len(nums))) as it will give correct element but indexing will be wrong
# 2) index should be kept in range of array length

#Better approach for brute force can be by starting the index2 at index+1 so that we do not have to repeat previous elements. the time and space complexities will remain the same
def twoSum_better(nums,target):
    for index1 in range(len(nums)):
        for index2 in range(index1+1,len(nums)):
            if index2  < len(nums) and nums[index1] + nums[index2] == target:
                return [index1,index2]

print("twoSum_better:",twoSum_better([2,7,15,22,1],22))