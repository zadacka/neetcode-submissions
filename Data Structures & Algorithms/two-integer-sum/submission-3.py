class Solution:
    def twoSum_On2(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length - 1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i,j]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict() 
        # Note: we can't pre-compute hashmap as the Key is n and there may be duplicates
        # so we get the guarantee of i != n by walking through once O(n) and looking at prev entries
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
