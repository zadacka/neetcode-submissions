class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.previous = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key to Node
        # left is oldest, right is newest
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.previous = self.right, self.left

    def remove(self, node):
        node.previous.next, node.next.previous = node.next, node.previous

    def insert(self, node):
        previous = self.right.previous
        self.right.previous = node
        previous.next = node
        node.previous = previous
        node.next = self.right

    def get(self, key: int) -> int:
        print(f"getting {key} from {self.cache}")
        if key in self.cache:
            # update LRU
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            oldest = self.left.next
            print(f"evicting {oldest.key} from {self.cache}")
            del self.cache[oldest.key]
            self.remove(oldest)
        
