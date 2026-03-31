class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        result = []
        for i in range(len(nums) + 1):
            result.extend(list(combo) for combo in combinations(nums, i))
        return result