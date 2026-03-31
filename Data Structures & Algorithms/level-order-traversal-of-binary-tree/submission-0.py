# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        from collections import deque
        q = deque([(root, 0)])
        result = []
        # breadth first search 
        while q:
            node, level = q.popleft()
            if len(result) > level:
                result[level].append(node.val)
            else:
                result += [[node.val]]
            
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return result