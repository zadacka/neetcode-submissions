class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l = 0
        import heapq
        h = []
        heapq.heapify(h)
        for r, num in enumerate(nums, start=1):
            heapq.heappush(h, (num * -1, r))
            if r >= k:
                l += 1
                while h[0][1] < l:
                    heapq.heappop(h)
                result.append(h[0][0] * -1)
        return result