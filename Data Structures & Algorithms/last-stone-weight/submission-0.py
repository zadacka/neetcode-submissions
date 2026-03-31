class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        import heapq
        maxheap = [-1 * s for s in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            x = heapq.heappop(maxheap) * -1
            y = heapq.heappop(maxheap) * -1
            if x != y:
                heapq.heappush(maxheap, -1 * (x - y))
        
        return maxheap[0] * -1 if maxheap else 0

