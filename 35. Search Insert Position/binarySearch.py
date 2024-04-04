def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        mid = 0
        while(l <= r):
            mid = int((l + r + 1)/2)
            if(nums[mid] == target):
                    return mid
            elif (nums[mid] > target):
                r = mid - 1
            else:
                l =3
            print("mid",mid)
            print("l",l)
            print("r",r)
        return l
print(searchInsert([1,3,5],2))