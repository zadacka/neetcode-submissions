# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy  = ListNode()
        curr = dummy
        while lists:
            smallest = ListNode(math.inf)
            small_idx = 0
            for idx, node in enumerate(lists):
                if node.val < smallest.val:
                    smallest = node
                    small_idx = idx
            curr.next = smallest
            curr = smallest
            lists[small_idx] = smallest.next
            lists = [l for l in lists if l]
        return dummy.next
            