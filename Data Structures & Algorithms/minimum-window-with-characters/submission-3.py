class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if Counter(t) - Counter(s): return "" # cannot be found

        target = Counter(t)
        search = Counter()
        substr = s
        
        l = 0
        for r, char in enumerate(s, start=1):
            search[char] += 1
                
            if len(target - search) == 0:  # match contained
                while len(target - (search - Counter(s[l]))) == 0:
                    search[s[l]] -= 1
                    l += 1
                if r - l < len(substr):
                    substr = s[l:r]
        return substr
            


        