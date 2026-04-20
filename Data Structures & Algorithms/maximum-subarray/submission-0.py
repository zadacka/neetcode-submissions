class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        current = 0
        for num in nums:
            if current < 0:
                current = 0
            current += num
            result = max(result, current)
        return result