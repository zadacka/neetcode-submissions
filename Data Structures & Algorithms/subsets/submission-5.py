class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # from itertools import combinations
        # result = []
        # for i in range(len(nums) + 1):
        #     result.extend(list(combo) for combo in combinations(nums, i))
        # return result

        ###################################################################

        # implementing dfs backtracking
        # result = []
        # subset = []
        # def dfs(idx):
        #     if idx == len(nums):
        #         result.append(subset.copy())
        #         return 
        #     # left branch of tree: add the element
        #     subset.append(nums[idx])
        #     dfs(idx + 1)
        #     # right branch of tree: do not add the element
        #     _ = subset.pop()
        #     dfs(idx + 1)
        # dfs(0)
        # return result

        result = [[], ]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result