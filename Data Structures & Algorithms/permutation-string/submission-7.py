class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        target = Counter(s1)
        window = len(s1)
        candidate = Counter(s2[0:window -1])
        for l, char in enumerate(s2[window-1:]):
            candidate[char] += 1
            print(candidate)
            if candidate == target:
                return True
            candidate[s2[l]] -= 1
        return False