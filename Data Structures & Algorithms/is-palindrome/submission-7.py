class Solution:
    def isPalindrome_alex(self, s: str) -> bool:
        word = [char.lower() for char in s if char.isalnum()]
        return word == list(reversed(word))

    def isPalindrome(self, s: str) -> bool:
        """ More code but lets us do this in O(1) space """
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True