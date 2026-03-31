class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if Counter(t) - Counter(s): # cannot be found
            return "" 

        from collections import Counter
        target = Counter(t)
        l = 0
        search = Counter()
        substr = s

        for r, char in enumerate(s):
            search[char] += 1
                
            if len(target - search) == 0:  # match contained
                print(f"{search} contains {target}")
                print("Match contained!")
                while len(target - (search - Counter(s[l]))) == 0:                    
                    lchar = s[l]
                    search[lchar] -= 1
                    l += 1
                    print("removing {lchar}")
                if len(s[l:r+1]) < len(substr):
                    print(f"Updating substring to {s[l:r]}")
                    substr = s[l:r+1]
        return substr
            


        