class Solution:
    def trap2(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = [0 for _ in height]
        
        while l < r:
            best = min(height[l], height[r])
            for idx in range(l+1, r):
                max_water[idx] = max(max_water[idx], best)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        result = 0
        for water, bar in zip(max_water, height):
            if water > bar:
                print(f"{water - bar}")
                result += water - bar
            else:
                print("nothing")
        
        return result

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) -1 
        left_max, right_max = height[l], height[r]
        result = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                result += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                result += right_max - height[r]
        return result