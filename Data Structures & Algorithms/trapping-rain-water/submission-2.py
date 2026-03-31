class Solution:
    def trap(self, height: List[int]) -> int:
        height_left = []
        max_left = 0
        for h in height:
            max_left = max(max_left, h)
            height_left.append(max_left)

        max_right = 0
        height_right = []
        for h in reversed(height):
            max_right = max(max_right, h)
            height_right.append(max_right)
        
        # fix em up
        height_left[0] = 0
        height_right = height_right[::-1]
        height_right[-1] = 0

        volume = 0
        for l, r, h in zip(height_left, height_right, height):
            depth = min(l, r) - h
            volume += max(depth, 0)
        return volume