class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seen = 0
        nums = set(nums)
        for num in nums:
            # magic hack: linear time walk past nums where
            # we would be starting our check in the middle
            # of a consecutive set
            if (num - 1) not in nums:
                run_length = 1
                while num + 1 in nums:
                    run_length += 1
                    num += 1
                max_seen = max(run_length, max_seen)
        return max_seen 