class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        l = 0
        for r, char in enumerate(s):
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
            longest = max(longest, len(seen))
        return longest