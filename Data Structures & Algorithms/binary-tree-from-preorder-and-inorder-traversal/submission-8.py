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
        # determine the index of the 'pivot' from the inorder tree
        idx = inorder.index(value)

        # preorder [1, 2, 3, 4]        < 2) and also splits the preorder left/right trees like this
        #           \ [2], [3, 4]
        # inorder  [2, 1, 3, 4]        < 1) the pivot splits the inorder left/right trees like so
        #          [2] . [3, 4]   
        root = TreeNode(value)
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root