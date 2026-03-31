class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        target = Counter(t)
        candidate = Counter()
        l = 0

        best_match = None
        for r, char in enumerate(s):
            candidate[char] += 1
            l_char = s[l]
            while l < r and candidate[l_char] > target[l_char]:
                candidate[l_char] -= 1
                l += 1
                l_char = s[l]

            if target <= candidate:
                if best_match is None or candidate.total() < len(best_match):
                    pbm = best_match
                    best_match = s[l:r+1]
                    print(f"new best match: {best_match} as {target.total()} is less than {0 if pbm is None else len(pbm)}")

        return best_match or ""