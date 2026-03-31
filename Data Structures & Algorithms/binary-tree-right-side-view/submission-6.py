# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:
        "thought process: do BFS and append the rightmost item in each 'level' to the result"
        result = []
        q = collections.deque()
        q.append(root)
        while q:
            items_in_level = len(q)
            level = []
            for _ in range(items_in_level):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level[-1])
        return result

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node, depth):
            if node:
                if len(result) == depth:  # we descent on the right, so each new depth will always be the rightmost node
                    result.append(node.val)
                dfs(node.right, depth+1)
                dfs(node.left, depth+1)
        dfs(root, 0)
        return result
