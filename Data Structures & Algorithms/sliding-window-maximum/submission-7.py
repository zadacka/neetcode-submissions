class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l = 0
        import heapq
        heapq.heapify(h := [])
        for r, num in enumerate(nums):
            heapq.heappush(h, (-num, r))
            print(f'{l}, {r}, {k}')
            if (r - l + 1) == k:
                print('here')
                while h[0][1] <  l:
                    _ = heapq.heappop(h) 
                result.append(-h[0][0])
                l += 1
        return result