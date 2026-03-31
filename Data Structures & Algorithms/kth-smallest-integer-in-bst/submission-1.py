# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
    #     def dfs(node, kth):
    #         if node is None:
    #             return None, kth
            
    #         val, lk = dfs(node.left, kth)
    #         if val:
    #             return val, None
            
    #         kth = lk + 1
    #         if kth == k:
    #             return node.val, None

    #         val, rk = dfs(node.right, kth)
    #         if val:
    #             return val, None

    #         return None, rk 
        
    #     val, _ = dfs(root, 0)
    #     return val
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root
        
        while curr or stack:
            # descend left if you can
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # can't descend left, take a step back up and check
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            
            # prepare to descend right
            curr = curr.right

