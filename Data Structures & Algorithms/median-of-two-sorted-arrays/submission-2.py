import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            shorter, longer = nums1, nums2
        else:
            shorter, longer = nums2, nums1

        total = len(shorter) + len(longer)
        half = total // 2

        l, r = 0, len(shorter) - 1
        while True:
            m = (l + r) // 2
            m2 = half - m - 2
            shorter_left = shorter[m] if m >= 0 else -math.inf
            shorter_right = shorter[m+1] if (m+1) < len(shorter) else math.inf
            longer_left = longer[m2] if m2 >= 0 else -math.inf
            longer_right = longer[m2 + 1] if (m2 + 1) < len(longer) else math.inf

            if shorter_left <= longer_right and longer_left <= shorter_right:
                if total % 2:
                    return min(shorter_right, longer_right)
                return (max(shorter_left, longer_left) + min(shorter_right, longer_right)) / 2
            elif shorter_left > longer_right:
                r = m - 1
            else:
                l = m + 1
