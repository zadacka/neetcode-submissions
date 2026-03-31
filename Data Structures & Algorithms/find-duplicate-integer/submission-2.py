class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
         for idx, num in enumerate(nums[:-1], start=1):
            print(f"is {num} in {nums[idx:]}")
            if num in nums[idx:]:
                return num
         return None