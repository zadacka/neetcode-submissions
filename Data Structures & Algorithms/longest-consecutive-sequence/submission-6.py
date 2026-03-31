class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        from heapq import heapify, heappop
        heap = [x for x in nums]
        heapify(heap)

        current = heappop(heap)
        length = 1
        max_length = 0
        while(heap):
            smallest = heappop(heap)
            if smallest == current:
                continue
            if smallest == current + 1:
                length += 1
            else:
                max_length = max(length, max_length)
                length = 1
            current = smallest
        max_length = max(length, max_length)
        return max_length