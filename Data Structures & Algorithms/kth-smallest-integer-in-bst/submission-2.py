# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        
        def dfs(node):
            if node is None:
                return None
            l = dfs(node.left)
            if l:
                return l
            nonlocal n 
            n += 1
            if n == k:
                return node.val
            r = dfs(node.right)
            if r:
                return r

        return dfs(root)            

        

        