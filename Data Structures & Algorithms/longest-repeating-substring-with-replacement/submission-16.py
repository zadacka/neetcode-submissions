class Solution:
    def characterReplacement2(self, s: str, k: int) -> int:
        longest = {char: {'left': 0, 'length': 0, 'jokers': k} for char in set(s)}
        for right, char in enumerate(s, start=1):
            for key, v in longest.items():
                if char == key:
                    pass # length increased
                else:
                    if v['jokers'] > 0:
                        v['jokers'] -= 1 # use a joker, don't move left
                    else: # need to free up one joker
                        while s[v['left']] == key: 
                            v['left'] += 1 # fast-forward past any matches
                        v['left'] += 1 # free up one joker

                v['length'] = max(v['length'], right - v['left'])

        return max(v['length'] for v in longest.values())

    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        result = 0
        l = 0
        for r, char in enumerate(s, start=1):
            count[char] += 1
            while r - l - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l)


        return result