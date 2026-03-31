# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        h1 = l1
        h2 = l2

        num1 = 0
        num2 = 0
        while h1:
            num1 = num1 * 10 + h1.val
            h1 = h1.next

        while h2:
            num2 = num2 * 10 + h2.val
            h2 = h2.next

        result = str(int(str(num1)[::-1]) + int(str(num2)[::-1]))
        print(result)

        dummy = ListNode(0, None)
        h3 = dummy
        for char in result[::-1]:
            h3.next = ListNode(0, None)
            h3 = h3.next
            h3.val = int(char)
        return dummy.next
            
        