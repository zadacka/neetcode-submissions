class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        return [num for num, count in counts.most_common(k)]
        