# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
             return True
        if not p or not q or p.val != q.val:
             return False
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        



# Creating a sample binary tree
#           1
#         /   \
#        2     3
#       / \   / \
#      4   5 6   7
node1 = TreeNode(1)
node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)
# node6 = TreeNode(6)
# node7 = TreeNode(7)

node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5
# node3.left = node6
# node3.right = node7

node8 = TreeNode(1)
node10 = TreeNode(2)
# node11 = TreeNode(4)
# node12 = TreeNode(5)
# node13 = TreeNode(6)


node8.right = node10
# node10.left = node11
# node11.right = node12
# node12.left = node13


print(isSameTree(node1,node8))
