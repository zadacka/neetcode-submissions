import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [s for s in stones]
        heapq.heapify_max(heap)
        while len(heap) > 1:
            largest = heapq.heappop_max(heap)
            second_largest = heapq.heappop_max(heap)
            difference = largest - second_largest
            if difference > 0:
                heapq.heappush_max(heap, difference)
        return heap[0] if heap else 0