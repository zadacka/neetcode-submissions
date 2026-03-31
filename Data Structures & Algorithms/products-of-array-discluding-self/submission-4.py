class Solution:
    def productExceptSelf(self, nums):
        result = [1] * len(nums)

        prefix = 1
        for idx, num in enumerate(nums):
            result[idx] = prefix
            prefix *= num

        postfix = 1
        for idx in range(len(nums)-1, -1, -1):
            result[idx] *= postfix
            postfix *= nums[idx]
    
        return result

    def __productExceptSelf(self, nums):
        result = [1] * len(nums)

        for idx, num in enumerate(nums):
            if idx == len(result) - 1: break
            result[idx + 1] = result[idx] * num

        print(result)

        idx = len(nums) - 2
        product = 1
        for num in reversed(nums):
            if idx == -1: break
            product = product * num
            result[idx] *= product
            idx -= 1
        
        return result


    def _productExceptSelf(self, nums: List[int]) -> List[int]:
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