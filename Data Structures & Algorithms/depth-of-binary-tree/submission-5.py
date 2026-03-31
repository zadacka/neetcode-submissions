# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def find_depth(node, current_depth):
            if node is None:
                return current_depth
            current_depth += 1
            print(f"node with val {node.val} has depth {current_depth}")
            return max(find_depth(node.left, current_depth), find_depth(node.right, current_depth))
        
        return find_depth(root, 0) 
