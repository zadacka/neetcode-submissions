class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {
            0:0,
            1:0,
            2:0
        }
        for c in nums:
            counts[c] += 1
        
        for idx in range(len(nums)):
            if counts[0]:
                nums[idx] = 0 
                counts[0] -= 1
            elif counts[1]:
                nums[idx] = 1
                counts[1] -= 1
            else:
                nums[idx] = 2
                counts[2] -= 1
        
        return nums