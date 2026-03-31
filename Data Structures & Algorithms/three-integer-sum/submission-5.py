class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        candidates = combinations(nums, 3)
        correct_sum = [c for c in candidates if sum(c) == 0]
        unique = {tuple(sorted(c)) for c in correct_sum}
        return list(unique)