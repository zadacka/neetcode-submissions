class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_len = 0

        while end != len(s):
            next_char = s[end]
            # move start until we can move the next character
            while next_char in s[start:end]:
                start += 1
            end += 1
            max_len = max(max_len, end - start)
        return max_len
            