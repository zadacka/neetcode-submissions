class Solution:
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        import heapq
        heapq.heapify([]) 
        
        for point in points:
            x, y = point
            d2 = x ** 2 + y ** 2
            heapq.heappush(maxheap, (-d2, point))
            if len(maxheap) > k:
                _ = heapq.heappop(maxheap) # pop the largest
        
        return [pt for _, pt in maxheap]

    def kClosest3(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        import heapq
        for point in points:
            x, y = point
            heapq.heappush(minheap, (x**2 + y ** 2, point))
        return [point for d2, point in heapq.nsmallest(k, minheap)]
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        h = []
        for (x, y) in points:
            r = (x**2 + y**2)**0.5
            heapq.heappush_max(h, (r, x, y))
            if len(h) > k:
                _ = heapq.heappop_max(h)
        return [[x, y] for (r, x, y) in h]