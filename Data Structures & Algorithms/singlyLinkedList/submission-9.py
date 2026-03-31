
class Node():
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        h = self.head.next
        for _ in range(index):
            h = h.next if h else None
        return -1 if h is None else h.val
        
    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head.next)
        self.head.next = new_node
        if new_node.next is None:
            # list was empty
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        h = self.head
        for _ in range(index): # nice - start on dummy node
            h = h.next

        if h and h.next:
            if h.next == self.tail:
                self.tail = h
            h.next = h.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        values = []
        h = self.head.next
        while h:
            values.append(h.val)
            h = h.next
        return values
        
