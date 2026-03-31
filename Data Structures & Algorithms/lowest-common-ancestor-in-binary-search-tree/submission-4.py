# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor_alex_not_good_version(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # think! The BST is ordered - so the common ancestor is one where p and q are not both on the same 'side'
        curr = root
        # I had 'while true' here - half iterative and half recursive !o.O!
        if p.val < curr.val and q.val < curr.val:
            return self.lowestCommonAncestor(curr.left, p, q)
        elif p.val > curr.val and q.val > curr.val:
            return self.lowestCommonAncestor(curr.right, p, q)
        else:
            return curr