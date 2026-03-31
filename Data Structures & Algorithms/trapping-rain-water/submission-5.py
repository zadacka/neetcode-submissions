class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        volume = 0
        while l < r:
            if height[l] < height[r]:  # trick: always move the smaller one
                l += 1
                l_max = max(l_max, height[l])  # trick: l_max is min(l_max, r_max)!
                volume += l_max - height[l]  # trick: height[l] <= l_max, so delta never -ve
            else:
                r -= 1
                r_max = max(r_max, height[r])
                volume += r_max - height[r]
        return volume