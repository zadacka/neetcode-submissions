from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result = []
        # for r in range(len(nums) + 1):
        #     result += list(combinations(nums, r))
        # return [list(x) for x in result]
        result = []
        subset = []
        def dfs(i):
            if i == len(nums):
                result.append(subset.copy())
                return result
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return result