class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B): # make sure A is shortest
            B, A = A, B
        
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2 # deal with zero indexing

            a_partition_l = A[i] if i >= 0 else float("-infinity")
            a_partition_r = A[i+1] if (i+1) < len(A) else float("infinity")
            b_partition_l = B[j]if j >= 0 else float("-infinity")
            b_partition_r = B[j + 1] if (j+1) < len(B) else float("infinity")

            if a_partition_l <= b_partition_r and b_partition_l <= a_partition_r:
                # good split!
                if total % 2: # odd
                    return min(a_partition_r, b_partition_r)
                avg = (min(a_partition_r, b_partition_r) + max(a_partition_l, b_partition_l)) / 2
                return avg
            else:
                if a_partition_l > b_partition_r:
                    r = i - 1
                else:
                    l = i + 1

