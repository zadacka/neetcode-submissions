# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        value = preorder[0]
        idx = inorder.index(value)

        # preorder [1, 2, 3, 4]
        #           \ [2], [3, 4]
        # inorder  [2, 1, 3, 4]
        #          [2] . [3, 4]   
        root = TreeNode(value)
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root