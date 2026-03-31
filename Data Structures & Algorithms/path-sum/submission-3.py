# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum_alex(self, root: Optional[TreeNode], targetSum: int) -> bool:        
        
        path = []

        def dfs(node):
            path.append(node.val)
            if node.left is None and node.right is None:
                print(path)
                return sum(path) == targetSum
            if node.left:
                if dfs(node.left):
                    return True
                _ = path.pop()
            if node.right:
                if dfs(node.right):
                    return True
                _ = path.pop()
            return False

        return False if root is None else dfs(root)
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:        
        if root is None:
            return False
        
        targetSum -= root.val
        if self.hasPathSum(root.left, targetSum):
            return True
        if self.hasPathSum(root.right, targetSum):
            return True
        if root.left is None and root.right is None and targetSum == 0:
            return True
        return False