class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx:int, curr:list, total:int) -> None:
            if total == target:
                result.append(curr.copy())
                return
            if total > target or idx == len(nums):
                return

            curr.append(nums[idx])
            dfs(idx, curr, total + nums[idx])
            curr.pop()
            dfs(idx + 1, curr, total)

        dfs(0, [], 0)
        return result