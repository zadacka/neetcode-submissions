class Solution:
    def _topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        most_common = c.most_common(k)
        return [x[0] for x in most_common]
        
    def __topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        count_items = sorted([(count, n) for n, count in counts.items()], reverse=True)
        return [x[1] for x in count_items[:k]]
        
    def topKFrequent(self, nums, k):
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # build a frequency list so we don't have to sort 
        frequency = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            frequency[count].append(num)

        result = []
        for countlist in reversed(frequency):
            for count in countlist:
                result.append(count)
                if len(result) == k:
                    return result