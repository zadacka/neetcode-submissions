class Solution:
    def maxArea1(self, heights: List[int]) -> int:
        from itertools import combinations
        max_area = 0

        for start, end in combinations(range(len(heights)), 2):
            area = min(heights[start], heights[end]) * (end - start)
            max_area = max(max_area, area)
        return max_area

    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0
        while l < r:
            area = min(heights[l] , heights[r]) * (r-l)
            result = max(result, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result