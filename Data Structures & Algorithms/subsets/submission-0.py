from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for r in range(len(nums) + 1):
            result += list(combinations(nums, r))
        return [list(x) for x in result]