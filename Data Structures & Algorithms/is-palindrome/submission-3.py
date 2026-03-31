def is_alphanumeric(char):
    return \
        ord("0") <= ord(char) <= ord("9") or \
        ord("a")<= ord(char) <= ord("z") or \
        ord("A") <= ord(char) <= ord("Z")


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = [c.lower() for c in s if is_alphanumeric(c)]
        return alnum == alnum[::-1]