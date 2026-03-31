class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if target == nums[r]:
                return r

            if nums[l] < nums[mid]: # LHS is sorted
                if nums[l] <= target < nums[mid]: # target in LHS
                    r = mid - 1
                else:
                    l = mid + 1

            else: # RHS is sorted
                if nums[mid] < target <= nums[r]: # target in RHS
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


