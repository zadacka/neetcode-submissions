class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        potential_depth = [0] * len(height)
        l, r = 0, len(height) - 1
        while l < r:
            l_height = height[l]
            r_height = height[r]
            l_highest = l_height if l == 0 else max(l_height, potential_depth[l-1])
            r_highest = r_height if r == len(height) - 1 else max(r_height, potential_depth[r+1])
            wall_height = min(l_highest, r_highest)
            potential_depth[l] = l_highest
            potential_depth[r] = r_highest
            if l_height < r_height:
                l += 1
            else:
                r -= 1
        result = 0
        for wall, depth in zip(height, potential_depth):
            result += depth - wall
        return result