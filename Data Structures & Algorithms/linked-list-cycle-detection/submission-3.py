# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # this has O(n) space
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        seen_before = set()
        while head:
            if head.next in seen_before:
                return True
            seen_before.add(head)
            head = head.next
        return False
        
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
            if slow == fast:
                return True
        return False
            