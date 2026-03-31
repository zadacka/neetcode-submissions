class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-/*':
                r = stack.pop()
                l = stack.pop()
                result = eval(f"{l}{token}{r}")
                stack.append(int(result))
            else:
                stack.append(int(token))
        return stack[-1]