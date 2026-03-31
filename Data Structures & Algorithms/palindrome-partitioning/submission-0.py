class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        dp = [
            [False] * length 
            for _ in range(length)
        ]
        for l in range(1, length + 1):       # length of potential pallindrome
            for i in range(length - l + 1):  # 'i' starting point(s) for palindromes of length l 
                j = i + l - 1  # end index
                # start_equals_end AND (two_long OR inner_palindrome)
                dp[i][j] = (s[i] == s[j] and  
                           (i+ 1 > (j - 1)  or 
                           dp[i+1][j-1]))
        
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