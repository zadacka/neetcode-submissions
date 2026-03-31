class Solution:
    def findMin_basic(self, nums: List[int]) -> int:
        result = nums[0]
        l, r = 0, len(nums) -1
        while l <= r:
            mid = (l + r) // 2
            lval, mval, rval = nums[l], nums[mid], nums[r]

            if lval < rval: # window is sorted
                return min(lval, result)
            #.         ^^^ didn't expect to need min here

            result = min(result, mval)
            if lval >= lval: # inversion point in left half
                l = mid + 1
            else: # inversion point in right half
                r = mid - 1

        return result

    def findMin(self, nums: List[int]) -> int:
        # one part is sorted 
        # one part contains the rotation point and min
 
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]: 
                # right half sorted so min in left half (INC m)
                r = m 
            else: 
                # right half NOT sorted so includes inversion and min
                # (EXCL m) since we already know nums[m] > nums[r]!
                l = m + 1
        return nums[l]

