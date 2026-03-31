class Solution:
    def trap(self, height: List[int]) -> int:
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