class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        
        ss_len = len(s1)
        substring = defaultdict(int)
        comparison = defaultdict(int)

        for char in s1:
            substring[char] += 1
        
        for idx, char in enumerate(s2):
            comparison[char] += 1
            
            if idx >= ss_len:
                char2 = s2[idx - ss_len]
                if comparison[char2] == 1:
                    comparison.pop(char2)
                else:
                    comparison[char2] -= 1

            if substring == comparison:
                return True
        return False