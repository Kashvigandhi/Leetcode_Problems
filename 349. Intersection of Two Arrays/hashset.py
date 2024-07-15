class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen = set(nums1)
        intersection = []
        for n in nums2:
            if n in seen:
                intersection.append(n)
                seen.remove(n)
        return intersection
