def minimumOperations(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] == 0:
                for j in nums[i::]:
                    j = 1 - j
                count += 1
        return count
             
        
                        
                
                
                
print(minimumOperations([0,1,1,0,1]))