class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    l = []
    def helper(root):
        if root != None:
            helper(root.left)
            helper(root.right)
            l.append(root.val)
    helper(root)
    return l
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
print(postorderTraversal(node1))
