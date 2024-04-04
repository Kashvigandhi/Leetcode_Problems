# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        curr = root
        while((curr != None) or (len(stack) != 0)):
            while(curr != None):
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
        
             

# Creating a sample binary tree
#           1
#         /   \
#        2     3
#       / \   / \
#      4   5 6   7
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

node8 = TreeNode(1)
s = Solution()
s1 = Solution()
node9 = None
print(s.inorderTraversal(node9))
print(s.inorderTraversal(node1))
print(s1.inorderTraversal(node1))
