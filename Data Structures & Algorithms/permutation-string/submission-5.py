class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        target = Counter(s1)
        window = len(s1)
        for idx in range(len(s2) - window + 1):
            candidate = Counter(s2[idx:idx+window])
            if target == candidate:
                return True
        return False