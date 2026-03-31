# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None and root2 is not None:
        return False
    if root1 is not None and root2 is None:
        return False
    if root1.val != root2.val:
        return False
    l1, r1 = (root1.left, root1.right) if root1 else (None, None)
    l2, r2 = (root2.left, root2.right) if root2 else (None, None)
    return same_tree(l1, l2) and same_tree(r1, r2)

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return False
            if same_tree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)