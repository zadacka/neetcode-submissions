# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def __init__(self):
        self.max_diameter = 0

    def node_height(self, root):
        if root is None:
            return 0
        l = self.node_height(root.left)
        r = self.node_height(root.right)
        self.max_diameter = max(self.max_diameter, r+l)
        return 1 + max(r, l)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _ = self.node_height(root)
        return self.max_diameter