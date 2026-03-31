class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the fastest possible time to clear all piles is at speed 
        # m = max(piles), which results in a time of len(piles)
        # so. ... the min speed to beat the time limit h must be
        # between 1 and m 
        l, r = 1, max(piles)
        best = None
        while l <= r:
            speed = (l + r) // 2
            time = sum(math.ceil(p / speed) for p in piles)
            if time <= h:
                r = speed - 1
                best = speed
            else:
                l = speed + 1
        return l