class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result  = [[]]
        nums.sort()
        for num in nums:
            result += [[num] + r for r in result]
        return list(set(tuple(r) for r in result))