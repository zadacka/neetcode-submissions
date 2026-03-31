class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        longest = 0
        l = 0
        for r, char in enumerate(s, start=1):  # hack so we don't need to add 1 for window size
            count[char] += 1
            while r - l - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            longest = max(r-l, longest)
        return longest