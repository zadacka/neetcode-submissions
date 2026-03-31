import math

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = math.inf
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        p = self.stack.pop()
        if p == self.min:
            self.min = min(self.stack) if self.stack else math.inf
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        
