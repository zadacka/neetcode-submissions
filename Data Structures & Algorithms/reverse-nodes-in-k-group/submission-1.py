# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_previous = dummy

        while True:
            kth = self.get_kth(group_previous, k)
            if not kth:
                break
            
            group_next = kth.next

            # reverse group
            prev, curr = group_next, group_previous.next  # sneaky! prev initialised to 'special' group_next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # special fix-up to point previous at kth
            temp = group_previous.next
            group_previous.next = kth
            # and group_previous needs to point at the thing before the next group, for the next go-around...
            group_previous = temp

        return dummy.next


    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -=1
        return curr