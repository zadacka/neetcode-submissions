class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        minheap = []
        for num in nums:
            heapq.heappush(minheap, num)
            if len(minheap) > k:
                _ = heapq.heappop(minheap)
        return heapq.heappop(minheap)
        