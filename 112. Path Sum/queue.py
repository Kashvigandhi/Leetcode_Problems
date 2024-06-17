# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.
# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    """
    :type root: TreeNode
    :type targetSum: int
    :rtype: bool
    """
    queue = collections.deque([root])
    # sums = {root: root.val}
    
    while(len(queue) != 0):
        for i in queue:
            print(i.val)
        print("-----------------")
        node = queue.popleft()
  
        if (not node.left and not node.right and node.val == targetSum):
            return True
        if node.left:
            node.left.val += node.val
            queue.append(node.left)
        if node.right:
            node.right.val += node.val
            queue.append(node.right)

    return False
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(hasPathSum(root, 22))
        





        