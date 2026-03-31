class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict, deque
        max_length = 0
        
        strs = defaultdict(deque)
        wildcards = defaultdict(lambda: k)
        
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for idx, char in enumerate(s):
            for letter in letters:
                if letter == char:
                    strs[letter].append(char)
                elif k > 0:
                    while wildcards[letter] == 0:
                        popped = strs[letter].popleft()
                        if popped == '*':
                            wildcards[letter] += 1
                    strs[letter].append('*')
                    wildcards[letter] -= 1
                else:
                    strs[letter] = deque() # no wildcards, and not the char
                
                max_length = max(max_length, len(strs[letter]))
        return max_length
                            