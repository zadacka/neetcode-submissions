class Solution:
    def isValid(self, s: str) -> bool:
        c2o = {
            ')':'(', 
            '}':'{', 
            ']':'['
        }
        stack = []
        for char in s:
            # close bracket
            if char in c2o:
                if stack and stack[-1] == c2o[char]:
                    stack.pop()
                else:
                    return False
            # open bracket 
            else:
                stack.append(char)

        return not stack # empty stack = valid string  

        