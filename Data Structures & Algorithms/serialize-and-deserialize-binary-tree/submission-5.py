# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# AAAAGH - attempt with inorder/preorder is (1) too complex an (2) breaks because we can have repeating nodes


class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []
        def dfs(node):
            nonlocal preorder
            if node is None:
                preorder.append('N')
            else:
                preorder.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ','.join(preorder)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')
        idx = 0
        # I neded to look this up ... we use an index which we move across the preorder list as the dfs continues
        def dfs():
            nonlocal idx
            if preorder[idx] == 'N':
                idx += 1
                return None
            else:
                node = TreeNode(int(preorder[idx]))
                idx += 1
                node.left = dfs()
                node.right = dfs()
                return node
        return dfs()