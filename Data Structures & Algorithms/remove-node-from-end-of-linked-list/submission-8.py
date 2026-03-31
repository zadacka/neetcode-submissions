# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # reverse the list
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        end = prev

        # walk back and count position, keeping track of prev
        pos = 1
        curr = end
        while pos != n:
            prev = curr
            curr = curr.next
            pos += 1

        # snip out the bad node
        if pos != 1:
            prev.next = curr.next
        else:
            end = end.next

        # reverse the list again
        prev = None
        curr = end
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
