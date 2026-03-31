# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node):
            nonlocal result  # update nonlocal with result as we go through dfs
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            result = max(result, left + right)
            return 1 + max(left, right)
        
        dfs(root)  # make sure we call dfs!
        return result