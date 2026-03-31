class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_guess = max(piles)
        min_guess = 0

        import math 
        while True:
            mid_guess = min_guess + (max_guess - min_guess) // 2
            print(f"{max_guess}, {min_guess} ... and {mid_guess}")
            time = sum(math.ceil(p / mid_guess) for p in piles)

            if time > h:
                min_guess = mid_guess
            else:
                max_guess = mid_guess
            
            if min_guess + 1 == max_guess:
                return max_guess