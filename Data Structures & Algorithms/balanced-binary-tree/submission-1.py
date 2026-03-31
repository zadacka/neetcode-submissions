# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced_alex(self, root: Optional[TreeNode]) -> bool:

        def descend(node):
            if node is None:
                return 0
            l = descend(node.left)
            r = descend(node. right)
            if abs(l - r) > 1:
                raise ValueError
            return 1 + max(l, r)
        
        if root is None:
            return True
        
        try:
            _ = descend(root)
        except ValueError as e:
            return False
        return True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right [0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]