# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, max_seen):
            nonlocal result
            if node:
                print(f"node {node.val} ... comparing with max_so_far {max_seen}")
                if max_seen <= node.val:
                    result += 1
                dfs(node.left, max(node.val, max_seen))
                dfs(node.right, max(node.val, max_seen))
        dfs(root, -math.inf)
        return result