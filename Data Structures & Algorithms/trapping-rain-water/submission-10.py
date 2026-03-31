class Solution:
    """ my solution here is a strange mix of the 'two pointer' and prefix / suffix approaches
        ... having looked at the options, I prefer the "pure" two-pointer approach
        and it also has the best time/space performance
    """

    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        result = 0
        while l < r:
            if max_l < max_r:  # limited by a low wall on the left
                l += 1
                max_l = max(max_l, height[l])
                result += max_l - height[l]  
                # think:
                # * 0 if this is a new high
                # ... or max_l - lower wall height in which case 
                # ... max_l was already less than max_r and hasn't moved

            else:
                r -= 1
                max_r = max(height[r], max_r)
                result += max_r - height[r]

        return result

    def trap_alex(self, height: List[int]) -> int:
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