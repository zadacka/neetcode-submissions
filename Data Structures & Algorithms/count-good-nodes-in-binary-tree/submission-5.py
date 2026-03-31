# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes_alex(self, root: TreeNode) -> int:
        " this was my own attempt ... works but uses a global for the count rather than resucrively summing/returning the count"
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

    def goodNodes(self, root: TreeNode) -> int:
        "this is the Neet approach - nicer since it is 'natively' recursive for the  return value"
        def dfs(node, max_seen):
            if node is None:
                return 0
            good_nodes = 1 if max_seen <= node.val else 0
            new_max = max(max_seen, node.val)
            good_nodes += dfs(node.left, new_max)
            good_nodes += dfs(node.right, new_max)
            return good_nodes
        return dfs(root, -math.inf)