class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        target = Counter(s1)
    
        window = len(s1)
        l = 0
        comparison = Counter(s2[l:window])
        for r in range(window, len(s2)):
            if target == comparison:
                return True
            comparison[s2[l]] -= 1
            comparison[s2[r]] += 1
            l += 1
        if target == comparison:
                return True
        return False
            
        