class Solution:
    def checkInclusion_neat(self, s1: str, s2: str) -> bool:
        from collections import deque, Counter
        target = Counter(s1)
        window = deque(maxlen=len(s1))
        
        for char in s2:
            window.append(char)
            # print(f"{target}, {window}")
            if Counter(window) == target:
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        target = Counter(s1)
        window = Counter()
        l = 0
        for r, char in enumerate(s2):
            window[char] += 1
            if (r - l + 1) > len(s1):
                window[s2[l]] -= 1
                l += 1
            if target == window:
                return True
        return False