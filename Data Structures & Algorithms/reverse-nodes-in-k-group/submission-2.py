# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prevblock = dummy

        while True: 
            r  = prevblock
            for _ in range(k):
                r = r.next
                if r is None: return dummy.next
            nextblock = r.next

            prev, curr = r.next, prevblock.next
            while curr != nextblock:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prevblock.next
            prevblock.next = r
            prevblock = temp

        return dummy.next
                
