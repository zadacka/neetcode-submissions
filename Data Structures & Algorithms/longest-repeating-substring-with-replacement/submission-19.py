class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, m, r = 0, 0, 0
        longest = 0
        seen = {}
        for m, char in enumerate(s):
            wildcards = k
            length = 1
            l = m
            r = m
            while l > 0:
                l -= 1
                if s[l] == char:
                    length += 1
                elif wildcards:
                    wildcards -= 1
                    length += 1
                else:
                    l += 1
                    break
            while r < len(s) - 1:
                r += 1
                if s[r] == char:
                    length += 1
                elif wildcards:
                    wildcards -= 1
                    length += 1
                elif s[l] != char:
                    l += 1
                else:
                    r -= 1
                    break
            longest = max(longest, length)
            print(f"starting at {m} has longest {longest}")
        return longest


            