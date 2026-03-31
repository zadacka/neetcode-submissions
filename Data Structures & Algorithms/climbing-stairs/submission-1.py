class Solution:
    def climbStairs(self, n: int) -> int:
        # thinking this through ... we can reach each step in two ways:
        # the number of permutations of the step two below ... plus
        # the number of permutations to go to the step one below
        # Default the DP array to 1 for the n-2th and n-1th steps...
        cache = [1] * (n + 1)
        for i in range(2, n+1):
            cache[i] = cache[i-2] + cache[i-1]
        return cache[-1]