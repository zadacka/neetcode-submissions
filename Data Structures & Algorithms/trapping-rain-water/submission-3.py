class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[0], height[-1]
        volume = 0
    
        while l != r:
            if height[l] < height[r]:
                l += 1
                h = height[l]
                max_l = max(max_l, h)
            else:
                r -= 1
                h = height[r]
                max_r = max(max_r, h)
            print(f"{h} ... {max_l}, {max_r}")
            volume += max(0, min(max_l, max_r) - h)
        return volume