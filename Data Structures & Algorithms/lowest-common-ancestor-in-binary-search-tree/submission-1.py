# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_to_p = []
        path_to_q = []
        def dfs(node, target, path):
            if node is None:
                return False
            
            path.append(node)
            print(f"searching for {target.val} current path is {[p.val for p in path]}")

            if node.val == target.val:    
                return True
            
            if dfs(node.left, target, path) or dfs(node.right, target, path):
                return True
            _ = path.pop()
            return False
        
        dfs(root, p, path_to_p)
        dfs(root, q, path_to_q)
        
        for node in reversed(path_to_p):
            if node.val in set(n.val for n in path_to_q):
                return node
            
        
                
