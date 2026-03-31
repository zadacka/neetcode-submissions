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
                if stack and char == parentheses[stack[-1]]:
                    _ = stack.pop()
                else:
                    return False

        if stack:
            return False  # unclosed parentheses
        return True

