# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_seen = -math.inf
        def dfs(node):
            if node is None:
                return 0
            nonlocal max_seen
            left_tree = max(dfs(node.left), 0)
            right_tree = max(dfs(node.right), 0)
            max_seen = max(max_seen, node.val + left_tree + right_tree)
            return node.val + max(left_tree, right_tree)

        dfs(root)
        return max_seen