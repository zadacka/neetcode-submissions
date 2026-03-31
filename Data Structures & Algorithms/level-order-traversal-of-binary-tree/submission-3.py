# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []
        stack = [(root, 0)]
        if root is None:
            return []
        
        while stack:
            node, level = stack.pop()
            
            # record the level order information
            if len(level_order) < level + 1:
                level_order.append([])
            level_order[level].append(node.val)

            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
            
        return level_order