def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        zeroPointer = m
        p1 = 0
        for i in range(n):
            while( (p1 != zeroPointer) and (nums1[p1] < nums2[i])):
                  p1 += 1
            for j in range(zeroPointer - p1 ):
                  nums1[zeroPointer - j] = nums1[zeroPointer - j - 1]
            nums1[p1] = nums2[i]
            zeroPointer += 1



merge([1],1,[],0)
