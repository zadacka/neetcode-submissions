class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {
            "+": int.__add__,
            "-": int.__sub__,
            "/": int.__floordiv__,  # care!! rounds down ... so -6/123 = -1, not 0 (rounds towards zero for this question)
            "*": int.__mul__,        
        }

        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                r, l = stack.pop(), stack.pop()
                stack.append(l - r)
            elif token == "/":
                r, l = stack.pop(), stack.pop()
                stack.append(int(l/r))
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(token))
        return stack[-1]