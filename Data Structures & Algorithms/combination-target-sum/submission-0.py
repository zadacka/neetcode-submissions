class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, cur, total):
            if total == target:  # found a solution
                result.append(cur.copy())
                return # index out of range or target overshot 
            if total > target or i == len(nums):
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        print(result)
        return result