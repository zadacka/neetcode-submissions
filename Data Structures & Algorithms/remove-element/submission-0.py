class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r, v in enumerate(nums):
            if v != val:
                nums[l] = v
                l += 1
        return l
                