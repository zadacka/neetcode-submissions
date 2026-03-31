class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        volume = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                l_max = max(l_max, height[l])
                volume += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                volume += r_max - height[r]
        return volume