class Solution:
    def topKFrequent_pythonic(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        return [num for num, count in counts.most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        high_scores = [[] for _ in range(len(nums) + 1)]
        for val, count in counts.items():
            high_scores[count].append(val)  # multiple numbers might occur with the same frequency
        
        # sorting is too expensive, but we know that ther cannot be more than len(n) different frequencies
        # so we can build a 'high scores' list, with each spot being a list of the count of numbers for that index
        # then, the 'result' can be simply gained from reversing through the high scores
        result = []
        for high_score in reversed(high_scores):
            for num in high_score:
                result.append(num)
                if len(result) == k:
                    return result