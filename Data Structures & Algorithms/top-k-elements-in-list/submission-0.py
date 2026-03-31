class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        return [c[0] for c in counter.most_common(k)]