class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            l_height = heights[l]
            r_height = heights[r]
            area = (r - l) * min(l_height, r_height)
            max_area = max(max_area,  area)
            if l_height < r_height:
                l += 1
            else:
                r -= 1
        return max_area