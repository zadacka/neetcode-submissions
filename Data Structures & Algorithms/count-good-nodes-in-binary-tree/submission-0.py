# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def count_good(node, current_max):
            if not node: return 0
            good = 1 if node.val >= current_max else 0
            new_max = max(node.val, current_max)
            return good + count_good(node.left, new_max) + count_good(node.right, new_max)
        return count_good(root, -math.inf)