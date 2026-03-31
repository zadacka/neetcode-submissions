class Solution:
    # def threeSum_n3(self, nums: List[int]) -> List[List[int]]:
    #     result = set()
    #     for i, num1 in enumerate(nums[:-2]):
    #         for j, num2 in enumerate(nums[i+1:-1], start=i+1):
    #             for k, num3 in enumerate(nums[j+1:], start=j+1):
    #                 if num1 + num2 + num3 == 0:
    #                     result.add(tuple(sorted([num1, num2, num3])))
    #     return [list(x) for x in result]

    def threeSum(self, nums):
        nums = sorted(nums)
        triplets = set()
        for l in range(len(nums)-2):
            m, r = l + 1, len(nums) - 1
            while m != r:
                current_triplet = (nums[l], nums[m], nums[r])
                current_sum = sum(current_triplet)
                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    m += 1
                else:
                    triplets.add(current_triplet)
                    m += 1
        return [list(x) for x in triplets]
