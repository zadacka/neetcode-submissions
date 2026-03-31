class Solution:
    def isAlnum(self, char):
        if 47 <= ord(char) <= 57:
            return True # number
        elif 65 <= ord(char) <= 90:
            return True # ascii Uppercase
        elif 97 <= ord(char) <= 122:
            return True # ascii lowercase
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        alphanumerical = [char.lower() for char in s if self.isAlnum(char)]
        print(alphanumerical)
        return alphanumerical == alphanumerical[::-1]