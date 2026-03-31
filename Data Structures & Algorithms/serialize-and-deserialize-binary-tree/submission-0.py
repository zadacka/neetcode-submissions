# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            if node is None:
                result.append('N')
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(result)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        idx = 0

        def dfs():
            nonlocal idx 
            if vals[idx] == 'N':
                idx += 1
                return None
            node = TreeNode(int(vals[idx]))
            idx += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()