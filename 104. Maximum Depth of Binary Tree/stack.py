# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#Time and Space complexity both O(n)
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    depths = []
    nodes = [[root,1]]
    while(len(nodes) != 0):
        node,depth = nodes.pop()
        if(not node.left and not node.right):
            depths.append(depth)
        else:
            if node.right : nodes.append([node.right,depth + 1]) 
            if node.left : nodes.append([node.left,depth + 1]) 
    return max(depths)

root = TreeNode(3)
node1_left = TreeNode(9)
node1_right = TreeNode(20)
# node2_left = TreeNode(15)
node2_right = TreeNode(7)
# node3_left = TreeNode(4)
# node3_right = TreeNode(3)

# Link the nodes to form the tree
root.left = node1_left
root.right = node1_right
# node1_right.left = node2_left
node1_right.right = node2_right
# node1_right.left = node3_left
# node1_right.right = node3_right

print(maxDepth(root))