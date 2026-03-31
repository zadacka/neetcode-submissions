class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we want:
        # [1,  1,  2, 8] product left
        # [1,  2,  4, 6] nums
        # [48, 12, 6, 1] product right
        left = [1]
        right= [1]
        for num in nums[:-1]:
            left.append(left[-1]*num)
        for num in reversed(nums[1:]):
            right.append(right[-1] * num)
        right = reversed(right)
        return [l * r for l, r in zip(left, right)]