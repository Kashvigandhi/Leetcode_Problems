def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashset = {}
        for i,n in enumerate(nums):
                print(hashset)
                if n in hashset:
                        if any(abs(index - i) <= k for index in hashset[n]):
                                return True
                        hashset[n].append(i)
                else:
                        hashset[n] = [i]
        return False

print(containsNearbyDuplicate([1,2,3,1],3))
