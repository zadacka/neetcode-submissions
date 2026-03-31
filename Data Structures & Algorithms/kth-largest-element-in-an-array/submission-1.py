class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k:
                _ = heapq.heappop(h)
        return h[0]