class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
 
        for num in nums:
            sequence_length = 1

            if num - 1 in nums:
                continue
            
            while num + 1 in nums:
                sequence_length += 1
                num += 1
            max_length = max(max_length, sequence_length)
        return max_length

        