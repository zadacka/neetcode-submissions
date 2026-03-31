# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Note: 
# fast and slow pointers is a nicer way to do this that doesn't screw upd the list as it 
# goes through!!

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        SEEN = object()
        while head:
            if head.next is SEEN:
                return True
            head.next, head = SEEN, head.next

        return False