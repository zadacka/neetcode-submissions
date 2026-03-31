# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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