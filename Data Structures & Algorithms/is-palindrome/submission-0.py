class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumerical = [char.lower() for char in s if char.isalnum()]
        print(alphanumerical)
        return alphanumerical == list(reversed(alphanumerical))