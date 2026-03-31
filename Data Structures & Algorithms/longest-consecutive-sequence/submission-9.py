class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seen = 0
        nums = set(nums)
        for num in nums:
            if (num - 1) not in nums:
                run_length = 1
                while num + 1 in nums:
                    run_length += 1
                    num += 1
                max_seen = max(run_length, max_seen)
        return max_seen 