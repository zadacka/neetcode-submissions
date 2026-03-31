class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1 for _ in nums]
        for idx1, num in enumerate(nums):
            results = [r if idx1 == idx2 else r * num for idx2, r in enumerate(results) ] 
        return results
        