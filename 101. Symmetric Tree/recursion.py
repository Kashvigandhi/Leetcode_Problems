# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def helper(left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and helper(left.left,right.right) and helper(left.right,right.left)
    return helper(root.left,root.right)

root = TreeNode(1)
node1_left = TreeNode(2)
node1_right = TreeNode(2)
node2_left = TreeNode(3)
node2_right = TreeNode(4)
node3_left = TreeNode(4)
node3_right = TreeNode(3)

# Link the nodes to form the tree
root.left = node1_left
root.right = node1_right
node1_left.left = node2_left
node1_left.right = node2_right
node1_right.left = node3_left
node1_right.right = node3_right

print(isSymmetric(root))