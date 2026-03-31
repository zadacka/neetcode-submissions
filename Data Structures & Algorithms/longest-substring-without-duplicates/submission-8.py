class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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