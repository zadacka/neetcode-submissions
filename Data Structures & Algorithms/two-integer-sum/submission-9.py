class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            sought = target - num
            candidates = set(nums[idx + 1:])
            if sought in candidates:
                idx2 = nums[idx+1:].index(sought) + 1
                return [idx, idx + idx2]