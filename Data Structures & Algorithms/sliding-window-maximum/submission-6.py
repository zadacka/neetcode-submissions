class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l = 0
        import heapq
        heapq.heapify(h := [])
        for r, num in enumerate(nums, start=1):
            # heapq is a minheap and we want a maxheap
            # so use the standard hack of inserting n*-1
            heapq.heappush(h, (num * -1, r))
            if r >= k: # window is moving now!
                l += 1
                while h[0][1] < l:  # pop max vals where index not in window
                    heapq.heappop(h)
                result.append(h[0][0] * -1)
        return result