class Solution:
    def isValid(self, s: str) -> bool:
        c2o = {
            ')':'(', 
            '}':'{', 
            ']':'['
        }
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else: 
                if not stack or c2o[char] != stack.pop():
                    return False
        return not stack

        