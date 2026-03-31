class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        dp = [
            [False] * length 
            for _ in range(length)
        ]
        # care: you need to do l before i so that dp[i][j] lookups can be done by computing length 1, length 2 entries first
        for l in range(1, length + 1):         # all possible palindrome lengths
            for i in range(length - l + 1):    # possible starting indices for that length
                j = i + l - 1                  # end index
                # start_equals_end AND (two_long OR inner_palindrome)
                start_equals_end = s[i] == s[j]
                one_or_two_long = l < 3
                dp[i][j] = start_equals_end and (one_or_two_long or dp[i+1][j-1]) # check inner is pallindrome
                print(f"i={i}, j={j}, l={l}, val={dp[i][j]}, s={s[i:j+1]} {start_equals_end}, {one_or_two_long}")
        
        result, part = [], []
        def dfs(i):
            if i >= length:
                result.append(part.copy())
                return
            for j in range(i, length):
                if dp[i][j]:
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return result