class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        return c.most_common()[-1][0]
        