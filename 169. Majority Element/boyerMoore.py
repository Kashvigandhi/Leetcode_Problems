# https://www.youtube.com/watch?v=M1IL4hz0QrE
# This is boyer-moore voting algo ... don't confuse with boyer-moore search algo
def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        candidate = nums[0]
        for num in nums:
            if(counter == 0):
                candidate = num
                counter += 1
            else:
                if(num == candidate):
                      counter += 1
                else:
                     counter -= 1
        return candidate
print(majorityElement([2,3,2]))
            
                
