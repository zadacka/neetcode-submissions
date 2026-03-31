class Solution:
    def _twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val1 in enumerate(nums[:-1]):
            remaining = target - val1
            for j, val2 in enumerate(nums[i+1:], start=i+1):
                if val2 == remaining:
                    return [i, j]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i  # may overwrite value in hashmap