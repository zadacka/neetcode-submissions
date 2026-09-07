from collections import deque
from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [n for n in nums]
        heapify(self.heap)
        while len(self.heap) > k:  # trim the heap to the k largest
            _ = heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap) > self.k:
            _ = heappop(self.heap) # trim the heap again to the k largest
        return self.heap[0]  # min in the heap *is* the k largest!