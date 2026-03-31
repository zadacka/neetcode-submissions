# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd_alexIsSilly(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Trick #1: use a dummy node so we can simply handle edge cases like a one element list
        dummy = ListNode(0, head)

        l = dummy
        r = head

        # trick #2, move r 'n' places ahead
        for _ in range(n):
            r = r.next
        
        # trick #3 ... now when r reached 'end', l must be 'end-n' places through!
        while r:
            l = l.next
            r = r.next

        # skip the node to remove
        l.next = l.next.next

        # and return from the dummy node as the 'safe starting point'
        return dummy.next

        
