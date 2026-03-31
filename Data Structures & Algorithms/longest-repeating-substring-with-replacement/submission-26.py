class Solution:
    def characterReplacement_alex(self, s: str, k: int) -> int:
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
    
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        char_counts = defaultdict(int)
        l = 0
        result = 0
        max_occurrence = 0
        for r, char in enumerate(s):
            char_counts[char] += 1
            max_occurrence = max(max_occurrence, char_counts[char])

            # maybe shrink window - this is the magic insight!
            # the window is valid so long as there are not more than k substitutions
            # ... and the number of substitutions = window width - most frequent char in window
            while (r - l + 1) - max_occurrence > k:

                left_char = s[l]
                char_counts[left_char] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result          