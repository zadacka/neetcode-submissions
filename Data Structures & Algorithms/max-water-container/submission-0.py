class Solution:
    def maxArea(self, heights: List[int]) -> int:
        from itertools import combinations
        max_area = 0

        for start, end in combinations(range(len(heights)), 2):
            area = min(heights[start], heights[end]) * (end - start)
            max_area = max(max_area, area)
        return max_area