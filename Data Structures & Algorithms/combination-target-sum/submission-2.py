class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx:int, curr:list, total:int) -> None:

            # base case: we have a hit!
            if total == target:
                result.append(curr.copy())
                return

            # another base case: we have overshot or our idx is out of bounds
            if total > target or idx == len(nums):
                return

            # left path: try adding nums[idx] again
            curr.append(nums[idx])
            dfs(idx, curr, total + nums[idx])

            # right path: nix that, try adding nums[idx+1]
            curr.pop()
            dfs(idx + 1, curr, total)

        # kick off the dfs
        dfs(0, [], 0)
        return result