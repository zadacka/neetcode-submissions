# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid_bst(node, lower, upper):
            if node is None:
                return True
            return (lower < node.val < upper) and valid_bst(node.left, lower, node.val) and valid_bst(node.right, node.val, upper)
        return valid_bst(root, -math.inf, math.inf)
