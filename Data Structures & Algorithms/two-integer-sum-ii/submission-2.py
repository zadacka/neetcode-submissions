class Solution:
    def twoSum_nice(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers[:-1]):
            remainder = target - num
            if remainder in numbers[idx + 1:]:
                r_index = numbers.index(remainder, idx + 1)
                return [idx + 1, r_index + 1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1
        while True:
            this = numbers[l] + numbers[r]
            if this > target:
                r -= 1
            elif this < target:
                l += 1
            else:
                return [l + 1, r + 1]
        