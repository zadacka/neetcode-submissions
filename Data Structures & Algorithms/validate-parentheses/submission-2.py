class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "(":")",
            "{":"}",
            "[":"]",
        }
        stack = []
        for char in s:
            if char in parentheses:
                stack.append(char)
            elif char in parentheses.values():
                if not stack:
                    return False  # stack empty
                openparen = stack.pop()
                if parentheses[openparen] != char:
                    return False
            else:
                pass # no paren char
        if stack:
            return False  # unclosed parentheses
        return True

