# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest_dfs(self, root: Optional[TreeNode], k: int) -> int:
        position = 0
        result = None
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            nonlocal position
            position += 1
            if position == k:
                nonlocal result
                result = node.val
            print(node.val, position)
            dfs(node.right)
        dfs(root)
        return result

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        n = 0
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k :
                return curr.val
            curr = curr.right
            