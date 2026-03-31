"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList_alex(self, head: 'Optional[Node]') -> 'Optional[Node]':
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

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {None: None}
        this = head
        dummy = Node(0)
        while this:
            new_node = Node(this.val)
            node_map[this] = new_node
            this = this.next
        
        this = head
        while this:
            new_node = node_map[this]
            new_node.next = node_map[this.next]
            new_node.random = node_map[this.random]
            this = this.next
        return node_map[head]