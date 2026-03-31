class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]: # LHS is sorted
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                #if nums[l] <= target < nums[mid]: # target in LHS
                    r = mid - 1

            else: # RHS is sorted
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                #if nums[mid] < target <= nums[r]: # target in RHS
                    l = mid + 1
        return -1


