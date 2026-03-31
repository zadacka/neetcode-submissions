import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):        
        self.k = k
        self.h = []
        for num in nums:
            _ = self.add(num)


    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            _ = heapq.heappop(self.h)
        return heapq.nsmallest(1, self.h)[0]

                
