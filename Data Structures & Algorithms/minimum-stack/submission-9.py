import math

class MinStack:

    def __init__(self):
        self.stack = [] # (val, min_at_this_point)
        # the trick for O(1) is to track this! ^^^

    def push(self, val: int) -> None:
        if self.stack:
            new_min = min(self.stack[-1][1], val)
        else:
            new_min = val
        self.stack.append( (val, new_min) )

    def pop(self) -> None:
        val, minval = self.stack.pop()     

    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        return self.stack[-1][1]
