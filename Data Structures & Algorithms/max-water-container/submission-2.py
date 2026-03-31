class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_volume = 0
        while l != r:
            this_volume = min(heights[l], heights[r]) * (r - l)
            max_volume = max(max_volume, this_volume)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -=1
        return max_volume
        