class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = [char.lower() for char in s if char.isalnum()]
        return word == list(reversed(word))