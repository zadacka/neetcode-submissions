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
        root = TreeNode(value)

        pivot = inorder.index(value)
        inorder_left = inorder[:pivot]
        inorder_right = inorder[pivot + 1:]

        left_tree_size = len(inorder_left)
        preorder_left = preorder[1:left_tree_size+1]
        preorder_right = preorder[left_tree_size+1:]
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root