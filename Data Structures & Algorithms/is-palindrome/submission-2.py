class Solution:
    def isAlnum(self, char):
        return (ord('0') <= ord(char) <= ord('9') or 
                ord('A') <= ord(char) <= ord('Z') or 
                ord('a') <= ord(char) <= ord('z'))

    def isPalindrome_nice(self, s: str) -> bool:
        alphanumerical = [char.lower() for char in s if self.isAlnum(char)]
        return alphanumerical == alphanumerical[::-1]

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.isAlnum(s[l]):
                l += 1
            while r > l and not self.isAlnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                # print(f"{l}, {r} {s[l]}, {s[r]}")
                return False
            l, r = l+1, r-1
        return True