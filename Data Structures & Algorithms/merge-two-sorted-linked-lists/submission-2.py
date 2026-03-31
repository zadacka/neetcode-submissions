# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        this = head
        
        while list1 or list2:
            if list1 is None:
                this.next = list2
                this = list2
                list2 = list2.next
            elif list2 is None:
                this.next = list1
                this = list1
                list1 = list1.next
            elif list1.val < list2.val:
                this.next = list1
                this = list1
                list1 = list1.next
            else:
                this.next = list2
                this = list2
                list2 = list2.next
        return head