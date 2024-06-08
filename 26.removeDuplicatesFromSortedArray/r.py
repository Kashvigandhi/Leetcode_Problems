# # Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# # Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# # Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# # Return k.

def removeDuplicates(nums):
    l = 1
    for r in range(1,len(nums)):
        # print(nums[l:r+1])
        if(nums[r] != nums[r - 1]):
            nums[l] = nums[r]
            l += 1
    print(nums)
    return l
        


print(removeDuplicates([1,1,2,2,2,3,4]))
