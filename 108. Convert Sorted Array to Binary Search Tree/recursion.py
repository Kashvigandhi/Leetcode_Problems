# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.
# Time & space comp. : O(n)
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(l, r):
             if l > r:
                  return None
             m = (l + r) // 2
             root = nums[m]
             left = helper(l,m - 1 )
             right = helper(m + 1,r)
             return TreeNode(root,left,right)
        helper(0,len(nums) - 1)
        


sortedArrayToBST([-10,-3,0,5,9])