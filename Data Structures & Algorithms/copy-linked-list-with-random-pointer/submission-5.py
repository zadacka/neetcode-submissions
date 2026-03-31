"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """two nicer ways to do this - let's do the map two/one pass approach"""

        if not head:
            return None
        dummy = Node(0, None, None)
        curr1 = head
        curr2 = dummy
        old2new = {}
        while curr1:
            curr2.val = curr1.val
            if curr1.next:
                curr2.next = Node(curr1.val)
            old2new[curr1] = curr2
            curr1, curr2 = curr1.next, curr2.next
        curr1 = head
        curr2 = dummy
        while curr1:
            if curr1.random is None:
                curr2.random = None
            else:
                curr2.random = old2new[curr1.random]
            curr1, curr2 = curr1.next, curr2.next
        return dummy