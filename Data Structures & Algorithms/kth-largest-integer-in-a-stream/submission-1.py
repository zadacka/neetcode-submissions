import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):        
        self.k = k
        self.minheap = []
        for num in nums:
            _ = self.add(num)


    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        # Insertion checl: ensure minheap stays at length K so the 0th element is always the kth largest
        if len(self.minheap) > self.k:  
            _ = heapq.heappop(self.minheap)
        return self.minheap[0]
