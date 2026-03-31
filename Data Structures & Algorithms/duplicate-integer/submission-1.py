class Solution:
    from collections import Counter
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        if c and c.most_common()[0][1] > 1:
            return True
        return False
        #return c.most_common()[0][1] > 1
         