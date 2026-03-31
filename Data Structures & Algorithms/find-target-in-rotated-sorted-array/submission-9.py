

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # first find the index of the minimum - then we can binary search in the 'upper' 
        # or 'lower' sorted section of the array

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            print(l, r, m)
            if nums[m] < nums[r]:
                # right side is sorted, min is at m or in left side
                r = m
            else:
                # left side is sorted, min is in right side (excluding m)
                l = m + 1
        min_index = l

        if target > nums[-1]:
            # binary search left half
            l, r = 0, min_index - 1
        else:
            # binary search left half
            l, r = min_index, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1