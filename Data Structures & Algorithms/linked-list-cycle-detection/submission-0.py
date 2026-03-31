# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_before = set()
        while head:
            if head.next in seen_before:
                return True
            seen_before.add(head)
            head = head.next
        return False
        