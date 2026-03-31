# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        from collections import deque
        queue = deque(maxlen=n+1)
        ptr = head
        while ptr is not None:
            queue.append(ptr)
            ptr = ptr.next
        
        if len(queue) >= 3:
            queue[0].next = queue[2]
        elif len(queue) == 2:
            queue[0].next = None
        else:
            return None

        if n == len(queue):
            return queue[1]

        return head
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # add a dummy pointer so so that Left is n + 1 separated from Right (as we need to re-map Left's ptr)
        # bonus side-effect, makes this 'just work' for input list of lenth 1 with no 'special case'
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n != 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
        