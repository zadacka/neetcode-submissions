class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx1, num1 in enumerate(numbers[:-1]):
            for idx2, num2 in enumerate(numbers[idx1+1:], start=idx1 + 1):
                if num1 + num2 == target:
                    return [idx1+1, idx2+1]
                if num1 + num2 > target:
                    break
        