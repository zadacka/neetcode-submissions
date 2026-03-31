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
            else:
                if not stack:
                    return False  # stack empty
                openparen = stack.pop()
                if parentheses[openparen] != char:
                    return False

        if stack:
            return False  # unclosed parentheses
        return True

