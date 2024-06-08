def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        candidate = nums[0]
        counter = 0
        for num in nums:
            if(counter == 0):
                candidate = num
                counter += 1
            else:
                if(candidate == num):
                    counter += 1
                else:
                    counter -= 1
            if counter == 2:
                 return True
        return False
print(containsDuplicate([1,2,3,4]))
              
            