class Solution:
    def lengthOfLongestSubstring_alex(self, s: str) -> int:
        from collections import deque
        q = deque()
        max_length = 0
        seen = set()
        for char in s:
            while char in seen:
                evicted = q.popleft()
                seen.remove(evicted)
            q.append(char)
            seen.add(char)
            max_length = max(max_length, len(q))
        return max_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_length = 0
        l = 0
        for idx, char in enumerate(s):
            if char in last_seen:
                l = max(last_seen[char] + 1, l)  # never move l backwards!
            last_seen[char] = idx
            max_length = max(max_length, idx - l + 1)
        return max_length
            
                