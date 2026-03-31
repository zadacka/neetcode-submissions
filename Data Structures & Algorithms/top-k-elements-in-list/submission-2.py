class Solution:
    def _topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        most_common = c.most_common(k)
        return [x[0] for x in most_common]
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        count_items = sorted([(count, n) for n, count in counts.items()], reverse=True)
        return [x[1] for x in count_items[:k]]
        