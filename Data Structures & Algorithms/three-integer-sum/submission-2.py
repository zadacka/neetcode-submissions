class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = set()
        
        for l in range(len(nums) - 2):
            m, r = l + 1, len(nums) - 1
            while m < r:
                current_sum = nums[l] + nums[m] + nums[r]
                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    m += 1
                else:
                    triplets.add((nums[l], nums[m], nums[r]))
                    m += 1
        return [list(x) for x in triplets]
                

        