class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers[:-1]):
            remainder = target - num
            if remainder in numbers[idx + 1:]:
                r_index = numbers.index(remainder, idx + 1)
                return [idx + 1, r_index + 1]
            
        