class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import math
        best, best_len = "", math.inf
        from collections import Counter
        target = Counter(t)
        active = Counter()
        missing = len(target)
        l = 0
        for r, char in enumerate(s, start=1):
            active[char] += 1
            if active[char] == target[char]:
                missing -= 1
            
            while missing == 0:
                this_len = r - l
                if this_len < best_len:
                    best, best_len = s[l:r], this_len
                lchar = s[l]
                if active[lchar] == target[lchar]:
                    missing += 1
                active[lchar] -= 1
                l += 1
        
        return best
