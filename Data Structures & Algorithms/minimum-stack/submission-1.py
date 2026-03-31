class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = min(self.minval[-1], val) if self.minval else val
        self.minval.append(new_min)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minval.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minval[-1]
        
