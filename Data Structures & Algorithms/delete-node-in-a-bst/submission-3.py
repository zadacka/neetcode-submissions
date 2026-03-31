# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find_min(root):
    while root.left:
        root = root.left
    return root.val

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key == root.val:
            # simple case
            if root.right is None and root.left is None: return None  # leaf node, no children
            elif root.right is None:                     return root.left  # leaf node, one child
            elif root.left is None:                      return root.right  # leaf node, one child
            else:
                root.val = find_min(root.right)
                root.right = self.deleteNode(root.right, root.val)
                return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root