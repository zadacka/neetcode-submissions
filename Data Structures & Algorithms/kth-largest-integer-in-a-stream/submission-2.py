from collections import deque
from heapq import heapify, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-n for n in nums] # maxheap
        heapify(self.heap)        

    def add(self, val: int) -> int:
        heappush(self.heap, -val)
        popped = []
        for _ in range(self.k):
            popped.append(heappop(self.heap))
        result = -popped[-1]
        for p in popped:
            heappush(self.heap, p)
        return result

