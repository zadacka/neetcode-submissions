class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        product_left = [1] * len(nums)
        product_right = [1] * len(nums)

        product = 1
        for idx, num in enumerate(nums):
            product_left[idx] = product * num
            product = product_left[idx]
        
        product = 1
        idx = len(nums) - 1
        for num in reversed(nums):
            product_right[idx] = product * num
            product = product_right[idx]
            idx -= 1

        product_left = [1] + product_left
        product_right = product_right + [1]

        for idx, _ in enumerate(nums):
            result[idx] = product_left[idx] * product_right[idx + 1]
        print(product_left)
        print(product_right)
        print(result)
        return result