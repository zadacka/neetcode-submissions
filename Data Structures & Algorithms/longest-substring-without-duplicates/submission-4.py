class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        active = set()
        left = 0
        for right, char in enumerate(s):
            while char in active:
                active.remove(s[left])
                left += 1
            active.add(char)
            result = max(result, right - left + 1)
        return result
            