class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i, num1 in enumerate(nums[:-2]):
            for j, num2 in enumerate(nums[i+1:-1], start=i+1):
                for k, num3 in enumerate(nums[j+1:], start=j+1):
                    if num1 + num2 + num3 == 0:
                        result.add(tuple(sorted([num1, num2, num3])))
        return [list(x) for x in result]