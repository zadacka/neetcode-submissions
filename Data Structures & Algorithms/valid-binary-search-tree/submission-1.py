# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node is None:
                return None, None, True
            
            lmin, lmax, lvalid = dfs(node.left)
            rmin, rmax, rvalid = dfs(node.right)

            if (lvalid and rvalid) and (lmax is None or lmax < node.val) and (rmin is None or rmin > node.val):
                return lmin or node.val, rmax or node.val,  True
            
            return None, None, False
        
        _, __, valid = dfs(root)
        return valid
