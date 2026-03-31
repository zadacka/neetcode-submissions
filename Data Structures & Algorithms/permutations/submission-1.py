class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # from itertools import permutations
        # return [list(x) for x in permutations(nums)]
        if len(nums) == 1:
            return [nums]

        result = []
        for idx, num in enumerate(nums):
            rest = [n for i, n in enumerate(nums) if i != idx]
            for permutation in self.permute(rest):
                result.append([num] + permutation)
        return result