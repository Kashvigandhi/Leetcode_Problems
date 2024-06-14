# Given a binary tree, determine if it is height-balanced.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def helper(root):
        if not root:
            return [True, 0]
        left, right = helper(root.left), helper(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1 + max(left[1], right[1])]
    return helper(root)[0]
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)

print(isBalanced(root))