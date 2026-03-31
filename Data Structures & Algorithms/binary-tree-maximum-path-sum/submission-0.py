# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best_seen = -math.inf

        def dfs(node):
            best_left = dfs(node.left) if node.left else 0
            best_right = dfs(node.right) if node.right else 0
            best_here = max(node.val, node.val + best_left, node.val + best_right, node.val + best_left + best_right)
            nonlocal best_seen
            best_seen = max(best_seen, best_here)
            return max(node.val, node.val + best_left, node.val + best_right)

        dfs(root)
        return best_seen