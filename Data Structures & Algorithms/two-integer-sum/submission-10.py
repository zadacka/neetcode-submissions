class Solution:
    def twoSum_alex(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            sought = target - num
            candidates = set(nums[idx + 1:])
            if sought in candidates:
                idx2 = nums[idx+1:].index(sought) + 1
                return [idx, idx + idx2]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # we build this map as we go...
        for idx, num in enumerate(nums):
            sought = target - num
            if sought in seen:
                return [seen[sought], idx]   # nice - we don't have to check other idx != this idx!
            seen[num] = idx
