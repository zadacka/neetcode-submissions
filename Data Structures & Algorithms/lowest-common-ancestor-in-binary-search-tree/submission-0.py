# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        a, b = min(p.val, q.val), max(p.val, q.val)
        if a <= root.val <= b:
            return root
        newroot = root.left if a < root.val else root.right
        return self.lowestCommonAncestor(newroot, p, q)
