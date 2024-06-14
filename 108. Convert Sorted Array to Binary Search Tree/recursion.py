# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

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
             root = TreeNode(nums[(l + r) // 2])
             root.left = helper(l,((l + r) // 2) - 1 )
             root.right = helper(l + 1,r)
             return root
        helper(0,len(nums) - 1)
        


sortedArrayToBST([-10,-3,0,5,9])