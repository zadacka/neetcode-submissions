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
        if head is None:
            return None

        random_map = {None: None}
        h1  = head
        head2 = Node(0, None, None)
        h2 = head2

        while h1:
            h2.val = h1.val
            if h1.next:
                h2.next = Node(0, None, None)
            else:
                h2.next = None
            
            random_map[h1] = h2
            
            h1 = h1.next
            h2 = h2.next
        
        h1 = head
        h2 = head2
        while h1:
            h2.random = random_map[h1.random]
            h1 = h1.next
            h2 = h2.next
        
        return head2