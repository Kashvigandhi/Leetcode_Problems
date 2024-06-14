# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def dfs(root):
        if not root: return 0
        left = dfs(root.left)
        right = dfs(root.right)
        if left == 0 : left = right
        if right == 0 : right = left
        return (min(left, right)) + 1
    return dfs(root)
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
print(minDepth(root))