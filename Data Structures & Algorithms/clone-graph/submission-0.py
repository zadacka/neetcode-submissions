"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = dict()

        def dfs(n):
            if n in node_map:
                return
            copy = Node(n.val)
            node_map[n] = copy
            for neighbor in n.neighbors:
                dfs(neighbor)
                copy.neighbors.append(node_map[neighbor])
        if not node:
            return None
        dfs(node)
        return node_map[node]