# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth_recursive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([root])
        level = 0
        while q:
            level += 1
            for i in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return level

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        result = 0
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1]) 
                stack.append([node.right, depth + 1])
        return result  