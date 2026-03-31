# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 and root2 and root1.val == root2.val:
        return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)
    return False

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)