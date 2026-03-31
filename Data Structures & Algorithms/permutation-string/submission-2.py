class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
    
        l, r0 = 0, len(s1)
        target = Counter(s1)
        comparison = Counter(s2[l:r0])
        for r in range(r0, len(s2)):
            if target == comparison:
                return True
            comparison[s2[l]] -= 1
            comparison[s2[r]] += 1
            l += 1
        return target == comparison
            
        