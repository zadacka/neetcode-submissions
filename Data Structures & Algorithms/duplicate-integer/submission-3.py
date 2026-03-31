class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
         
    def _hasDuplicate(self, nums):
        from collections import Counter
        c = Counter(nums)
        if c.most_common(1)[0][1] > 1:
            return True
        return False