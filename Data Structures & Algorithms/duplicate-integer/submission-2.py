class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_before = set()
        for num in nums:
            if num in seen_before:
                return True
            seen_before.add(num)
        return False

    from collections import Counter
    def hasDuplicate2(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        if c and c.most_common()[0][1] > 1:
            return True
        return False
        #return c.most_common()[0][1] > 1
         