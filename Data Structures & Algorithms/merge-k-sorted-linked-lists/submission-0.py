# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(l1, l2):
    dummy = ListNode()
    head = dummy
    h1, h2 = l1, l2
    while h1 or h2:
        if h1 and h2:
            if h1.val < h2.val:
                head.next = h1
                h1 = h1.next
            else:
                head.next = h2
                h2 = h2.next
            head = head.next
        elif h1:
            head.next = h1
            return dummy.next
        elif h2:
            head.next = h2
            return dummy.next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode(-1001, None)
        for l in lists:
            result = merge(l, result)
        return result.next
        