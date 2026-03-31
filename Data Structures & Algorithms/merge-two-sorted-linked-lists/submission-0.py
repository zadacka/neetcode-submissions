# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        if h1 and not h2:
            return h1
        if h2 and not h1:
            return h2

        current = ListNode()
        result = current

        while h1 or h2:
            if h1 and h2:
                if h1.val <= h2.val:
                    current.next = h1
                    current = h1
                    h1 = h1.next
                else:
                    current.next = h2
                    current = h2
                    h2 = h2.next
            elif h1:
                current.next = h1
                current = h1
                h1 = h1.next
            else:
                current.next = h2
                current = h2
                h2 = h2.next
        return result.next