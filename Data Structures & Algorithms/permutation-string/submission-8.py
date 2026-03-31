class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import deque, Counter
        target = Counter(s1)
        window = deque(maxlen=len(s1))
        for char in s2:
            window.append(char)
            # print(f"{target}, {window}")
            if Counter(window) == target:
                return True
        return False